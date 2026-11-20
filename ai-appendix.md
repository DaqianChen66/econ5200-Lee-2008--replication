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


## Section 4: Does the Finding Hold?

### Entry: Checking and Editing the Final Conclusion

- **Model and version:** [Fill in the actual model used]
- **Date:** [Fill in the actual date]

**[Prep]** I used AI as an English writing and checking assistant. I wanted to make my final conclusion clear and easy to understand.

**[Request]** I asked AI to help me organize Section 4 and check whether my conclusion was consistent with the replication and robustness results.

**[Iterate]** I asked for simple English, short sentences, and a writing style suitable for a student report. I also wanted the conclusion to explain the limitations of my replication instead of only saying that the original paper was correct.

**[Mechanism Check]** I checked the conclusion against my actual results. My direct replication estimate was 0.086126, compared with 0.077 in Lee (2008). I also checked the four robustness exercises. The estimates remained positive under different bandwidths, polynomial orders, and donut restrictions. The two placebo cutoffs did not show statistically significant effects.

I checked that the conclusion did not claim that these tests could prove all the assumptions of the RDD design.

**[Evaluate]** I compared the edited text with the output from `python reproduce.py`. The main conclusion was that Lee's positive party incumbency advantage was supported by my replication, but the exact size of the effect was not identical to the original paper. I also kept the limitation about the different sample periods and the unresolved difference in sample size.

**Full transcript**

[Paste the complete original conversation about writing and editing Section 4. Include your prompts, the AI replies, and any suggestions you did not use. This summary is not a replacement for the original transcript.]

**What I changed, and why:**

- I used shorter sentences and simpler words to explain my conclusion.
- I made the conclusion more specific by referring to the replication and robustness results.
- I explained that the positive effect was supported, but the exact effect size was different.
- I kept the sample differences and RDD identification assumptions as limitations.
- I checked the numerical statements against my own results before using them in the report.

## Section 5: Peer audit

TODO

## Section 6: Your Own Repository

### Entry 1: Checking the GitHub Repository Structure

- **Model and version:** [Check the model used in the original conversation]
- **Date:** [Enter the actual date]

**[Prep]** I used AI as a technical assistant to help me organize my GitHub repository.

**[Request]** I asked AI to check the required files and folders for my replication project.

**[Iterate]** I explained that I was using Google Colab and GitHub. I wanted to make sure the notebook names and file paths matched the reproduction script.

**[Mechanism Check]** I checked whether the repository contained `reproduce.py`, `requirements.txt`, `download_data.py`, and the two required notebooks. I also checked whether the `.git` folder existed after cloning the repository.

**[Evaluate]** After cloning the repository again, all required files were found. The repository check showed `True` for the Git repository and `OK` for the required files.

**Full transcript**

[Paste the complete original conversations about the repository structure, notebook filenames, GitHub cloning, and file path errors.]

**What I changed, and why:**

- I checked the names and locations of the two notebooks.
- I used a fresh GitHub clone to avoid local file path problems.
- I confirmed that the main scripts and requirements file were present.

---

### Entry 2: Fixing Colab Environment and Reproduction Errors

- **Model and version:** [Check the model used in the original conversation]
- **Date:** [Enter the actual date]

**[Prep]** I used AI as a debugging assistant when the reproduction code did not run correctly in Google Colab.

**[Request]** I shared error messages from Colab and asked AI to help me understand and fix them.

**[Iterate]** I reported different problems, including missing files, a missing Git repository, dependency conflicts, and a missing output CSV. I followed the suggested steps and checked the results after each attempt.

**[Mechanism Check]** I checked the current working directory and confirmed that `reproduce.py` was being run from the repository root. I also checked the required packages and whether the expected output files were created.

**[Evaluate]** After correcting the environment and running the code from a clean clone, the reproduction script completed successfully. Both notebooks were executed and the script finished without a reported reproduction failure.

**Full transcript**

[Paste the complete original debugging exchanges, including error messages, AI replies, unsuccessful attempts, and the final successful run.]

**What I changed, and why:**

- I restarted the Colab runtime after dependency warnings.
- I cloned the repository again when the local project folder was missing.
- I ran the reproduction script from the correct directory.
- I checked the script output instead of assuming that installation success meant reproduction success.

---

### Entry 3: Checking the One-Command Reproduction Results

- **Model and version:** [Check the model used in the original conversation]
- **Date:** November 19, 2026 [verify against the original chat]

**[Prep]** I used AI to help check whether my repository met the course reproducibility requirement.

**[Request]** I shared the full output of `python reproduce.py` and asked AI to check whether the replication was successful.

**[Iterate]** I wanted to confirm that both notebooks ran, that the Section 2 and Section 3 baseline estimates matched, and that the robustness results were generated.

**[Mechanism Check]** I compared the printed results with my replication values. The script reported a replication estimate of 8.61 percentage points, compared with 7.70 percentage points in Lee (2008). It also reported that the robustness baseline matched Section 2 at 0.08612600.

**[Evaluate]** The script finished in 16.4 seconds and reported 12 robustness rows from four exercises. This gave evidence that the main analysis could be reproduced from a fresh GitHub clone.

**Full transcript**

[Paste the complete original exchange containing the successful `python reproduce.py` output and the AI response.]

**What I changed, and why:**

- I checked the main estimate against the paper's reported number.
- I confirmed that the robustness baseline matched the Section 2 estimate.
- I recorded the actual runtime and robustness output count.
- I used these verified results when updating the repository documentation.

---

### Entry 4: Editing README and Organizing Output Files

- **Model and version:** [Check the model used in the original conversation]
- **Date:** November 19, 2026 [verify against the original chat]

**[Prep]** I used AI as a documentation assistant to help organize the repository files and improve the README.

**[Request]** I uploaded the course README template and asked AI to help write the README using my project information. I also asked which output files were needed in the repository.

**[Iterate]** I explained that I wanted to keep only the required output files. I asked AI to organize the files according to the README.

**[Mechanism Check]** I checked that the README described the same headline estimate as the reproduction script. I also checked the expected output file names:

- `output/headline_table.csv`
- `output/robustness_baseline.csv`
- `output/robustness_summary.csv`
- `output/executed/`

I understood that the executed notebooks should come from running the code, rather than from manually creating empty files.

**[Evaluate]** I checked the output structure against the course template and the results from Colab. I used the README to explain the data source, reproduction command, and main findings.

**Full transcript**

[Paste the complete original exchanges about the README template, output file generation, the four required output items, and uploading files to GitHub.]

**What I changed, and why:**

- I organized the README using the course template.
- I checked that the README used the same 8.61 percentage-point estimate as the reproduction script.
- I kept the output file list focused on the required results.
- I distinguished automatically generated notebook outputs from manually prepared files.
