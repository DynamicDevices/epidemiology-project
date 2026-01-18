# Scenario datasets (synthetic)

This project can be done two ways:

1. **Real surveillance data** (UKHSA API): observed proxies like confirmed cases, positivity, admissions.
2. **Synthetic scenario data** (SIR model): clean “what-if” comparisons with controlled interventions.

For the **interventions** requirement, synthetic data is often easiest because:
- you can define “no interventions” precisely
- you can create multiple scenarios that differ by exactly one change

## Baseline observed dataset (pre-existing real data)

If you want to start from **pre-existing data**, use the UKHSA API to download an observed “infected vs time” proxy:

- **Notebook**: `notebooks/09_download_baseline_observed_ukhsa_covid_cases.ipynb`
- **Output**: `data/processed/observed/ukhsa_covid19_cases_by_day_england.csv`

Note: this is **observed history** (not “policy-free”). It’s a clean time series you can treat as a baseline input before doing synthetic intervention scenarios.

## Dataset schema (all scenarios)

Generated CSVs share a consistent schema:

- `t_day`: time in days from start (0, 1, 2, ...)
- `date`: synthetic calendar date (for plotting convenience)
- `S`, `I`, `R`: compartment counts
- `N`: population size
- `beta`: transmission rate used on that day
- `gamma`: recovery rate
- `scenario`: scenario id (string)

## Baseline dataset (no interventions)

- **Scenario id**: `baseline_no_intervention`
- **Idea**: constant \(\\beta\) and \(\\gamma\) for the full time period.
- **Output**: `data/processed/scenarios/baseline_no_intervention.csv`

## Intervention datasets (each is different)

Each scenario changes **one thing** compared to baseline:

1. **Contact reduction (lockdown)**: reduce \(\\beta\) by a fixed fraction after day \(t_0\)
2. **Improved recovery (treatment)**: increase \(\\gamma\) after day \(t_0\)
3. **Vaccination pulse**: move a fraction of \(S\\rightarrow R\) at day \(t_0\)

Outputs:
- `data/processed/scenarios/intervention_lockdown_beta_step.csv`
- `data/processed/scenarios/intervention_treatment_gamma_step.csv`
- `data/processed/scenarios/intervention_vaccination_pulse.csv`

## How to generate

Run:
- `notebooks/09_download_baseline_observed_ukhsa_covid_cases.ipynb` (pre-existing observed baseline)
- `notebooks/10_generate_baseline_no_intervention.ipynb`
- `notebooks/11_generate_intervention_scenarios.ipynb`
- `notebooks/12_compare_scenarios.ipynb`

These notebooks write CSV outputs to `data/processed/scenarios/`.

