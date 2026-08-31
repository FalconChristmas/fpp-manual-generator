# Task: add mike versioning to the FPP manual web edition

## Status

**Nothing is implemented yet.** The working tree is clean — this is a plan, and
all of the work below is yours. The decisions in *Agreed design* were settled
with the maintainer and are not up for renegotiation; the questions at the end
are the ones he still wants to be asked.

## Goal

Publish the MkDocs web edition as **multiple selectable versions** using
[mike](https://github.com/jimporter/mike), so readers can pick FPP 10 / 11 / …
from a dropdown in the Material header.

**Hard constraint from the maintainer: no local commands before committing.**
He commits and pushes; CI does the entire build and publish. Do not design
anything that requires him to run `mike deploy`, tag a release, or run a release
script by hand.

## How mike works (so the design below makes sense)

`mike deploy 10` runs `mkdocs build`, then commits the resulting **HTML** into an
orphan `gh-pages` branch under a directory named for the version, and rewrites a
root `versions.json` that Material's version selector fetches at runtime:

```text
gh-pages/
├── versions.json      # [{"version":"10","title":"v10","aliases":["latest"]}]
├── index.html         # redirect to the default version (mike set-default)
├── 10/                # a full, frozen copy of the built site
└── 9/
```

Consequences to respect:

- Versions are **built files, not commits**. An old version is never rebuilt; to
  fix one you re-run the deploy from that version's source branch.
- Each version costs a full site copy (~88 PNGs here). Fine for a few versions;
  worth remembering if minor versions (`10.1`, `10.2`, …) each get their own
  entry, since that multiplies the count fast.
- Aliases (`latest`) default to git symlinks, which **GitHub Pages does not
  follow** — must use `--alias-type=copy`.

## Agreed design

### 1. The version number lives in `metadata.yaml`

`metadata.yaml` already carries the manual's identity for Pandoc's title page, so
it becomes the single source of truth. **Do not add a `VERSION` file** — the
maintainer explicitly rejected a separate file for this.

Target shape:

```yaml
---
title: "Falcon Player (FPP) User Manual"
# The FPP version this branch documents. Single source of truth: names the
# deliverables, fills the web edition's download links, and picks the version
# directory the site publishes into. Bump here and nowhere else.
version: "10"
author: "The FPP Community"
date: "2026"
lang: en-GB
toc-title: "Contents"
...
```

Note `subtitle: "Version 10.x"` is **removed** from the file — `build.sh` derives
it instead (see below), so the number cannot drift between two keys. Removing the
key rather than overriding it also sidesteps any question about whether a
command-line `--metadata` beats a YAML metadata block in an input file.

The value may later carry a minor (`"10.1"`) — see question 1. Everything that
parses or formats it must tolerate a dot, not assume a bare integer.

### 2. Branch name decides the alias; `metadata.yaml` decides the number

- push to `main` → deploy that version with alias `latest`, plus
  `mike set-default latest`
- push to a `v<N>` maintenance branch → deploy that version, **no alias**
- CI must **assert** that on a `v<N>` branch, `metadata.yaml`'s version == `<N>`,
  and fail loudly otherwise. This catches a branch cut without freezing the file.

Cutting a release then looks like:

```bash
git branch v10 main        # metadata.yaml on v10 already says 10
git checkout main          # edit version: "11", commit, push
```

### 3. Publishing switches to the `gh-pages` branch

mike pushes there directly. The current workflow's `upload-pages-artifact` /
`deploy-pages` steps and the separate `deploy` job get removed; `permissions`
becomes `contents: write` (drop `pages` / `id-token`).

One-time manual step for the maintainer: repo Settings → Pages → Source =
"Deploy from a branch" → `gh-pages` / `(root)`. **Tell him to do this** — the
site will not update until he does.

## Work items

### `metadata.yaml`

Add the `version:` key and drop `subtitle:` as described above.

### `tools/build.sh`

- Parse the version out of `metadata.yaml` near the top, e.g.

  ```bash
  MANUAL_VERSION="$(sed -n 's/^version:[[:space:]]*"\{0,1\}\([0-9][0-9.]*\).*/\1/p' \
      "$MANUAL_DIR/metadata.yaml" | head -1)"
  ```

  Fail loudly with a clear message if it comes back empty.
- `OUT="${OUT:-$MANUAL_DIR/FPP_Manual_v${MANUAL_VERSION}.docx}"` — currently
  hardcoded `FPP_Manual_v10.docx` at line 18. Keep the `OUT=` override working.
- Add `--metadata subtitle="Version ${MANUAL_VERSION}.x"` to the pandoc call so
  the title page still reads "Version 10.x". (If minor versions land, revisit
  this string — "Version 10.1.x" would be wrong.)
- Update the usage comment at the top (it says `v10`).

### `tools/build-web.sh`

- Parse the same version the same way, and **`export MANUAL_VERSION`** — the
  mkdocs config reads it as an env var (below).
- The deliverable staging loop at line 82 hardcodes
  `FPP_Manual_v10.docx FPP_Manual_v10.pdf`; build those names from the version.
- Replace the `if [ "$1" = "serve" ]` / `mkdocs build` tail with a
  `build` / `serve` / `deploy` `case`. The `deploy` arm should `shift` and exec:

  ```bash
  mike deploy \
      --update-aliases \
      --alias-type=copy \
      --title "v$MANUAL_VERSION" \
      "$MANUAL_VERSION" "$@"
  ```

  so the caller supplies the alias and `--push`. `--alias-type=copy` is
  load-bearing (GitHub Pages does not follow git symlinks) — say so in a comment.
  Guard with a `command -v mike` check and a useful install hint.
- Keep the existing "not `--strict`" behaviour and its comment: a missing
  screenshot must stay a warning, not a build failure.

### `mkdocs.yml`

- Add the version selector and the download-link variable:

  ```yaml
  extra:
    version:
      provider: mike
      default: latest
    manual_version: !ENV [MANUAL_VERSION, "10"]
  ```

- `site_description` says "FPP version 10 User Manual" — make it version-free,
  since one config now builds every version.

Some YAML editors flag `!ENV` as "Unresolved tag". That is an editor limitation;
`!ENV` is a native MkDocs feature. Ignore it, or add a schema exclusion cleanly.

### `web/overrides/main.html`

The Download bar hardcodes `FPP_Manual_v10.pdf` / `.docx`. Build the filename
from `{{ config.extra.manual_version }}`. Update the comment too: under mike,
`base_url` resolves to the *version* directory (`…/10/`), so each published
version's bar correctly points at its own downloads.

### `.github/workflows/deploy-web.yml`

The main piece. Rewrite it to:

- trigger on push to `main` and `v[0-9]*` branches, plus `workflow_dispatch`
- `permissions: contents: write`
- `concurrency: { group: gh-pages-deploy, cancel-in-progress: false }` — deploys
  must **serialize**, not cancel, or two runs race to push `gh-pages` and the
  second fails non-fast-forward
- `actions/checkout` with `fetch-depth: 0`, then explicitly fetch the `gh-pages`
  branch (guarded with `|| true` for the very first run). Without the existing
  branch locally, mike recreates it and the push drops every previously
  published version — worth an inline comment saying exactly that.
- configure `git config user.name` / `user.email` for the bot committer
- `pip install mkdocs-material pillow pyyaml mike` (adds `mike`)
- derive version and alias from `github.ref_name` per *Agreed design 2*,
  including the `v<N>` consistency assertion
- run `./generate.sh` (docx+pdf) **before** `./generate-web.sh deploy …`, so the
  downloads are staged into the version directory
- `./generate-web.sh deploy latest --push` on `main`;
  `./generate-web.sh deploy --push` on a maintenance branch
- `mike set-default --push latest` on `main` only
- keep the existing `upload-artifact` step for the `.docx`/`.pdf`, but make its
  name and paths version-aware rather than hardcoded `FPP_Manual_v10`

### `.gitignore`

`/FPP_Manual_v10.docx` and `/FPP_Manual_v10.pdf` are hardcoded; widen to
`/FPP_Manual_v*.docx` and `/FPP_Manual_v*.pdf`.

### `install.sh`

Decide whether to add `mike` — see question 3 below.

### `README.md`

The `## Web edition` and `### Publishing to GitHub Pages` sections describe the
old single-version Actions-artifact flow and will be wrong. Rewrite them, and add
a short **Cutting a new version** section with the branch + bump recipe. Keep the
existing voice.

### `CLAUDE.md`

Add the versioning model to *Conventions*: `metadata.yaml`'s `version:` is the
single source of truth; the branch decides the alias; old versions are frozen
HTML in `gh-pages` and are never rebuilt from `chapters/`.

## Verification (actually run these and report real output)

`pandoc` and `mkdocs` were **not installed** on the maintainer's machine when
this brief was written, so nothing here has been proven locally. Install what you
need, or verify in CI — but do not report any of it as passing unless you ran it.

- `./generate.sh` → confirm it still writes `FPP_Manual_v10.docx` / `.pdf` (no
  filename regression) and that the title page still reads "Version 10.x".
- `./generate-web.sh` → confirm the site builds and the Download bar in
  `web/site/index.html` points at `FPP_Manual_v10.pdf`. This is the proof that
  the `metadata.yaml` → `MANUAL_VERSION` → `!ENV` → `config.extra.manual_version`
  chain works; it is the most fragile link in the design.
- Temporarily set `version: "11"`, rebuild the web edition, confirm the links
  become `FPP_Manual_v11.pdf`, then **set it back to `10`**.
- `pip install mike && ./generate-web.sh deploy` (no `--push`) → confirm a local
  `gh-pages` branch appears with a `10/` directory and a `versions.json`. Then
  delete that local branch so the maintainer's clone is left clean.
- Lint every Markdown file you touch.

## Repo conventions you must follow

- Read `CLAUDE.md` before starting. Smallest **correct** change; no unrelated
  refactors or formatting passes.
- Comments lead with *why*, not *what*.
- **Do not run `git add`, `git commit`, or `git push`.**
- Markdown must be lint-clean (fenced blocks need a language; blank lines around
  headings, lists and fences; table pipes spaced `| --- |`).

## Ask the maintainer before you build (use AskUserQuestion)

He has opinions on presentation. Ask these up front rather than guessing:

1. **Version selector labels** — what should the dropdown read? Options:
   latest with plain `v10` and eventually minor versions `v10.1` (Recommended),
   `10 (latest)` for the aliased one, or `FPP 10`.
2. **Old-version banner** — should a reader on an outdated version see a warning
   bar ("You're viewing the docs for FPP 10; the latest is 11")? Material
   supports this by overriding the `outdated` block in `web/overrides/main.html`,
   alongside the existing Download bar. Offer: yes with a link to latest / yes
   plain / no banner.
3. **`install.sh`** — add `mike` to the local install, or keep local installs
   lean since only CI deploys? (He does not want to run deploys locally, so the
   only benefit is being able to preview the multi-version site with
   `mike serve`.)
4. **Alias name** — `latest` (assumed) or `stable`? This becomes a public URL
   (`/latest/`) and is painful to change later.
