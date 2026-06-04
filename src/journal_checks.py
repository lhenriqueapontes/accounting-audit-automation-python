from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

REQUIRED_COLUMNS = [
    "entry_id",
    "posting_date",
    "account",
    "cost_center",
    "vendor",
    "amount",
    "created_by",
    "approved_by",
]


def load_journal(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["posting_date"])
    missing = sorted(set(REQUIRED_COLUMNS) - set(df.columns))
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df


def duplicate_entries(df: pd.DataFrame) -> pd.DataFrame:
    keys = ["posting_date", "account", "cost_center", "vendor", "amount"]
    return df[df.duplicated(subset=keys, keep=False)].sort_values(keys)


def high_value_entries(df: pd.DataFrame, z_limit: float = 3.0) -> pd.DataFrame:
    absolute_amount = df["amount"].abs()
    z = (absolute_amount - absolute_amount.mean()) / absolute_amount.std(ddof=0)
    result = df[z.abs() >= z_limit].copy()
    result["amount_abs_zscore"] = z.loc[result.index].round(2)
    return result.sort_values("amount_abs_zscore", ascending=False)


def weekend_entries(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["posting_date"].dt.weekday >= 5].copy()


def pending_approval_entries(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["approved_by"].astype(str).str.lower().eq("pending")].copy()


def benford_table(df: pd.DataFrame) -> pd.DataFrame:
    amounts = df["amount"].abs()
    amounts = amounts[amounts > 0]
    first_digits = amounts.astype(str).str.replace(".", "", regex=False).str.lstrip("0").str[0]
    observed = first_digits.value_counts(normalize=True).reindex(list("123456789"), fill_value=0)
    expected = pd.Series({str(d): np.log10(1 + 1 / d) for d in range(1, 10)})
    return pd.DataFrame({
        "digit": observed.index,
        "observed_pct": (observed.values * 100).round(2),
        "expected_pct": (expected.values * 100).round(2),
        "difference_pct": ((observed.values - expected.values) * 100).round(2),
    })


def summary(df: pd.DataFrame) -> pd.DataFrame:
    rows = [
        ("total_entries", len(df)),
        ("duplicate_entries", len(duplicate_entries(df))),
        ("high_value_entries", len(high_value_entries(df))),
        ("weekend_entries", len(weekend_entries(df))),
        ("pending_approval_entries", len(pending_approval_entries(df))),
        ("total_absolute_amount", round(float(df["amount"].abs().sum()), 2)),
    ]
    return pd.DataFrame(rows, columns=["metric", "value"])


def run_checks(input_path: str | Path, output_dir: str | Path = "reports") -> None:
    df = load_journal(input_path)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    summary(df).to_csv(output / "summary.csv", index=False)
    duplicate_entries(df).to_csv(output / "duplicates.csv", index=False)
    high_value_entries(df).to_csv(output / "high_value_entries.csv", index=False)
    weekend_entries(df).to_csv(output / "weekend_entries.csv", index=False)
    pending_approval_entries(df).to_csv(output / "pending_approval_entries.csv", index=False)
    benford_table(df).to_csv(output / "benford_table.csv", index=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/synthetic_journal.csv")
    parser.add_argument("--output-dir", default="reports")
    args = parser.parse_args()
    run_checks(args.input, args.output_dir)
    print(f"Reports saved to {args.output_dir}")


if __name__ == "__main__":
    main()
