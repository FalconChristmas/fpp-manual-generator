#!/bin/bash
# (Re)capture the manual's screenshots from a running FPP web UI.
#
# Usage: ./capture.sh [base_url] [shotlist]
#   base_url  default http://localhost   (use http://<fpp-host> for a remote FPP)
#   shotlist  default tools/shotlist.txt
#
# Requires chromium (see ./install.sh) and a reachable, running FPP. Screens that
# need cape hardware (or an xLights-uploaded show) only capture correctly on a
# device that has them -- see the notes in tools/shotlist.txt.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
URL="${1:-http://localhost}"
LIST="${2:-$HERE/tools/shotlist.txt}"

echo "Capturing screenshots from $URL"
echo "  shotlist: $LIST"
echo "  output  : $HERE/images"
python3 "$HERE/tools/shoot.py" "$URL" "$LIST" "$HERE/images"
echo "Done."
