# Liebherr Group – 10-minute presentation (HAT1 Financial Reporting)

| File | Use |
|---|---|
| `Liebherr_Presentation_animated.html` | **For presenting.** Open in Chrome, Edge or Firefox (works offline, one self-contained file). Slide transitions, staggered build-ups, growing charts and counting key figures. On slide 10 the three conditions are highlighted one by one with a yellow frame (3 extra clicks). |
| `Liebherr_Presentation_animated_B.html` | Alternative effect style for comparison: camera-focus transition, wipe reveals, springy bars, marker highlights on key figures, slow photo zoom, dot progress. Same focus clicks on slide 10. |
| `Liebherr_Presentation_Backup.pptx` | **Backup if the browser version fails.** Looks identical; fade transitions, content builds in automatically (charts wipe up), speaker notes in PowerPoint's presenter view. One click per slide; on slide 10 three extra clicks highlight the conditions, as in the HTML version. |
| `Liebherr_Investment_Analysis_Presentation.pdf` | Backup and hand-in. Fade transitions play in full-screen mode (Acrobat: Ctrl+L). |
| `Liebherr_Speaker_Notes.pdf` / `Speaker_Notes.md` | Speaker notes with timing per slide (~9:40 min). |

## Backup slides (13–29)

Slides 1–12 are the 10-minute talk. Slides 13–29 are backup for the Q&A: index (13), A business model (14–16), B accounting analysis (17–20), C financial analysis (21–24), D recommendation, scenarios and risks (25–27), E likely questions (28–29). The index sections and every ◂ INDEX button are clickable (HTML and PowerPoint slide show). In the HTML version press **I** to jump to the index; End returns to the last talk slide.

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
