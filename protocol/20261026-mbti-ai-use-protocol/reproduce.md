# 复现与构建 / Reproduction and build

没有真人统计结果或功效计算。题数来自 `scripts/survey_items_v03.py`：选择题 19 项、故事版 11 项，共享 7 项，23 个不同题项。`survey/locales/` 提供 12 语种的文字，选项编码和条件规则共享。TEST_ONLY 是界面检查材料，排除于数据和公开包。

No participant statistics or power analysis exist. `scripts/survey_items_v03.py` defines 19 choice items, 11 story items, 7 shared and 23 distinct. `survey/locales/` supplies 12 languages with shared option codes and routing. TEST_ONLY fixtures are excluded from participant data and public source control.

```text
python -m pip install -r requirements.txt
python scripts/build_questionnaires.py
python scripts/check_publication.py --release
python scripts/build_site.py
```

使用 Python 3.12+、Quarto 1.10.19、PyYAML 6.0.3。Quarto 不在 PATH 时设置 QUARTO_BIN。Windows 使用 Arial、Noto Sans SC、Yu Gothic、Malgun Gothic、Nirmala UI；Linux 安装 fonts-liberation、fonts-noto-cjk、fonts-noto-core。输出 `_site/` 包含 12 介绍、12 设计说明和 PDF、独立 HTML 问卷、24 Markdown 问卷及旧版入口。

Use Python 3.12+, Quarto 1.10.19 and PyYAML 6.0.3; set QUARTO_BIN if needed. Windows fonts: Arial, Noto Sans SC, Yu Gothic, Malgun Gothic and Nirmala UI. Linux packages: fonts-liberation, fonts-noto-cjk and fonts-noto-core. `_site/` contains 12 introductions, 12 guides/PDFs, the standalone form, 24 Markdown forms and the legacy route.

`--preview` 仅用于检查，跳过尚待完成的验收锁，不能据此发布。正式构建核验 review.json 和 instrument-lock.json。实际核验后才能更新指纹。发布为手动工作流，推送后的检查工作流不自动部署。

`--preview` is for inspection only and bypasses pending review locks; it does not authorize release. Release builds check review.json and instrument-lock.json. Update fingerprints only after actual checks. Deployment is manual; push/PR checks do not deploy.

实际验证包括各语言的近期用户/非使用者两种模式、必答项、互斥、草稿恢复、语言切换和导出，桌面/手机阅读、内部链接、PDF 逐页显示、公开范围。未进行真人问卷试填、母语者访谈或测量验证，不能以工具测试替代。

Actual checks cover each language's user/nonuser routes in both modes, required and exclusive fields, drafts, switching and exports; desktop/mobile reading, links, every PDF page and public scope. These do not replace a human pilot, native-speaker interviews or measurement validation, none of which has been completed.
