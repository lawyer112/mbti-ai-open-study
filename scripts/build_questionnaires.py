"""Build complete, offline, localized questionnaires from one shared item schema."""
from pathlib import Path
import argparse
import copy
import json
import re
import yaml
from survey_items_v03 import DATA

ROOT=Path(__file__).resolve().parents[1]
SURVEY=ROOT/'survey'
REVISION='2026-10-26.fun.1'

def localized(code):
    pack=json.loads((SURVEY/'locales'/f'{code}.json').read_text(encoding='utf-8'))
    en=json.loads((SURVEY/'locales/en.json').read_text(encoding='utf-8'))
    assert set(pack['ui'])==set(en['ui']), (code,'UI keys')
    assert len(pack['consents'])==3 and all(pack['consents'])
    for key,value in pack['ui'].items():
        assert type(value)==type(en['ui'][key]) and value,(code,key)
        source=' '.join(en['ui'][key]) if isinstance(value,list) else en['ui'][key]
        target=' '.join(value) if isinstance(value,list) else value
        assert set(re.findall(r'\{\w+\}',source))==set(re.findall(r'\{\w+\}',target)),(code,key,'variables')
    bank=copy.deepcopy(DATA);bank['title']=pack['ui']['title'];bank['ui']=pack['ui'];bank['consents']=pack['consents']
    assert set(pack['groups'])=={g['id'] for g in bank['groups']}
    assert set(pack['items'])=={q['id'] for g in bank['groups'] for q in g['items']}
    for group in bank['groups']:
        group['title'],group['intro']=pack['groups'][group['id']]
        for q in group['items']:
            local=pack['items'][q['id']]
            assert set(local)==({'title','purpose','hint','options'} if q.get('options') else {'title','purpose','hint'}),(code,q['id'],'keys')
            for key in ['title','purpose','hint']:
                assert bool(local[key])==bool(q[key]),(code,q['id'],key)
                q[key]=local[key]
            if q.get('options'):
                assert len(local['options'])==len(q['options']),(code,q['id'],'option count')
                assert all(local['options'])
                for option,label in zip(q['options'],local['options']):option['label']=label
                if q['id']=='A01':assert local['options'][:16]==[o['label'] for g in DATA['groups'] for item in g['items'] if item['id']=='A01' for o in item['options']][:16]
    return bank

def readable(bank,code,mode):
    ui=bank['ui'];groups=[g for g in bank['groups'] if g['mode'] in ['shared',mode]];all_items={q['id']:q for g in bank['groups'] for q in g['items']}
    lines=[f"# {bank['title']} · {ui[mode]} v{bank['version']}",'',ui['mdintro'],'',ui['entrytext'],'',ui['mdexposure'],'',f"## {ui['consent']}",'']
    lines += [f'- [ ] {s}' for s in bank['consents']]
    lines += ['',ui['item_count'].format(n=sum(len(g['items']) for g in groups)),'',f"- {ui['language']}: {code}",f"- {ui['case_label']}:",f"- {ui['modeorder']}:",f"- {ui['purposeviewed']}: {ui['mdexposure']}",'']
    for group in groups:
        lines += [f"## {group['title']}",'',group['intro'],'']
        for q in group['items']:
            lines += [f"### {q['id']} {q['title']} ({ui['required' if q['required'] else 'optional']})",'']
            if q.get('show_if'):
                dep=q['show_if'];key='equals' if 'equals' in dep else 'not_equals';label=next(o['label'] for o in all_items[dep['id']]['options'] if o['value']==dep[key])
                lines += [ui['condition_equal' if key=='equals' else 'condition_not_equal'].format(id=dep['id'],label=label),'']
            if q['hint']:lines += [q['hint'],'']
            if q.get('options'):
                lines += [f"- [ ] {o['label']}" for o in q['options']]
                if q.get('exclusive'):lines += ['',ui['exclusive'].format(labels=' / '.join(o['label'] for o in q['options'] if o['value'] in q['exclusive']))]
            else:lines += [ui['answer']+':','']
            lines += ['',f"**{ui['purpose']}** {q['purpose']}",'']
    lines += [f"## {ui['return']}",'',*ui['return_steps'],'',ui['privacy'],'',ui['reportnote'],'']
    return '\n'.join(lines)

def issue_forms(bank,code):
    ui=bank['ui'];suffix='' if code=='zh-CN' else '-'+code
    intro='\n\n'.join([ui['mdintro'],ui['privacy'],*ui['return_steps'],f'https://lawyer112.github.io/mbti-ai-open-study/survey/index.html?lang={code}'])
    body=[{'type':'markdown','attributes':{'value':intro}}]
    for item,label,desc in [('case-id','case_label',ui['case']),('schema-version','version','0.3')]:
        attrs={'label':ui[label],'description':desc}
        if item=='schema-version':attrs['value']='0.3'
        if item=='case-id':attrs['description']=ui['reportnote']
        body.append({'type':'input','id':item,'attributes':attrs,'validations':{'required':True}})
    body += [{'type':'dropdown','id':'questionnaire-mode','attributes':{'label':ui['mode_label'],'options':[ui['choice'],ui['text'],ui['choice']+' + '+ui['text']]},'validations':{'required':True}},
             {'type':'input','id':'instrument-language','attributes':{'label':ui['language'],'value':code},'validations':{'required':True}}]
    for item,key in [('report-files','files'),('amendments','corrections')]:body.append({'type':'textarea','id':item,'attributes':{'label':ui[key],'description':ui['submit_description'] if key=='files' else ui['reportnote']},'validations':{'required':item=='report-files'}})
    body.append({'type':'checkboxes','id':'confirmation','attributes':{'label':ui['consent'],'options':[{'label':c,'required':True} for c in bank['consents']]}})
    base=ROOT/'.github/ISSUE_TEMPLATE'
    forms=[('01-individual-report',ui['submit_title'],ui['submit_description'],body,'needs-review')]
    for stem,prefix in [('02-study-report','study'),('03-research-discussion','discussion')]:
        forms.append((stem,ui[prefix+'_title'],ui[prefix+'_description'],[{'type':'markdown','attributes':{'value':ui['privacy']}},{'type':'textarea','id':'report','attributes':{'label':ui[prefix+'_title'],'description':ui[prefix+'_body']},'validations':{'required':True}}], 'needs-review' if prefix=='study' else 'method-discussion'))
    for stem,name,description,form,label in forms:
        entry={'name':f'{code} · {name}','description':description,'title':f'[{code} v0.3] ','labels':[label],'body':form}
        assert len(entry['name'])<=64 and len(description)<=200,(code,stem,'GitHub limits')
        (base/f'{stem}{suffix}.yml').write_text(yaml.safe_dump(entry,allow_unicode=True,sort_keys=False,width=110),encoding='utf-8',newline='\n')

def build():
    parser=argparse.ArgumentParser();parser.add_argument('--preview-locales',help='Local preview only. Never use for publication.');args=parser.parse_args()
    languages=json.loads((SURVEY/'languages.json').read_text(encoding='utf-8'))
    if args.preview_locales:languages=[l for l in languages if l['code'] in args.preview_locales.split(',')]
    banks={l['code']:localized(l['code']) for l in languages}
    payload=json.dumps({'version':DATA['version'],'revision':REVISION,'languages':languages,'banks':banks},ensure_ascii=False).replace('<','\\u003c').replace('&','\\u0026')
    text=(SURVEY/'page.template.html').read_text(encoding='utf-8').replace('__SURVEY_CSS__',(SURVEY/'styles.css').read_text(encoding='utf-8')).replace('__SURVEY_JS__',(SURVEY/'app.js').read_text(encoding='utf-8')).replace('__QUESTIONNAIRE_DATA__',payload)
    (SURVEY/'index.html').write_text(text,encoding='utf-8',newline='\n')
    for code,bank in banks.items():
        folder=SURVEY/code;folder.mkdir(exist_ok=True)
        for mode in ['choice','text']:
            text=readable(bank,code,mode);(folder/f'{mode}-questionnaire.md').write_text(text,encoding='utf-8',newline='\n')
            if code=='zh-CN':(SURVEY/f'{mode}-questionnaire.md').write_text(text,encoding='utf-8',newline='\n')
        if not args.preview_locales:issue_forms(bank,code)
    print(json.dumps({'version':DATA['version'],'languages':list(banks),'items_per_language':23,'choice_items':19,'text_items':11,'preview':bool(args.preview_locales)}))

if __name__=='__main__':build()
