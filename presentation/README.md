# Liebherr Group – 10-minute presentation (HAT1 Financial Reporting)

| File | Use |
|---|---|
| `Liebherr_Presentation_animated.html` | **For presenting.** Open in Chrome, Edge or Firefox (works offline, one self-contained file). Slide transitions, staggered build-ups, growing charts and counting key figures. |
| `Liebherr_Investment_Analysis_Presentation.pdf` | Backup and hand-in. Fade transitions play in full-screen mode (Acrobat: Ctrl+L). |
| `Liebherr_Speaker_Notes.pdf` / `Speaker_Notes.md` | Speaker notes with timing per slide (~9:40 min). |

## Presenting with the animated version

| Key | Action |
|---|---|
| → / Space / Page Down / clicker | next slide |
| ← / Page Up | previous slide |
| F | full screen |
| P | presenter view in a second window (notes, slide timer vs. plan, total time, next slide) |
| B | black screen (pause) |
| Home / End | first / last slide |

Tip: open the file, press **P**, move the presenter window to your laptop screen and the main window to the projector, then press **F** in the main window.

All figures come from the report (`Liebherr-Report-PDF-fix.docx`) and the workbook
(`Liebherr-Caterpillar-Restructured-financial-statements.xlsx`).
Photos: the team's original images (source/build/img/1, 2, 3, 6 and 9.jpg) and three photos from the Canva working design (canva_*.jpg).

Rebuild (from `source/`):

```bash
python3 scripts/build.py build && node scripts/render.js build && python3 scripts/add_transitions.py build/deck.pdf build/deck.pdf
```
