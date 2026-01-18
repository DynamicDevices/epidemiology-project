# Project context (living document)

## One-sentence goal

> TODO: e.g. “Use real public health data to answer a clear epidemiology question with simple maths + clear visuals.”

## Research question (pick one)

- Option A (time-series): TODO
- Option B (SIR/SEIR model): TODO
- Option C (excess mortality): TODO

### Suggested (UK + infectious + respiratory)

> **“Time vs infected” question (simple): How does the number of infections change over time?**

Important note: “infected” is rarely observed directly. In public surveillance you usually use a **proxy**:
- **confirmed cases** (best match to “infected”, when available; COVID has this)
- **test positivity** (fraction positive; good for comparing waves)
- **syndromic indicators** (e.g. NHS 111/GP “acute respiratory infection” counts/rates)
- **hospital admissions** (severe end; good quality but not “all infections”)

Minimum viable analysis:
- pick one proxy series and plot **date/week vs metric_value**
- optionally smooth (7-day or 3–5 week rolling mean) and find the peak

Suggested starting point if you truly want “infected counts”:
- UKHSA dashboard API: **COVID-19 confirmed cases by day** (England)

## Scope (keep it small)

- **Geography**: TODO (e.g. UK, England regions, one country)
- **Time window**: TODO
- **Outcomes**: TODO (cases / hospitalisations / deaths / excess deaths)

## Team roles (suggested)

- **Data**: ingestion + cleaning + dataset documentation
- **Analysis**: computations + model fitting
- **Visuals**: figures for poster/report + styling
- **Write-up**: narrative + limitations + references

## Outputs

- `notebooks/`: analysis notebooks
- `reports/`: report/poster/slides (export final figures to `reports/figures/`)

