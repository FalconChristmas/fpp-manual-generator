# FPP Manual Generator

Tooling and source for building the **Falcon Player (FPP) User Manual** (v10) as a
Microsoft Word `.docx`. This lives in its own repository so the manual and its
build tooling can be installed *alongside* FPP on a device when the manual needs
updating, without adding manual‑related churn to the core `fpp` repo.

The manual is authored in Markdown, illustrated with real screenshots captured
from a running FPP web UI, and rendered to `.docx` with Pandoc.

## Layout

```
install.sh          Install the build/capture dependencies (Debian/Ubuntu)
generate.sh         Build FPP_Manual_v10.docx from the chapters (no FPP needed)
capture.sh          (Re)capture screenshots from a running FPP web UI
metadata.yaml       Title-page metadata for the document
OUTLINE.md          Chapter plan / structure
chapters/           The manual, one Markdown file per chapter (combined in
                    filename order, e.g. 00-*, 02-*, 20-* ...)
images/             Screenshots referenced by the chapters
tools/
  build.sh          Pandoc build (invoked by generate.sh)
  shoot.py          Headless-Chromium screenshot driver (Chrome DevTools
                    Protocol; Python standard library only)
  shotlist.txt      The list of pages to screenshot
  reference.docx    Pandoc reference document (Word styles/template)
```

## Quick start

```bash
./install.sh          # one-time: pandoc, chromium, poppler-utils, python3
./generate.sh         # build ./FPP_Manual_v10.docx
```

To refresh the screenshots against a live FPP (the device can be this one or a
remote):

```bash
./capture.sh                      # captures from http://localhost
./capture.sh http://192.168.1.50  # ...or a remote FPP
./generate.sh                     # rebuild with the new images
```

## Requirements

- **pandoc** – Markdown → `.docx`.
- **chromium** – headless screenshots. Started detached by `shoot.py`.
- **python3** – build/capture scripts (standard library only; no `pip` needed).
- **poppler-utils** – only used when refreshing content from a reference PDF.
- A **running FPP** reachable over HTTP is required for `capture.sh` (not for
  `generate.sh`).

## Editing the manual

- Edit the Markdown in `chapters/`. Files are combined in filename order, so the
  numeric prefixes (`00-`, `02-`, `20-` …) set the book order — leave gaps so new
  chapters can be inserted.
- Reference images as `images/<name>.png`; the build adds `images/` to Pandoc's
  resource path.
- Each chapter file should have a single top-level `#` heading (its chapter
  title); use `##`/`###` for sections.
- Run `./generate.sh` to rebuild.

## Screenshots

`tools/shotlist.txt` lists every page to capture. Each line is tab‑separated:

```
outfile.png <TAB> path_or_url <TAB> settle_ms [ <TAB> js_after_load [ <TAB> clip_height_px ] ]
```

- **settings tabs** are captured with a `#hash` so the page's onload JavaScript
  selects the correct tab (the driver forces a full reload per shot).
- an optional **`js_after_load`** expression runs after the page settles — used to
  open a modal (e.g. `showModelPreview('...')`) or click a sub‑tab before the shot.
- an optional **`clip_height_px`** captures just that many pixels from the top of a
  fixed‑height viewport — used to frame a centred modal or the top of a very tall
  page.

Some screens require hardware or data that a given device may not have:

- **Cape screens** (Pixel Strings / LED Panel ports, Cape Info, EEPROM signing,
  Current Monitor) only render on a device with the relevant cape/hat. Their lines
  are commented at the bottom of `tools/shotlist.txt`; enable them on a
  cape‑enabled device.
- **Pixel Overlay preview modals** reference example model/submodel names; edit
  them to models present on your device, or remove those lines.

## Notes

- The manual's prose builds on the community FPP Manual originally written by Rick
  Harris (Poporacer), updated for FPP 10.
- `generate.sh` writes `FPP_Manual_v10.docx` to the repository root; it is a build
  artifact and is git‑ignored by default.
