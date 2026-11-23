from pathlib import Path
import json,re,sys,copy
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'data'/'knowledge_base.json').read_text(encoding='utf8'))

def validate(d,strict_files=True):
 errors=[]; sources=d['sources']; wiki=d['entries']; slides=d['slides']
 source_ids=[s['id'] for s in sources]; wiki_ids=[w['id'] for w in wiki]
 if len(set(source_ids))<5:errors.append('source count < 5')
 if len(source_ids)!=len(set(source_ids)):errors.append('source ID duplicate')
 if len(wiki_ids)!=len(set(wiki_ids)):errors.append('Wiki ID duplicate')
 for w in wiki:
  if not w['sources']:errors.append(w['id']+' without source')
  for x in w['sources']:
   if x not in source_ids:errors.append(w['id']+' invalid source '+x)
 for p in slides:
  if not p['wiki']: errors.append(p['id']+' without Wiki')
  for x in p['wiki']:
   if x not in wiki_ids:errors.append(p['id']+' invalid Wiki '+x)
  for x in p['sources']:
   if x not in source_ids:errors.append(p['id']+' invalid source '+x)
  referenced={x for w in wiki if w['id'] in p['wiki'] for x in w['sources']}
  for x in p['sources']:
   if x not in referenced:errors.append(p['id']+' source '+x+' not supported by its Wiki')
 if strict_files:
  src_files=list((ROOT/'sources').glob('S*.md'))
  if len(src_files)!=len(sources):errors.append('Source Markdown count incorrect')
  if len(list((ROOT/'wiki').glob('W*.md')))!=len(wiki):errors.append('Wiki Markdown count incorrect')
  for name in ['index.html','wiki.html','slides.html','workflow.html','assets/site.css','assets/slides.css','assets/slides.js','assets/workflow.png']:
   if not (ROOT/name).exists():errors.append('File missing '+name)
  soup=BeautifulSoup((ROOT/'slides.html').read_text('utf8'),'html.parser')
  blocks=soup.select('section.slide')
  if len(blocks)!=len(slides):errors.append('slide count mismatch')
  for b,p in zip(blocks,slides):
   if b.get('data-slide')!=p['id']:errors.append('slide id mismatch '+p['id'])
   if set(b.get('data-wiki','').split(','))!=set(p['wiki']):errors.append('slide Wiki HTML mismatch '+p['id'])
   if set(b.get('data-sources','').split(','))!=set(p['sources']):errors.append('slide source HTML mismatch '+p['id'])
 return errors

errors=validate(data)
print('VALIDATION: sources=',len(data['sources']),'wiki=',len(data['entries']),'slides=',len(data['slides']))
print('FINAL RESULT:', 'PASS' if not errors else 'FAIL')
for e in errors:print(' -',e)
# Intentional fault injection for loop check (does not modify final project)
broken=copy.deepcopy(data)
broken['slides'][0]['wiki']=['W99']
faults=validate(broken,strict_files=False)
print('FAULT INJECTION:', 'PASS (invalid Wiki ID was blocked)' if 'P01 invalid Wiki W99' in faults else 'FAIL')
print('FAULT DETAIL:',faults)
res={'date':'2026-11-24','sources':len(data['sources']),'wiki':len(data['entries']),'slides':len(data['slides']),'validation':'PASS' if not errors else 'FAIL','validation_errors':errors,'fault_injection':'PASS' if 'P01 invalid Wiki W99' in faults else 'FAIL','fault_injection_errors':faults}
(ROOT/'tests'/'test_report.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf8')
sys.exit(1 if errors else 0)
