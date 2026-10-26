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

Quarto/Pandoc 会提示 `zh-CN` 翻译资源和 Abstract 术语警告；实际中文页面与 PDF 的“摘要”已核对显示正常。原始检查材料保存在被忽略的 `output/` 中，不提交为研究数据。

## 线上检查

尚待完成：GitHub Pages 部署、公开网址及 PDF 下载、真实仓库回传通路。完成后在此记录具体链接和结果。

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

Quarto/Pandoc emits warnings about the `zh-CN` translation resource and the Abstract term. The actual Chinese abstract heading was checked and displays correctly. Raw verification materials remain in ignored `output/`, outside research data.

## Online checks

Pending: GitHub Pages deployment, public URLs and PDF downloads, and the repository return path. Concrete links and results will be added after verification.

Not completed: real participant pilot responses, downloads on physical phones, reliability, validity, formal sample-size planning or independent methods review. The narrative form is not a validated scale. English participation guidance and the full English protocol are available; an English instrument has not been released.
