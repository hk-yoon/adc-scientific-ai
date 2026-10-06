# ADC Scientific AI v0.1.0 — Release Notes

## Scope

v0.1.0 is an educational, executable prototype covering the path from ADC target-prioritization concepts to the first construct-level representation.

### Included

1. ADC target biology and toy baseline
2. TCGA/GTEx-style tumor–normal feature engineering
3. HPA-style normal-tissue protein safety
4. ADC target feature matrix
5. Rule-based ranking and sensitivity analysis
6. Supervised machine-learning ranking
7. Positive–Unlabeled learning
8. Simulated wet-lab feedback
9. Active learning and closed-loop candidate selection
10. ADC construct representation

## What v0.1.0 is not

- It is not a clinical or regulatory system.
- It does not claim validated prediction of ADC efficacy or toxicity.
- It does not bundle real TCGA, GTEx, HPA, or wet-lab datasets.
- Synthetic scores, thresholds, labels, and assay outcomes are teaching devices.

## Reproducibility

Notebooks 01–10 have been executed sequentially in the release workspace using fixed random seeds where simulation is involved. Canonical intermediate outputs are written to `outputs/`.

## Known limitations

- The executable tumor/normal and HPA examples are synthetic rather than direct public-data downloads.
- The educational positive target set is intentionally small.
- Supervised-model metrics are not estimates of real-world ADC discovery performance.
- PU scores are ranking signals, not calibrated probabilities.
- Random-forest tree variation is used only as an uncertainty proxy.
- Wet-lab and construct outcomes are simulated.
- Notebook 09 deliberately operates with a very small tested set to demonstrate the loop, so its surrogate model is not research-grade.

## Next phase

Planned Phase II topics include multi-objective construct optimization, construct-level surrogate modeling, Bayesian optimization, and later PK/PD–PBPK–QSP integration.
