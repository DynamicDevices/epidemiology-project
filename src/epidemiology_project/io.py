from __future__ import annotations

from pathlib import Path

import pandas as pd


def read_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    """Read a CSV with sensible defaults for analysis."""
    return pd.read_csv(Path(path), **kwargs)


def write_csv(df: pd.DataFrame, path: str | Path, *, index: bool = False, **kwargs) -> None:
    """Write a CSV, creating parent directories if needed."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=index, **kwargs)

