"""Self-contained animated presentation (present.html) built from the same slides as the PDF."""
import base64, json, pathlib, re

PRESENT_CSS = r"""
html,body{margin:0;height:100%;background:#000;overflow:hidden}
#stage{position:fixed;left:50%;top:50%;width:1920px;height:1080px;transform-origin:0 0}
#stage .slide{position:absolute;inset:0;opacity:0;visibility:hidden;transform:translateX(60px);
  transition:opacity .55s ease,transform .7s cubic-bezier(.2,.7,.2,1),visibility 0s linear .7s;page-break-after:auto}
#stage .slide.active{opacity:1;visibility:visible;transform:none;transition:opacity .55s ease,transform .7s cubic-bezier(.2,.7,.2,1),visibility 0s}
#stage .slide.past{transform:translateX(-60px)}
#progress{position:fixed;left:0;bottom:0;height:6px;background:#00182E;transition:width .5s ease;z-index:5}
#blank{position:fixed;inset:0;background:#000;display:none;z-index:9}
#hint{position:fixed;right:16px;bottom:16px;color:#fff;font:600 14px/1.4 Arimo,Arial,sans-serif;background:rgba(0,24,46,.85);
  padding:10px 14px;border-radius:10px;z-index:6;transition:opacity .6s}

/* entrance of slide elements, staggered with --d */
@keyframes fxUp{from{opacity:0;transform:translateY(26px)}to{opacity:1;transform:none}}
@keyframes fxFade{from{opacity:0}to{opacity:1}}
@keyframes fxZoom{from{opacity:0;transform:scale(1.08)}to{opacity:1;transform:scale(1)}}
@keyframes growV{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@keyframes growH{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes draw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
@keyframes pop{0%{opacity:0;transform:translateX(-50%) scale(.85)}70%{transform:translateX(-50%) scale(1.03)}100%{opacity:1;transform:translateX(-50%) scale(1)}}
.slide .fx{opacity:0}
.slide.in .fx{animation:fxUp .75s cubic-bezier(.2,.7,.2,1) both;animation-delay:var(--d)}
.slide.in .fx.fade{animation-name:fxFade;animation-duration:.6s}
.slide.in .fx.photo{animation-name:fxZoom;animation-duration:1.4s}
.slide.in .fx.pill{animation:pop .7s cubic-bezier(.2,.7,.2,1) both;animation-delay:var(--d)}
.slide .gv,.slide .gvn,.slide .gh{transform-box:fill-box}
.slide .gv{transform-origin:50% 100%}.slide .gvn{transform-origin:50% 0}.slide .gh{transform-origin:0 50%}
.slide.in .gv,.slide.in .gvn{animation:growV .9s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(var(--d) + 250ms + var(--b,0ms))}
.slide.in .gh{animation:growH .9s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(var(--d) + 250ms + var(--b,0ms))}
.slide .ln{stroke-dasharray:1;stroke-dashoffset:1}
.slide.in .ln{animation:draw 1.4s ease-in-out both;animation-delay:calc(var(--d) + 200ms)}
.slide.in svg text,.slide.in svg circle{animation:fxFade .5s both;animation-delay:calc(var(--d) + 900ms)}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.slide .fx{opacity:1}.slide .ln{stroke-dashoffset:0}}
"""

PRESENT_JS = r"""
const slides=[...document.querySelectorAll('#stage .slide')];
const NOTES=__NOTES__;
let cur=0, pres=null, t0=null, slideT0=Date.now();
const stage=document.getElementById('stage');
function fit(){const s=Math.min(innerWidth/1920,innerHeight/1080);
  stage.style.transform=`scale(${s}) translate(-50%,-50%)`;stage.style.transformOrigin='0 0';
  stage.style.left='50%';stage.style.top='50%';stage.style.transform=`translate(-50%,-50%) scale(${s})`;stage.style.transformOrigin='50% 50%';}
addEventListener('resize',fit);fit();

// tag elements for staggered entrance
slides.forEach(s=>{
  let i=0;
  [...s.children].forEach(el=>{
    if(el.classList.contains('strip')||el.classList.contains('pno')||el.classList.contains('src'))return;
    el.classList.add('fx');
    const r=el.getBoundingClientRect?el:null;
    const w=parseFloat(el.style.width)||0, isBg=(w>=1100&&(parseFloat(el.style.top)||0)<=0)||el.classList.contains('band');
    if(isBg)el.classList.add('fade');
    if(el.classList.contains('photo'))el.classList.add('photo');
    el.style.setProperty('--d',(isBg?0:(120+i++*110))+'ms');
  });
  s.querySelectorAll('svg').forEach(svg=>{
    svg.querySelectorAll('.gv,.gvn,.gh').forEach((b,k)=>b.style.setProperty('--b',(k*70)+'ms'));
  });
});

// count-up for single key figures
function countUp(s){
  s.querySelectorAll('.big').forEach(el=>{
    const txt=el.dataset.orig||el.textContent; el.dataset.orig=txt;
    if(/[–→]/.test(txt)||el.children.length)return;
    const m=txt.match(/^([^\d]*)([\d,]*\.?\d+)(.*)$/s); if(!m)return;
    const raw=m[2], dec=(raw.split('.')[1]||'').length, comma=raw.includes(','), target=parseFloat(raw.replace(/,/g,''));
    if(!isFinite(target)||target===0)return;
    const fx=el.closest('.fx'), delay=fx?parseFloat(getComputedStyle(fx).getPropertyValue('--d'))||0:0;
    const dur=1100, start=performance.now()+delay+150;
    const fmt=v=>{let t=v.toFixed(dec);if(comma){const [a,b]=t.split('.');t=a.replace(/\B(?=(\d{3})+(?!\d))/g,',')+(b?'.'+b:'');}return m[1]+t+m[3];};
    el.textContent=fmt(0);
    const step=now=>{const p=Math.min(1,Math.max(0,(now-start)/dur)),e=1-Math.pow(1-p,3);
      el.textContent=fmt(target*e); if(p<1&&s.classList.contains('active'))requestAnimationFrame(step); else el.textContent=txt;};
    requestAnimationFrame(step);
  });
}

function show(n,instant){
  n=Math.max(0,Math.min(slides.length-1,n)); const prev=cur; cur=n;
  slides.forEach((s,i)=>{s.classList.toggle('active',i===n);s.classList.toggle('past',i<n);if(i!==n)s.classList.remove('in');});
  const s=slides[n]; s.classList.remove('in'); void s.offsetWidth; s.classList.add('in');
  countUp(s);
  document.getElementById('progress').style.width=((n+1)/slides.length*100)+'%';
  history.replaceState(null,'','#'+(n+1));
  if(prev!==n)slideT0=Date.now();
  if(t0===null&&n>0)t0=Date.now();
  updatePresenter();
}
function go(d){show(cur+d)}
addEventListener('keydown',e=>{
  if(['ArrowRight','PageDown',' ','Enter','ArrowDown'].includes(e.key)){e.preventDefault();go(1)}
  else if(['ArrowLeft','PageUp','Backspace','ArrowUp'].includes(e.key)){e.preventDefault();go(-1)}
  else if(e.key==='Home')show(0); else if(e.key==='End')show(slides.length-1);
  else if(e.key==='f'||e.key==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}
  else if(e.key==='b'||e.key==='B'||e.key==='.'){const b=document.getElementById('blank');b.style.display=b.style.display==='block'?'none':'block'}
  else if(e.key==='p'||e.key==='P')openPresenter();
});
document.getElementById('stage').addEventListener('click',e=>{ if(e.clientX<innerWidth*0.25)go(-1); else go(1); });
let tx=null;addEventListener('touchstart',e=>tx=e.touches[0].clientX);
addEventListener('touchend',e=>{if(tx===null)return;const dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>50)go(dx<0?1:-1);tx=null});

// presenter view: notes, next slide, timers
function openPresenter(){
  pres=window.open('','liebherr_presenter','width=1100,height=760');
  if(!pres)return;
  pres.document.write(`<!doctype html><title>Presenter view</title><style>
  body{margin:0;font-family:Arimo,Arial,sans-serif;background:#00182E;color:#fff;display:grid;grid-template-rows:auto 1fr auto;height:100vh}
  header{display:flex;gap:24px;align-items:center;padding:16px 24px;background:#FFCF00;color:#00182E;font-weight:700}
  #cur{font-size:26px;flex:1}#clock,#slideclock{font-size:30px;font-variant-numeric:tabular-nums}
  #notes{padding:22px 28px;font-size:23px;line-height:1.5;overflow:auto}#notes p{margin:0 0 14px}
  footer{display:flex;justify-content:space-between;padding:12px 24px;background:#0b2a45;font-size:17px}
  .lbl{font-size:13px;letter-spacing:2px;opacity:.7;display:block}</style>
  <header><div id="cur"></div><div><span class="lbl">SLIDE / PLAN</span><span id="slideclock"></span></div><div><span class="lbl">TOTAL</span><span id="clock">0:00</span></div></header>
  <div id="notes"></div><footer><span id="next"></span><span>← → navigate · B blank · F fullscreen (main window)</span></footer>`);
  pres.document.close();
  pres.addEventListener('keydown',e=>{ if(['ArrowRight','PageDown',' ','Enter'].includes(e.key)){e.preventDefault();go(1)}
    else if(['ArrowLeft','PageUp','Backspace'].includes(e.key)){e.preventDefault();go(-1)}
    else if(e.key==='b'||e.key==='B'){const b=document.getElementById('blank');b.style.display=b.style.display==='block'?'none':'block'} });
  updatePresenter();
}
const mmss=s=>Math.floor(s/60)+':'+String(Math.floor(s%60)).padStart(2,'0');
function updatePresenter(){
  if(!pres||pres.closed)return; const d=pres.document, n=NOTES[cur]||['','',''];
  d.getElementById('cur').textContent=(cur+1)+' / '+slides.length+' · '+n[0];
  d.getElementById('notes').innerHTML=n[2].split('\n\n').map(p=>'<p>'+p.replace(/&/g,'&amp;').replace(/</g,'&lt;')+'</p>').join('');
  const nx=NOTES[cur+1]; d.getElementById('next').textContent=nx?'Next: '+nx[0]:'End of presentation';
}
setInterval(()=>{ if(!pres||pres.closed)return; const d=pres.document, n=NOTES[cur]||['','—'];
  d.getElementById('clock').textContent=t0?mmss((Date.now()-t0)/1000):'0:00';
  d.getElementById('slideclock').textContent=mmss((Date.now()-slideT0)/1000)+' / '+n[1]; },500);

setTimeout(()=>{const h=document.getElementById('hint');if(h)h.style.opacity=0},6000);
show((parseInt(location.hash.slice(1))||1)-1);
"""


def build_present(build: pathlib.Path, css: str, slides: list, notes: list):
    def data_uri(path: pathlib.Path, mime: str) -> str:
        return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()

    # fonts: only Arimo, embedded, so the deck looks identical on any laptop
    font = data_uri(build / "fonts" / "Arimo-700.woff2", "font/woff2")
    font_css = "".join(
        f"@font-face{{font-family:'Arimo';font-style:normal;font-weight:{w};src:url({font}) format('woff2')}}"
        for w in (400, 700)) + "".join(
        f"@font-face{{font-family:'Assistant';font-style:normal;font-weight:{w};src:url({font}) format('woff2')}}"
        for w in (400, 600, 700, 800))
    css = re.sub(r"@font-face \{.*?\}\s*", "", css, flags=re.S)
    html_slides = "".join(slides)
    for name in sorted(set(re.findall(r"url\(img/([^)]+)\)", html_slides))):
        html_slides = html_slides.replace(f"url(img/{name})", f"url({data_uri(build / 'img' / name, 'image/jpeg')})")
    js = PRESENT_JS.replace("__NOTES__", json.dumps(notes, ensure_ascii=False))
    hint = '<div id="hint">→ / Space: next · ←: back · F: fullscreen · P: presenter view · B: blank</div>'
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>Liebherr Group Investment Analysis</title><style>{font_css}{css}{PRESENT_CSS}</style></head>'
           f'<body><div id="stage">{html_slides}</div><div id="progress"></div><div id="blank"></div>{hint}<script>{js}</script></body></html>')
    (build / "present.html").write_text(doc)
    return len(doc)
