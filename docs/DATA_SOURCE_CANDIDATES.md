# Candidate data sources (online)

This is a curated menu of reliable public health datasets that are typically suitable for a first-year maths + Python project.

Use `docs/DATA_SOURCES.md` to record the *specific* dataset(s) you actually choose and download, including download date and file paths.

## Infectious disease surveillance (cases / tests / hospitalisations)

- **UKHSA dashboard (England)**
  - **What**: respiratory infections (incl. COVID-19, influenza, RSV) and other UKHSA metrics, often with regional breakdowns.
  - **Access**: public site + “access our data” page (CSV/API style access varies by dataset).
  - **Link**: `https://ukhsa-dashboard.data.gov.uk/` (see “Access our data” from the site menu)

- **CDC open data (US)**
  - **What**: many public health datasets (infectious diseases, vaccination, etc.) with a consistent open-data interface.
  - **Access**: web portal + API/CSV exports (dataset-specific).
  - **Link**: `https://open.cdc.gov/data.html`

- **ECDC (EU/EEA)**
  - **What**: communicable disease surveillance datasets for Europe.
  - **Access**: dataset downloads (varies by topic).
  - **Link**: `https://www.ecdc.europa.eu/en/publications-data`

- **WHO COVID-19 data / dashboards**
  - **What**: global COVID indicators and other health indicators (country-level).
  - **Access**: downloads via WHO data portals (varies by indicator).
  - **Link**: `https://data.who.int/`

## Mortality / excess mortality / population denominators

- **ONS (UK)**
  - **What**: mortality, population, and many health indicators; good for UK-focused analyses and excess deaths work.
  - **Access**: dataset downloads (often XLS/CSV) and sometimes APIs depending on series.
  - **Link**: `https://www.ons.gov.uk/`

- **World Bank indicators (population denominators, GDP, etc.)**
  - **What**: country-year indicators (useful for per-capita rates, comparisons).
  - **Access**: API + downloads.
  - **Link**: `https://data.worldbank.org/`

## Vaccination

- **Our World in Data (OWID)**
  - **What**: widely-used global COVID dataset (cases/deaths/tests/vaccines) with consistent country time series.
  - **Access**: CSV download + GitHub mirror.
  - **Link**: `https://ourworldindata.org/coronavirus`

- **CDC vaccination datasets (US)**
  - **What**: vaccination coverage and related surveillance (dataset-specific).
  - **Access**: via CDC open data portal.
  - **Link**: `https://open.cdc.gov/data.html`

## Government interventions / policy indices

- **Oxford COVID-19 Government Response Tracker (OxCGRT)**
  - **What**: policy measures and “stringency”-type indices by country over time.
  - **Access**: downloadable dataset(s), sometimes mirrored on cloud/open-dataset platforms.
  - **Link**: `https://www.bsg.ox.ac.uk/research/research-projects/covid-19-government-response-tracker`

## Mobility / behaviour proxies (useful covariates)

- **Google Community Mobility Reports (historical)**
  - **What**: mobility change indices during COVID period (availability is historical/archived in some regions).
  - **Access**: downloadable reports.
  - **Link**: `https://www.google.com/covid19/mobility/`

## Surveys / risk factors / determinants of health (non-infectious epidemiology)

- **WHO Health Inequality Data Repository**
  - **What**: disaggregated health indicators (inequality by income, education, sex, etc.).
  - **Access**: API + downloads.
  - **Link**: `https://www.who.int/data/inequality-monitor/data`

- **CDC NCHS public-use data (US)**
  - **What**: major surveys (NHIS, NHANES, etc.) and vital statistics (public-use versions).
  - **Access**: downloads; sometimes large and requires careful variable selection.
  - **Link**: `https://www.cdc.gov/rdc/public-nchs-data/index.html`

## UK health service / prescribing (often open and very “data friendly”)

- **NHS England / NHS Digital datasets**
  - **What**: many health system datasets; some open, some restricted.
  - **Access**: dataset pages; check whether data is openly downloadable.
  - **Link**: `https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets`

- **NHSBSA prescribing (English Prescribing Dataset)**
  - **What**: prescribing volumes over time (good for time-series and geographic comparisons).
  - **Access**: open data downloads (CSV); updated regularly.
  - **Link**: `https://opendata.nhsbsa.net/`

## Notes on choosing for a first-year project

- Prefer **aggregated** (country/region/week) datasets over individual-level patient records (ethics + complexity).
- Prefer **one primary dataset** + at most **one covariate dataset** (e.g. policy index or mobility) to keep scope realistic.
- When combining datasets, decide and document:
  - **unit of analysis** (country vs region, daily vs weekly)
  - **definitions** (cases: confirmed? probable? by specimen date vs report date)
  - **smoothing** (rolling average window) and why

