# OmniLatent TCGA-BRCA Model Card

## Model Overview

OmniLatent is an autoencoder-based representation learning model designed for high-dimensional biomedical gene expression data.

The model learns compact latent representations from TCGA-BRCA RNA-seq expression profiles.

---

## Model Details

| Parameter | Value |
|---|---|
| Dataset | TCGA-BRCA |
| Model type | Autoencoder |
| Input dimension | 23,375 genes |
| Latent dimension | 128 |
| Framework | PyTorch |

---

## Training Information

The model was trained to minimize reconstruction error between input gene expression profiles and reconstructed outputs.

Best training loss:

0.32262297719717026

---

## Available Files

- `best_model.pt`  
  Trained OmniLatent autoencoder weights.

- `model_config.json`  
  Model configuration containing dataset and architecture information.

---

## Usage

The model can be used for:

- latent representation extraction
- dimensionality reduction
- downstream biomedical analysis
- clustering analysis

---

## Input Format

Expected input:

(samples, 23375)

where each sample represents a normalized gene expression profile.

---

## Output Format

The encoder produces:

(samples, 128)

latent representations.

---

## Evaluation Results

Reconstruction performance:

| Method | Latent Dimension | MSE |
|---|---:|---:|
| PCA baseline | 128 | 0.933 |
| OmniLatent Autoencoder | 128 | 0.3129 |

---

## Limitations

This initial release was evaluated on TCGA-BRCA.

Further validation is planned on:

- TCGA-LUAD
- TCGA-KIRC
- TCGA-COAD

Additional biological validation will include:

- molecular subtype association
- pathway enrichment analysis
- survival analysis

---

## License

MIT License

