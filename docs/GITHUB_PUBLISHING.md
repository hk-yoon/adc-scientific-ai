# GitHub Publishing Guide — v0.1.0

## Canonical repository metadata

**Repository name**

`adc-scientific-ai`

**Repository description**

`Educational Scientific AI notebooks for ADC development, from target prioritization to closed-loop experimental design and construct representation.`

**Recommended visibility**

Public

**Canonical topics**

- `scientific-ai`
- `antibody-drug-conjugate`
- `adc`
- `drug-discovery`
- `machine-learning`
- `positive-unlabeled-learning`
- `active-learning`
- `bioinformatics`
- `computational-biology`
- `jupyter-notebook`

## Initial commit

Recommended first commit message:

`Release educational ADC Scientific AI notebooks v0.1.0`

## Release

**Tag**

`v0.1.0`

**Release title**

`ADC Scientific AI v0.1.0 — Target Discovery to Construct Representation`

**Release body**

Use the contents of `docs/RELEASE_NOTES_v0.1.0.md`.

## Suggested publishing sequence

From the repository root after creating an empty GitHub repository:

```bash
git init
git add .
git commit -m "Release educational ADC Scientific AI notebooks v0.1.0"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

After reviewing the rendered notebooks on GitHub:

```bash
git tag -a v0.1.0 -m "ADC Scientific AI v0.1.0"
git push origin v0.1.0
```

Then create a GitHub Release from tag `v0.1.0` and paste `docs/RELEASE_NOTES_v0.1.0.md` into the release body.

## Before creating the tag

1. Run the notebooks in the intended release environment.
2. Confirm GitHub renders all ten notebooks correctly.
3. Verify no private, proprietary, patient-level, controlled-access, or accidental large files are present.
4. Confirm synthetic and simulated data labels remain visible.
5. Confirm links in `docs/DATA_SOURCES.md` still resolve.
6. Only then create the immutable `v0.1.0` release tag.

## Versioning direction

- `v0.1.x` — corrections and documentation improvements to the current educational scope.
- `v0.2.0` — Phase II: multi-objective ADC construct optimization and construct-level surrogate modeling.
- Later versions — Bayesian optimization, PK/PD, PBPK/QSP, and broader Scientific AI / DBTL integration.
