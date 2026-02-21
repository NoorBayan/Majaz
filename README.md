# Majaz: A Pragmatic Analysis of Qur'anic Figurative Language

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Data Format](https://img.shields.io/badge/Data-JSON-green.svg)]()
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17983729.svg)](https://doi.org/10.5281/zenodo.17983729)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Majaz** is a comprehensive, exhaustively annotated corpus and computational toolkit for the cognitive-pragmatic analysis of figurative language (similes and metaphors) in Qur'anic Arabic. 

This repository contains the dataset, extraction scripts, and statistical analysis code underlying the research paper: *"Figurative Language as Inferential Communication: Form–Function Relations in Authoritative Discourse."*

## 📖 Overview

While classical rhetorical traditions (*Balāgha*) have extensively cataloged figurative language, accounts of how form, function, and inference interact in authoritative discourse remain limited. **Majaz** addresses this gap by providing an exhaustively annotated corpus of **1,402 figurative expressions (402 similes and 979 metaphors)** extracted from the Qur'an (Tanzil v1.1).

The project integrates **Relevance Theory (RT)** and **Conceptual Metaphor Theory (CMT)** to model online inferential processes and underlying conceptual structures, treating figurative meaning as an inferentially guided communicative practice.

## 🗂 Dataset Description

The dataset is provided in `JSON` format to accommodate the hierarchical nature of pragmatic information. It encompasses the entirety of the Qur'anic text (6,236 verses) and features a multi-layered annotation scheme:

1. **Structural Layer**: Documents morphosyntactic features and procedural particles (e.g., *ka-*, *inna*, *qad*).
2. **Conceptual Layer (CMT)**: Tags the underlying Source and Target domains (e.g., *GUIDANCE IS LIGHT*).
3. **Pragmatic Layer (RT)**: Captures the inferential dimension, including ad hoc concept construction, processing effort, implicature strength, and illocutionary force.

*Note: The complete annotated records are also preserved and openly accessible via the Zenodo repository: [10.5281/zenodo.17983729](https://doi.org/10.5281/zenodo.17983729).*


## 🛠 Methodology Pipeline

1. **Preprocessing**: Full diacritics (*tashkīl*) were retained for structural disambiguation and rhetorical emphasis (e.g., *tanwīn*).
2. **Extraction**: 
   - **Similes**: Automated Regex sweeps targeting canonical particles (*ka-*, *mithl*), yielding 402 verified instances.
   - **Metaphors**: Adapted MIPVU procedure tailored for Classical Arabic morphosyntax, verified against classical lexicons and exegesis, yielding 979 instances.
3. **Validation**: Inter-Annotator Agreement (IAA) was calculated using Cohen’s Kappa (κ), achieving near-perfect agreement for the Structural Layer (0.92) and substantial agreement for Pragmatic Layers (0.71-0.78).

## 📊 Key Findings

- **Form–Function Dichotomy**: Explicitly marked similes predominantly occur in nominal constructions associated with propositional stabilization (assertoric reinforcement). Metaphors favor dynamic verbal structures, construing abstract meanings as temporally unfolding processes.
- **Conceptual Grounding**: Figurative patterns cluster heavily around anthropocentric domains, specifically "Transactional Logic" (moral deeds as exchangeable entities) and "Embodied Logic" (spiritual states as physiological conditions).
- **Pragmatic Strategy**: Complex imagery is frequently deployed not to minimize processing costs, but to intentionally increase processing effort, generating dense sets of weak implicatures that modulate epistemic asymmetry.

## 🚀 Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/majaz.git
   cd majaz
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebooks to reproduce the analysis:
   ```bash
   jupyter notebook notebooks/
   ```

