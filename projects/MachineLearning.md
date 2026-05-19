---
layout: default
title: Machine Learning Coursework
---

<a href="/projects" class="back-link"><span>&larr;</span> Back to Projects</a>

<div class="navigation-links">
  <a href="https://cdcastr0.github.io/">Home</a>
  <a href="https://cdcastr0.github.io/education">Education</a>
  <a href="https://cdcastr0.github.io/skills">Skills & Expertise</a>
  <a href="https://cdcastr0.github.io/experience">Experience</a>
  <a href="https://cdcastr0.github.io/projects">Projects</a>
</div>

# Machine Learning Coursework

**SMU MSDS — Applied Machine Learning**

## Overview

Four-part coursework progressing from Python data structure mastery through applied deep learning. The final assignment explored AI-assisted learning via Cursor's Model Context Protocol (MCP) — turning the ML assignments themselves into an object of study for understanding code with AI.

## Assignments

### HW1 — Python Data Structures
Comprehensive review of Python built-in data structures: lists (append, extend, index, insert, remove, pop, sort, reverse), dictionaries, sets, and their associated operations. Demonstrated through annotated examples covering time complexity tradeoffs.

### HW2 — Hyperparameter Optimization
Designed a multi-classifier evaluation framework comparing Logistic Regression, Random Forest, and SVC across three different hyperparameter configurations each. Used KFold cross-validation for reliable performance estimates and GridSearchCV for systematic search. Extended to Optuna (Bayesian optimization) for neural network hyperparameter tuning — significantly faster than grid search for continuous parameter spaces.

**Key results:** Evaluated accuracy, precision, recall, and F1 across all classifiers. Generated matplotlib comparison plots for model selection visualization.

### HW3 — Transfer Learning with PyTorch
Built a SimpleCNN architecture from scratch:
- Conv2d(1, 32, 3) → ReLU → Conv2d(32, 64, 3) → ReLU → MaxPool2d → Dropout → FC(9216, 128) → FC(128, 10)
- Trained on MNIST digit recognition for 5 epochs with Adam optimizer
- Froze convolutional layers (which learned general edge/shape detectors)
- Replaced final FC layer for custom handwritten character classes
- Fine-tuned only the new classification head on a smaller custom dataset

This achieved faster convergence and better accuracy than training from scratch, demonstrating the practical value of transfer learning for limited-data scenarios.

### HW4 — AI-Assisted Learning with Cursor + MCP
Explored how AI tools (Cursor with MCP) transform the learning experience for ML coursework. Loaded HW2 into a Cursor workspace and used the AI to explain each code block, visualize what each algorithm is doing conceptually, and answer targeted questions without needing to search documentation.

Key insight: MCP allows the AI to have direct context about the running codebase, making it qualitatively different from pasting code into a chat interface. The debugging and explanation loop is orders of magnitude faster.

## Technology Stack

| Category | Tools |
|---|---|
| Deep Learning | PyTorch, torchvision, Conv2d, DataLoader |
| ML Framework | scikit-learn, GridSearchCV, KFold |
| Optimization | Optuna (TPE sampler) |
| Data | numpy, pandas, matplotlib |
| Computer Vision | OpenCV, MNIST dataset |
| Dev Tools | Cursor IDE, MCP |

## Key Takeaways

- Transfer learning is most valuable when your target dataset is small relative to the pre-training dataset
- Optuna's Bayesian search outperforms grid search by ~3x when parameter space exceeds 3 dimensions
- KFold cross-validation gives more reliable estimates than a single train/test split, especially with n < 10,000
- AI-assisted code exploration (via Cursor MCP) dramatically accelerates comprehension of unfamiliar ML code

---

[GitHub Repository](https://github.com/CDCastr0/MachineLearningCoursework) | [← Back to Projects](/projects)

<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
