# v0.1 Pre-Release Checklist

## Repository
- [x] Canonical repository structure created
- [x] README with Korean summary
- [x] LICENSE added
- [x] `.gitignore` added
- [x] `requirements.txt` added
- [x] Roadmap/data-source/glossary documentation added

## Notebook consistency
- [x] Notebook 01–10 canonical titles fixed
- [x] Notebook numbering fixed
- [x] Canonical input/output filenames aligned
- [x] Core feature column names aligned
- [x] Random seeds specified for synthetic examples
- [x] Relative paths standardized to `data/` and `outputs/`
- [x] Notebooks 01–10 executed successfully in sequence
- [x] CPU-oriented model settings reduced to practical educational runtime
- [x] Tested-environment package versions recorded
- [x] Canonical run-all script added

## Scientific integrity
- [x] Synthetic/simulated data explicitly identified
- [x] Heuristic scores described as educational constructs
- [x] Unknown/unlabeled distinguished from true negative
- [x] PU score described as a ranking signal, not calibrated probability
- [x] Random-forest tree variation described only as an uncertainty proxy
- [x] Wet-lab validation requirement stated

## Data and provenance
- [x] Large public datasets excluded from repository
- [x] Public-source guidance documented
- [x] Example/synthetic data separated from outputs
- [x] Example known-target labels include source metadata
- [x] Re-verified current public source URLs and access/licence notes on 2026-10-06

- [x] Third-party data notice added (`NOTICE.md`)
- [x] Release audit and release notes added

## Final GitHub release tasks
- [ ] Initialize/push GitHub repository
- [x] Canonical repository name and description fixed (`adc-scientific-ai`)
- [ ] Run notebooks once in the user's target environment (Windows/Jupyter or chosen release environment)
- [ ] Review rendered notebooks on GitHub
- [ ] Create `v0.1.0` tag
- [x] Release notes / known limitations prepared
