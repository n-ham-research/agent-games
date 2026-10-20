"""Audit compiled PDF links against LaTeX labels (requires pypdf)."""
from pathlib import Path
import argparse,json,re
from pypdf import PdfReader


def groups(text):
    out=[];depth=0;start=0
    for i,c in enumerate(text):
        if c=='{' and (i==0 or text[i-1]!='\\'):
            if depth==0:start=i+1
            depth+=1
        elif c=='}' and (i==0 or text[i-1]!='\\'):
            depth-=1
            if depth==0:out.append(text[start:i])
    return out


def audit(pdf,aux):
    r=PdfReader(pdf);dest=r.named_destinations
    assert r.metadata.author=='Nicholas Ham'
    assert r.metadata.title and r.metadata.title!='main'
    links=0;internal=0;external=set();label_count=0
    for page in r.pages:
        assert '??' not in (page.extract_text() or '')
        for ref in page.get('/Annots',[]):
            a=ref.get_object()
            if a.get('/Subtype')!='/Link':continue
            links+=1;action=a.get('/A',{})
            if action.get('/S')=='/URI':
                uri=str(action['/URI']);assert uri.startswith(('https://','http://')),uri
                external.add(uri)
            elif action.get('/S')=='/GoTo' or '/Dest' in a:
                target=action.get('/D',a.get('/Dest'))
                if isinstance(target,bytes):target=target.decode()
                if isinstance(target,str):
                    assert target in dest,target
                    assert 0<=r.get_destination_page_number(dest[target])<len(r.pages)
                else:assert target is not None
                internal+=1
            else:raise AssertionError(('unsupported link',a))
    for line in Path(aux).read_text().splitlines():
        if not line.startswith('\\newlabel{') or '@cref' in line:continue
        outer=groups(line[len('\\newlabel'):])
        if len(outer)<2:continue
        label,fields=outer[0],groups(outer[1])
        if len(fields)>=4 and fields[3]:
            anchor=fields[3];assert anchor in dest,(label,anchor)
            if fields[1].isdigit():assert r.get_destination_page_number(dest[anchor])==int(fields[1])-1,(label,fields[1])
            label_count+=1
    assert internal>0 and external and label_count>0
    return {'pdf':str(pdf),'pages':len(r.pages),'metadata':dict(r.metadata),
            'annotations':links,'internal_links':internal,'distinct_external_uris':sorted(external),
            'latex_labels_with_valid_page_destinations':label_count,'named_destinations':len(dest),
            'status':'pass; external URI targets checked, HTTP availability recorded separately'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('pdf');p.add_argument('aux');p.add_argument('--output');a=p.parse_args()
    result=audit(a.pdf,a.aux);encoded=json.dumps(result,indent=2)+'\n'
    if a.output:Path(a.output).write_text(encoded)
    print(encoded)
