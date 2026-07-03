#!/bin/bash
# Build the FPP v10 manual as a browsable web site (sidebar nav + search) from the
# Markdown chapters. Requires mkdocs-material (see ./install.sh). No FPP needed.
#
#   ./generate-web.sh          # build the static site into web/site/
#   ./generate-web.sh serve    # live preview at http://localhost:8000
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
exec "$HERE/tools/build-web.sh" "$@"
