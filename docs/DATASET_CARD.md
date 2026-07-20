# OmniLatent TCGA-BRCA Dataset Card

## Dataset Overview

This dataset contains processed biomedical data used for training and evaluating the OmniLatent representation learning framework.

The dataset is derived from:

- TCGA-BRCA (The Cancer Genome Atlas Breast Invasive Carcinoma)

---

## Data Source

Original data source:

https://portal.gdc.cancer.gov/

TCGA data are publicly available under the corresponding data access policies.

---

## Dataset Structure

dataset/ ├── raw/ │   └── Original downloaded data │ ├── processed/ │   ├── train_samples.csv │   ├── val_samples.csv │   └── test_samples.csv │ └── metadata/

---

## Data Characteristics

| Property | Value |
|---|---:|
| Cohort | TCGA-BRCA |
| Input type | RNA-seq gene expression |
| Features | 23,375 genes |
| Samples | 1,231 |
| Latent dimension | 128 |

---

## Processing Pipeline

The preprocessing workflow includes:

- quality control
- feature selection
- normalization
- train/validation/test splitting
- preparation for neural representation learning

---

## Files

### Raw Data

Contains original downloaded biomedical data.

### Processed Data

Contains model-ready matrices used by OmniLatent training pipeline.

---

## Usage

The dataset is intended for:

- representation learning research
- latent space analysis
- biomedical clustering experiments
- downstream evaluation

---

## License and Attribution

TCGA data usage follows the policies of the Genomic Data Commons (GDC).

Users should cite the original TCGA publications when using the data.

بعد:
