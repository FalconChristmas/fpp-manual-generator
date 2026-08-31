# Task: add branch preview deploys alongside mike versioning

## Status

**Nothing is implemented yet.** This is an addendum to `MIKE-VERSIONING-BRIEF.md`
— it assumes that brief lands first (or in the same PR), since it reuses the same
`gh-pages` branch, the same `generate-web.sh` build, and the branch-classification
logic that brief already introduces.

## Goal

Give any working branch (not `main`, not a `v<N>` release branch) a disposable,
publicly-reachable preview of the web edition, so the maintainer can review
in-progress chapter work in a browser before merging — without that branch
appearing as a real version in the mike dropdown.

This is a *different* problem from mike versioning: mike publishes released FPP
versions side-by-side; this publishes **unreleased, in-progress** work at a
throwaway URL that never shows up in the version selector.

## Design

- **Trigger**: extend `deploy-web.yml`'s `on.push.branches` beyond `main` and
  `v[0-9]*`. To avoid every scratch branch producing a public URL, restrict the
  match to an explicit prefix — see open question 1.
- **Branch decides the path** (reuses the classification `MIKE-VERSIONING-BRIEF.md`
  already adds):
  - `main` → `mike deploy … latest` (per that brief)
  - `v[0-9]*` → `mike deploy …` (per that brief)
  - anything else matching the preview trigger → a plain `mkdocs build` (no
    `mike` involved at all — previews must never touch `versions.json`), copied
    into `preview/<sanitized-branch>/` on `gh-pages`
- **URL**: `manual.falconplayer.com/preview/<sanitized-branch>/`. Sanitize the
  branch name for filesystem/URL safety (e.g. `feature/foo` → `feature-foo`).
- **Cleanup**: add a second job triggered on `delete` (branch deletion) that
  removes the matching `preview/<sanitized-branch>/` directory from `gh-pages`
  and pushes, so previews don't accumulate indefinitely.
- **Concurrency**: reuse the `gh-pages-deploy` concurrency group from
  `MIKE-VERSIONING-BRIEF.md` (`cancel-in-progress: false`) — a burst of preview
  pushes must serialize with version deploys against the same `gh-pages` branch,
  or pushes race and the second fails non-fast-forward.
- **Downloads**: no changes needed to `web/overrides/main.html` — a preview build
  is a plain (non-`mike`) `mkdocs build`, so the Download bar behaves exactly as
  it did before `MIKE-VERSIONING-BRIEF.md`'s changes; the docx/pdf simply land
  under `preview/<branch>/` alongside the rest of that build's output.

## Work items

### `.github/workflows/deploy-web.yml`

- Reuse the branch classification (`main` / `v[0-9]*` / other) from
  `MIKE-VERSIONING-BRIEF.md`; route "other" branches matching the preview
  trigger to a preview build instead of `mike deploy`.
- Preview build step: `mkdocs build` (not `./generate-web.sh deploy`).
- Publish step: checkout `gh-pages`, copy the built site into
  `preview/<sanitized-branch>/`, commit, push.
- New job, triggered on `delete`: remove `preview/<sanitized-branch>/` from
  `gh-pages` for the deleted branch, commit, push.

### `mkdocs.yml`

- None. The same config already used for `main`/version builds works unchanged
  for a plain, non-`mike` build.

### `web/overrides/main.html`

- None. Preview builds don't invoke `mike`, so the Download bar's existing
  (pre-mike) behavior already applies.

## Open questions for the maintainer

1. **Trigger scope** — preview *every* branch, or only ones matching a prefix
   like `preview-*` / `draft-*`? Recommend a prefix, so an arbitrary WIP branch
   doesn't silently start publishing a public URL.
2. **Search indexing** — should preview pages carry `noindex` (robots meta) so
   they don't show up in search results for what is, functionally, unreleased
   content?
3. **Notification** — does the maintainer want the preview URL posted somewhere
   (e.g. a PR comment) once built, or is checking
   `manual.falconplayer.com/preview/<branch>/` by convention enough?
