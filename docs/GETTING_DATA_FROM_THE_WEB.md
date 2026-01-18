# Getting data from the web (different ways)

This project uses public health data from the UKHSA dashboard API. There are a few different ways you can “get data from the web”, and they each have pros/cons.

## 1) Manual download (click download on a website)

**What it is**
- You open a dashboard in your browser and click “Download CSV”.

**Pros**
- Fastest for a one-off.
- No programming required.

**Cons (for a group project)**
- Hard to reproduce exactly (different people may click different filters).
- Easy to lose track of *which* file version you used and when you downloaded it.
- Not scalable if you need many datasets (baseline + multiple scenarios).

## 2) Direct file URL (one-shot CSV/Excel link)

**What it is**
- Some sites provide a stable URL to a CSV/Excel file, so you can do:
  - `pandas.read_csv("https://.../file.csv")`

**Pros**
- Very simple code.
- Reproducible if the URL is stable and versioned.

**Cons**
- Not always available (many dashboards don’t expose a single CSV link).
- Sometimes the URL changes or the file is replaced without versioning.

## 3) API access (what we use here)

**What it is**
- An **API** (Application Programming Interface) returns data in a structured format (usually JSON).
- You write code to request the data (HTTP GET), then convert it into a table.

**Pros (why we use it)**
- **Reproducible**: the code records exactly what you downloaded (topic, geography, metric).
- **Scales well**: you can download multiple datasets by changing a few query fields.
- **Automatable**: rerun later to update data, or rerun on a new machine (e.g. Codespaces).
- **Safer for “missing data” problems**: APIs often provide consistent schemas.

**Cons**
- Slightly more code to learn (requests + pagination).

## Why do we handle pagination?

Many APIs return results in pages (e.g. 100–500 rows at a time) to avoid huge responses.

The UKHSA API commonly returns:
- `results`: rows on the current page
- `next`: a URL for the next page (or `null` when finished)

If you only download the first page, you silently miss most of the dataset — that’s why our helper follows `next` until it is `None`.

## Where this appears in the project

- The tutorial notebook (walkthrough): `notebooks/00_tutorial_swagger_openapi_ukhsa.ipynb`
- The API helper code: `src/epidemiology_project/ukhsa.py`
- The “baseline observed” dataset notebook: `notebooks/09_download_baseline_observed_ukhsa_covid_cases.ipynb`

