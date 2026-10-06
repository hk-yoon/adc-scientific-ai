# v0.1 Release Audit

_Audit date: 2026-10-06_

## Result

**Status: Release candidate, pending user-environment render test and GitHub publication steps.**

## Findings and actions

### 1. Executability — PASS

Notebooks 01–10 form an executable sequential pipeline. Relative input/output paths are canonicalized under `data/` and `outputs/`.

### 2. Educational clarity — IMPROVED

Each notebook now explicitly states:

- learning objectives;
- data mode;
- inputs;
- canonical outputs;
- scientific limitation;
- next step.

This is especially important for Notebooks 02–03, whose titles refer to TCGA/GTEx and HPA while the executable v0.1 core intentionally uses synthetic data.

### 3. Synthetic vs real data — PASS after clarification

Notebooks 08–10 prominently identify simulated wet-lab or construct data. The public-data notebooks now distinguish executable synthetic examples from real-data extension paths.

### 4. Scientific claims — PASS with caveats

The repository consistently treats heuristic scores as educational constructs, PU outputs as ranking signals rather than calibrated probabilities, and model uncertainty as a proxy rather than complete biological uncertainty.

### 5. Public source verification — PASS

Provider documentation was rechecked on 2026-10-06 and summarized in `DATA_SOURCES.md`:

- NCI GDC/TCGA access policy and current portal status;
- GTEx open/protected access and current Adult GTEx V11 availability;
- UCSC Xena / Toil public-data workflow;
- HPA v25.1, normal IHC resource, and current HPA licence/citation terms.

### 6. Third-party licensing — IMPROVED

Added `NOTICE.md` to separate the repository's MIT-licensed original code/docs from third-party biological data terms.

### 7. Remaining pre-release tasks

- Run and visually inspect notebooks in the user's intended Windows/Jupyter environment.
- Confirm GitHub rendering of Markdown, tables, and plots.
- Create/push the repository.
- Create tag `v0.1.0` and publish the release notes.
