#!/usr/bin/env python3
"""One-command clean-checkout reproduction of S1/S2 and S3.

From repository root, after installing requirements: python reproduce.py
"""
from pathlib import Path
import sys
import time
import pandas as pd
import nbformat
from nbclient import NotebookClient
from download_data import fetch

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output"
NOTEBOOKS = ROOT / "notebooks"


def execute_notebook(path: Path) -> None:
    print(f"\nExecuting {path.relative_to(ROOT)}", flush=True)
    notebook = nbformat.read(path, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=900,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}},
        allow_errors=False,
    )
    client.execute()
    executed = OUTPUT / "executed" / path.name
    executed.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(notebook, executed)
    print(f"Saved {executed.relative_to(ROOT)}", flush=True)


def main() -> int:
    start = time.monotonic()
    if not NOTEBOOKS.is_dir():
        raise FileNotFoundError("notebooks/ directory missing")
    OUTPUT.mkdir(exist_ok=True)
    fetch("lee")
    # Remove prior derived summaries to avoid reporting stale outputs on failure.
    for old in ("headline_table.csv", "headline_report_table.csv",
                "robustness_baseline.csv", "robustness_summary.csv"):
        (OUTPUT / old).unlink(missing_ok=True)
    for name in ("01_positioning_and_replication.ipynb", "02_robustness.ipynb"):
        execute_notebook(NOTEBOOKS / name)
    headline_path = OUTPUT / "headline_table.csv"
    robustness_path = OUTPUT / "robustness_summary.csv"
    baseline_path = OUTPUT / "robustness_baseline.csv"
    for required in (headline_path, robustness_path, baseline_path):
        if not required.is_file():
            raise RuntimeError(f"Expected output missing: {required}")
    table = pd.read_csv(headline_path, index_col=0)
    effect_rows = table.index[table.index.str.contains("incumbency jump", case=False)]
    if len(effect_rows) != 1:
        raise RuntimeError("Expected exactly one incumbency-jump row")
    paper = float(table.loc[effect_rows[0], "paper_estimate"])
    replication = float(table.loc[effect_rows[0], "my_estimate"])
    robustness_base = float(pd.read_csv(baseline_path).iloc[0]["estimate"])
    if abs(replication - robustness_base) > 1e-8:
        raise AssertionError(
            f"Baseline mismatch: Section 2 = {replication:.8f}; Section 3 = {robustness_base:.8f}"
        )
    results = pd.read_csv(robustness_path)
    if len(results) < 4 or results["exercise"].nunique() < 4:
        raise AssertionError("Expected four robustness exercises")
    print("\n=== Headline replication: Lee (2008) Table 2 (1) ===")
    print(f"Paper:       {100*paper:.2f} percentage points")
    print(f"Replication: {100*replication:.2f} percentage points")
    print(f"Gap:         {100*(replication-paper):+.2f} percentage points")
    print(f"Robustness baseline matches S2: {robustness_base:.8f}")
    print(f"Robustness rows: {len(results)}, exercises: {results['exercise'].nunique()}")
    print(f"Finished in {time.monotonic()-start:.1f} seconds")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"REPRODUCTION FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise
