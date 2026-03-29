# entropy-based-analytic-model
Implementation of Method Described in 10.1109/BigData.2016.7841035

## Project Overview

This project provides an analytical exploration of a synthetic dataset using entropy-based methods.
A Jupyter notebook (`analysis.ipynb`) generates a 1000-row synthetic dataset and performs
descriptive statistics and Shannon entropy analysis across all categorical columns.

### Dataset columns

| Column | Description |
|---|---|
| `text_message` | Short example text messages |
| `url` | Example URLs |
| `language` | Language of the message |
| `country` | Country of origin |
| `device` | Device type (Mobile / Desktop / Tablet) |
| `star_review` | 5-star review rating (1–5) |

---

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the Jupyter notebook

```bash
jupyter notebook analysis.ipynb
```

Run all cells in order to:
- Generate the 1000-row synthetic dataset
- View descriptive statistics (using Python's built-in `statistics` module and pandas)
- Compute Shannon entropy for each column
- Plot distribution and entropy charts
- Export the dataset to `synthetic_dataset.csv`

---

## Dependencies

- **pandas** – data manipulation and analysis
- **numpy** – random data generation
- **jupyter / notebook** – interactive notebook environment
- **matplotlib** – visualisation
- **scipy** – `scipy.stats.entropy` for Shannon entropy calculation
- **statistics** (Python built-in) – mean, median, mode, stdev
