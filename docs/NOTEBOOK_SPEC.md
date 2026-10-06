# Canonical Notebook Specification — v0.1

| Notebook | Primary input | Canonical output | Role |
|---|---|---|---|
| 01 | none | none required | Synthetic biological baseline |
| 02 | internal synthetic example / later public TCGA-GTEx | `outputs/tcga_gtex_expression_features.csv` | Tumor-normal expression features |
| 03 | internal synthetic HPA-style example | `outputs/hpa_normal_tissue_features.csv` | Normal-tissue protein safety |
| 04 | Notebook 02 + 03 outputs + surface annotation | `outputs/adc_target_feature_matrix_v01.csv` | ADC target feature matrix |
| 05 | target feature matrix | rule ranking + sensitivity outputs | Transparent rule baseline |
| 06 | target feature matrix + known target example labels | ML predictions/ranking | Supervised ML baseline |
| 07 | target feature matrix + ML/rule results | PU ranking + batch 001 | PU target discovery |
| 08 | PU ranking + batch 001 | simulated wet-lab results + feature matrix v02 | Experimental feedback bridge |
| 09 | feature matrix v02 | active-learning log + batch 002 | Closed-loop selection |
| 10 | internal synthetic component tables | `outputs/adc_construct_dataset_v01.csv` | Construct representation bridge |

## Canonical target-level ML features

- `tumor_score`
- `selectivity_score`
- `prevalence_score`
- `surface_score_norm`
- `heterogeneity_risk`
- `normal_rna_risk`
- `normal_protein_risk_norm`
- `critical_organ_risk`

## Canonical identifiers

Target-level notebooks use `gene_symbol` as the executable v0.1 example index. Production workflows should retain a stable identifier such as Ensembl ID alongside human-readable symbols.

Construct-level modeling uses:

- `construct_id`
- `target_id`
- `antibody_id`
- `linker_id`
- `payload_id`
- `conjugation_id`
