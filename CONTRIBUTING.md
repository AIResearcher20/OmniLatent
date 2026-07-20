# Contributing to OmniLatent

Thank you for your interest in contributing to **OmniLatent**.

OmniLatent is an open-source scientific framework dedicated to **multimodal biomedical representation learning**. The project is developed to support reproducible computational research, biologically meaningful representation learning, and transparent software engineering for biomedical artificial intelligence.

Rather than focusing exclusively on predictive performance, OmniLatent aims to establish a reusable research framework capable of supporting diverse biomedical discovery tasks through robust latent representations.

Contributions from researchers, software engineers, computational biologists, clinicians, and students are welcome.

Every contribution—whether scientific, technical, or documentation-related—helps improve the quality, reproducibility, and long-term sustainability of the project.

---

# Project Philosophy

Development decisions within OmniLatent are guided by the following principles:

- Scientific questions drive methodological choices.
- Reproducibility takes precedence over complexity.
- Biological interpretability is considered a primary objective.
- Software should remain modular, maintainable, and extensible.
- Open science practices maximize transparency and collaboration.

The framework is intended to evolve incrementally while maintaining a stable and reproducible scientific foundation.

---

# Ways to Contribute

Contributions may include, but are not limited to:

## Scientific Contributions

- Novel representation learning methods
- Baseline model implementations
- Biological interpretation techniques
- Evaluation methodologies
- Cross-cancer benchmarking
- Statistical analysis improvements

---

## Software Contributions

- Data preprocessing improvements
- Training pipeline enhancements
- Visualization modules
- Performance optimization
- Software architecture improvements
- Testing infrastructure
- Documentation improvements

---

## Community Contributions

- Bug reports
- Feature requests
- Reproducibility reports
- Documentation corrections
- Tutorial notebooks
- Example workflows

Every contribution that improves scientific quality or software reliability is valued.

---

# Before Contributing

Before implementing substantial methodological or architectural modifications, contributors are encouraged to open a GitHub Issue describing:

- the proposed change,
- its scientific motivation,
- expected benefits,
- possible limitations,
- implementation strategy (when applicable).

Early discussion helps ensure that proposed developments remain aligned with the long-term scientific objectives of OmniLatent and avoids duplicated development effort.

Small documentation improvements and minor bug fixes generally do not require prior discussion.

---

# Development Workflow

To ensure code quality and reproducibility, contributors are encouraged to follow the workflow below.

1. Fork the repository.
2. Create a dedicated development branch.
3. Implement the proposed modification.
4. Add or update tests when appropriate.
5. Verify that existing functionality remains unaffected.
6. Update documentation if necessary.
7. Submit a Pull Request for review.

Every Pull Request should represent a logically consistent contribution.

Large methodological or architectural changes should be discussed before implementation whenever possible.

---

# Branch Naming Convention

Branch names should clearly describe the purpose of the contribution.

Examples:

```text
feature/add-mofa-baseline
feature/new-visualization
feature/contrastive-learning
experiment/survival-analysis
fix/preprocessing-error
docs/update-documentation
refactor/model-cleanup
```

Using descriptive branch names improves repository organization and simplifies code review.

---

# Repository Organization

OmniLatent follows a modular software architecture in which reusable implementation is separated from exploratory analysis.

Production code belongs inside:

```text
src/
```

The repository is organized as:

```text
src/
├── data/
├── models/
├── training/
├── evaluation/
├── visualization/
└── utils/
```

Each module has a clearly defined responsibility.

| Module | Responsibility |
|---------|----------------|
| `data` | Data loading, validation, preprocessing, and dataset management |
| `models` | Representation learning architectures and neural network components |
| `training` | Optimization, checkpointing, training loops, and experiment execution |
| `evaluation` | Quantitative evaluation and downstream biomedical analyses |
| `visualization` | Publication-quality figures and exploratory visualizations |
| `utils` | Shared utilities, logging, helper functions, and reproducibility tools |

Keeping responsibilities isolated improves maintainability and facilitates future extensions.

---

# Notebooks

Jupyter notebooks are intended exclusively for:

- exploratory data analysis,
- visualization,
- rapid prototyping,
- demonstration examples.

Core implementation should **never** reside inside notebooks.

Reusable code should always be migrated into the `src/` package.

---

# Coding Standards

Contributors are encouraged to write clean, maintainable, and well-documented Python code.

General principles include:

- Prefer readability over clever implementations.
- Use descriptive variable and function names.
- Keep functions focused on a single responsibility.
- Avoid unnecessary duplication.
- Minimize hidden side effects.
- Write self-documenting code whenever possible.
- Clearly document important scientific assumptions.

Scientific software should prioritize correctness, transparency, and maintainability over premature optimization.

---

# Code Style

The project adopts a consistent formatting style across the repository.

Recommended tools include:

- **Black** for automatic formatting.
- **Flake8** for static code analysis.
- **PyTest** for testing.

Whenever possible, code should be formatted before submission.

Maintaining a consistent coding style significantly improves readability and long-term maintenance.

---

# Experiment Reproducibility

Reproducibility is considered a fundamental requirement of the OmniLatent project.

Every computational experiment should contain sufficient information to allow independent researchers to reproduce the reported results.

Each experiment should preserve, whenever applicable:

- configuration file,
- dataset version,
- preprocessing settings,
- random seed,
- model hyperparameters,
- optimizer configuration,
- training settings,
- evaluation metrics,
- generated embeddings,
- software version,
- execution logs.

A typical experiment directory may follow the structure below.

```text
results/
└── experiment_001/
    ├── config.yaml
    ├── model.pt
    ├── embeddings.csv
    ├── metrics.json
    ├── figures/
    └── logs/
```

Experimental outputs should never overwrite previous experiments.

Each experiment should produce an independent and traceable record.

---

# Testing

Before submitting changes, contributors are expected to verify that their implementation behaves correctly.

Recommended validation steps include:

- execute existing tests,
- verify backward compatibility,
- add tests for newly introduced functionality,
- confirm reproducibility whenever model behavior is affected.

Testing primarily focuses on:

- data preprocessing,
- model behavior,
- training pipeline,
- evaluation pipeline,
- reproducibility,
- software integrity.

Project tests are located in:

```text
tests/
```

Scientific correctness should always be validated before performance optimization.

---

# Development Environment

When reporting issues or submitting Pull Requests involving training, evaluation, or performance, contributors are encouraged to include relevant environment information.

Examples include:

- Python version,
- operating system,
- dependency versions,
- PyTorch version,
- CUDA version (when applicable),
- GPU model (if relevant).

Providing environment information substantially improves reproducibility and facilitates debugging.

---

# Documentation

Documentation is treated as a first-class component of OmniLatent.

Documentation updates are expected whenever contributors introduce:

- new models,
- new experiments,
- architectural modifications,
- configuration options,
- evaluation procedures,
- scientific methodologies.

Clear documentation ensures that scientific results remain understandable, reproducible, and reusable.

---

# Pull Requests

Every Pull Request should include:

- a concise description of the proposed modification,
- scientific motivation,
- implementation summary,
- testing information,
- expected impact,
- documentation updates (if applicable).

Whenever relevant, contributors are encouraged to reference the corresponding GitHub Issue.

Large architectural modifications should normally be discussed before implementation.

---

# Pull Request Checklist

Before submitting a Pull Request, verify the following:

- [ ] Code follows project style guidelines.
- [ ] Existing functionality remains unaffected.
- [ ] New functionality has been tested.
- [ ] Documentation has been updated when necessary.
- [ ] Experimental results remain reproducible.
- [ ] Commit history is clean and meaningful.

Completing this checklist greatly simplifies project maintenance and code review.

---

# Review Criteria

All Pull Requests are evaluated according to both scientific and software engineering standards.

The primary review criteria include:

| Criterion | Description |
|-----------|-------------|
| Scientific validity | Is the proposed approach scientifically justified? |
| Reproducibility | Can independent researchers reproduce the reported results? |
| Software quality | Is the implementation modular, readable, and maintainable? |
| Documentation | Are new features adequately documented? |
| Experimental design | Are experiments appropriately designed and reported? |
| Biological relevance | Does the contribution improve biological understanding? |
| Computational efficiency | Is the implementation reasonably efficient without sacrificing clarity? |

Acceptance decisions consider the overall contribution to both scientific quality and long-term maintainability.

---

# Commit Message Convention

OmniLatent follows the **Conventional Commits** specification.

General format:

```text
type(scope): short description
```

Examples:

```text
feat(models): add multimodal encoder

feat(evaluation): implement survival benchmark

fix(data): correct preprocessing pipeline

docs(protocol): update research protocol

docs(contributing): improve contribution guidelines

refactor(training): simplify training loop

test(models): add embedding validation tests
```

Commit messages should be concise, descriptive, and focused on a single logical change.

---

# Scientific Integrity

OmniLatent is developed according to principles of responsible scientific computing.

Contributors are expected to prioritize:

- reproducibility over unnecessary complexity,
- transparent reporting over selective reporting,
- biological interpretation over black-box performance,
- rigorous evaluation over isolated metrics,
- honest discussion of limitations,
- evidence-based scientific conclusions.

Scientific claims introduced through code or documentation should be supported by appropriate experimental evidence whenever possible.

---

# Code of Conduct

OmniLatent promotes an open, respectful, and collaborative research environment.

All contributors are expected to:

- communicate respectfully,
- provide constructive feedback,
- welcome different scientific perspectives,
- acknowledge prior work appropriately,
- maintain professional behavior throughout discussions.

Healthy scientific collaboration relies on mutual respect, openness, and intellectual honesty.

---

# License

By contributing to OmniLatent, contributors agree that their contributions will be distributed under the terms of the **MIT License** included in this repository.

---

# Citation

If OmniLatent contributes to published scientific work, please cite the project using the citation information provided in the repository.

Future releases will include a dedicated `CITATION.cff` file to facilitate proper academic citation.

---

# Acknowledgements

We sincerely appreciate every contribution that improves the scientific quality, software engineering standards, documentation, or reproducibility of OmniLatent.

Open scientific collaboration is essential for advancing biomedical artificial intelligence.

---

# Guiding Principle

> **"Build reliable scientific software that enables reproducible biomedical discovery."**

Every contribution—whether scientific, technical, or documentation-related—should strengthen the framework's reliability, transparency, and long-term scientific value.

Thank you for contributing to **OmniLatent** and supporting open, reproducible biomedical research.





