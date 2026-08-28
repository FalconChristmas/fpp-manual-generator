#!/bin/bash
# (Re)capture the manual's screenshots from a running FPP web UI.
#
# Usage: ./capture.sh [--only token1,token2] [base_url] [shotlist]
#   --only    capture just these shots instead of the whole shotlist (comma
#             separated) -- handy for touching up one screenshot without
#             re-shooting everything else. Each token can be either the output
#             image name (e.g. "network.png") or the page it's captured from
#             (e.g. "networkconfig.php", or "settings.php" to match every tab
#             of that page at once) -- see tools/filter_shotlist.py.
#   base_url  default http://localhost   (use http://<fpp-host> for a remote FPP)
#   shotlist  default tools/shotlist.txt
#
# Requires chromium (see ./install.sh) and a reachable, running FPP. Screens that
# need cape hardware (or an xLights-uploaded show) only capture correctly on a
# device that has them -- see the notes in tools/shotlist.txt.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"

ONLY=""
if [ "$1" = "--only" ]; then
    ONLY="$2"
    shift 2
fi

URL="${1:-http://localhost}"
LIST="${2:-$HERE/tools/shotlist.txt}"

if [ -n "$ONLY" ]; then
    FILTERED="$(mktemp)"
    trap 'rm -f "$FILTERED"' EXIT
    python3 "$HERE/tools/filter_shotlist.py" "$LIST" "$ONLY" > "$FILTERED"
    LIST="$FILTERED"
fi

echo "Capturing screenshots from $URL"
echo "  shotlist: $LIST$([ -n "$ONLY" ] && echo " (filtered to: $ONLY)")"
echo "  output  : $HERE/images"
python3 "$HERE/tools/shoot.py" "$URL" "$LIST" "$HERE/images"
echo "Done."
