from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd
import requests


@dataclass(frozen=True)
class UksHaMetricQuery:
    """Identifies a *single* dataset/metric in the UKHSA dashboard API.

    The UKHSA API is organised like a tree:

    theme → sub_theme → topic → geography_type → geography → metric

    Example (COVID cases for England):
    - theme: infectious_disease
    - sub_theme: respiratory
    - topic: COVID-19
    - geography_type: Nation
    - geography: England
    - metric: COVID-19_cases_casesByDay

    We keep these fields together so notebooks can clearly show *what* data they are downloading.
    """

    theme: str
    sub_theme: str
    topic: str
    geography_type: str
    geography: str
    metric: str


def _get_json(url: str, *, session: requests.Session | None = None) -> dict[str, Any]:
    """GET a URL and parse the response as JSON.

    Why we use a `requests.Session()`:
    - It can reuse HTTP connections, which is faster when we have to request many pages.
    - It keeps our code tidy (one place to add headers/timeouts later if needed).
    """

    s = session or requests.Session()
    # `timeout` prevents the request hanging forever if something goes wrong.
    r = s.get(url, timeout=60)
    # If the server returns an error code (404/500/etc), raise an exception.
    r.raise_for_status()
    return r.json()


def fetch_metric(
    query: UksHaMetricQuery,
    *,
    base_url: str = "https://api.ukhsa-dashboard.data.gov.uk",
    api_version: str = "v2",
    filters: dict[str, Any] | None = None,
    page_size: int | None = None,
    session: requests.Session | None = None,
) -> pd.DataFrame:
    """Fetch a full metric dataset from the UKHSA dashboard API (auto-paginates).

    What this function does:
    - Builds the correct metric URL from the query fields
    - Downloads *all* pages of results (the API returns paginated data)
    - Returns a single pandas DataFrame

    Why pagination matters:
    - Many APIs limit responses to (say) 100–500 rows per request.
    - The UKHSA API returns something like:
      - `results`: the rows on this page
      - `next`: a URL for the next page (or null/None if this is the last page)

    Returns a DataFrame containing the concatenated `results` rows across all pages.
    """
    if api_version not in {"v2"}:
        raise ValueError(f"Unsupported api_version: {api_version!r}")

    # Construct the URL for the dataset we want.
    # This is the core idea of a REST API: a specific URL uniquely identifies a resource (here: a metric dataset).
    url = (
        f"{base_url}/{api_version}/themes/{query.theme}"
        f"/sub_themes/{query.sub_theme}"
        f"/topics/{query.topic}"
        f"/geography_types/{query.geography_type}"
        f"/geographies/{query.geography}"
        f"/metrics/{query.metric}"
    )

    # We'll collect every row from every page in this list, then convert to a DataFrame at the end.
    rows: list[dict[str, Any]] = []
    # Start by requesting the first page (the base metric URL). The API returns `next` if more pages exist.
    next_url: str | None = url
    s = session or requests.Session()

    # Middle ground: use OpenAPI-documented query parameters to reduce downloads.
    #
    # The UKHSA metric endpoint supports filters like `year`, `date`, `age`, `sex`, etc.
    # It also supports `page_size` to request larger pages (the server may still cap this).
    params: dict[str, Any] = {}
    if filters:
        params.update(filters)
    if page_size is not None:
        params["page_size"] = int(page_size)

    while next_url:
        # Download one page of results
        # Only send params on the *first* request. After that we follow the server-provided `next` URL
        # (which already contains the correct query string).
        if next_url == url and params:
            r = s.get(next_url, params=params, timeout=60)
            r.raise_for_status()
            payload = r.json()
        else:
            payload = _get_json(next_url, session=s)
        # DRF-like pagination schema (common pattern):
        # payload = {"count": ..., "next": "...", "previous": "...", "results": [...]}
        results = payload.get("results")
        if not isinstance(results, list):
            raise ValueError(f"Unexpected payload shape from {next_url}: keys={list(payload.keys())}")
        rows.extend(results)
        # Move to next page (or None, which ends the loop)
        next_url = payload.get("next")

    # Turn list-of-dicts into a tabular DataFrame.
    df = pd.DataFrame(rows)
    if "date" in df.columns:
        # Parse ISO dates into pandas datetime objects so sorting/plotting works properly.
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")
    return df.reset_index(drop=True)


def fetch_metric_by_url(
    url: str,
    *,
    filters: dict[str, Any] | None = None,
    page_size: int | None = None,
    session: requests.Session | None = None,
) -> pd.DataFrame:
    """Simplest form: fetch a metric given its full URL (auto-paginates).

    This is the “middle ground” approach:
    - You copy a metric URL (found via Swagger/OpenAPI or by browsing the API)
    - You optionally pass filters like `{\"year\": 2022}` to reduce the download size
    - You get a pandas DataFrame back

    Example:
    - url = \"https://api.ukhsa-dashboard.data.gov.uk/v2/themes/infectious_disease/sub_themes/respiratory/topics/RSV/geography_types/Nation/geographies/England/metrics/RSV_testing_positivityByWeek\"
    - df = fetch_metric_by_url(url, filters={\"year\": 2022}, page_size=1000)
    """

    rows: list[dict[str, Any]] = []
    next_url: str | None = url
    s = session or requests.Session()

    params: dict[str, Any] = {}
    if filters:
        params.update(filters)
    if page_size is not None:
        params["page_size"] = int(page_size)

    while next_url:
        if next_url == url and params:
            r = s.get(next_url, params=params, timeout=60)
            r.raise_for_status()
            payload = r.json()
        else:
            payload = _get_json(next_url, session=s)

        results = payload.get("results")
        if not isinstance(results, list):
            raise ValueError(f"Unexpected payload shape from {next_url}: keys={list(payload.keys())}")
        rows.extend(results)
        next_url = payload.get("next")

    df = pd.DataFrame(rows)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")
    return df.reset_index(drop=True)

