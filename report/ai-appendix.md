# AI Appendix — Lee (2008) Replication

## Policy clarification

The original teaching template describes Sections 1 and 2 as unaided. The student reports that the instructor **subsequently removed the no-AI restriction and encouraged using AI to improve understanding**. This project therefore reports AI use truthfully in all sections; it does **not** claim that Sections 1 and 2 were unaided.

## P.R.I.M.E. activity log (working record)

The following entries describe observable work from the ChatGPT project conversation. Review and expand each record against the actual interaction history before submitting.

| Section | Purpose / prompt summary | AI role | Human review and verification still required |
|---|---|---|---|
| S1 | Write and then simplify the English positioning section for Lee (2008); repair formula rendering | Drafted background, identification explanation, and critical-literature discussion | Check sources, page limit, personal understanding and final wording |
| S2 | Interpret the Lee starter, fill the repository's 01 notebook, build quartic RD and discrepancy table | Proposed Python regression and template-cell changes | Student ran Colab and shared jump 0.0861, SE 0.0098, N 13,566; verify again from repository |
| S3 | Fill `02_robustness.ipynb` with four appropriate robustness exercises | Developed bandwidth, polynomial, donut and placebo checks and automated interpretation | Run against actual dataset; interpret each exercise from actual outputs |
| S6 | Make repository reproducible with download script, dependencies, README, one-command execution and AI documentation | Generated an integration package and consistency checks | Clean-clone test, measure runtime, verify output numbers, commit changes |

## Full transcripts (submission action required)

The course brief asks for **full transcripts**, not just this short log. **No unabridged conversation transcript is included in this generated file**, because the complete conversation export was not supplied as a file. Export the relevant ChatGPT conversations and add them to `ai-transcripts/` (or paste them as appendices here), including prompts and model responses for S1–S6. Do not imply the transcripts are complete before adding them.

Suggested record fields per P.R.I.M.E. entry: task/problem; requested assistance and exact prompt; AI response/output; independent verification; modification and explanation. Follow the instructor's exact P.R.I.M.E. specification if it differs.

## Current verification statement

- Direct-replication figures **reported by student from a prior Colab run**: jump 0.0861 (8.61 pp), SE 0.0098, N 13,566.
- The new integration package **has not been validated against the real `.dta` in a clean checkout** due to unavailable network access in the build environment.
- Any later reruns or edits must be reflected in this appendix and in the final report.
