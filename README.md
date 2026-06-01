# Triagegeist — Emergency Triage Acuity Prediction & Demographic Bias Audit

**Competition:** [Triagegeist — AI in Emergency Triage](https://www.kaggle.com/competitions/triagegeist)  
**Organizer:** Laitinen-Fredriksson Foundation, Helsinki  
**Author:** [Your Name]  

---

## Overview

This project builds an XGBoost classifier predicting emergency triage acuity (ESI 1–5) 
from patient intake data, then conducts a systematic demographic bias audit identifying 
which patient groups are systematically undertriaged in a simulated Finnish emergency 
department network.

**Key Results:**
- 85.9% validation accuracy, 0.86 weighted F1
- 96% recall on ESI 1 (critical) patients — near-perfect on highest-risk cases
- Overall undertriage rate: 5.27%
- Highest risk group: Pediatric / Somali-speaking patients at 7.2% undertriage rate
- Elderly / Russian-speaking patients at 6.6% — 25% above overall rate

---

## Repository Structure
triagegeist/
├── data/                          # Competition dataset (Laitinen-Fredriksson Foundation)
│   ├── train.csv                  # 80,000 patients with features + target
│   ├── test.csv                   # 20,000 patients, features only
│   ├── chief_complaints.csv       # Free-text triage narratives
│   ├── patient_history.csv        # 25 binary comorbidity flags
│   └── sample_submission.csv      # Submission format
├── notebooks/
│   ├── 01_eda.ipynb               # Exploratory data analysis
│   ├── 02_modeling.ipynb          # XGBoost classifier
│   └── 03_bias_analysis.ipynb     # Demographic bias audit
├── outputs/                       # Generated charts and CSV results
└── README.md

---

## Methodology

### 1. Exploratory Data Analysis
- Clinical validity check — vital signs degrade cleanly ESI 1→5
- Demographic analysis — 8 language groups, 5 insurance types, 4 age groups
- Missingness analysis — BP missing only in low-acuity patients (clinically realistic)

### 2. Predictive Modeling
- XGBoost multiclass classifier (ESI 1–5)
- 58 features: vitals, demographics, comorbidities, triage context
- Early stopping at iteration 336, validation log-loss: 0.311
- SHAP values for clinical interpretability

### 3. Demographic Bias Audit
- Undertriage defined as: model predicts higher acuity than was assigned
- Rates compared across language, insurance type, sex, and age group
- Compound risk analysis: age + language combinations

---

## Key Findings

| Finding | Detail |
|---|---|
| Model accuracy | 85.9% on 16,000 held-out patients |
| ESI 1 recall | 96% — critical patients almost never missed |
| Top predictive features | NEWS2 score (32%), GCS (28%), pain score (10%) |
| Highest undertriage risk | Pediatric / Somali: 7.2% |
| Language pattern | Russian, Arabic, Estonian speakers consistently above average |
| Age pattern | Elderly (5.4%) > Pediatric (4.7%) |
| Sex | No meaningful difference across F, M, Other |

---

## Setup & Reproducibility

### Requirements
```bash
pip install pandas numpy scikit-learn xgboost shap fairlearn 
imbalanced-learn matplotlib seaborn jupyterlab
```

### Run locally
```bash
git clone https://github.com/rtsdque/triagegeist-triage-ai.git
cd triagegeist-triage-ai
pip install -r requirements.txt
jupyter lab
```

### Data
Dataset provided by the Laitinen-Fredriksson Foundation via Kaggle. 
Download from [competition page](https://www.kaggle.com/competitions/triagegeist/data) 
and place in `data/` folder.

---

## Kaggle Notebook
Full end-to-end notebook with SHAP values available at:  
[Link to be added after submission]

---

## License
This project is for competition and educational purposes. 
Dataset licensed under Non-Commercial Research License — Laitinen-Fredriksson Foundation.