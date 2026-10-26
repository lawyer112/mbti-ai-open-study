"""Compact authored translations. IDs, option order and routing stay in one source."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def from_lines(code, ui_lines, group_lines, consents, rows):
    english = json.loads((ROOT/'survey/locales/en.json').read_text(encoding='utf-8'))
    values = ui_lines.strip().splitlines()
    assert len(values) == len(english['ui']), (code, 'UI', len(values))
    ui = dict(zip(english['ui'], values))
    ui['return_steps'] = ui['return_steps'].split('¦')
    assert len(ui['return_steps']) == 3
    values = [s.split('¦') for s in group_lines.strip().splitlines()]
    assert len(values) == len(english['groups']) and all(len(v)==2 for v in values)
    save(code, ui, dict(zip(english['groups'], values)), consents.strip().splitlines(), rows)

def save(code, ui, groups, consents, rows):
    items = {}
    for line in rows.strip().splitlines():
        parts = line.split('\t')
        if len(parts) != 5:
            raise ValueError((code, line, len(parts)))
        qid, title, purpose, hint, options = parts
        items[qid] = {'title': title, 'purpose': purpose, 'hint': '' if hint == '-' else hint}
        if options != '-':
            items[qid]['options'] = options.split('|')
    data = {'ui': ui, 'groups': groups, 'consents': consents, 'items': items}
    (ROOT/'survey/locales'/f'{code}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
