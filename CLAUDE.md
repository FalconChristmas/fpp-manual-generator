# CLAUDE.md

Guidance for working in this repository.

## What this repo is

Source and tooling for the **FPP (Falcon Player) v10 User Manual**. The manual is
authored in Markdown (`chapters/`), illustrated with screenshots (`images/`), and
rendered to three deliverables from the same chapters:

- `FPP_Manual_v10.docx` — Pandoc (`generate.sh`)
- `FPP_Manual_v10.pdf` — LibreOffice converts the `.docx` (`generate.sh`)
- a browsable **web edition** in `web/site/` — MkDocs + Material theme, with a
  chapter sidebar and search (`generate-web.sh`)

See `README.md` and `OUTLINE.md`.

## Always regenerate the deliverables after changing manual content

The `.docx`, `.pdf`, and the web edition are the deliverables. **Whenever you
change anything that goes into the manual, rebuild before considering the task
done:**

```bash
./generate.sh          # rebuilds the .docx (+ .pdf) from chapters/ (no FPP needed)
./generate-web.sh      # rebuilds the web edition into web/site/ (no FPP needed)
```

"Manual content" includes any of:

- a chapter under `chapters/` (added, removed, or edited)
- an image referenced by a chapter (`images/`)
- build configuration: `metadata.yaml`, `tools/reference.docx`, `tools/build.sh`,
  `mkdocs.yml`, `tools/build-web.sh`
- a screenshot annotation under `annotations/` (see *Annotating screenshots* below)

`generate.sh` / `generate-web.sh` do **not** require a running FPP. A missing
screenshot is a non-fatal warning (Pandoc substitutes the image's caption text;
MkDocs logs a warning and builds anyway), so both builds still succeed; capture the
image later with `./capture.sh`.

The web edition builds from the same `chapters/`, so it needs no separate content.
`generate-web.sh` stages a lightly-transformed copy under `web/docs/` (it strips
Pandoc's `{-}` heading markers and promotes the lowest-numbered chapter to the site
home page) and never edits `chapters/`. Both `web/docs/` and the built `web/site/`
are git-ignored build artifacts. If you add a Pandoc-only Markdown construct to a
chapter, check it renders in the web edition too (or handle it in `build-web.sh`).

The PDF is produced by converting the `.docx` with LibreOffice, so it inherits the
Word styling automatically — there is no separate PDF stylesheet to maintain. If
LibreOffice isn't installed the PDF step is skipped with a hint and the `.docx`
still builds; run `PDF=0 ./generate.sh` to skip the PDF deliberately.

## Annotating screenshots (arrows, callouts, redactions)

Screenshots can be marked up **declaratively** so `capture.sh` can still re-shoot
the raw images: `images/` stays pristine and annotations are baked on at build time
into `build/images/`, which every deliverable then uses. When the maintainer asks to
annotate an image (e.g. "put an arrow on the Save button and number the tabs on
`status.png`"):

1. **Read the source image** (`images/<name>.png`) to find pixel coordinates —
   the Read tool shows it to you; coordinates are pixels from the top-left.
2. **Write/edit the sidecar** `annotations/<name>.yaml` (same stem as the image).
   Supported types: `box`, `circle`, `marker` (numbered badge), `arrow`,
   `highlight`, `text`, `blur` (redaction). Full format + an example are in
   `annotations/README.md`.
3. **Preview and verify placement**: run `./annotate.sh`, then Read
   `build/images/<name>.png` and adjust coordinates until it looks right. Iterate
   here rather than rebuilding the whole manual each time.
4. **Rebuild the deliverables** (`./generate.sh` and `./generate-web.sh`) — both
   apply annotations automatically.

Rendering is `tools/annotate.py` (Pillow + PyYAML). If `annotations/` has sidecars
but those libs are missing, the build **fails loudly** (rather than silently
shipping un-annotated images) — `./install.sh` installs them (`python3-pil`,
`python3-yaml`), and the CI workflow `pip install`s `pillow pyyaml`. A repo with no
sidecars skips the step and needs neither. `annotations/` is the source of truth
(committed); `build/` is a git-ignored artifact.

## Conventions

- Chapters are combined in **filename order**; the numeric prefixes (`00-`, `02-`,
  `52-` …) set the book order. Leave gaps so new chapters can be inserted.
- Each chapter file has a single top-level `#` heading (its title); use `##`/`###`
  for sections.
- Reference images as `images/<name>.png`. If you add a new screenshot, also add a
  capture line to `tools/shotlist.txt` so it can be (re)captured from a live FPP.
- Match the surrounding prose style: user-focused (web UI), with `> **Note:**` /
  `> **Tip:**` blockquotes for asides.
