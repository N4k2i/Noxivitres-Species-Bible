from pathlib import Path
import re, hashlib, sys
root=Path(__file__).resolve().parents[1]
src=root/'assets/source/NOXIVITRES_SPECIES_BIBLE.md'
text=src.read_text(encoding='utf-8')
expected='f48011228b5abc47bfb3c1d25c51a46d03e46f636422dc626f1707a4ba518895'
checks=[]
checks.append(('source SHA-256',hashlib.sha256(text.encode()).hexdigest()==expected))
checks.append(('336 source entry metadata records',len(re.findall(r'^\*\*PART\s+[IVXLCDM]+.*?ENTRY\s+\d{3}',text,re.M))==336))
checks.append(('275 source plate metadata records',len(re.findall(r'^\*\*TECHNICAL PLATE\s+\d{3}',text,re.M))==275))
checks.append(('336 generated entry files',len(list((root/'_entries').glob('*.md')))==336))
checks.append(('275 generated plate files',len(list((root/'_plates').glob('*.md')))==275))
for name,ok in checks: print(('OK   ' if ok else 'FAIL ')+name)
if not all(ok for _,ok in checks): sys.exit(1)
