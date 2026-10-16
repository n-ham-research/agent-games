from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
record=json.loads((root/'provenance/feasibility-import.json').read_text())
for f in record['files']:
    p=root/f['destination']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'],p
print(f"Verified {len(record['files'])} frozen feasibility imports.")
