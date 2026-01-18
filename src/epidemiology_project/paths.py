from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    """Return the repository root (assumes this file lives in src/epidemiology_project/)."""
    return Path(__file__).resolve().parents[2]


def data_dir() -> Path:
    return project_root() / "data"


def raw_data_dir() -> Path:
    return data_dir() / "raw"


def interim_data_dir() -> Path:
    return data_dir() / "interim"


def processed_data_dir() -> Path:
    return data_dir() / "processed"


def reports_dir() -> Path:
    return project_root() / "reports"


def figures_dir(final: bool = True) -> Path:
    """Default figure output directory.

    If final=True, use reports/figures. Otherwise use figures/ for scratch.
    """
    return (reports_dir() / "figures") if final else (project_root() / "figures")

