"""Build the reviewed protocol and the pilot survey; never deploy automatically."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from check_publication import check_all, ROOT

PINNED_QUARTO = '1.10.19'
ARTICLE = ROOT / 'protocol' / '20261026-mbti-ai-use-protocol'

def check_instrument():
    expected = json.loads((ARTICLE / 'instrument-lock.json').read_text(encoding='utf-8'))
    for filename, digest in expected['files_sha256'].items():
        actual = hashlib.sha256((ROOT / filename).read_bytes()).hexdigest()
        if actual != digest:
            raise SystemExit(f'Instrument changed since protocol review: {filename}')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview', action='store_true', help='Local layout inspection before review; cannot approve a release.')
    args = parser.parse_args()
    subprocess.run([sys.executable, str(ROOT/'scripts/build_questionnaires.py')], cwd=ROOT, check=True)
    if not args.preview:
        check_instrument()
    if not args.preview:
        _, errors = check_all(release=True)
        if errors:
            raise SystemExit('\n'.join(errors))
    executable = os.environ.get('QUARTO_BIN') or shutil.which('quarto')
    if not executable:
        raise SystemExit('Install Quarto 1.10.19, or set QUARTO_BIN to its executable.')
    command = [executable]
    if os.name == 'nt' and executable.lower().endswith(('.cmd','.bat')):
        command = [os.environ.get('COMSPEC','cmd.exe'), '/d', '/c', executable]
    version = subprocess.check_output(command+['--version'], text=True).strip()
    if version != PINNED_QUARTO:
        raise SystemExit(f'Expected Quarto {PINNED_QUARTO}, got {version}')
    fonts = '"Arial", "Noto Sans SC", "Yu Gothic", "Malgun Gothic", "Nirmala UI"' if os.name=='nt' else '"Liberation Sans", "Noto Sans CJK SC", "Noto Sans CJK JP", "Noto Sans CJK KR", "Noto Sans Arabic", "Noto Sans Devanagari"'
    metadata = '''format:
  html:
    toc: true
    toc-depth: 3
  typst:
    papersize: a4
    fontsize: 11pt
    margin:
      left: 22mm
      right: 22mm
      top: 20mm
      bottom: 20mm
    toc: false
    number-sections: false
    include-in-header:
      text: |
        #set text(font: (FONTS))
        #set table.cell(breakable: false)
        #show table.cell: set par(justify: false)
        #set bibliography(title: none)
        #show bibliography: set text(dir: ltr)
        #show bibliography: set align(left)
'''.replace('FONTS',fonts)
    (ROOT/'protocol/_metadata.yml').write_text(metadata,encoding='utf-8')
    subprocess.run(command+['render','--to','all'],cwd=ROOT,check=True)
    site=ROOT/'_site'
    expected_files=['survey/index.html','survey/v0.2/index.html']
    for language in json.loads((ROOT/'survey/languages.json').read_text(encoding='utf-8')):
        code=language['code'];stem='zh' if code=='zh-CN' else code
        expected_files.append('index.html' if code=='zh-CN' else code+'/index.html')
        expected_files.extend(f'protocol/{ARTICLE.name}/{stem}.{ext}' for ext in ['html','pdf'])
        expected_files.extend(f'survey/{code}/{mode}-questionnaire.md' for mode in ['choice','text'])
    for filename in expected_files:
        if not (site/filename).is_file():
            raise SystemExit(f'Missing built file: {filename}')
    print('Built 12 complete survey guides/PDFs, homepages and offline questionnaires.')

if __name__=='__main__':
    main()
