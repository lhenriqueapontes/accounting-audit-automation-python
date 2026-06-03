import pandas as pd
import numpy as np


def generate_transactions(num_records: int = 1000, seed: int = 42) -> pd.DataFrame:
    """Gera um DataFrame de lançamentos contábeis sintéticos.

    Args:
        num_records: número de registros a serem gerados.
        seed: semente para reproducibilidade.

    Returns:
        DataFrame com colunas: date, account, vendor, amount.
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start="2025-01-01", periods=num_records, freq="D")
    accounts = rng.choice(["Receita", "Despesa", "Ativo", "Passivo"], size=num_records)
    vendors = rng.choice(["FornecedorA", "FornecedorB", "FornecedorC", "FornecedorD"], size=num_records)
    amounts = rng.lognormal(mean=4.0, sigma=1.0, size=num_records).round(2)
    df = pd.DataFrame({
        "date": dates,
        "account": accounts,
        "vendor": vendors,
        "amount": amounts
    })
    return df


def main() -> None:
    """Gera dados e salva em data/synthetic_transactions.csv"""
    df = generate_transactions()
    import os
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", "synthetic_transactions.csv")
    df.to_csv(file_path, index=False)
    print(f"Generated {len(df)} synthetic transactions and saved to {file_path}")


if __name__ == "__main__":
    main()
