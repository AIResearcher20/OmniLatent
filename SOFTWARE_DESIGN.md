SOFTWARE_DESIGN

«Software Architecture & Design Specification

Project: OmniLatent

Version: 1.0

Status: Active Development»

---

Purpose

OmniLatent is a research software framework for multimodal biomedical representation learning. The architecture is designed to support reproducible research while remaining modular, extensible, and maintainable.

The framework separates data processing, model development, evaluation, and visualization into independent components to simplify experimentation and future extensions.

---

Design Goals

The software architecture is designed to satisfy the following engineering goals:

- Reproducibility
- Modularity
- Extensibility
- Maintainability
- Scalability
- Scientific Transparency

---

Design Philosophy

OmniLatent follows a framework-oriented design rather than a model-oriented implementation.

The architecture follows the principle of Separation of Concerns, where each software module has a clearly defined responsibility and minimal dependency on other modules.

The following principles guide all implementation decisions:

- Scientific questions drive software design.
- Configuration is preferred over hard-coded parameters.
- Production code belongs in "src/".
- Notebooks are reserved for exploratory analysis and visualization.
- Every experiment must be reproducible.

---

High-Level Architecture

                 Raw Data
                     │
                     ▼
              Preprocessing
                     │
                     ▼
          Feature Engineering
                     │
                     ▼
      Representation Learning
                     │
                     ▼
          Embedding Storage
                     │
                     ▼
              Model Evaluation
                     │
                     ▼
              Visualization

The patient embedding is considered the primary output of the framework and serves as the input for all downstream analyses.

---

Repository Structure

OmniLatent/

configs/
    brca.yaml
    luad.yaml
    kirc.yaml

data/
    raw/
    processed/
    metadata/

docs/

figures/

notebooks/

paper/

results/

src/
    data/
    models/
    training/
    evaluation/
    visualization/
    utils/

tests/

Repository organization is designed to separate reusable source code, experimental outputs, documentation, and exploratory notebooks.

---

Software Components

Module| Responsibility
"data"| Data loading, validation and preprocessing
"models"| Neural network architectures
"training"| Model training, optimization and checkpointing
"evaluation"| Quantitative benchmarking and downstream analyses
"visualization"| UMAP, heatmaps and publication-quality figures
"utils"| Shared utilities, logging and helper functions

Each module should be independently maintainable and reusable.

---

Data Pipeline

The preprocessing pipeline follows a deterministic workflow.

Raw Data
    ↓
Validation
    ↓
Cleaning
    ↓
Normalization
    ↓
Feature Engineering
    ↓
Training Dataset

Intermediate outputs should be stored whenever appropriate to improve reproducibility and reduce redundant computation.

---

Model Pipeline

The initial implementation employs a lightweight modality-specific encoder architecture.

RNA ───────┐
Clinical ──┼────► Shared Latent Space ───► Decoders
Mutation ──┘

The representation learning module is intentionally isolated so that future algorithms can replace it without affecting the remaining software components.

---

Configuration Strategy

All experiments are configured through external YAML configuration files.

Typical configuration parameters include:

- dataset
- latent dimension
- batch size
- learning rate
- number of epochs
- optimizer
- random seed

No experimental parameter should be hard-coded inside the implementation.

---

Output Organization

Each experiment automatically creates an independent output directory containing:

- configuration file
- trained model weights
- patient embeddings
- evaluation metrics
- publication figures
- execution logs
- software version

Experimental outputs must never overwrite previous results.

---

Design Decisions

The first implementation adopts a Multimodal Autoencoder as the representation learning backbone.

This choice provides:

- architectural simplicity,
- efficient CPU/GPU training,
- interpretable latent representations,
- straightforward comparison with classical baselines.

The framework architecture is intentionally independent of the underlying representation learning algorithm.

---

Quality Attributes

The software architecture prioritizes the following quality attributes:

- Reproducibility
- Readability
- Modularity
- Extensibility
- Maintainability
- Scientific Interpretability

Performance optimization is considered only after correctness and reproducibility have been established.

---

Future Evolution

The architecture is designed to support incremental extensions, including:

- Variational Autoencoders
- Contrastive Representation Learning
- Graph Neural Networks
- Self-Supervised Learning
- Additional Biomedical Modalities

Future developments should integrate into the existing framework without requiring substantial architectural modifications.

---

Guiding Principle

«Build a reusable scientific framework rather than a task-specific deep learning model.»

Every architectural decision should improve scientific reproducibility, software quality, and long-term maintainability.
