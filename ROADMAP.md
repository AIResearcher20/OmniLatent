ROADMAP

«Development Roadmap

Project: OmniLatent

Version: 1.0

Status: Active Development»

---

Vision

OmniLatent aims to become a reproducible, modular, and extensible framework for multimodal biomedical representation learning.

The framework is designed to learn biologically meaningful patient representations that generalize across multiple cancer types while supporting downstream biomedical analyses.

---

Development Phases

Phase 0 — Project Foundation ✅

Establish the scientific and software foundations of the project.

Objectives

- Define the research protocol
- Design the software architecture
- Organize the repository
- Prepare project documentation

Deliverable

A well-documented and reproducible research framework.

---

Phase 1 — Data Acquisition 🟡

Collect, validate, and organize multimodal TCGA datasets.

Tasks

- Acquire TCGA-BRCA RNA-seq data
- Acquire TCGA-BRCA clinical data
- Acquire TCGA-BRCA mutation data
- Harmonize patient identifiers
- Validate dataset consistency
- Organize raw datasets

Deliverable

A validated multimodal BRCA dataset ready for preprocessing.

---

Phase 2 — Data Preprocessing ⚪

Prepare multimodal datasets for machine learning.

Tasks

- RNA normalization
- Gene filtering
- Clinical preprocessing
- Mutation preprocessing
- Feature engineering
- Dataset integration

Deliverable

A clean and standardized multimodal dataset.

---

Phase 3 — Baseline Models ⚪

Implement reference methods for benchmarking.

Methods

- Principal Component Analysis (PCA)
- RNA Autoencoder
- MOFA+

Deliverable

Baseline performance benchmarks.

---

Phase 4 — OmniLatent v1 ⚪

Develop the first version of the proposed framework.

Tasks

- RNA encoder
- Clinical encoder
- Mutation encoder
- Shared latent space
- Modality-specific decoders
- Training pipeline

Deliverable

A fully functional multimodal autoencoder capable of generating patient embeddings.

---

Phase 5 — Evaluation ⚪

Assess the quality and biological relevance of the learned representations.

Tasks

- UMAP visualization
- Clustering evaluation
- Clinical association analysis
- Molecular subtype analysis
- Survival analysis
- Latent space interpretation

Deliverable

A comprehensive evaluation of representation quality.

---

Phase 6 — Cross-Cancer Generalization ⚪

Evaluate representation transferability across independent cancer cohorts.

Tasks

- Train on TCGA-BRCA
- Freeze the encoder
- Generate embeddings for TCGA-LUAD
- Generate embeddings for TCGA-KIRC
- Compare against baseline methods

Deliverable

Cross-cancer generalization benchmark.

---

Phase 7 — Robustness Analysis ⚪

Evaluate model robustness under imperfect data conditions.

Tasks

- Missing modality experiments
- Noise injection
- Feature corruption
- Ablation studies

Deliverable

Robustness analysis of learned representations.

---

Phase 8 — Manuscript Preparation ⚪

Prepare publication-ready scientific materials.

Tasks

- Methods
- Results
- Discussion
- Figures
- Supplementary materials

Deliverable

A complete, submission-ready research manuscript.

---

Expected Outputs

The completed project will provide:

- A reproducible research software framework
- A multimodal representation learning model
- Patient embedding datasets
- Standardized evaluation pipelines
- Publication-quality figures
- Comprehensive project documentation
- A publication-ready scientific manuscript

---

Future Evolution

The architecture is designed to support future extensions, including:

- Variational Autoencoders
- Contrastive Representation Learning
- Graph Neural Networks
- Self-Supervised Learning
- Additional biomedical modalities
- Expanded cross-cancer validation

---

Guiding Principle

«Develop a reusable scientific framework through incremental, reproducible, and scientifically motivated development.»
