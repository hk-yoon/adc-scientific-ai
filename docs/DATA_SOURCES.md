# Data Sources and Access Notes

_Last verified: 2026-10-06._

## v0.1 policy

The executable v0.1 notebooks do **not** redistribute TCGA, GTEx, or Human Protein Atlas datasets. They use small synthetic or example data so the complete educational pipeline can run end-to-end on an ordinary laptop.

The public resources below are the intended real-data extension paths. Users must check the current provider documentation, version, citation guidance, and access conditions before downloading or redistributing data.

## TCGA / NCI Genomic Data Commons (GDC)

- GDC Data Portal: https://portal.gdc.cancer.gov/
- GDC data-access policies: https://gdc.cancer.gov/access-data/data-access-policies
- TCGA resources: https://gdc.cancer.gov/about-data/gdc-data-processing/resources-tcga-users

As of 2026-10-06, the GDC Portal reports Data Release 46.0 (2026-08-10). TCGA includes both open- and controlled-access data. Open-access data do not require authentication, but users must follow the NIH Genomic Data Sharing policy, including no re-identification attempts and appropriate acknowledgement. Controlled-access data require dbGaP authorization.

For this repository, a real-data extension should preferentially use open, harmonized expression-level data unless there is a specific need for controlled raw sequencing files.

## GTEx

- GTEx Portal: https://gtexportal.org/
- Adult GTEx open-access downloads: https://gtexportal.org/home/downloads/adult-gtex/

As of 2026-10-06, the Adult GTEx Portal provides V11 bulk RNA-seq open-access files. The V11 update uses GENCODE 47 annotation and contains no new samples or donors relative to V10. Open-access expression data can be downloaded through the GTEx Portal; raw sequence data and full donor metadata are protected-access data and require the appropriate authorization path.

Users should acknowledge GTEx according to the current portal guidance and record the download date/version used for any reproducible analysis.

## UCSC Xena / Toil RNA-seq recompute

- UCSC Xena: https://xena.ucsc.edu/
- Public-data overview: https://xena.ucsc.edu/public/
- Data download overview: https://xena.ucsc.edu/download-data/
- Xena Browser data pages: https://xenabrowser.net/datapages/

UCSC Xena provides precompiled public datasets and exposes the **UCSC Toil RNA-seq Recompute** hub. Xena explicitly supports comparisons of TCGA tumor samples with GTEx normal samples. The Toil recompute approach is useful educationally because samples from different projects can be processed with a common RNA-seq pipeline.

Important: uniform reprocessing does not remove all cohort, sampling, tissue-composition, or biological confounding. Always inspect phenotype metadata, sample type, gene identifiers, and expression transformation before comparing tumor and normal cohorts.

The exact Xena dataset filenames and schemas can change. The v0.1 repository therefore does not hard-code a remote filename; a future real-data notebook should discover/verify the current dataset before download.

## Human Protein Atlas (HPA)

- Downloadable data: https://www.proteinatlas.org/about/download
- Tissue data: https://www.proteinatlas.org/humanproteome/tissue/data
- Licence and citation: https://www.proteinatlas.org/about/licence

As of 2026-10-06, the current HPA release is **version 25.1** (released 2026-05-25; Ensembl 109). The normal-tissue IHC resource covers 45 tissues and 76 standard annotated cell types. The downloadable normal IHC file is listed as `normal_ihc_data.tsv.zip` and includes Ensembl gene identifier, tissue, cell type, expression level, and reliability.

HPA states that copyrightable parts of its database are licensed under **CC BY 4.0**, while third-party data included in HPA may have separate constraints. Users must follow HPA citation guidance and verify third-party terms where applicable.

For ADC work, HPA IHC is a normal-tissue protein-expression signal, not a direct measurement of extracellular epitope accessibility, receptor density, internalization, systemic exposure, or clinical toxicity.

## Synthetic vs public data in v0.1

| Notebook | Executable v0.1 data mode | Real-data extension |
|---|---|---|
| 01 | Synthetic | Not required |
| 02 | Synthetic TCGA/GTEx-style matrices | TCGA + GTEx, preferably harmonized/reprocessed |
| 03 | Synthetic HPA-style IHC | HPA normal-tissue IHC |
| 04–07 | Derived from the above example data | Derived real feature matrices |
| 08–09 | Simulated wet-lab outcomes | Actual assay/LIMS results |
| 10 | Simulated ADC components/constructs | Curated construct and assay records |

## Reproducibility rule

For any real-data extension, record at minimum:

- provider and dataset/project name;
- version/release date;
- download date;
- accession or dataset identifier;
- gene annotation version;
- sample inclusion/exclusion rules;
- expression scale/transformation;
- code/commit used for feature generation;
- applicable data-use or licence notes.
