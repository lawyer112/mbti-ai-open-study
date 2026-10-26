# 发布检查记录 / Publication verification

检查日期 / Date: 2026-10-26。方案 / Protocol: 0.3.0；中文试填问卷 / Chinese pilot instrument: 0.2。

## 本地检查

检查由 Codex 辅助完成，属于内部技术与内容核对，不是独立同行评审，也不代表问卷已经完成心理测量验证。

- 已逐项核对研究问题、题号、编码和可支持的结论。全文未报告真实参与者结果，也未预设哪种人格最好。正式收集前还须根据试填情况冻结分析模型并规划样本量。
- 选择题共 49 题、文字题共 34 题；包括两版共享的 21 题。均可填写并导出 JSON 和可读 Markdown。测试使用明确标注 `TEST_ONLY` 的虚拟内容，不属于研究样本。
- 已验证参与确认、适用必答题、互斥选项、条件跳题及隐藏旧答案不导出；切换两版保留共同背景和同一 `case_id`，仅导出当前版内容。
- 已验证草稿保存、清空和恢复；错误草稿不会覆盖现有内容；每题设计目的可展开，暴露记录仅对应实际适用并展开的题目。
- 本地 HTML 可直接打开、恢复草稿和导出；没有自动上传或外部请求，未发现浏览器脚本错误。
- 中英文主页及完整方案、语言切换、下载入口已检查；五个网页在桌面与 390 像素宽度下没有页面整体横向溢出。英文宽表使用表内滚动。
- HTML 与 PDF 来自同一份各语言源文件。本地中文 PDF 为 4 页、英文为 6 页；逐页查看排版并检查文本可提取，未发现空白页或缺字。英文表格行跨页断裂已经修复。
- 已检查公开文件范围、相对链接、三类 Issue 表单及 PR 模板。构建、发布流程分离；发布需要手动启动，检查流程不会部署。
- 发布源文件设为 LF 换行，核对暂存版本与文件字节一致，避免跨平台哈希失配。方案审阅记录及问卷锁定文件保存对应源文件哈希。

Quarto/Pandoc 会提示 `zh-CN` 翻译资源和 Abstract 术语警告；实际中文页面与 PDF 的“摘要”已核对显示正常。原始检查材料保存在被忽略的 `output/` 中，不提交为研究数据；公开的技术回传测试单独标记，见下文。

## 线上检查

- 公开仓库：[lawyer112/mbti-ai-open-study](https://github.com/lawyer112/mbti-ai-open-study)，公开署名 `lawyer112`，默认分支 `main`，Issue 已启用。
- 网站：[研究主页](https://lawyer112.github.io/mbti-ai-open-study/)。Pages 使用 Actions 部署并强制 HTTPS；部署源提交为 `2a946a83d6e98a59b956939491eb93cfb918c6dd`。
- [源文件检查](https://github.com/lawyer112/mbti-ai-open-study/actions/runs/40335735945)与[部署运行](https://github.com/lawyer112/mbti-ai-open-study/actions/runs/40335772881)均成功。
- 已实际访问两种语言的主页、全文、PDF，以及 HTML 问卷与两份可读问卷，共 9 个网址，均返回 HTTP 200。线上 HTML 问卷与受检源文件字节完全相同。
- 线上五个网页分别以 1440 和 390 像素宽度打开，10 次检查均无整体横向溢出或脚本错误。
- 已在浏览器点击主页语言切换并往返成功；点击“下载独立 HTML 问卷”得到的文件与受检源文件完全一致。
- 自动化浏览器从线上问卷逐步填写两种模式，成功下载两份 JSON 和两份 Markdown；同一任务编号保持一致。此次每版各有一个不适用的条件题，实际导出 48/33 项，并分别保留在 `not_applicable`，符合 49/34 的总题数。
- 线上下载的两个 PDF 仍为中文 4 页、英文 6 页；逐页查看、文本可提取检查均通过。Linux 与 Windows 字体可能造成换行位置差异。
- 已通过真实仓库创建并回读[测试 Issue #1](https://github.com/lawyer112/mbti-ai-open-study/issues/1)，核对报告正文一致后关闭。该记录明确标为 `TEST_ONLY`，具有 `test-only` 和 `excluded` 标签；不是参与者提交或真实同意，不得进入任何研究统计。

回传验证使用 GitHub 命令行提交完整测试报告，验证了仓库接收和回读；未模拟网页登录后上传附件，也未专门创建测试 PR。两条贡献路径及其操作说明已经公开。

未完成：真实参与者试填、手机实机下载、信度与效度、正式样本量和独立方法审查。文字问卷不是已验证量表；英文参与说明与研究方案已提供，英文问卷尚未发布。

## Local checks

These are Codex-assisted internal content and technical checks, not independent peer review or psychometric validation.

- Research questions, item IDs, coding and supported conclusions were checked together. No real participant results or preferred personality type are claimed. Formal models and sample-size planning must be frozen after the pilot and before formal collection.
- The choice form has 49 items and the narrative form 34, including 21 shared items. Both export JSON and readable Markdown. All fixtures are explicitly `TEST_ONLY` and are excluded from research data.
- Consent, applicable required fields, exclusive choices, conditional routing and removal of hidden answers were checked. Switching forms preserves shared context and the same `case_id`; exports include only the active form.
- Draft saving, clearing and restoring work; invalid imports preserve existing responses. Item purposes are expandable, and exposure records only include applicable purposes actually opened.
- The standalone HTML works locally, including draft restoration and export, without automatic uploads, external requests or observed browser errors.
- Both homepages, full protocols, language switches and download links were checked. Five webpages passed desktop and 390-pixel viewport checks without whole-page horizontal overflow; wide English tables scroll within their own container.
- Each language's HTML and PDF are built from the same source. Local PDFs contain 4 Chinese pages and 6 English pages. Every page was visually inspected and text extraction checked; no blank pages or missing characters were observed. Split English table rows were corrected.
- Public file scope, relative links, the three Issue forms and PR template were checked. Checks do not deploy; publication is a separate manually triggered workflow.
- Published text uses LF endings. Staged and working-file bytes were compared. Review fingerprints and the instrument lock identify the reviewed sources.

Quarto/Pandoc emits warnings about the `zh-CN` translation resource and the Abstract term. The actual Chinese abstract heading was checked and displays correctly. Raw verification materials remain in ignored `output/`, outside research data. The public technical return test is separately marked below.

## Online checks

- Public repository: [lawyer112/mbti-ai-open-study](https://github.com/lawyer112/mbti-ai-open-study), with public byline `lawyer112`, default branch `main`, and Issues enabled.
- Website: [project home](https://lawyer112.github.io/mbti-ai-open-study/). Pages uses Actions deployment with HTTPS enforced. Deployed source commit: `2a946a83d6e98a59b956939491eb93cfb918c6dd`.
- Both the [source checks](https://github.com/lawyer112/mbti-ai-open-study/actions/runs/40335735945) and [deployment](https://github.com/lawyer112/mbti-ai-open-study/actions/runs/40335772881) succeeded.
- Nine URLs returned HTTP 200: both homepages, both complete protocols, both PDFs, the HTML questionnaire, and two readable questionnaires. The online questionnaire matches the checked source byte for byte.
- Five online webpages were opened at 1440 and 390 pixels: all ten checks passed without whole-page horizontal overflow or script errors.
- Browser clicks switched the homepages between languages and back. The standalone HTML download matched the checked questionnaire source exactly.
- An automated browser completed both online modes step by step and downloaded two JSON and two Markdown reports. The task ID remained unchanged. One conditional item was inapplicable in each mode, leaving 48/33 exported items plus `not_applicable`, consistent with the 49/34 totals.
- The downloaded live PDFs still contain 4 Chinese and 6 English pages. Every page was viewed and text extraction passed. Linux and Windows fonts may produce different line wrapping.
- [Technical test Issue #1](https://github.com/lawyer112/mbti-ai-open-study/issues/1) was created in the real repository, read back with an identical report body, and closed. It is explicitly `TEST_ONLY` and labeled `test-only` and `excluded`. It is neither a participant submission nor human consent and must never enter research statistics.

The return test submitted a complete fixture through the GitHub CLI and verified repository receipt and read-back. Browser attachment uploading after sign-in and a separate test pull request were not exercised. Both contribution pathways and their instructions are public.

Not completed: real participant pilot responses, downloads on physical phones, reliability, validity, formal sample-size planning or independent methods review. The narrative form is not a validated scale. English participation guidance and the full English protocol are available; an English instrument has not been released.
