# Questionnaire design and workflow

[中文](QUESTIONNAIRE_DESIGN.md) · [Complete protocol](protocol/20261026-mbti-ai-use-protocol/en.qmd)

## Completing and returning a form

Open the [online questionnaire](https://lawyer112.github.io/mbti-ai-open-study/survey/index.html), or download survey/index.html and open it in a browser. Choose one form and consistently recall your most recent real task that ended or was paused within the past 30 days. The pilot is for recent users aged 18 or older who understand the Chinese instrument.

Answers stay in the current page. Save draft downloads a local draft; Load draft restores it later. Once complete, inspect and export JSON and Markdown, attach them to a [questionnaire-return Issue](https://github.com/lawyer112/mbti-ai-open-study/issues/new?template=01-individual-report.yml), or submit them through a pull request under submissions/individual/. Do not return the blank HTML or an unconfirmed draft. The page does not upload answers automatically. Redact attachments before public submission; a participant code does not guarantee anonymity.

## Purposes of the two forms

The closed-ended form has 28 core process items and 49 items overall; the narrative form has 13 open-ended questions and 34 items overall. Totals include shared background, optional and conditional fields. Closed-ended responses support distributional comparisons. Narratives explore processes and reasons. Shared themes do not establish measurement equivalence.

| Theme | Closed-ended items | Narrative items |
| --- | --- | --- |
| Initiation and planning | C01 to C03 | T01 to T02 |
| Initial expression | C04 to C08 | T03 |
| Iteration and difficulty | C09 to C13 | T04 to T06 |
| Verification and adoption | C14 to C17 | T07 to T09 |
| Outcomes and experience | C18 to C28 | T10 to T13 |

Each item has an explanation that can be expanded individually or through the global purpose switch. Explanations are collapsed by default, and exposed item IDs are recorded as method information. The [closed-ended text](survey/choice-questionnaire.md) and [narrative text](survey/text-questionnaire.md), both in Chinese, display all purposes for review or manual response. Rationales prescribe no type-specific answer. Personality questions follow process recall to reduce stereotype cues, without claiming that this eliminates bias.

## Conditional questions and linked forms

C16 is answered only when C15 reports an error; C20 only when C19 supplies a time band; R03 only when R02 reports AI-assisted preparation. Mutually exclusive options cannot be combined with other answers. All currently applicable required items and the three participation confirmations must be completed before formal export. Unknown or inapplicable experiences can be reported honestly.

One form is sufficient. If adding the other form, retain case_id and viewing order, and explain corrections to shared information. A new task gets a new case ID while retaining the participant code. Each response export contains only its own form; a saved draft retains progress in both.

## Questionnaire versus experiment

This stage fixes the questions while collecting accounts of different real tasks. It studies associations in self-reported behavior. Common tasks with independent scoring belong to a later study; estimating AI gains also requires AI and no-AI conditions. That experiment has not been implemented.

The first 20 to 30 volunteers help identify comprehension problems, missing options, completion time, and submission difficulties. They do not guarantee comparisons among 16 types. Freeze methods and plan the sample before formal comparisons. The English overview and protocol are complete, but an English instrument would require its own meaning and comparability checks rather than automatic equivalence.

## Maintenance

scripts/questionnaire_items.py is the instrument source; scripts/build_questionnaires.py generates HTML and both readable questionnaires. Publication uses a manually triggered workflow; the check workflow only checks. Changes to items, references, or conclusions require synchronized bilingual protocol updates and fresh review. See [contribution rules](CONTRIBUTING.md) and [data/README.md](data/README.md) for participation and data handling.
