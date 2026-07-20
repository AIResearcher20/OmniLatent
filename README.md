<div align="center">

# **OmniLatent**

### A Generalizable Multimodal Representation Learning Framework for Biomedical AI

<br>

<p>
<img src="https://img.shields.io/badge/Field-Biomedical%20AI-0077B6?style=for-the-badge&logo=biolink">
<img src="https://img.shields.io/badge/Method-Multimodal%20Learning-6C5CE7?style=for-the-badge&logo=pytorch">
<img src="https://img.shields.io/badge/Focus-Interpretability-00A896?style=for-the-badge&logo=target">
<img src="https://img.shields.io/badge/License-MIT-F39C12?style=for-the-badge">
</p>

<br>

<i>
A modular framework for interpretable and generalizable multimodal representation learning from heterogeneous biomedical data.
</i>

</div>
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

## Model Availability

The pretrained OmniLatent TCGA-BRCA model is available on Hugging Face:

https://huggingface.co/Sepideh2027/OmniLatent-TCGA-BRCA-model

Available files:

- `best_model.pt` — trained OmniLatent autoencoder weights
- `model_config.json` — model architecture configuration

The model can be used for latent representation extraction and downstream biomedical analysis.
---

License

MIT License
---
