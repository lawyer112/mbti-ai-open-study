# How the forms work

[中文 / English](QUESTIONNAIRE_DESIGN.md) · [Why this survey exists](protocol/20261026-mbti-ai-use-protocol/en.qmd)

## How the forms work

Think about the past 30 days. Quick choices contain 19 items and the story form 11, with 7 shared items. Totals include optional and conditional items; only applicable questions appear. One form is enough; use the same report ID to add the other. Uncertain MBTI skips the source question. Recent nonusers answer why they have not used AI, without inventing an experience. The final one-sentence reflection is optional. Choices describe uses, conversation habits and opinions; stories add context. Each item’s purpose can be opened, and that exposure is recorded. Actual completion time still needs human pilot feedback.

## What we will do with responses

First report valid counts and option percentages for each item, then explore distributions by MBTI, type source, frequency and experience. Multiple-choice percentages may exceed 100%. Missing, inapplicable, uncertain and explicit absence remain distinct. Satisfaction is a self-report, and checking frequency is not checking quality. Code stories for uses, conversation habits, benefits, complaints and exceptions, preserving opposing accounts; quote verbatim only with A05 permission. Do not double-count both forms, an Issue and its PR, or corrections from one person, or treat an independent study as one participant.

## What we cannot conclude

This volunteer internet sample describes contributors, not all people in the 16 types. It cannot establish personality causation or superior work ability. Small samples do not justify forced rankings or significance claims. The forms are not equivalent scales; the 12 translations have not undergone native-speaker cognitive interviews or cross-cultural measurement validation. Keep instrument language, switching history and the language of each answer; report languages and versions separately before considering any justified pooling. Keep old v0.2 single-task reports separate from v0.3 everyday-habit records.

## Taking part and sharing

Participation is voluntary for adults aged 18 or older who understand their chosen language, including recent nonusers. Complete the online form or download the standalone HTML for offline use, inspect and export JSON data and a Markdown report, then return them through an Issue or PR. The form does not upload answers automatically. Readable Markdown forms are also available; retain item IDs, confirmations, version and purpose-exposure records. GitHub submissions are public and linked to accounts; a report ID is not anonymity. Remove private, client, employer-confidential and credential information. Aggregate-use consent and quotation permission are separate; do not redistribute individual data freely without separate authorization. Request withdrawal at the original submission; later analyses exclude it, but downloaded or forked copies may remain.

[Markdown: choices](survey/en/choice-questionnaire.md) · [Markdown: stories](survey/en/text-questionnaire.md)

Item mapping: A01–A04 background; Q01–Q02 uses; Q03–Q07 conversation and checking; Q08–Q12 views and nonuse; S01–S04 stories; A05–A07 quotation, AI disclosure and optional reflection. Every item purpose appears in the full forms above.

Uncertain A01 skips A02. A03 = 0 days skips A04, Q01–Q10 and S01–S03, routing to Q11/S04; other answers skip Q11/S04. Q09 no-complaint is exclusive. A07 is optional. Switching language retains answers but resets participation confirmations.

Editable sources: `scripts/survey_items_v03.py`, `survey/locales/`, `survey/app.js`, `survey/page.template.html`.

Generation: `python scripts/build_questionnaires.py`.

Instrument v0.3; guide 0.4.0. Meaning changes require a version increase, synchronized languages and fresh review.
