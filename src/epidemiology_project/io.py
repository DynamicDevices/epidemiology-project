from __future__ import annotations

"""Small I/O helpers for notebooks.

These wrappers do two simple (but helpful) things for a student project:
- accept either strings or `Path` objects
- ensure parent folders exist before writing outputs

They keep notebooks slightly cleaner and reduce repeated boilerplate code.
"""

from pathlib import Path

import pandas as pd


def read_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    """Read a CSV into a pandas DataFrame.

    Parameters
    - path: file path (string or Path)
    - kwargs: passed through to `pandas.read_csv`
    """
    return pd.read_csv(Path(path), **kwargs)


def write_csv(df: pd.DataFrame, path: str | Path, *, index: bool = False, **kwargs) -> None:
    """Write a DataFrame to CSV, creating parent directories if needed.

    This helps because we often write outputs like:
    - `data/processed/...`
    - `reports/tables/...`
    and we don't want notebooks to fail just because the folder doesn't exist yet.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=index, **kwargs)

