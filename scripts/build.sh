#!/usr/bin/env bash
set -euo pipefail
root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root/paper"
mkdir -p build
latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
python3 - <<'CHECK'
from pathlib import Path
import re
log = Path('build/main.log').read_text()
if re.search(r'undefined references|Citation .* undefined|Reference .* undefined|There were undefined|Rerun to get cross-references right', log):
    raise SystemExit('Unresolved manuscript references.')
CHECK
