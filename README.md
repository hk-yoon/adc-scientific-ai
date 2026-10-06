# ADC Scientific AI

**Educational notebooks for AI-assisted antibody-drug conjugate development**

This repository presents a hands-on, educational workflow for applying **Scientific AI** to antibody-drug conjugate (ADC) development.

The project begins with **ADC target prioritization** using public biological data and progressively extends toward machine learning, positive–unlabeled learning, experimental validation, active learning, and ADC construct representation.

The goal is not to build a clinical decision system or claim automated ADC discovery. Instead, the repository demonstrates how biological reasoning, public data, machine learning, uncertainty, and experimental feedback can be connected in a reproducible Scientific AI workflow.

## 한국어 요약

이 저장소는 **항체-약물 접합체(ADC, Antibody-Drug Conjugate) 개발에 Scientific AI를 적용하는 과정을 단계적으로 학습하기 위한 교육용 프로젝트**입니다.

TCGA, GTEx, Human Protein Atlas(HPA)와 같은 공개 생물학 데이터를 이용한 표적 후보 평가에서 시작하여,

```text
ADC 표적 후보 발굴
→ 생물학적 feature engineering
→ Rule-based ranking
→ Machine Learning
→ Positive–Unlabeled Learning
→ Wet-lab validation
→ Active Learning
→ Closed-loop DBTL
→ ADC construct representation
```

으로 확장합니다.

이 프로젝트의 목적은 AI가 ADC를 자동으로 설계하거나 임상적 의사결정을 대신하도록 만드는 것이 아닙니다. 오히려 **생물학적 문제 정의, 데이터, AI 모델, 불확실성, 실험 결과와 다음 실험 설계를 어떻게 하나의 Scientific AI workflow로 연결할 수 있는지**를 Python/Jupyter Notebook을 통해 이해하는 데 목적이 있습니다.

일부 예제에서는 교육과 재현성을 위해 synthetic 또는 simulated data를 사용합니다. 이러한 데이터는 실제 실험 결과와 명확하게 구분하여 표시합니다.


## v0.1 Data Mode

The **executable core of v0.1 is intentionally self-contained**. Notebooks 01–03 use synthetic or HPA-style example data rather than redistributing large public datasets, and Notebooks 08–10 use simulated wet-lab or construct outcomes.

The repository therefore demonstrates the **workflow and scientific reasoning** end-to-end while keeping public-data acquisition as an explicit extension path. See `docs/DATA_SOURCES.md` for currently verified TCGA/GDC, GTEx, UCSC Xena/Toil, and HPA access notes.

This distinction is important: notebook titles such as “TCGA–GTEx” and “HPA” describe the intended data model and real-data extension, not a claim that the bundled example values are downloaded patient or tissue measurements.

## Notebook Roadmap

| # | Notebook | Role |
|---|---|---|
| 01 | ADC Target Discovery: Biological Problem | Define the biological problem with a small synthetic example |
| 02 | TCGA–GTEx Tumor–Normal Analysis | Build tumor/normal transcriptomic features |
| 03 | HPA Normal-Tissue Safety Filtering | Add normal-tissue protein safety features |
| 04 | ADC Target Feature Engineering | Build an ADC-specific target feature matrix |
| 05 | Rule-Based ADC Target Ranking and Validation | Transparent baseline ranking and sensitivity analysis |
| 06 | Machine-Learning ADC Target Ranking | Logistic Regression, Random Forest, XGBoost |
| 07 | Positive–Unlabeled Learning for ADC Target Discovery | Known-positive vs unlabeled learning |
| 08 | From AI Ranking to Wet-Lab Validation | Simulated binding/internalization/trafficking/killing feedback |
| 09 | Active Learning and Closed-Loop ADC Target Discovery | Acquisition functions, diversity, iterative learning |
| 10 | ADC Construct Representation | Transition from target-level to construct-level modeling |

## Scientific AI Perspective

The workflow progressively combines:

```text
Domain knowledge
+
Public biological data
+
Feature engineering
+
Machine learning
+
Uncertainty
+
Experimental evidence
+
Experimental design
```

The long-term direction is toward hybrid workflows connecting AI with mechanistic models, PK/PD, PBPK, QSP, and automated experimental systems.

## Data

The repository uses a mixture of:

1. **Small synthetic datasets** for teaching and reproducibility.
2. **Public-data workflows** inspired by resources such as TCGA, GTEx, and the Human Protein Atlas.
3. **Synthetic experimental outcomes** where real wet-lab measurements are unavailable.

Synthetic or simulated data are explicitly identified in the notebooks. Large public datasets are intentionally not bundled in this repository.

## Important Scientific Limitations

This repository is an educational and research prototype. It is **not** intended for clinical decision-making, patient treatment recommendations, regulatory evaluation, or direct prediction of clinical ADC safety or efficacy.

Scores, weights, thresholds, simulated outcomes, and example labels used in the notebooks are educational constructs unless explicitly stated otherwise. High model scores should be interpreted as **candidate prioritization signals**, not proof that a biological target or ADC construct is safe or effective. Experimental validation remains essential.

## Requirements

Core packages:

```text
numpy
pandas
matplotlib
scipy
scikit-learn
xgboost
jupyter
```

GPU hardware is not required for the v0.1 notebooks.

## Quick Start

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Run the notebooks in numerical order. Notebooks 02–09 form the main target-discovery pipeline; Notebook 10 is the bridge to construct-level optimization.

To execute the complete canonical sequence from the repository root:

```bash
python scripts/run_all_notebooks.py
```

`requirements-tested.txt` records the exact package versions used in the v0.1 release audit; `requirements.txt` keeps broader minimum versions for ordinary installation.


## Documentation

- `docs/NOTEBOOK_SPEC.md` — canonical notebook dependencies and outputs
- `docs/DATA_SOURCES.md` — public-data access, version, and licensing notes
- `docs/GLOSSARY.md` — key terminology
- `docs/RELEASE_AUDIT.md` — v0.1 release audit
- `docs/RELEASE_NOTES_v0.1.0.md` — release notes and known limitations
- `docs/GITHUB_PUBLISHING.md` — canonical GitHub metadata and publishing steps
- `CHANGELOG.md` — release history
- `NOTICE.md` — third-party data notice

## Repository Status

### v0.1

```text
Target Discovery
→ Machine Learning
→ Positive–Unlabeled Learning
→ Wet-Lab Validation
→ Active Learning
→ ADC Construct Representation
```

### Planned next phase

- multi-objective ADC optimization
- construct-level surrogate models
- Bayesian optimization
- PK/PD and PBPK/QSP integration
- full Scientific AI / DBTL architectures

## Educational Philosophy

> Understand the biological problem first, build an interpretable baseline, then introduce more sophisticated AI only where it adds value.

## Disclaimer

This project is provided for educational and research purposes only. Nothing in this repository constitutes medical advice, clinical guidance, or a validated drug-development decision system.
