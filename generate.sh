#!/bin/bash
# Build FPP_Manual_v10.docx from the Markdown chapters and screenshots.
# Requires pandoc (see ./install.sh). Does NOT need a running FPP.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
exec "$HERE/tools/build.sh"
