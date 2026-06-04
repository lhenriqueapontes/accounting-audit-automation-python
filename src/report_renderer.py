from pathlib import Path
import pandas as pd


def render_table(path):
    path = Path(path)
    if not path.exists():
        return 'missing file'
    df = pd.read_csv(path)
    if df.empty:
        return 'empty table'
    return df.head(10).to_markdown(index=False)


def main():
    folder = Path('reports')
    folder.mkdir(exist_ok=True)
    output = folder / 'report.md'
    text = '# Demo Review Report\n\n'
    for filename in ['summary.csv', 'duplicates.csv', 'high_value_entries.csv', 'weekend_entries.csv', 'pending_approval_entries.csv', 'benford_table.csv']:
        text += f'## {filename}\n\n'
        text += render_table(folder / filename) + '\n\n'
    output.write_text(text, encoding='utf-8')
    print(output)


if __name__ == '__main__':
    main()
