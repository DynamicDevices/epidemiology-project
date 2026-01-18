# Epidemiology Project (Maths + Python)

This workspace is organised to make it easy to collaborate, keep notebooks reproducible, and avoid losing context (data sources, assumptions, decisions).

## Folder layout

- `notebooks/`: Jupyter notebooks (analysis, exploration, modelling)
- `src/epidemiology_project/`: reusable Python code (loading/cleaning/modelling helpers)
- `data/`:
  - `data/raw/`: raw datasets (do not edit in-place)
  - `data/external/`: externally sourced reference data (e.g. shapefiles)
  - `data/interim/`: intermediate datasets (cleaned but not final)
  - `data/processed/`: final datasets ready for analysis
- `reports/`: write-ups, slides, exports
  - `reports/figures/`: figures for the report/poster
  - `reports/tables/`: tables for the report/poster
- `figures/`: quick ad-hoc figures (optional; prefer `reports/figures/` for final outputs)
- `docs/`: project context (brief, data sources, decisions)

## Getting started

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

2. Launch Jupyter:

```bash
jupyter lab
```

## Reproducibility conventions

- Keep **raw data immutable**: add new raw files to `data/raw/`, never overwrite with cleaned versions.
- Notebooks should use **relative paths** rooted at the repo, e.g. `../data/raw/...` from inside `notebooks/`.
- When you make a key modelling choice, record it in `docs/DECISIONS.md`.

See `docs/PROJECT_CONTEXT.md` for the living project brief and current plan.

