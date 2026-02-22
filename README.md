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

## 📊 Interactive Analysis & Visualizations

The statistical analysis, data processing, and visualization generation for this study were developed using Python (Pandas, Seaborn, NetworkX) in a Jupyter/Colab environment. 

You can interactively explore the code, generate the figures, and read the auto-generated academic narratives using the provided Google Colab notebooks below:

| Analysis / Visualization | Description & Utility | Explore in Colab |
| :--- | :--- | :---: |
| **Morpho-Syntactic Distribution (Fig 1 & 2)** | Generates Pie and Bar charts to analyze the explicit vs. implicit forms of similes and the linguistic structures of metaphors, highlighting the text's preference for direct evidentiality. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK_HERE) |
| **Grammatical Structure Dynamics (Fig 3)** | Compares Verbal (dynamic/temporal processes) and Nominal (static/timeless truths) structures across figurative expressions using count plots. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK_HERE) |
| **Conceptual Domain Mapping (Fig 4 & 5)** | Produces frequency charts and a cross-tabulation Heatmap detailing how anthropocentric source domains (e.g., Commerce, Body) are mapped onto abstract target domains. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK_HERE) |
| **Form-Function Correlations** | Employs Heatmaps to statistically validate pragmatic routines, demonstrating how specific syntactic structures strictly correlate with particular pragmatic functions (e.g., Clarification, Warning). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK_HERE) |
| **Functional Typology Engine** | An algorithmic extraction tool that scans the corpus to automatically retrieve and format the best representative textual examples for the qualitative functional typology table. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK_HERE) |
| **Cognitive Inference Case Studies** | Generates structured "Ad Hoc Concept" analysis cards based on Relevance Theory, detailing the processing effort and implicit derivations for selected verses. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK_HERE) |
| **Conceptual Network Logic (Fig 6)** | Visualizes the underlying cognitive topology using directed graphs (NetworkX) and detects primary Image Schemas (Path, Container, Force) driving the pragmatic force. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK_HERE) |

> **Note:** To run the Colab notebooks successfully, ensure you mount your Google Drive and verify that the JSON dataset paths match the directories in your Drive environment.
> 
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

