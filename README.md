# Triagegeist — Emergency Triage Acuity Prediction & Demographic Bias Audit

**Competition:** [Triagegeist](https://www.kaggle.com/competitions/triagegeist)  
**Organizer:** Laitinen-Fredriksson Foundation
**Version:** V1 — Synthetic ED Data + NHAMCS Real-World Validation

## Overview

This project builds an XGBoost classifier predicting emergency triage acuity
from patient intake data, which then conducts a systematic demographic bias audit identifying 
which patient groups are systematically undertriaged. Findings are validated against 
real US emergency department data from the NHAMCS 2018-2022 survey.

**Key Results:**
- 85.9% validation accuracy on synthetic data
- 96% recall on ESI 1 (critical) patients
- Overall undertriage rate: 5.27% (synthetic), 22.93% (NHAMCS real data)
- Highest risk group: Pediatric / Somali-speaking patients at 7.2% (synthetic)
- Cross-dataset finding: Uninsured patients face elevated undertriage risk in both datasets
- New finding in real data: Female patients undertriaged at 24.1% vs 21.6% for males

## Datasets

| Dataset | Source | Records | Access |
|---|---|---|---|
| Triagegeist synthetic ED data | Laitinen-Fredriksson Foundation | 100,000 | Kaggle competition |
| NHAMCS 2018-2022 | CDC / Kaggle (reaper0ai) | 58,124 | Public |
| MIMIC-IV-ED | PhysioNet | ~200,000 | Credentialed (V2) |

## Methodology

### 1. Exploratory Data Analysis
- Clinical validity check, with vitals stabilizing as ESI increases
- Demographic analysis showcasing 8 language groups, 5 insurance types and 4 age groups
- Missingness analysis, such as BP missing only in low-acuity patients, which points toward data that's usually omitted for stable patients

### 2. Predictive Modeling
- XGBoost multiclass classifier (ESI 1–5)
- 58 features: vitals, demographics, comorbidities, triage context
- SHAP values for clinical interpretability

### 3. Demographic Bias Audit (Synthetic Data)
- Undertriage is when the model predicts higher acuity than assigned
- Analysis across language, insurance, sex, and age group
- Risks compound for patients with more unique age and language combinations

### 4. NHAMCS Real-World Validation
- Independent XGBoost model trained on 58,124 real US ED visits
- Bias patterns compared across race, insurance, and sex
- Cross-dataset comparison of undertriage signals

## Key Findings

### Synthetic Finnish ED Data
| Finding | Detail |
|---|---|
| Model accuracy | 85.9% on 16,000 held-out patients |
| ESI 1 recall | 96% with critical patients almost never missed |
| Top features | NEWS2 score (32%), GCS (28%), pain score (10%) |
| Highest undertriage risk | Pediatric / Somali: 7.2% |
| Language pattern | Russian, Arabic, Estonian speakers above average |
| Age pattern | Elderly (5.4%) > Pediatric (4.7%) |

### NHAMCS Real US ED Data
| Finding | Detail |
|---|---|
| Model accuracy | 54.4% which means real data is harder to predict |
| Highest undertriage risk | Self-pay (uninsured): 29.3% |
| Race pattern | Black/African American: 24.3% vs Asian: 15.7% |
| Sex pattern | Female: 24.1% vs Male: 21.6% |

### Cross-Dataset Finding
Uninsured patients face elevated undertriage risk in **both** datasets — 
a consistent signal across synthetic Finnish and real US emergency department data.

## Project Setup

### Requirements
```bash
pip install -r requirements.txt
```

### Run locally
```bash
git clone https://github.com/rtsdque/triagegeist-triage-ai.git
cd triagegeist-triage-ai
pip install -r requirements.txt
jupyter lab
```

### Data
- Competition data: [Kaggle competition page](https://www.kaggle.com/competitions/triagegeist/data)
- NHAMCS data: [Kaggle dataset](https://www.kaggle.com/datasets/reaper0ai/nhamcs-2018-22)
- Place all files in `data/` folder

## Kaggle Notebook
Full end-to-end notebook with SHAP values:  
[Link to be added after submission]

## Dashboards
- **Tableau:** [Interactive Bias Audit Dashboard](https://public.tableau.com/views/TriagegeistEmergencyTriageBiasAudit/BiasAuditDashboard)
- **Power BI:** `dashboards/triagegeist_bias_dashboard.pbix` — two-page report covering synthetic Finnish ED and NHAMCS real US ED validation

## Roadmap

- **V1 (current):** Synthetic ED data + NHAMCS validation
- **V2 (planned):** Add MIMIC-IV-ED validation (pending PhysioNet access)

## License
Competition and educational use only.  
Triagegeist dataset: Non-Commercial Research License, Laitinen-Fredriksson Foundation.  
NHAMCS: Public domain, CDC/NCHS.