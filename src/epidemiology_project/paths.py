from __future__ import annotations

"""Project path helpers.

Why this file exists:
- In a group project, notebooks often break because people run them from different folders.
- Using *one* shared set of path functions keeps file locations consistent:
  - raw data always goes in `data/raw/`
  - processed data always goes in `data/processed/`
  - final figures always go in `reports/figures/`

These functions return `pathlib.Path` objects, which are the standard Python way to work with paths.
"""

from pathlib import Path


def project_root() -> Path:
    """Return the repository root folder.

    How it works:
    - `__file__` is the path to *this* file on disk.
    - `parents[2]` walks up:
      - `.../src/epidemiology_project/paths.py` → `.../src/epidemiology_project/` (parents[0])
      - → `.../src/` (parents[1])
      - → repo root (parents[2])
    """
    return Path(__file__).resolve().parents[2]


def data_dir() -> Path:
    """Top-level data folder: `data/`."""
    return project_root() / "data"


def raw_data_dir() -> Path:
    """Raw data folder: `data/raw/` (do not edit files in-place)."""
    return data_dir() / "raw"


def interim_data_dir() -> Path:
    """Intermediate data folder: `data/interim/` (cleaned/merged but not final)."""
    return data_dir() / "interim"


def processed_data_dir() -> Path:
    """Processed data folder: `data/processed/` (final datasets used for plots/models)."""
    return data_dir() / "processed"


def reports_dir() -> Path:
    """Reports folder: `reports/` (write-ups, slides, final exports)."""
    return project_root() / "reports"


def figures_dir(final: bool = True) -> Path:
    """Default figure output directory.

    If final=True, use reports/figures. Otherwise use figures/ for scratch.
    """
    return (reports_dir() / "figures") if final else (project_root() / "figures")

