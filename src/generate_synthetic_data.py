"""Synthetic accounting journal generator.

The generated file is fake and exists only for audit automation practice.
It intentionally includes a few anomalies so the audit scripts have something
realistic to detect: duplicates, unusual values, weekend entries and late approvals.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

ACCOUNTS = [
    "Sales revenue",
    "Service revenue",
    "Office supplies",
    "Travel expenses",
    "Software subscriptions",
    "Consulting services",
    "Maintenance",
    "Taxes and fees",
]

COST_CENTERS = ["Finance", "Accounting", "Operations", "Sales", "IT", "HR"]
VENDORS = [
    "Vendor Alpha",
    "Vendor Beta",
    "Vendor Gamma",
    "Vendor Delta",
    "Vendor Omega",
    "Vendor Sigma",
]
APPROVERS = ["analyst_01", "analyst_02", "manager_01", "manager_02"]


def generate_transactions(rows: int = 1200, seed: int = 42) -> pd.DataFrame:
    """Create a synthetic accounting journal.

    Parameters
    ----------
    rows:
        Number of base records to generate before injecting anomalies.
    seed:
        Random seed for reproducibility.
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2025-01-01", periods=365, freq="D")

    df = pd.DataFrame(
        {
            "entry_id": [f"JE-{i:06d}" for i in range(1, rows + 1)],
            "posting_date": rng.choice(dates, size=rows),
            "account": rng.choice(ACCOUNTS, size=rows),
            "cost_center": rng.choice(COST_CENTERS, size=rows),
            "vendor": rng.choice(VENDORS, size=rows),
            "amount": rng.lognormal(mean=7.2, sigma=0.75, size=rows).round(2),
            "created_by": rng.choice(["user_a", "user_b", "user_c", "user_d"], size=rows),
            "approved_by": rng.choice(APPROVERS, size=rows),
        }
    )

    # Make revenue entries negative to mimic a common accounting sign convention.
    revenue_mask = df["account"].str.contains("revenue", case=False)
    df.loc[revenue_mask, "amount"] = -df.loc[revenue_mask, "amount"]

    # Inject controlled anomalies.
    duplicate_sample = df.sample(n=max(8, rows // 80), random_state=seed).copy()
    duplicate_sample["entry_id"] = [f"JE-DUP-{i:04d}" for i in range(len(duplicate_sample))]
    df = pd.concat([df, duplicate_sample], ignore_index=True)

    high_value_idx = rng.choice(df.index, size=max(5, rows // 100), replace=False)
    df.loc[high_value_idx, "amount"] = (df.loc[high_value_idx, "amount"].abs() * rng.uniform(6, 12)).round(2)

    late_approval_idx = rng.choice(df.index, size=max(10, rows // 60), replace=False)
    df.loc[late_approval_idx, "approved_by"] = "pending"

    df["posting_date"] = pd.to_datetime(df["posting_date"]).dt.date
    return df.sort_values("posting_date").reset_index(drop=True)


def save_dataset(df: pd.DataFrame, output: str | Path) -> Path:
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a synthetic accounting journal.")
    parser.add_argument("--rows", type=int, default=1200)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", default="data/synthetic_journal.csv")
    args = parser.parse_args()

    path = save_dataset(generate_transactions(args.rows, args.seed), args.output)
    print(f"Saved synthetic accounting journal to {path}")


if __name__ == "__main__":
    main()
