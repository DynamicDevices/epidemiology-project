# Data folder rules

## Subfolders

- `raw/`: original data exactly as downloaded (immutable)
- `external/`: reference data (e.g. shapefiles, lookup tables)
- `interim/`: cleaned/merged intermediate datasets
- `processed/`: final dataset(s) used for modelling/plots

## Conventions

- Never edit files in `raw/`. If you need changes, write a script/notebook that outputs to `interim/` or `processed/`.
- Include a short note for each dataset in `docs/DATA_SOURCES.md` (where it came from, date downloaded, key columns).
- Prefer storing **small** CSVs; if data becomes large, store only links + a download script.

