# Healthcare ETL Pipeline

A Python ETL pipeline that extracts patient data from JSON, flags health risks,
and loads the results into a SQLite database — with a live Streamlit dashboard
for real-time risk visualization.

> **Live Demo:** [healthcare-etl-dashboard.streamlit.app](https://9doyfrufk22skc46xhh28b.streamlit.app/)

---

## What it does

- Extracts raw patient records from JSON source files
- Transforms data by calculating health risk scores and categorizing patients
  into risk levels (low / medium / high)
- Loads the transformed records into a structured SQLite database
- Visualizes patient risk distribution in an interactive Streamlit dashboard

---

## Architecture
```
┌─────────────────────────────────────────────┐
│              Data Source                    │
│         data/raw_patients.json              │
└────────────────────┬────────────────────────┘
                     │
         ┌───────────▼───────────┐
         │     ETL Pipeline      │
         ├───────────────────────┤
         │ app/extract.py        │  Load + validate raw JSON records
         │ app/transform.py      │  Add risk flags + categorize patients
         │ app/load.py           │  Write transformed data to SQLite DB
         └───────────┬───────────┘
                     │
         ┌───────────▼───────────┐
         │      Data Store       │
         │  data/healthcare.db   │  SQLite database
         └───────────┬───────────┘
                     │
         ┌───────────▼───────────┐
         │   Streamlit Dashboard │
         │     dashboard.py      │  Live risk visualization
         └───────────────────────┘
```

---

## Tech stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Data format | JSON |
| Database | SQLite |
| Dashboard | Streamlit |
| Dev environment | VS Code + devcontainer |

---

## Project structure
```
Healthcare-ETL-Pipeline/
├── app/
│   ├── extract.py        # Extract and validate raw patient data from JSON
│   ├── transform.py      # Apply risk flags and categorize patient risk levels
│   └── load.py           # Load transformed records into SQLite database
├── data/
│   ├── raw_patients.json # Source patient data
│   └── healthcare.db     # SQLite output database
├── dashboard.py          # Streamlit dashboard for risk visualization
├── requirements.txt
└── .gitignore
```

---

## Local setup
```bash
# 1. Clone the repo
git clone https://github.com/AshraySikka/Healthcare-ETL-Pipeline.git
cd Healthcare-ETL-Pipeline

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the ETL pipeline
python app/extract.py
python app/transform.py
python app/load.py

# 5. Launch the dashboard
streamlit run dashboard.py
```

---

## How the risk flagging works

Each patient record is evaluated against threshold rules during the
transform step:

| Risk level | Criteria |
|---|---|
| High | Any critical vitals outside safe range |
| Medium | One or more borderline readings |
| Low | All vitals within normal parameters |

Flagged records are tagged before being written to the database,
allowing the dashboard to filter and visualize by risk category.

---

## Why I built this

Healthcare data pipelines are a real-world use case for ETL engineering.
This project demonstrates modular pipeline design — separating extract,
transform, and load into distinct, testable stages — alongside database
management and data visualization skills.

Built as part of my transition into backend Python development.

---

## Author

**Ashray Sikka** — Backend Developer (Python · MySQL · SQLite)
[LinkedIn](https://www.linkedin.com/in/ashraysikka) · [GitHub](https://github.com/AshraySikka)
