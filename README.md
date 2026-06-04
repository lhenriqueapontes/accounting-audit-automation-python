# Accounting Audit Automation Python

Projeto funcional de revisao contabil com Python e dados sinteticos.

## Objetivo

Simular uma rotina de analise de lancamentos contabeis. O projeto gera uma base ficticia, roda testes de consistencia e produz arquivos de saida para revisao.

## Funcionalidades

- Geracao de diario contabil sintetico.
- Identificacao de lancamentos parecidos.
- Deteccao de valores muito altos por z-score.
- Lista de lancamentos em fim de semana.
- Lista de aprovacoes pendentes.
- Tabela de primeiro digito inspirada na Lei de Benford.
- Relatorio simples em Markdown.

## Estrutura

```text
src/
  generate_synthetic_data.py
  journal_checks.py
  report_renderer.py

data/
  synthetic_journal.csv

reports/
  summary.csv
  duplicates.csv
  high_value_entries.csv
  weekend_entries.csv
  pending_approval_entries.csv
  benford_table.csv
  report.md
```

## Como executar

```bash
pip install -r requirements.txt
python src/generate_synthetic_data.py --rows 1200 --output data/synthetic_journal.csv
python src/journal_checks.py --input data/synthetic_journal.csv --output-dir reports
python src/report_renderer.py
```

Abra `reports/report.md` para visualizar o relatorio.

## Tutorial resumido

1. O arquivo `generate_synthetic_data.py` cria transacoes ficticias.
2. O arquivo `journal_checks.py` aplica regras de revisao.
3. O arquivo `report_renderer.py` transforma os CSVs em um relatorio.
4. Os resultados em `reports/` devem ser interpretados como fila de revisao, nao como conclusao automatica.

## Dados

Todos os dados sao ficticios e existem apenas para demonstrar programacao, analise de dados e automacao de auditoria.

## Licenca

MIT License.
