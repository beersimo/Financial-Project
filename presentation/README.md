# Liebherr Group – 10-minute presentation (HAT1 Financial Reporting)

| File | Use |
|---|---|
| `Liebherr_Presentation_animated.html` | **For presenting.** Open in Chrome, Edge or Firefox (works offline, one self-contained file). Slide transitions, staggered build-ups, growing charts and counting key figures. On slide 10 the three conditions are highlighted one by one with a yellow frame (3 extra clicks). |
| `Liebherr_Presentation_animated_B.html` | Alternative effect style for comparison: camera-focus transition, wipe reveals, springy bars, marker highlights on key figures, slow photo zoom, dot progress. Same focus clicks on slide 10. |
| `Liebherr_Presentation_Backup.pptx` | **Backup if the browser version fails.** Looks identical; fade transitions, content builds in automatically (charts wipe up), speaker notes in PowerPoint's presenter view. One click per slide; on slide 10 three extra clicks highlight the conditions, as in the HTML version. |
| `Liebherr_Investment_Analysis_Presentation_FINAL.pdf` | **Final hand-in version:** the 12 talk slides plus the reference list (page 13), without backup slides. Fade transitions in full-screen mode. |
| `Liebherr_Backup_Slides.pdf` | Backup slides 13–52 only (index, A–F, references), with clickable index and ◂ INDEX links. |
| `Liebherr_Investment_Analysis_Presentation.pdf` | Backup and hand-in. Fade transitions play in full-screen mode (Acrobat: Ctrl+L). |
| `Liebherr_Speaker_Notes_FINAL.pdf` | **Final speaker notes for the talk:** speaker plan (Adam 1–3, Zarah 4–5, Philipp 6–8, Simon 9–12), handover lines and click cues, ≈ 9:45 min. |
| `Moderation_Cards_Simon.pdf` | Moderator cards for Simon (slides 9–12): A4, three cards per page (210 × 99 mm), cut along the dashed lines. Back side, two versions: `Moderation_Cards_Simon_back_yellow.pdf` (black logo on Liebherr yellow) or `Moderation_Cards_Simon_back_white.pdf` (black logo on white); print double-sided, flip on long edge. Build others with `python3 scripts/cards.py build <Name> out.pdf` and `python3 scripts/cards_back.py <cards> out.pdf yellow|white build/img/liebherr_black.png`. |
| `Liebherr_Speaker_Notes.pdf` / `Speaker_Notes.md` | Same notes plus the backup slides. |

## Backup slides (13–52)

Slides 1–12 are the 10-minute talk. Slides 13–52 are backup for the Q&A: index of every backup slide, each clickable (13); A ratios (profitability, efficiency, leverage, liquidity, cash flow and growth), workbook-to-ratio excerpt, what-if logic, provisions, sensitivities, long list (Table G2), key accounts, red-flag screen, short list, workbook (14–29); B business model (30–32); C accounting analysis incl. conservative vs. aggressive and Table J13 (33–37); D financial analysis incl. common size (38–42); E recommendation, levers, changes to monitor and Table 3 (43–47); F likely questions (48–51); references in APA (52). The index sections and every ◂ INDEX button are clickable (HTML and PowerPoint slide show). In the HTML version press **I** to jump to the index; End returns to the last talk slide.

## Presenting with the animated version

| Key | Action |
|---|---|
| → / Space / Page Down / clicker | next slide |
| ← / Page Up | previous slide |
| F | full screen |
| P | presenter view in a second window (notes, slide timer vs. plan, total time, next slide) |
| B | black screen (pause) |
| Home / End | first slide / last talk slide (12) |
| I | backup index (slide 13) |

Tip: open the file, press **P**, move the presenter window to your laptop screen and the main window to the projector, then press **F** in the main window.

All figures come from the report (`Liebherr-Report-PDF-fix.docx`) and the workbook
(`Liebherr-Caterpillar-Restructured-financial-statements.xlsx`).
Photos: the team's original images (source/build/img/1, 2, 3, 6 and 9.jpg) and three photos from the Canva working design (canva_*.jpg).

Rebuild (from `source/`):

```bash
# PDF + animated HTML
python3 scripts/build.py build && node scripts/render.js build && python3 scripts/add_transitions.py build/deck.pdf build/deck.pdf
# backup PowerPoint
node scripts/capture_layers.js build pptx/layers && node scripts/capture_focus.js build pptx/layers && node scripts/build_pptx.js pptx/layers build/notes.json pptx/raw.pptx
# unzip raw.pptx to pptx/un, then: python3 scripts/pptx_effects.py pptx/un and zip it again
```
