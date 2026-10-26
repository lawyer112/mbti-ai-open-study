"""生成不依赖服务器的 HTML，以及带逐题目的说明的两版问卷。"""
from pathlib import Path
import json
from questionnaire_items import DATA

ROOT = Path(__file__).resolve().parents[1]
SURVEY = ROOT / "survey"

def selected(mode):
    return [g for g in DATA['groups'] if g['mode'] in ['shared', mode]]

def build():
    all_items = [q for g in DATA['groups'] for q in g['items']]
    ids = [q['id'] for q in all_items]
    assert len(ids) == len(set(ids)), '题号重复'
    for q in all_items:
        assert q['purpose'] and q['title']
        if 'show_if' in q:
            assert q['show_if']['id'] in ids
    payload = json.dumps(DATA, ensure_ascii=False).replace('<', '\\u003c').replace('&', '\\u0026')
    template = (SURVEY / 'page.template.html').read_text(encoding='utf-8')
    (SURVEY / 'index.html').write_text(template.replace('__QUESTIONNAIRE_DATA__', payload), encoding='utf-8', newline='\n')
    for mode, label in [('choice', '选择题版'), ('text', '文字版')]:
        groups = selected(mode)
        items = [q for g in groups for q in g['items']]
        lines = [f'# {DATA["title"]} · {label} v{DATA["version"]}', '',
            '试填稿。研究问题：人格偏好与 AI 使用过程有什么关系？本问卷不测定 MBTI，也不产生人格优劣排名。', '',
            '请回顾最近30天内最近一次已经结束或决定暂停的真实 AI 任务；成功、失败、未完成都可以。所有题围绕同一次任务。首次参与任选一版；如补填另一版，沿用同一报告编号，并注明顺序。', '',
            '下面同时展示题目与研究目的，供审阅和协作。网页填写时研究目的默认折叠；主动查看会记录为方法信息。', '',
            '## 参与确认', '']
        lines += [f'- [ ] {c}' for c in DATA['consents']]
        lines += ['', f'共{len(items)}个题项，含背景、人格、可选补充及条件题；符合跳题条件才回答。耗时待试填验证。', '',
                  '- 研究代号：见 B01', '- 报告编号：网页自动生成；手工提交请自定并沿用，例如“研究代号-任务日期-01”。',
                  '- 是否已经看过另一版：', '- 是否查看本文件的逐题研究目的：是（本文件同时展示）。', '']
        for g in groups:
            lines += [f'## {g["title"]}', '', g['intro'], '']
            for q in g['items']:
                optional = '必答' if q['required'] else '可选'
                kind = {'radio':'单选','select':'单选','multi':'多选','short':'简答','long':'文字'}[q['kind']]
                lines += [f'### {q["id"]} {q["title"]}（{kind}；{optional}）', '']
                if q.get('show_if'):
                    dep=q['show_if']; parent=next(x for x in all_items if x['id']==dep['id'])
                    key = 'equals' if 'equals' in dep else 'not_equals'
                    label2=next(o['label'] for o in parent['options'] if o['value']==dep[key])
                    lines += [f'仅在 {dep["id"]} 已回答且{ "选择" if key=="equals" else "未选择" }“{label2}”时回答。', '']
                if q['hint']: lines += [q['hint'], '']
                if q.get('options'):
                    lines += [f'- [ ] {o["label"]}' for o in q['options']]
                    if q.get('exclusive'):
                        labels=[o['label'] for o in q['options'] if o['value'] in q['exclusive']]
                        lines += ['', '互斥选项：'+'、'.join(labels)+'；任一互斥项不可与其他项同时选择。']
                else: lines += ['回答：', '']
                lines += ['', f'**设计目的：** {q["purpose"]}', '']
        lines += ['## 回传', '', '网页填写可导出 JSON 与 Markdown；在个人问卷回传 Issue 中附文件，或通过 PR 提交。直接填写本 Markdown 也可以，但维护者需核对并人工结构化。不要回传含私人内容的完整聊天记录。', '']
        (SURVEY / f'{mode}-questionnaire.md').write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    print(json.dumps({'version':DATA['version'], 'choice_items':sum(len(g['items']) for g in selected('choice')),
                      'text_items':sum(len(g['items']) for g in selected('text')),
                      'outputs':['survey/index.html','survey/choice-questionnaire.md','survey/text-questionnaire.md']}, ensure_ascii=False))

if __name__ == '__main__':
    build()
