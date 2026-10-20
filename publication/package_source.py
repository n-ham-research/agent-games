"""Create a self-contained conventional LaTeX review bundle; never submits."""
from pathlib import Path
import hashlib,json,shutil,tarfile,tempfile
ROOT=Path(__file__).resolve().parents[1]
NAME=ROOT.name
out=ROOT/'output'/'pdf';out.mkdir(parents=True,exist_ok=True)
source=Path(tempfile.mkdtemp(prefix=NAME+'-source-'))
for path in (ROOT/'paper').rglob('*'):
    if not path.is_file() or 'build' in path.relative_to(ROOT/'paper').parts:continue
    if path.suffix not in {'.tex','.bib','.sty','.bst','.cls','.pdf','.png','.jpg','.eps','.tikz'}:continue
    target=source/path.relative_to(ROOT/'paper');target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,target)
shutil.copy2(ROOT/'paper/build/main.bbl',source/'main.bbl')
ancillary=[]
if NAME=='game-symmetry':
    ancillary=['phase5_ternary_audit.py','phase5-ternary-audit-results.json','phase5_ternary_six_crosscheck.py','phase5_six_independent.py']
    (source/'anc').mkdir()
    for name in ancillary:shutil.copy2(ROOT/'experiments'/name,source/'anc'/name)
manifest={str(p.relative_to(source)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(source.rglob('*')) if p.is_file()}
(source/'SOURCE-MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(source/'README.txt').write_text('Human-review source bundle. Not submitted or author-approved.\nCompile main.tex with pdfLaTeX; the supplied main.bbl avoids a remote bibliography dependency.\nBibliography source is references.bib (plainnat/BibTeX). No shell escape.\nAncillary certificates, where present, use Python3 standard library; see manuscript appendix.\n')
archive=out/(NAME+'-source.tar.gz')
with tarfile.open(archive,'w:gz') as t:
    for p in sorted(source.rglob('*')):
        if p.is_file():t.add(p,arcname=str(p.relative_to(source)))
shutil.copy2(ROOT/'paper/build/main.pdf',out/(NAME+'.pdf'))
print(json.dumps({'archive':str(archive),'source_directory':str(source),'pdf':str(out/(NAME+'.pdf')),'ancillary':ancillary},indent=2))
