# AI Appendix

## Sections 1 and 2

Sections 1 and 2 were completed without AI.

Name: Daqian Chen
Date: 11.19.2026

Using AI in Sections 1 or 2 is an integrity violation. Do not edit the statement above; if it
is not true, talk to the instructor before you submit.

## How to file an entry

Sections 3 to 6 allow AI as a documented co-pilot under P.R.I.M.E. File one entry for each
piece of work you used it on, under the section it belongs to. Paste the full exchange: every
prompt as you sent it and every reply as it came back, including what you rejected. A summary
is not a transcript. If you cannot explain a line of what the model gave you, you cannot
submit it.

If you did not use AI in a section, write "No AI used in this section." under its heading.

Copy this block for each entry:

```
### Entry: TODO what it was for (for example, Exercise 1, not-yet-treated comparison)

- Model and version: TODO
- Date: TODO

**[Prep]** TODO: the role you gave the model.
**[Request]** TODO: what you asked for.
**[Iterate]** TODO: the constraints you added, and the version-2 prompt.
**[Mechanism Check]** TODO: what you asked it to explain, and whether the explanation held.
**[Evaluate]** TODO: how you checked the output against your own data or results.

**Full transcript**

TODO: paste the exchange here, unedited.

**What I changed, and why:** TODO, one line per change.
```


## Section 3: Robustness

### Exercise 1: Bandwidth Sensitivity

- **Model and version:** [Fill in the actual model used]
- **Date:** [Fill in the actual date]

**[Prep]** I used AI as an assistant to check my robustness results and edit my English writing.

**[Request]** I asked AI to help me check the bandwidth sensitivity results and explain them in simple English.

**[Iterate]** I wanted to follow the report template: What I did, What I found, and What it implies. I also asked for shorter sentences and simpler words.

**[Mechanism Check]** I checked the estimates for bandwidths 0.025, 0.05, 0.10, and 0.20. I compared the numbers and confidence intervals with my output table.

**[Evaluate]** The estimates were between 0.092134 and 0.102668. All four confidence intervals were above zero. I checked that the report used these values correctly.

**Full transcript**

[Paste the complete original conversation related to checking and editing Exercise 1, including all prompts and replies.]

**What I changed, and why:**

- I made the explanation shorter and easier to read.
- I checked the numbers against `robustness_summary.csv`.
- I explained that the positive result was stable across different bandwidths.

---

### Exercise 2: Polynomial Order

- **Model and version:** [Fill in the actual model used]
- **Date:** [Fill in the actual date]

**[Prep]** I used AI to help check the results and improve my English explanation.

**[Request]** I asked AI to review the results from different polynomial orders and help organize the discussion.

**[Iterate]** I asked for simple English and wanted the discussion to focus on the differences between linear, quadratic, and cubic models.

**[Mechanism Check]** I compared the estimates and standard errors in the output table. I also checked that the three models used the same bandwidth of 0.10.

**[Evaluate]** The estimates were 0.094930, 0.088344, and 0.095394. They were all positive and statistically significant. I checked these values before using them in the report.

**Full transcript**

[Paste the complete original conversation related to checking and editing Exercise 2, including all prompts and replies.]

**What I changed, and why:**

- I organized the explanation by polynomial order.
- I used simpler sentences to explain the results.
- I checked that the reported numbers matched the notebook output.

---

### Exercise 3: Donut RD

- **Model and version:** [Fill in the actual model used]
- **Date:** [Fill in the actual date]

**[Prep]** I used AI as a coding assistant to help fix a sample selection problem in the Donut RD exercise.

**[Request]** I asked for help checking the Donut RD code and fixing the condition used to remove observations near the cutoff.

**[Iterate]** I needed the code to handle donut radius zero and positive donut radii correctly. I also asked for help checking the results after the code change.

**[Mechanism Check]** I reviewed the suggested sample selection code:

```python
keep = (x.abs() <= h)

if donut > 0:
    keep &= x.abs() > donut
```

This condition applies the additional exclusion only when the donut radius is positive.

**[Evaluate]** After the correction, the notebook ran successfully. The estimates were 0.094930, 0.091796, and 0.094835 for donut radii 0, 0.005, and 0.01. All three estimates remained positive.

**Full transcript**

[Paste the complete original exchange about the Donut RD code, including the error, AI suggestions, revisions, and final check.]

**What I changed, and why:**

- I corrected the Donut RD sample selection condition.
- I checked that the zero-radius case worked correctly.
- I compared the results with `robustness_summary.csv`.

---

### Exercise 4: Placebo Cutoffs

- **Model and version:** [Fill in the actual model used]
- **Date:** [Fill in the actual date]

**[Prep]** I used AI to help check the placebo results and edit the report discussion.

**[Request]** I asked AI to help explain the placebo cutoff results in simple English.

**[Iterate]** I wanted the explanation to be clear and not make claims that were too strong. I also wanted the writing to follow the course report template.

**[Mechanism Check]** I checked the results at the two artificial cutoffs, −0.10 and +0.10. I compared the estimated effects, confidence intervals, and p-values with my output table.

**[Evaluate]** The estimated effects were −0.007751 and −0.001528, with p-values of 0.522 and 0.923. Both confidence intervals included zero. I checked that the report described them as statistically insignificant, rather than saying they proved there was no effect.

**Full transcript**

[Paste the complete original conversation related to checking and editing Exercise 4, including all prompts and replies.]

**What I changed, and why:**

- I simplified the explanation of the two placebo tests.
- I checked the estimated effects and p-values against the output.
- I changed the wording to avoid saying that an insignificant estimate proves the effect is zero.

## Section 4: Does the finding hold?

TODO

## Section 5: Peer audit

TODO

## Section 6: Your own repository

TODO
