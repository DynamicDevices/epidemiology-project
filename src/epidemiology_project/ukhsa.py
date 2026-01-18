from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd
import requests


@dataclass(frozen=True)
class UksHaMetricQuery:
    theme: str
    sub_theme: str
    topic: str
    geography_type: str
    geography: str
    metric: str


def _get_json(url: str, *, session: requests.Session | None = None) -> dict[str, Any]:
    s = session or requests.Session()
    r = s.get(url, timeout=60)
    r.raise_for_status()
    return r.json()


def fetch_metric(
    query: UksHaMetricQuery,
    *,
    base_url: str = "https://api.ukhsa-dashboard.data.gov.uk",
    api_version: str = "v2",
    session: requests.Session | None = None,
) -> pd.DataFrame:
    """Fetch a full metric time series from the UKHSA dashboard API (auto-paginates).

    Returns a DataFrame containing the concatenated `results` rows across all pages.
    """
    if api_version not in {"v2"}:
        raise ValueError(f"Unsupported api_version: {api_version!r}")

    url = (
        f"{base_url}/{api_version}/themes/{query.theme}"
        f"/sub_themes/{query.sub_theme}"
        f"/topics/{query.topic}"
        f"/geography_types/{query.geography_type}"
        f"/geographies/{query.geography}"
        f"/metrics/{query.metric}"
    )

    rows: list[dict[str, Any]] = []
    next_url: str | None = url
    s = session or requests.Session()

    while next_url:
        payload = _get_json(next_url, session=s)
        # DRF-like pagination schema
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

