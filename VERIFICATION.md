# 发布检查记录 / Publication verification

检查日期 / Checked: **2026-10-27**。设计说明 / Guide: **0.4.0**；趣味问卷 / Instrument: **0.3**，修订 / revision `2026-10-26.fun.1`。

本记录描述内部技术和内容核对。检查与翻译由 Codex 辅助完成，不代表母语者审查、独立同行评审或心理测量验证。所有填答测试均使用 `TEST_ONLY` 内容，未作为真人参与或研究样本提交。

## 当前版本

- 项目围绕真实的日常 AI 用法、聊天习惯、评价、吐槽与故事展开。介绍写明调查目的、参与方式及计划产出，不预设获胜人格，也不声称已有参与者统计结果。
- 提供简体中文、英语、日语、韩语、西班牙语、法语、德语、葡萄牙语、俄语、阿拉伯语、印地语、印度尼西亚语的完整问卷、题目目的、回传入口、主页、设计说明和同源 PDF。
- 选择版共 19 项、故事版共 11 项，共享 7 项，共 23 个不同题项。总数包含条件与可选题；近期非使用者及 MBTI 不确定者可以参加。
- 旧 v0.2 单任务问卷保留在独立入口，回传与新 v0.3 日常习惯记录分开。旧技术记录中的 49/34 题、`case_id` 和“尚无英文问卷”仅适用于旧版。

## 本地核对

- 完成 12 语言 × 两种问卷 × 近期使用/未使用两条路线，共 48 次填答与导出检查。已知 MBTI 的测试路线实际导出 18/10/8/7 项，其余记录为不适用，符合总题数。
- 完成 12 次草稿保存和恢复，核对切换语言保留回答并重新确认参与条款、切换形式保留同一 `response_id`、隐藏旧答案不导出。
- 核对必答校验、不确定类型跳题、互斥选项、设计目的展开记录、错误草稿保留原内容、文字按普通文本显示。离线填写、导出未产生答案上传请求。
- 24 个主页/设计说明页面在 390 与 1440 像素宽度下无整体横向溢出，相对链接可访问；各语言具有对应 canonical 和 12 个 hreflang。
- 本地 12 份 PDF 共 34 页，全部渲染并逐页查看；文字可提取，无空页、替换字形或越界文本。已修正重复参考资料标题、阿拉伯语数字范围及英文/印度尼西亚语参考资料标题分页。
- 发布检查、完整构建、脚本语法和 diff 检查通过；公开范围不包含测试回答、缓存、凭据或工作区其他论文。问卷锁定记录和设计说明审阅指纹对应受检文件。

Quarto 仍提示 `zh-CN` 翻译资源警告；已检查实际中文摘要标签与正文显示。原始截图和测试文件保存在忽略的 `output/`，不是研究数据。

## 线上核对

- 仓库：[lawyer112/mbti-ai-open-study](https://github.com/lawyer112/mbti-ai-open-study)；网站：[调查主页](https://lawyer112.github.io/mbti-ai-open-study/)。公开署名 `lawyer112`。
- 问卷与完整改版提交：`1a47d18d17dec42aa17c68a9c58cc42ec7d7957b`。[检查](https://github.com/lawyer112/mbti-ai-open-study/actions/runs/40358339321)与[部署](https://github.com/lawyer112/mbti-ai-open-study/actions/runs/40358369013)成功。
- 最终英文 PDF 分页修正提交：`d57d0780c7d5bdfc6028e83b90117b10d789429c`。[检查](https://github.com/lawyer112/mbti-ai-open-study/actions/runs/40360093294)与[部署](https://github.com/lawyer112/mbti-ai-open-study/actions/runs/40360142294)成功。修正后重新下载并查看英文 PDF；参考资料标题与正文在同一页。
- 实际访问 62 个线上资源：新版与旧版 HTML 问卷，以及各语言主页、设计说明、PDF 和两份可读问卷，均返回 HTTP 200。线上新版 HTML 问卷与受检源文件字节相同。
- 在线上中文、英文、日文、韩文、阿拉伯文、印地文各完成选择版与故事版，下载 JSON 和 Markdown；确认报告编号一致、语言正确、无浏览器脚本错误，移动宽度无整体横向溢出。
- 下载并查看 12 份线上 PDF，共 33 页，文本提取和边界检查通过。Linux 与本地 Windows 字体造成页数或换行差异，内容来自同一份各语言源文件。
- 初次发布时曾创建、回读并关闭[旧版技术测试 Issue #1](https://github.com/lawyer112/mbti-ai-open-study/issues/1)，标签为 `test-only` 和 `excluded`。它验证仓库接收与回读，不是真实参与或同意；本次没有把自动化填答重新提交为参与者数据。

未验证：真实参与者试填、手机实机下载、12 种译文的母语认知访谈、跨文化可比性、信效度或因果结论。网页登录后的附件上传和测试 PR 未专门执行。先分别报告语言、版本及自愿样本；任何正式推断另需适用的研究设计。

## English verification record

These are Codex-assisted internal technical and content checks, not native-speaker review, independent peer review or psychometric validation. All automated responses are `TEST_ONLY` fixtures, excluded from research data and never represented as human participation or consent.

- The informal survey concerns everyday AI use, conversations, opinions, complaints and stories. Its introductions explain the purpose, participation and planned outputs. No preferred personality type or participant findings are claimed.
- All 12 languages above include complete questionnaires, item purposes, return routes, homepages, guides and matching PDFs. Instrument v0.3 has 19 choice items, 11 story items, 7 shared and 23 distinct; totals include conditional and optional items. Recent nonusers and uncertain types are welcome. Legacy v0.2 single-task records remain separate.
- Local checks completed 48 language/mode/usage-route export flows and 12 draft roundtrips. Conditional totals, required fields, exclusive options, purpose exposure, invalid-import retention, literal text display, shared response IDs and renewed consent after language changes passed. The offline flow did not upload answers.
- All 24 home/guide pages passed 390/1440-pixel width and relative-link checks, with language-specific canonical URLs and 12 hreflang links. All 34 pages across 12 local PDFs were rendered and visually inspected; text extraction and page bounds passed. Release checks, full build, script syntax, diff and public-scope checks passed. A Quarto Chinese-resource warning remains, but the visible Chinese abstract label and body were verified.
- The redesign and final layout commits, checks and deployments are linked above. All 62 live assets returned HTTP 200; the live questionnaire matched the reviewed source byte for byte. Both live modes and Markdown export passed in Chinese, English, Japanese, Korean, Arabic and Hindi, without script errors or whole-page mobile overflow.
- All 12 downloaded Linux-built PDFs were checked visually and for searchable text/page bounds, totaling 33 pages. Font differences explain local/live pagination differences. The final English reference-heading correction was re-downloaded and visually confirmed.
- The closed legacy technical Issue #1 only verifies repository receipt/read-back and remains excluded. Browser attachment uploading after sign-in, a test PR, physical-phone downloads, human pilot responses, native-speaker cognitive interviews, cross-cultural comparability, reliability, validity and causal claims have not been validated. Report language, version and volunteer-sample boundaries explicitly; formal inference needs an appropriate additional design.

The earlier v0.2 verification record remains in [Git history](https://github.com/lawyer112/mbti-ai-open-study/blob/1a47d18d17dec42aa17c68a9c58cc42ec7d7957b/VERIFICATION.md); its former item counts and English-instrument status do not describe this release.
