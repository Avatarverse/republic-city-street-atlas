#!/usr/bin/env python3
"""Validate the public street register and embed it in the static HTML entry point."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'data.json').read_text(encoding='utf-8'))
ids = set()
for street in data['streets']:
    assert street['id'] not in ids, f"Duplicate section ID: {street['id']}"
    ids.add(street['id'])
    assert street['name'].strip(), f"Missing street name: {street['id']}"
    assert 0 <= street['x'] <= data['width'], street['id']
    assert 0 <= street['y'] <= data['height'], street['id']
    for x, y in street['points']:
        assert 0 <= x <= data['width'] and 0 <= y <= data['height'], street['id']
    assert not any(key in street for key in ('status', 'notes', 'originalName')), 'Public register must omit editor metadata'
for area in data['areas'].values():
    assert (ROOT / area['image']).is_file(), f"Missing map image: {area['image']}"

page = ROOT / 'index.html'
html = page.read_text(encoding='utf-8')
payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
pattern = r'(<script id="atlas-data" type="application/json">).*?(</script>)'
html, replaced = re.subn(pattern, lambda match: match[1] + payload + match[2], html, flags=re.S)
assert replaced == 1, 'Expected exactly one atlas-data script'
page.write_text(html, encoding='utf-8')
print(f"Validated and embedded {len(ids)} sections / {len({r['name'] for r in data['streets']})} streets.")
