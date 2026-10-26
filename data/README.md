# 数据整理规范

目前没有参与者数据，不放模拟样本充当真实提交。

## 分层保存

- `submissions/individual/`：通过PR接收的个人报告；Issue报告保留来源链接。
- `submissions/studies/`：独立调研报告与方法。
- `data/derived/`：维护者依据问卷规则整理的结构化数据。首次发布前明确授权范围、数据字典和版本。
- `analysis/`：后续可复现分析脚本与运行说明。
- `paper/`：有数据后逐步形成的论文与版本记录。

这些目录按首次实际使用时建立，不预填结果。

## 记录原则

保留report_id、participant_code、来源、问卷版本、记录时间、审核状态与更正历史。来源链接本身可能关联GitHub账号，不能称为匿名数据。面向统计的表不直接使用用户名，不携带对话中的联系方式或私人文本。

v0.2另保留case_id、questionnaire_mode、task_protocol、purpose_viewed及浏览问卷顺序；公开表单同时标记instrument_language=zh-CN和collection_stage=pilot。正式导出kind为mbti-ai-response；kind为mbti-ai-draft的草稿不纳入。选择题与文字题针对同一任务时关联同一case_id，共同信息若冲突需核对更正。题库中的字符串选项编号只是编码，不是分数；必须结合版本与标签解释。

题目未填、跳题不适用、记不清与明确没有分别保存。两种模式的回答分别分析，不因主题对应就直接混算量表。试填和正式数据分开；旧v0.1与v0.2不得静默合并。

output/中若出现TEST_ONLY文件，仅为界面检查材料，不是参与者数据，禁止纳入分析。公开Issue或PR中明确标注TEST_ONLY、test-only或excluded的测试记录同样排除，不因格式完整、具有case_id或出现勾选确认就视为真人参与。

不得用报告条数代替参与人数，不把同一内容的Issue与PR重复计入，不把一篇调研报告当作一名参与者。原报告、人工编码和统计结果分开保存；缺失不填0。

公开数据集与论文中的逐字引文分别核对许可；默认先发布获准的汇总统计。个人提交的同意范围不自动等于第三方可无限再利用。

## English

This release contains no real participant dataset. Do not substitute simulated or generated responses for participants.

Use submissions/individual/ for individual reports submitted by pull request, preserving source links for Issue reports; submissions/studies/ for separate studies; data/derived/ for checked structured records; analysis/ for reproducible analyses; and paper/ for later empirical manuscripts. Create these directories when actual materials exist, without placeholder findings. The current protocol is separately available under protocol/.

Keep report_id, participant_code, provenance, version, recording dates, review state and corrections. v0.2 also retains case_id, questionnaire_mode, task_protocol, purpose_viewed and form-viewing order; the public form adds instrument_language=zh-CN and collection_stage=pilot. Provenance can identify GitHub accounts, so do not call the data anonymous. Statistical tables should omit account names, contact details and private conversation content.

Only kind=mbti-ai-response is a formal exported response. A saved draft with kind=mbti-ai-draft is not a submission. Link both forms for the same task by case_id and resolve conflicts in shared information. String option IDs are version-specific codes, not scores; interpret them with labels and the instrument version.

Count participants, tasks, forms and separate studies distinctly. Do not count an Issue and its pull request twice, or treat one study report as one participant. Keep raw reports, coding and statistical outputs separate. Missing, inapplicable, uncertain and explicit absence are distinct. Do not combine the two forms as equivalent scales, mix pilot and formal records, or silently pool v0.1 and v0.2 anchors.

TEST_ONLY files under output/ are interface fixtures excluded from public source control and all analyses. Test records in public Issues or pull requests marked TEST_ONLY, test-only, or excluded must also be excluded. A complete format, case_id or checked confirmations does not turn a fixture into human participation. Dataset redistribution and verbatim quotations require separate permission checks; begin with authorized aggregate results. A person's participation consent is not unlimited third-party reuse permission.
