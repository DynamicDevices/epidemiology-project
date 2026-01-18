# Notebooks

## Naming

- Start with an order prefix: `00_`, `01_`, `02_`…
- Use short descriptive names, e.g. `01_load_and_clean.ipynb`, `02_exploration.ipynb`, `03_model_fit.ipynb`

## Path convention

Assume notebooks run from this folder.

- Read raw data from `../data/raw/`
- Write cleaned outputs to `../data/interim/` or `../data/processed/`
- Save final figures to `../reports/figures/`

## Keep notebooks readable

- Put reusable functions in `src/epidemiology_project/` and import them.
- Record assumptions/choices in `../docs/DECISIONS.md`.

