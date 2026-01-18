from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Callable

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class SirParams:
    """Parameters for a simple discrete-time SIR model."""

    N: int
    beta: float
    gamma: float


def simulate_sir(
    *,
    params: SirParams,
    I0: int,
    R0: int = 0,
    days: int = 160,
    start_date: date = date(2020, 1, 1),
    beta_schedule: Callable[[int, float], float] | None = None,
    gamma_schedule: Callable[[int, float], float] | None = None,
    vaccination_pulse: tuple[int, float] | None = None,
    scenario: str = "baseline_no_intervention",
) -> pd.DataFrame:
    """Simulate a simple SIR model in discrete time (daily steps).

    Notes:
    - This is a teaching-friendly model. It’s deterministic and uses a simple Euler-style update.
    - `beta_schedule(day, beta0)` can change transmission over time (e.g. lockdown).
    - `gamma_schedule(day, gamma0)` can change recovery over time (e.g. treatment).
    - `vaccination_pulse=(t0, frac)` moves frac of S -> R at day t0.
    """

    if I0 < 0 or R0 < 0:
        raise ValueError("I0 and R0 must be non-negative")
    if I0 + R0 > params.N:
        raise ValueError("I0 + R0 must be <= N")
    if days < 1:
        raise ValueError("days must be >= 1")

    beta0 = float(params.beta)
    gamma0 = float(params.gamma)

    S = float(params.N - I0 - R0)
    I = float(I0)
    R = float(R0)

    rows: list[dict] = []

    for t in range(days):
        beta_t = beta_schedule(t, beta0) if beta_schedule else beta0
        gamma_t = gamma_schedule(t, gamma0) if gamma_schedule else gamma0

        if vaccination_pulse and t == vaccination_pulse[0]:
            frac = float(vaccination_pulse[1])
            frac = max(0.0, min(1.0, frac))
            moved = frac * S
            S -= moved
            R += moved

        # New infections and recoveries (discrete-time approximation)
        new_inf = beta_t * S * I / params.N
        new_rec = gamma_t * I

        # Clamp so we don't go negative due to approximation
        new_inf = min(new_inf, S)
        new_rec = min(new_rec, I)

        S -= new_inf
        I += new_inf - new_rec
        R += new_rec

        rows.append(
            {
                "t_day": t,
                "date": (start_date + timedelta(days=t)).isoformat(),
                "S": S,
                "I": I,
                "R": R,
                "N": params.N,
                "beta": beta_t,
                "gamma": gamma_t,
                "scenario": scenario,
            }
        )

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    return df


def step_change(after_day: int, factor: float) -> Callable[[int, float], float]:
    """Return a schedule that multiplies the baseline value by factor after after_day."""

    f = float(factor)

    def schedule(day: int, base: float) -> float:
        return base * f if day >= after_day else base

    return schedule

