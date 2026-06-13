from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
import sys

# If the GOOGLE_SCHOLAR_ID secret isn't configured, skip cleanly instead of
# crashing the workflow with a parse error from Google Scholar's response.
gs_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip()
if not gs_id:
    print('GOOGLE_SCHOLAR_ID secret is missing; skipping citation refresh.', file=sys.stderr)
    sys.exit(0)

author: dict = scholarly.search_author_id(gs_id)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
