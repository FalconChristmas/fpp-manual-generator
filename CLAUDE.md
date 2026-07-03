# CLAUDE.md

Guidance for working in this repository.

## What this repo is

Source and tooling for the **FPP (Falcon Player) v10 User Manual**. The manual is
authored in Markdown (`chapters/`), illustrated with screenshots (`images/`), and
rendered to `FPP_Manual_v10.docx` with Pandoc — then converted to a matching
`FPP_Manual_v10.pdf` with LibreOffice. See `README.md` and `OUTLINE.md`.

## Always regenerate the docx after changing manual content

`FPP_Manual_v10.docx` / `FPP_Manual_v10.pdf` are the deliverables. **Whenever you
change anything that goes into the manual, rebuild before considering the task
done:**

```bash
./generate.sh          # rebuilds the .docx (+ .pdf) from chapters/ (no FPP needed)
```

"Manual content" includes any of:

- a chapter under `chapters/` (added, removed, or edited)
- an image referenced by a chapter (`images/`)
- build configuration: `metadata.yaml`, `tools/reference.docx`, `tools/build.sh`

`generate.sh` does **not** require a running FPP. A missing screenshot is a
non-fatal warning (Pandoc substitutes the image's caption text), so the build still
succeeds; capture the image later with `./capture.sh`.

The PDF is produced by converting the `.docx` with LibreOffice, so it inherits the
Word styling automatically — there is no separate PDF stylesheet to maintain. If
LibreOffice isn't installed the PDF step is skipped with a hint and the `.docx`
still builds; run `PDF=0 ./generate.sh` to skip the PDF deliberately.

## Conventions

- Chapters are combined in **filename order**; the numeric prefixes (`00-`, `02-`,
  `52-` …) set the book order. Leave gaps so new chapters can be inserted.
- Each chapter file has a single top-level `#` heading (its title); use `##`/`###`
  for sections.
- Reference images as `images/<name>.png`. If you add a new screenshot, also add a
  capture line to `tools/shotlist.txt` so it can be (re)captured from a live FPP.
- Match the surrounding prose style: user-focused (web UI), with `> **Note:**` /
  `> **Tip:**` blockquotes for asides.
