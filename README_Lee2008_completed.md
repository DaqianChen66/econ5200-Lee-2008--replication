# Replicating Lee (2008): Party Incumbency Advantage in U.S. House Elections

## The paper and its headline claim

- **Paper:** Lee, David S. (2008). “Randomized Experiments from Non-random Selection in U.S. House Elections.” *Journal of Econometrics*, 142(2), 675–697. https://doi.org/10.1016/j.jeconom.2007.05.004
- **Identification strategy:** Sharp regression discontinuity design (RDD). The cutoff is a zero Democratic victory margin in the prior election. The central assumption is that potential future electoral outcomes are continuous at the cutoff, so parties that barely win and barely lose are comparable locally.
- **Headline claim:** Lee (2008), Table 2, column (1), reports that winning a close election increases the Democratic Party's vote share in the next election by **0.077 (7.70 percentage points)**.
- **My replication:** Using the assigned Lee, Moretti, and Butler (2004) data, the estimate is **0.086126 (8.61 percentage points)**, compared with **0.077** in Lee (2008). The difference is **+0.91 percentage points**, or **+11.85% relative to the published estimate**. The replication's clustered standard error is **0.009777**, based on **13,566 observations**; Lee reports **0.011** and **6,558 observations**. The distinct sample periods and construction choices are discussed in the report's discrepancy log.

## Reproduce the headline table

Python 3.11 or newer. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python reproduce.py
```

**The one reproduction command is `python reproduce.py`.** It uses `download_data.py` to obtain the dataset when needed, executes `notebooks/01_positioning_and_replication.ipynb` followed by `notebooks/02_robustness.ipynb` in fresh kernels, and prints the headline comparison from `output/headline_table.csv`. Executed notebook copies are saved to `output/executed/`.

- **Measured analysis runtime:** approximately **16.4 seconds** in a fresh Google Colab checkout, excluding dependency installation. Timing may vary with hardware and network access.
- **Verified run:** the clean-clone test printed an incumbency estimate of **8.61 percentage points**, a gap of **+0.91 percentage points**, and `Robustness baseline matches S2: 0.08612600`; it completed four robustness exercises containing 12 specification rows.
- **Environment note:** Colab may warn about conflicts between pinned Jupyter/kernel packages and its preinstalled packages. A clean virtual environment is preferable for independent reproduction.

## Data: source and licence

- **Source:** `lmb-data.dta`, publicly available at https://raw.githubusercontent.com/scunning1975/mixtape/master/lmb-data.dta . The file is associated with Lee, Moretti, and Butler (2004), rather than the exact Lee (2008) analysis sample.
- **Coverage:** the assigned dataset covers **1948–1990**, while Lee (2008) uses **1946–1998**. This matters when interpreting the numerical gap.
- **Included or downloaded:** The project has been tested with `data/lmb-data.dta` present. `download_data.py` provides a reproducible download path when that file is absent, so manual data placement is not necessary for a clean checkout.
- **Redistribution:** Before publicly committing a copy of the `.dta` file, verify the applicable source licence and preserve any required notice. If its redistribution terms are uncertain, remove the tracked copy and rely on the downloader instead.

## Repository map

| Path | What it is |
|---|---|
| `reproduce.py` | Runs both notebooks, checks expected outputs, and prints the replication comparison |
| `download_data.py` | Downloads the chosen dataset; `python download_data.py --paper lee` obtains the Lee file |
| `data/lmb-data.dta` | Assigned input dataset, if included locally or in the repository |
| `notebooks/01_positioning_and_replication.ipynb` | Sections 1–2: positioning, direct replication, comparison table, and discrepancy log |
| `notebooks/02_robustness.ipynb` | Section 3: bandwidth, polynomial order, donut RD, and placebo-cutoff checks |
| `output/headline_table.csv` | Generated comparison between Lee's estimate and the replication |
| `output/robustness_baseline.csv` | Generated baseline estimate used to cross-check Sections 2 and 3 |
| `output/robustness_summary.csv` | Generated results for the four robustness exercises |
| `output/executed/` | Executed notebooks with results |
| `output/` | All generated tables and figures used for reporting |
| `report/` | Final report PDF (add before submission) |
| `ai-appendix.md` | Disclosure of AI-assisted work, checks, and relevant transcripts |
| `AUDIT.md` | Peer-audit guidance; the submitted peer audit is a GitHub issue in another student's repository |
| `requirements.txt` | Pinned Python dependencies |
| `.gitignore` | Excludes temporary or generated files according to repository configuration |

## Use of AI

AI assistance was used during this project for research explanation and drafting/revision, including discussion of the Sections 1–2 analysis, support for Section 3 robustness code and interpretation, writing and self-review for Sections 3–5, and troubleshooting/documentation of the Section 6 reproducibility workflow. Reported estimates were obtained by running the Python code on the assigned data, not by generating numerical outputs with AI. See [`ai-appendix.md`](ai-appendix.md) for a detailed account and supporting transcripts. The course's most recent permission to use AI should be applied together with any remaining documentation requirements.
