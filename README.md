# Simple Streamlit Data App

A minimal **Streamlit app** that loads a CSV, filters rows by a numeric threshold, 
and shows the results interactively.  
The sidebar also displays the **current date and time**.

This project is containerized with Docker, includes tests for the data utilities, 
and runs CI to validate changes automatically.

---

## �� Overview

- **app.py** → Streamlit UI (loads data, filters, shows time)  
- **data_utils.py** → data logic (`load_data`, `filter_by_threshold`)  
- **tests/** → pytest unit tests for the data utils  
- **sample_data.csv** → demo dataset  
- **Dockerfile** → containerization  
- **.github/workflows/ci.yml** → GitHub Actions CI workflow  

---

## ✨ Features

- Streamlit interface with sidebar date/time  
- Load and preview CSV data  
- Filter rows interactively by numeric threshold  
- Fully containerized with Docker  
- Tested with pytest (data import & filtering)  
- CI pipeline to run tests on every commit/PR  

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+  
- (Optional) Docker  
- (Optional) virtual environment (`venv`, `pipenv`, etc.)

### Installation

Clone the repo:
```bash
git clone https://github.com/<your-username>/simple-streamlit-app.git
cd simple-streamlit-app

