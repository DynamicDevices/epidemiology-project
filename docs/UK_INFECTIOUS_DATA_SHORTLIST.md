# UK infectious disease data shortlist (student friendly)

These sources are chosen because they are typically **public**, **aggregated** (safer ethically), and suitable for Jupyter/pandas workflows.

## 1) UKHSA infectious disease data dashboard (England)

- **Best for**: respiratory viruses (COVID-19, influenza, RSV), healthcare-associated infections (HCAI), antimicrobial resistance (AMR), vaccination-related indicators (varies).
- **Why it’s great**: modern dashboard with **download/API options**, usually weekly time series and (often) regional breakdowns.
- **Start here**:
  - Main dashboard: `https://ukhsa-dashboard.data.gov.uk/`
  - Data access page: `https://ukhsa-dashboard.data.gov.uk/access-our-data`

**Project ideas**
- Compare **seasonality** of RSV vs influenza (peak timing, peak size, year-to-year variation).
- Analyse **HCAI** trends (e.g. MRSA, E. coli bloodstream infections): trend lines + change-point style “did it change?”.
- AMR: track resistance percentages over time (simple trend + interpretation).

## 2) Notifications of Infectious Diseases (NOIDs) – England & Wales (UKHSA / GOV.UK collection)

- **Best for**: legally notifiable diseases (weekly totals by disease; format varies by report).
- **Start here**: `https://www.gov.uk/government/collections/notifications-of-infectious-diseases-noids`

**Project ideas**
- Choose one vaccine-preventable disease (e.g. measles/pertussis if available) and study long-run trends / recent spikes.
- Compare pre/post a chosen date (reporting change, intervention, etc.) with cautious interpretation.

## 3) Notifications of Infectious Diseases – Northern Ireland (OpenDataNI via data.gov.uk CKAN)

- **Best for**: simple, downloadable weekly notification counts in a tidy-ish form.
- **Start here**: `https://ckan.publishing.service.gov.uk/dataset/notification-of-infectious-diseases`

**Project ideas**
- Seasonal patterns for one disease across multiple years.
- “Outbreak detection lite”: flag weeks unusually high vs baseline (z-scores, percentile thresholds).

## 4) Public Health Scotland (notifiable disease statistics) (historical)

- **Best for**: Scotland-focused notifiable disease time series (often historical).
- **Start here**: `https://ckan.publishing.service.gov.uk/dataset/notifiable_infectious_disease_statistics`

## 5) ONS deaths + population (supporting data for rates)

These aren’t “infection datasets” themselves, but they’re extremely helpful for:
- converting counts → **rates per 100k**
- adding context (mortality impact, denominators, age structure)

- **ONS main portal**: `https://www.ons.gov.uk/`

## Recommendation (fastest path to a strong project)

If you want the simplest, most robust workflow:

- **Primary dataset**: UKHSA dashboard (pick *one* theme: respiratory OR HCAI OR AMR)
- **Supporting dataset**: ONS population denominators (optional, but improves quality by allowing per-capita rates)

This usually yields 3–6 excellent figures with minimal wrangling.

