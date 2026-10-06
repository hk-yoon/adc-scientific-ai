"""Execute notebooks 01-10 in canonical order.

Run from the repository root:
    python scripts/run_all_notebooks.py

This script stops on the first execution failure.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "notebooks").glob("[0-9][0-9]_*.ipynb"))

if len(NOTEBOOKS) != 10:
    raise SystemExit(f"Expected 10 notebooks, found {len(NOTEBOOKS)}")

for notebook in NOTEBOOKS:
    print(f"\n=== Executing {notebook.name} ===", flush=True)
    cmd = [
        sys.executable,
        "-m",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--inplace",
        str(notebook),
        "--ExecutePreprocessor.timeout=180",
    ]
    subprocess.run(cmd, cwd=ROOT, check=True)

print("\nAll canonical notebooks executed successfully.")
