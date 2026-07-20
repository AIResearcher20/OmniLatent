
<div align="center">

# 🧬 OmniLatent

### *A Generalizable Latent Representation Framework for Biomedical Transcriptomic Data*

<br>

<p>
<img src="https://img.shields.io/badge/Field-Biomedical%20AI-0077B6?style=for-the-badge&logo=biolink">
<img src="https://img.shields.io/badge/Method-Autoencoder-6C5CE7?style=for-the-badge&logo=pytorch">
<img src="https://img.shields.io/badge/Focus-Representation%20Learning-00A896?style=for-the-badge&logo=target">
<img src="https://img.shields.io/badge/Status-Research%20Prototype-FFA500?style=for-the-badge">
<img src="https://img.shields.io/badge/Version-v1.0-8E44AD?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-F39C12?style=for-the-badge">
<img src="https://img.shields.io/badge/TCGA-BRCA-FF6B6B?style=for-the-badge">
</p>

<br>

**OmniLatent** is a research-oriented framework for learning robust, interpretable, and transferable latent representations from high-dimensional biomedical data — with a focus on RNA-seq expression profiles.

The project is motivated by the hypothesis that **heterogeneous biomedical observations can be mapped into shared latent spaces** that capture underlying biological structure, enabling downstream analyses and future evaluation of cross-cancer generalization.

</div>

---

## 📋 Table of Contents

- [Current Status](#-current-status)
- [Overview](#-overview)
- [Research Questions](#-research-questions)
- [Datasets](#-datasets)
- [Methodology](#-methodology)
- [Architecture](#-architecture)
- [Results](#-results)
- [Visualizations](#-visualizations)
- [🧪 Example Usage](#-example-usage)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Model Availability](#-model-availability)
- [Repository Structure](#-repository-structure)
- [Reproducibility](#-reproducibility)
- [Limitations & Future Work](#-limitations--future-work)
- [Relation to Biomedical Representation Learning](#-relation-to-biomedical-representation-learning)
- [Citation](#-citation)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 📍 Current Status

**OmniLatent v1.0** is an initial research prototype focused on validating latent representation learning from TCGA-BRCA RNA-seq data. Future releases will expand toward multimodal biomedical representation learning.

| Aspect | Status |
|--------|--------|
| **RNA-seq representation** | ✅ Evaluated on TCGA-BRCA |
| **Multimodal integration** | 🔬 Under development |
| **Cross-cancer validation** | 📋 Planned |
| **Biological interpretation** | 🔬 Ongoing |

---


---

## 🚧 Project Status

OmniLatent is an actively developed research project.

The current repository presents **Version 1.0**, which focuses on validating latent representation learning from TCGA-BRCA RNA-seq data using a deep autoencoder architecture. The experiments reported in this repository have been completed and form the foundation of the project.

Current development is focused on extending the framework toward its next research milestones, including:

- 🔬 Integration of multimodal biomedical data (clinical variables and somatic mutations)
- 🔬 Cross-cancer validation on independent TCGA cohorts (e.g., LUAD, KIRC)
- 🔬 Biological interpretation of learned representations
- 🔬 Comparative evaluation against additional baseline methods
- 🔬 Manuscript preparation for peer-reviewed publication

The repository will continue to be updated as these research components are completed.
----

## 🔬 Overview

### The Problem

Modern biomedical datasets generate massive amounts of high-dimensional data. A single RNA-seq experiment measures expression levels of over **23,000 genes** per sample. This dimensionality creates several challenges:

1. **Curse of Dimensionality**: Statistical methods become unreliable
2. **Computational Inefficiency**: Processing 23,000+ features is resource-intensive
3. **Interpretability**: Understanding patterns across thousands of genes is nearly impossible
4. **Generalization**: Models trained on high-dimensional data often overfit

### The Solution

OmniLatent employs a **deep autoencoder architecture** to learn a **nonlinear, 128-dimensional latent representation** that:

- Compresses 23,375 genes into 128 features (~99.5% reduction)
- Preserves biologically relevant structure
- Enables downstream tasks (clustering, visualization, classification)
- Provides a foundation for multimodal integration

### Philosophy

> *"Rather than claiming superiority, we position OmniLatent as an exploratory framework for learning biologically meaningful representations from high-dimensional transcriptomic data."*

---

## 🎯 Research Questions

| # | Research Question | Status | Evidence |
|---|-------------------|--------|----------|
| **RQ1** | Can high-dimensional RNA-seq data (23,375 genes) be compressed into a meaningful latent space (128 dims)? | ✅ **Yes** | 99.5% reduction, Test Loss = 0.313 |
| **RQ2** | Does the latent space preserve biological structure? | 🔬 **Preliminary evidence** | Structured latent organization observed, with exploratory tumor/normal separation |
| **RQ3** | How does nonlinear compression compare to linear PCA? | 🔬 **Under investigation** | Initial results promising |
| **RQ4** | Are the learned representations biologically interpretable? | 🔬 **Ongoing** | Tumor/normal patterns observed |
| **RQ5** | Can one representation support multiple downstream tasks? | 🔬 **Planned** | Clustering + visualization + classification |
| **RQ6** | Can representations generalize across different cancer types? | 🔬 **Planned** | TCGA-LUAD, TCGA-KIRC, TCGA-COAD |
| **RQ7** | Which modality contributes most to the learned representation? | 🔬 **Planned** | RNA-seq, clinical, mutation |
| **RQ8** | How robust are representations to missing or noisy data? | 🔬 **Planned** | Ablation studies |

---

## 🧬 Datasets

### Primary Training Cohort

| Dataset | Source | Samples | Features | Type | Version |
|---------|--------|---------|----------|------|---------|
| **TCGA-BRCA** | The Cancer Genome Atlas | 1,231 | 23,375 genes | RNA-seq (log1p) | v1.0.0 |

**Preprocessing:**
1. Raw RNA-seq counts from TCGA-GDC
2. Log1p transformation: `log(x + 1)`
3. Filtering for protein-coding genes
4. Standardization per gene (mean=0, std=1)

### Generalization Cohorts *(Planned)*

| Dataset | Cancer Type | Status |
|---------|-------------|--------|
| TCGA-LUAD | Lung Adenocarcinoma | 📋 Planned |
| TCGA-KIRC | Kidney Renal Cell Carcinoma | 📋 Planned |
| TCGA-COAD | Colon Adenocarcinoma | 📋 Planned |

### Data Split

| Split | Samples | Percentage |
|-------|---------|------------|
| **Training** | 984 | 80% |
| **Validation** | 123 | 10% |
| **Test** | 124 | 10% |

---

## 🏗️ Methodology

### Core Approach

OmniLatent uses a **stacked autoencoder architecture**:

1. **Encoder**: Dimensionality reduction through successive linear layers with ReLU activations
2. **Bottleneck**: 128-dimensional latent space (the compressed representation)
3. **Decoder**: Reconstruction back to the original 23,375-dimensional space

### Loss Function

Mean Squared Error (MSE):

$$\mathcal{L}_{MSE} = \frac{1}{n} \sum_{i=1}^{n} ||x_i - \hat{x}_i||^2$$

### Training Configuration

| Parameter | Value |
|-----------|-------|
| **Batch Size** | 32 |
| **Learning Rate** | 1e-3 |
| **Optimizer** | Adam |
| **Epochs** | 10 |
| **Seed** | 42 |

---

## 🧮 Architecture

### Model Structure

```

INPUT (23,375) → 4096 → 1024 → 256 → 128 (Latent) → 256 → 1024 → 4096 → OUTPUT (23,375)

```

### Parameter Count

| Component | Parameters |
|-----------|------------|
| **Encoder** | ~95.9M |
| **Decoder** | ~95.9M |
| **Total** | **~191.8M** |

**Note:** The model has a large parameter-to-sample ratio (1,231 samples, ~156K parameters per sample), which is addressed in the Limitations section. The current architecture was selected as an initial proof-of-concept design. Architecture scaling and parameter-efficient variants will be investigated in future versions.

---

## 📊 Results

### Training Performance

| Metric | Value |
|--------|-------|
| **Best Validation Loss** | **0.3226** |
| **Final Train Loss** | 0.3171 |
| **Final Validation Loss** | 0.3226 |
| **Test Loss** | **0.3129** |

**Interpretation:** The near-identical training and validation losses (0.3171 vs 0.3226) suggest that the model generalizes without significant overfitting on this dataset.

### Dimensionality Reduction Analysis

**PCA on the Learned Latent Space:**

| Component | Variance Explained |
|-----------|-------------------|
| PC1 | 56.23% |
| PC2 | 31.94% |
| **Total (PC1+PC2)** | **88.17%** |

**Interpretation:** The first two principal components capture 88.17% of latent-space variance, suggesting that the learned representation contains strong low-dimensional organization.

#### Exploratory Reconstruction Comparison

| Method | Dimensions | Reconstruction MSE | Notes |
|--------|------------|-------------------|-------|
| **PCA (2D)** | 2 | 0.933 | Linear projection for visualization |
| **OmniLatent** | 128 | **0.313** | Learned nonlinear representation |

**Important Note:** This is an exploratory comparison, not a formal benchmark. OmniLatent achieves lower reconstruction error than a 2D PCA visualization baseline, while a dimensionality-matched comparison with PCA (128 components) remains future work.

---

### Clustering Analysis

#### Optimal Number of Clusters

| k | Silhouette ↑ | Davies-Bouldin ↓ | Calinski-Harabasz ↑ |
|---|-------------|------------------|---------------------|
| **2** | **0.540** | **0.694** | 169.436 |
| 3 | 0.432 | 0.737 | 182.406 |
| 4 | 0.458 | 0.672 | 202.283 |
| 5 | 0.462 | 0.577 | 193.066 |
| 6 | 0.417 | 0.639 | 197.964 |
| 7 | 0.435 | 0.633 | 185.235 |
| 8 | 0.428 | 0.649 | 178.901 |
| 9 | 0.420 | 0.658 | 172.346 |
| 10 | 0.402 | 0.689 | 165.432 |

Among evaluated cluster numbers, k=2 achieved the highest Silhouette score (0.540).

#### Cluster Stability (k=2)

**ARI Calculation:** Adjusted Rand Index was calculated between K-means runs using different random seeds to evaluate clustering reproducibility (not compared to biological labels).

| Metric | Value |
|--------|-------|
| **Mean ARI (10 runs)** | **1.000** |
| **Standard Deviation** | **0.000** |

**Interpretation:** This indicates that K-means assignments were highly reproducible across different initializations. The latent space shows consistent structure that leads to stable clustering outcomes.

#### Cluster Sizes (k=2)

| Cluster | Count |
|---------|-------|
| Cluster 0 | 62 |
| Cluster 1 | 62 |

### Biological Structure Preservation

#### Unsupervised Clustering (k=2)
- **Purpose:** Evaluates global latent structure
- **Result:** Clear separation into two clusters, indicating strong latent structure

#### Exploratory Clustering (k=5)
- **Purpose:** Reveals finer-grained patterns
- **Result:** All primary tumor samples (120) cluster together; the only normal samples (4) appear in a separate cluster (83.3% tumor in cluster 4)

**Interpretation:** The latent space shows preliminary separation patterns consistent with tumor-normal identity. However, with only 4 normal samples in the test set, larger balanced validation cohorts are required to make definitive claims about biological separation.

#### Sample Type Distribution (Test Set)

| Sample Type | Count | Percentage |
|-------------|-------|------------|
| **Primary Tumor** | 120 | 96.8% |
| **Solid Tissue Normal** | 4 | 3.2% |

---

## 📊 Visualizations

### Training Performance

<p align="center">
  <img src="outputs/loss_curve.png" width="600" alt="Loss Curve"/>
</p>

*Training and validation loss across 10 epochs. Rapid convergence and minimal overfitting indicate successful learning.*

---

### Dimensionality Reduction

<p align="center">
  <img src="outputs/pca_latent_space.png" width="400" alt="PCA"/>
  <img src="outputs/umap_latent_space.png" width="400" alt="UMAP"/>
</p>

*PCA projection (left) captures 88.17% variance in 2D. UMAP projection (right) preserves local and global structure.*

---

### Clustering Visualization

<p align="center">
  <img src="outputs/umap_clusters_k2.png" width="400" alt="Clusters k=2"/>
  <img src="outputs/umap_clusters_k5.png" width="400" alt="Clusters k=5"/>
</p>

*UMAP with K-means clustering: k=2 (left) shows global structure, k=5 (right) reveals finer patterns.*

---

### Latent Space Analysis

<p align="center">
  <img src="outputs/latent_distribution.png" width="400" alt="Distribution"/>
  <img src="outputs/latent_boxplot.png" width="400" alt="Boxplot"/>
</p>

*Latent distribution (left) approximates normal distribution. Feature boxplot (right) shows variation across 128 dimensions.*

---

### Correlation Analysis

<p align="center">
  <img src="outputs/latent_correlation_heatmap.png" width="500" alt="Correlation Heatmap"/>
</p>

*Correlation heatmap of 128 latent features showing independence patterns.*

---

## 🧪 Example Usage

### Complete Workflow

```python
import torch
import pandas as pd
from src.omnilatent.model import OmniLatentAutoEncoder

# 1. Load pretrained model
model = OmniLatentAutoEncoder(input_dim=23375, latent_dim=128)
model.load_state_dict(torch.load("best_model.pt"))
model.eval()

# 2. Load RNA-seq data
data = pd.read_parquet("expression_matrix.parquet")
X = torch.tensor(data.values, dtype=torch.float32)

# 3. Extract latent embeddings
with torch.no_grad():
    _, embeddings = model(X)

# 4. Downstream analysis
print(f"Original: {X.shape} → Compressed: {embeddings.shape}")  # (n, 23375) → (n, 128)

# 5. Visualization
from umap import UMAP
import matplotlib.pyplot as plt

umap = UMAP(n_components=2)
emb_2d = umap.fit_transform(embeddings)

plt.scatter(emb_2d[:, 0], emb_2d[:, 1], s=5)
plt.title("Latent Space Visualization")
plt.show()
```

Data Flow:

```
RNA-seq matrix (n, 23375)
        ↓
OmniLatent Encoder
        ↓
128-dimensional latent embedding (n, 128)
        ↓
UMAP / clustering / downstream analysis
```

---

⚙️ Installation

Clone Repository

```bash
git clone https://github.com/AIResearcher20/OmniLatent.git
cd OmniLatent
```

Install Dependencies

```bash
pip install -r requirements.txt
```

requirements.txt:

```
torch>=2.0.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
umap-learn>=0.5.0
pyarrow>=12.0.0
```

---

🚀 Quick Start

1. Train the Model

```bash
python src/omnilatent/train.py
```

2. Extract Latent Embeddings

```bash
python src/omnilatent/extract_embeddings.py
```

3. Evaluate the Model

```bash
python src/omnilatent/evaluate.py
```

4. Analyze the Latent Space

```bash
python src/omnilatent/visualization.py
```

---

📦 Model Availability

Hugging Face Repository

Model: Sepideh2027/OmniLatent-TCGA-BRCA-model

Available Files:

· best_model.pt — Trained OmniLatent autoencoder weights
· model.safetensors — SafeTensors format
· config.json — Model configuration

Dataset: Sepideh2027/OmniLatent-TCGA-BRCA

Load Pretrained Model

```python
import torch
from src.omnilatent.model import OmniLatentAutoEncoder

model = OmniLatentAutoEncoder(input_dim=23375, latent_dim=128)
model.load_state_dict(torch.load("best_model.pt"))
model.eval()

with torch.no_grad():
    _, embeddings = model(data)
```

---

📂 Repository Structure

```
OmniLatent/
├── configs/
├── docs/
├── src/omnilatent/
├── tests/
├── .gitignore
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

---

🔬 Reproducibility

Key Results Summary

Metric Value
Best Validation Loss 0.3226
Test Loss 0.3129
PCA Explained Variance (in latent space) 88.17%
PCA Reconstruction MSE (Exploratory) 0.933
Best Silhouette Score 0.540
Mean ARI (10 runs) 1.000
Optimal Clusters 2

Stability Analysis

· ✅ Training converges consistently across runs
· ✅ Clustering stable (ARI = 1.0) across 10 random seeds
· ✅ No overfitting: train/val gap = 0.0055
· ✅ Deterministic results with seed=42

Reproducibility Checklist

· Fixed random seed (42)
· Version-controlled code
· Documented preprocessing
· Pretrained model published
· Dataset published
· Visualization scripts provided
· Comprehensive evaluation metrics

---

⚠️ Limitations & Future Work

Current Limitations

Limitation Description
Dataset Size 1,231 samples may limit generalization
Model Size 192M parameters (~156K per sample) requiring further evaluation of regularization and scaling strategies
Single Modality Currently RNA-seq only
Single Cancer Type Only TCGA-BRCA validated
Interpretability Biological interpretation limited
Normal Samples Only 4 normal samples in test set

Future Work

Short-term (0-6 months):

· Add regularization (dropout, weight decay)
· Variational autoencoder (VAE) implementation
· Cross-cancer validation on TCGA-LUAD, TCGA-KIRC
· Evaluate smaller architectures for comparable performance
· Direct comparison with PCA (128 components)

Medium-term (6-12 months):

· Multimodal integration (clinical, mutation, methylation)
· Survival analysis using latent features
· Pathway-level biological interpretation
· Robustness studies with simulated missing data

Long-term (12+ months):

· Large-scale pretraining on Pan-Cancer data
· Transfer learning across cancer types
· Integration with histopathology images
· Clinical outcome prediction

---

🧬 Relation to Biomedical Representation Learning

OmniLatent is motivated by recent efforts in biomedical foundation models and representation learning, where the objective is to learn transferable latent representations from heterogeneous biological data.

The current version focuses on transcriptomic representation learning as a first step toward future multimodal extensions.

Key Connections:

· Shared representations across biological contexts
· Transfer learning between cancer types
· Multimodal integration for comprehensive patient profiles
· Interpretable features for biological discovery

This direction is related to recent biomedical foundation models and large-scale representation learning approaches.

---

📝 Citation

```bibtex
@misc{omnilatent2026,
  author = {Sepideh2027},
  title = {OmniLatent: A Generalizable Latent Representation Framework for Biomedical Data},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/AIResearcher20/OmniLatent}
}
```

---

📄 License

MIT License

---

🙏 Acknowledgments

· The Cancer Genome Atlas (TCGA) — Data source
· Hugging Face — Model and dataset hosting
· Open-source community — Tools and libraries

---

<div align="center">

OmniLatent — Advancing Biomedical AI through Open Science

<br>

<p>
<a href="https://github.com/AIResearcher20/OmniLatent"> GitHub</a> •
<a href="https://huggingface.co/Sepideh2027/OmniLatent-TCGA-BRCA-model">  Model</a> •
<a href="https://huggingface.co/datasets/Sepideh2027/OmniLatent-TCGA-BRCA">📊 Dataset</a>
</p>

</div>
```

---
