# 提交与协作

## 提交个人报告

先打开[HTML 问卷](survey/index.html)，任选选择题版或文字版，填写并检查后导出 JSON 与 Markdown。在 Issues 中选择“个人问卷回传”，附上文件；也可粘贴导出的可读报告。不要回传问卷 HTML 或尚未脱敏的草稿。

通过 PR 贡献时，把导出的两个文件放到 `submissions/individual/`。文件名包含自动生成的报告编号与问卷类型，不放真实姓名。不能使用 HTML 时，可直接填写[选择题 Markdown](survey/choice-questionnaire.md)或[文字 Markdown](survey/text-questionnaire.md)，保留题号、版本、同意项和目的查看声明，由维护者核对后结构化。

两版任选其一，不要求都填。补填另一版应沿用同一报告编号，记录顺序；共同信息有修改时注明更正，维护者核对差异。不同问卷模式分别标记，不能当作两次独立任务。

同一人沿用同一代号。若报告已通过 Issue 提交，在 PR 中链接原 Issue；这只是补充材料，不重复计数。修改原报告时说明更正内容，保留来源与修改日期。

## 提交独立调研

在 Issues 中选择调研报告表单，或把[调研模板](templates/study-report.md)复制到 `submissions/studies/`。需说明样本、招募、人格测量、任务或问卷、分析方法、授权及与本项目既有记录的重叠情况。没有个体数据也可以提交，但应标为汇总报告。

## 改进方法与论文

使用研究讨论 Issue 提出问题。方法、问卷或论文修改通过 PR 说明改了什么、依据是什么、是否改变既有数据的解释。正式收集后的问卷变更提高版本号，不能静默改动。

## 维护者处理步骤

1. 核对参与确认、材料使用范围、类型测量来源、任务与模型信息。
2. 检查重复记录、补充材料及研究间样本重叠。
3. 必要时请求补充；仍缺关键字段时注明原因，保留在待补充池。
4. 接受后建立report_id，保留问卷case_id、版本和模式，按数据规范整理；仅接收正式报告，不把kind为mbti-ai-draft的文件当作已同意投稿。定量分析只纳入符合该项指标要求的记录。

建议维护标签：`needs-review`、`needs-info`、`accepted`、`excluded`、`withdrawn`、`method-discussion`。标签需建仓后创建；当前表单不依赖标签存在。

## 撤回与引用

可在原 Issue 或关联 PR 中申请撤回，不必公开说明理由，也不要为撤回再次上传私人材料。维护者从后续分析中排除并记录撤回状态；已被下载或分叉的内容不能保证收回。

允许本项目进行统计分析和论文汇总，不等于允许逐字引用或将材料任意再分发。逐字引用按提交者单独选择执行。对外发布数据集前需明确授权范围。贡献者名单依据本人意愿公开，论文作者署名按实际研究贡献讨论。

## English: participation and contribution

The pilot instrument is in Simplified Chinese, for volunteers aged 18 or older who understand it and have a real AI task from the previous 30 days. Open survey/index.html, choose either form, complete it, inspect your answers, and export JSON and Markdown. Attach them to a “个人问卷回传 / Return a questionnaire” Issue, or paste the complete readable report. Do not upload the blank HTML or an unconfirmed draft. Public submissions and attachments are associated with your GitHub account; remove private or confidential information before uploading.

For a pull request, put the exported files in submissions/individual/. Their filenames contain the case ID and mode, not a real name. If you cannot use HTML, complete the corresponding Chinese Markdown form while preserving item IDs, version, consent and quotation permission. State that its item purposes were visible. Maintainers must check and structure manual reports.

One form is sufficient. Retain your participant code across tasks and use the same case ID when adding the other form for one task. Record order and explain corrections to shared information. Link an earlier Issue or pull request instead of counting it twice. Corrections retain provenance and dates.

Independent studies use the study-report Issue or templates/study-report.md and submissions/studies/. Describe recruitment, sample, instruments, tasks, methods, permissions, and overlap with existing records. Aggregated reports without participant-level data are welcome but are not pooled as individual observations.

Use a discussion Issue for methodological questions and a pull request for instrument, analysis or manuscript changes. Explain the evidence and implications. Changes after formal collection starts require a new version rather than silent edits. Synchronize the complete Chinese and English protocol when methods or conclusions change.

Maintainers check consent, permitted uses, measurement source, task/model information, duplicates, and study overlap. They may request clarification and keep incomplete material pending. Accepted records receive report_id while retaining case_id, version and mode. Files with kind=mbti-ai-draft are not consented research submissions. Each analysis includes only records eligible for that indicator. Suggested labels are needs-review, needs-info, accepted, excluded, withdrawn and method-discussion; labels alone do not establish research validity.

Request withdrawal in the original Issue or linked pull request without giving private reasons. The project excludes withdrawn material from later analyses and records its status; already downloaded or forked copies may not be retrievable. Analysis/aggregate-reporting consent does not authorize verbatim quotation or unlimited redistribution. Check quotation choices separately and obtain appropriate scope before releasing individual datasets. Contributor acknowledgement is voluntary, and authorship follows actual research contributions rather than a single submission.
