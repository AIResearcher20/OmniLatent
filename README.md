OmniLatent

![Framework](https://img.shields.io/badge/Framework-OmniLatent-darkgreen)
![Biomedical AI](https://img.shields.io/badge/Biomedical-AI-blueviolet)
![Multimodal](https://img.shields.io/badge/Multimodal-Learning-red)
![Interpretability](https://img.shields.io/badge/Interpretable-Yes-brightgreen)
![Generalization](https://img.shields.io/badge/Cross--Cancer-Evaluation-critical)

A Modular Framework for Generalizable Multimodal Representation Learning from Biomedical Data

---

Overview

OmniLatent is a research-oriented framework for learning robust, interpretable, and transferable latent representations from heterogeneous biomedical data.

Instead of focusing on a single prediction task, OmniLatent aims to learn a shared representation that integrates multiple biomedical modalities into a unified latent space suitable for a wide range of downstream analyses.

The project is motivated by recent advances in Representation Learning and AI for Scientific Discovery.

---

Research Questions

This project investigates the following scientific questions:

- How can heterogeneous biomedical modalities be integrated into a unified latent representation?
- Does multimodal representation learning outperform single-modal learning?
- Does nonlinear representation learning outperform classical dimensionality reduction methods such as PCA?
- Are the learned representations biologically meaningful?
- Can one representation support multiple downstream tasks?
- Can representations generalize across different cancer types?
- Which modality contributes most to the learned representation?
- How robust are learned representations to missing or noisy biomedical data?

---

Datasets

Training cohort:

- TCGA-BRCA

Generalization cohorts:

- TCGA-LUAD
- TCGA-KIRC

Future evaluation:

- TCGA-COAD

---

Modalities

- RNA sequencing
- Clinical data
- Somatic mutation profiles

Future versions may include DNA methylation, copy number variation, and histopathology.

---

Initial Framework

RNA Encoder
           \
Clinical -----> Shared Latent Space -----> Decoders
           /
Mutation Encoder

The initial implementation is intentionally lightweight and serves as the first version of the OmniLatent framework.

---

Baselines

- PCA
- RNA-only Autoencoder
- MOFA+
- OmniLatent

---

Planned Evaluation

- Latent space visualization (UMAP)
- Biological association
- Survival analysis
- Cross-cancer generalization
- Ablation studies
- Robustness evaluation

---

Repository Structure

configs/
data/
notebooks/
src/
results/
figures/
paper/

---

Development Status

Current phase:

Phase 1 — Data Acquisition and Research Infrastructure

---

License

MIT License
---
