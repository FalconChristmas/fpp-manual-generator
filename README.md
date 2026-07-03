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
generate.sh         Build FPP_Manual_v10.docx (+ .pdf) from the chapters (no FPP needed)
generate-web.sh     Build the browsable web edition into web/site/ (no FPP needed)
annotate.sh         Render annotated screenshots into build/images/ for preview
capture.sh          (Re)capture screenshots from a running FPP web UI
metadata.yaml       Title-page metadata for the document
mkdocs.yml          MkDocs config for the web edition (theme, nav, search)
OUTLINE.md          Chapter plan / structure
chapters/           The manual, one Markdown file per chapter (combined in
                    filename order, e.g. 00-*, 02-*, 20-* ...)
images/             Raw screenshots referenced by the chapters (kept pristine)
annotations/        Optional YAML sidecars that mark up screenshots (see README there)
tools/
  build.sh          Pandoc build (invoked by generate.sh)
  build-web.sh      MkDocs build (invoked by generate-web.sh)
  annotate.py       Bakes annotations/ onto images/ at build time (Pillow)
  shoot.py          Headless-Chromium screenshot driver (Chrome DevTools
                    Protocol; Python standard library only)
  shotlist.txt      The list of pages to screenshot
  reference.docx    Pandoc reference document (Word styles/template)
```

## Quick start

```bash
./install.sh          # one-time: pandoc, libreoffice, chromium, poppler-utils, python3
./generate.sh         # build ./FPP_Manual_v10.docx (+ ./FPP_Manual_v10.pdf)
```

To refresh the screenshots against a live FPP (the device can be this one or a
remote):

```bash
./capture.sh                      # captures from http://localhost
./capture.sh http://192.168.1.50  # ...or a remote FPP
./generate.sh                     # rebuild with the new images
```

## Web edition

The same chapters also build into a browsable web site with a chapter sidebar and
built-in search (in the style of the xLights manual), using
[MkDocs](https://www.mkdocs.org/) with the Material theme:

```bash
./generate-web.sh          # build the static site into web/site/
./generate-web.sh serve    # live preview at http://localhost:8000
```

`web/site/` is a self-contained folder of static HTML — host it on any web server,
GitHub Pages, Netlify, etc., or open `web/site/index.html` locally. It needs only
`mkdocs-material` (installed by `./install.sh`), no running FPP. The chapters stay
the single source of truth: `generate-web.sh` stages a copy under `web/docs/`
(git-ignored) and never edits `chapters/`. Chapters appear in the sidebar in
filename order, with the lowest-numbered chapter (*About This Manual*) as the home
page; nav labels come from each chapter's top-level heading. A not-yet-captured
screenshot is a non-fatal warning here too, so the site still builds.

The staging step (`tools/webify.py`) also turns the manual's `> **Note:** …` /
`> **Tip:** …` blockquotes into Material's styled admonition callouts for the web
edition — the `.docx`/`.pdf` keep the plain blockquotes.

### Publishing to GitHub Pages

`.github/workflows/deploy-web.yml` builds and publishes the web edition on every
push to `main` that changes manual content (and on demand from the Actions tab).
Enable it once under **repo Settings → Pages → Build and deployment → Source =
"GitHub Actions"**; the site then goes live at the `site_url` in `mkdocs.yml`
(<https://falconchristmas.github.io/fpp-manual-generator/>).

## Annotating screenshots

Screenshots can be marked up with arrows, boxes, numbered callouts, highlights,
text labels, and blur/redactions — **without touching the raw images**. The raw
captures in `images/` stay pristine (so `capture.sh` can re-shoot them); the markup
lives in small YAML sidecars under `annotations/` and is baked on at build time into
`build/images/`, which the `.docx`, `.pdf`, and web builds all use automatically.

```bash
# 1. describe the overlays for images/status.png in annotations/status.yaml
# 2. preview placement:
./annotate.sh                 # renders build/images/*.png (images/ untouched)
# 3. rebuild the deliverables (they apply annotations for you):
./generate.sh
./generate-web.sh
```

Coordinates are pixels from the top-left of the source screenshot. The full sidecar
format, the list of annotation types, and an example are in
[`annotations/README.md`](annotations/README.md). Rendering needs `python3-pil` and
`python3-yaml` (installed by `./install.sh`); if they're missing the build falls
back to un-annotated images with a warning, so the manual still builds.

## Requirements

- **pandoc** – Markdown → `.docx`.
- **libreoffice** – converts the `.docx` → `.pdf` (headless) so the PDF matches the
  Word styling. Optional: if it's missing, `generate.sh` still builds the `.docx`
  and skips the PDF (or run `PDF=0 ./generate.sh` to skip it deliberately).
- **mkdocs-material** – builds the web edition (`./generate-web.sh`). Only needed
  for the web output; the `.docx`/`.pdf` build doesn't use it.
- **python3-pil** / **python3-yaml** – render the screenshot annotations. Only
  needed if `annotations/` is used; the build degrades to raw images without them.
- **chromium** – headless screenshots. Started detached by `shoot.py`.
- **python3** – build/capture scripts.
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
- **Always run `./generate.sh` to rebuild `FPP_Manual_v10.docx` after any change to
  manual content** (a chapter, an image, or the build config). The `.docx` is the
  deliverable, so a content change isn't finished until it's regenerated. The build
  needs only Pandoc — no running FPP — and a not‑yet‑captured screenshot is only a
  warning, so the build still succeeds.

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
- `generate.sh` writes `FPP_Manual_v10.docx` (and `FPP_Manual_v10.pdf`) to the
  repository root; they are build artifacts and are git‑ignored by default.
