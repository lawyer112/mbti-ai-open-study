# MBTI and AI Use: An Open Collaborative Study

[中文](README.md) · [Research site](https://lawyer112.github.io/mbti-ai-open-study/en/) · [Chinese questionnaire](https://lawyer112.github.io/mbti-ai-open-study/survey/index.html)

**Type: research protocol | Stage: pilot | Protocol: 0.3.0 | Chinese instrument: v0.2 | Not externally peer reviewed.** This release reports no human-participant findings and does not presuppose a personality type best suited to AI.

We ask whether reported MBTI types or preference labels are associated with prompting, interaction, verification, adoption, and experience. External verification is the intended primary exploratory outcome for the formal stage; other processes remain separate. Objective work performance and gains from AI require a later standardized-task study.

## Participate

1. Choose your most recent real AI task that ended or was paused within the past 30 days. The pilot is for users aged 18 or older who can understand the Chinese instrument.
2. Open the [questionnaire](https://lawyer112.github.io/mbti-ai-open-study/survey/index.html) and choose either the closed-ended or the narrative form. You can also download [survey/index.html](survey/index.html) and open it offline in a browser.
3. Inspect your answers, export JSON and Markdown, and attach them to a [questionnaire-return Issue](https://github.com/lawyer112/mbti-ai-open-study/issues/new?template=01-individual-report.yml), or submit through a pull request.

The page does not upload answers automatically. Public submissions are associated with GitHub accounts, so participant codes do not provide anonymity. Remove private and confidential information first and read the [participation/contribution rules](CONTRIBUTING.md). Unchecked, unsuccessful, and incomplete tasks are welcome. When adding the other form for the same task, retain its case ID; it is not another person or task.

The closed-ended form has 28 process/experience questions and 49 items overall. The narrative form has 13 open-ended questions and 34 items overall. Totals include shared background, optional, and conditional items. The initial 20 to 30 volunteers help improve the instrument; they do not guarantee comparisons among 16 types. There is no validated English questionnaire in this release. Complete English texts provide the protocol and participation information.

## Read and contribute

- [Complete English protocol](https://lawyer112.github.io/mbti-ai-open-study/protocol/20261026-mbti-ai-use-protocol/en.html) · [English PDF](https://lawyer112.github.io/mbti-ai-open-study/protocol/20261026-mbti-ai-use-protocol/en.pdf)
- [中文研究方案](https://lawyer112.github.io/mbti-ai-open-study/protocol/20261026-mbti-ai-use-protocol/zh.html) · [中文PDF](https://lawyer112.github.io/mbti-ai-open-study/protocol/20261026-mbti-ai-use-protocol/zh.pdf)
- [Closed-ended items/rationales in Chinese](survey/choice-questionnaire.md) · [Narrative items/rationales in Chinese](survey/text-questionnaire.md)
- [Workflow and design](QUESTIONNAIRE_DESIGN.en.md) · [Data rules](data/README.md)
- [Submit an independent study](https://github.com/lawyer112/mbti-ai-open-study/issues/new?template=02-study-report.yml) · [Discuss methods](https://github.com/lawyer112/mbti-ai-open-study/issues/new?template=03-research-discussion.yml)

Project byline: lawyer112. Codex assisted with drafting, translation, implementation, and checking. No independent or external peer review is claimed. [PERMISSIONS.md](PERMISSIONS.md) states the separate scopes for manuscripts, code, third-party sources, and participant materials; reports are not blanket-relicensed.

## Build and verification

Use Python 3.12 or later, Quarto 1.10.19, and Chinese fonts. Install requirements.txt, then run `python scripts/build_site.py`. Both language pages and PDFs are generated from their shared manuscript sources. See [reproduction instructions](protocol/20261026-mbti-ai-use-protocol/reproduce.md) and [verification records](VERIFICATION.md). The check workflow does not deploy; Pages publication requires manually dispatching the publish workflow.
