# 数据整理 / Data handling

## 中文

当前没有本项目真人统计结果。生成答案、界面测试和独立研究的汇总人数不能充当本问卷样本。个人 PR 放 `submissions/individual/`，独立研究放 `submissions/studies/`，Issue 保留来源。实际使用时再建 `data/derived/`、`analysis/` 和 `paper/`，不预填结果。

正式导出 `kind=mbti-ai-response`，保留 `response_id`、`schema_version`、`record_protocol=everyday-ai-habits-recent30-v0.3`、`questionnaire_mode`、`instrument_language`、`instrument_revision`、`exported_at`、`collection_stage`、`consent`、`answers`、`answer_labels`、`not_applicable`、`answer_ui_language` 与 `method`。method 包含模式顺序、目的展示、语言历史、自报性质和验证状态。导出时间不是提交时间。

维护者另记来源、参与轮次、内部参与者关联、审核状态和更正。一个报告 ID 可有两版；同一人重建 ID、Issue 转 PR、更正和补充都要核对，不能按报告条数算人数。账号也不保证一人一号，无法确认的重叠注明不确定。来源可关联账号，不能称匿名数据。

编码不是分数，必须结合版本及标签。未答、不适用、记不清、明确没有分别保存，不填 0。统计展示每题有效分母；多选比例可超过 100%。故事和选择题不能合成总分，满意度不能变成正确率或工作增益。文字保留相反意见和例外。

语言和版本先分层，译文未经母语者认知访谈或等价验证。旧 v0.2 的 case_id/task_protocol 描述单项任务，不能换字段后视为 v0.3 日常习惯。试填与后续正式轮次也分开，合并须有依据。

草稿 `kind=mbti-ai-draft` 不是已确认投稿。所有 TEST_ONLY、test-only、excluded、withdrawn 材料排除；格式完整或勾选不能让测试变真人。A06 说明 AI 写作帮助不自动排除真实参与，但不能编造经历。

先发布获准的汇总；引用核对 A05；个体数据再发布另查许可。公开原投稿仍可关联账号，分析表去用户名不让它追溯性变匿名。撤回影响后续分析，不能保证收回互联网副本。

## English

No human participant statistics are reported. Generated answers, interface fixtures and aggregate study counts are not questionnaire participants. Individual PRs use `submissions/individual/`, separate studies use `submissions/studies/`, and Issues retain provenance. Create `data/derived/`, `analysis/` and `paper/` only when needed, without invented findings.

Exports use `kind=mbti-ai-response`. Retain `response_id`, `schema_version`, `record_protocol=everyday-ai-habits-recent30-v0.3`, `questionnaire_mode`, `instrument_language`, `instrument_revision`, `exported_at`, `collection_stage`, `consent`, `answers`, `answer_labels`, `not_applicable`, `answer_ui_language` and `method`. Method records form order, purpose exposure, language history, self-report and validation status. Export time is not submission time.

Maintain provenance, participation round, internal participant linkage, review state and corrections. One ID can contain both forms. Check regenerated IDs, Issue/PR duplicates, supplements and corrections; report counts are not person counts. Accounts do not guarantee one person per account. State uncertain overlap. Provenance may identify accounts, so do not call records anonymous.

Codes are not scores; interpret them with version and labels. Missing, inapplicable, uncertain and explicit absence remain separate, never filled with zero. Show each item's valid denominator; multiple-choice percentages may exceed 100%. Do not combine stories and choices into a total score or turn satisfaction into accuracy or productivity. Preserve opposing stories and exceptions.

Stratify by language and version first; translations lack native-speaker cognitive interviews and equivalence validation. Old v0.2 case_id/task_protocol records concern one task, not v0.3 everyday habits. Renaming fields does not make them equivalent. Separate pilot and later formal rounds and justify pooling.

`kind=mbti-ai-draft` is not a confirmed submission. Exclude all TEST_ONLY, test-only, excluded and withdrawn material; complete formatting and confirmations do not make tests into people. A06 AI writing help does not automatically exclude real participation, but invented experiences are unacceptable.

Publish authorized aggregates first; check A05 for quotations and separate permissions for individual-data releases. Public originals may identify accounts; removing usernames from tables cannot retroactively anonymize them. Withdrawal affects later analysis, without promising recall of internet copies.
