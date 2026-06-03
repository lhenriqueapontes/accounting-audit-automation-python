# Accounting Audit Automation Python

## Objetivo do projeto

Automatizar tarefas de auditoria contábil usando Python, incluindo detecção de duplicidades, lançamentos fora de padrão, concentração de fornecedores e aplicação da lei de Benford a um conjunto de lançamentos contábeis sintéticos.

## Problema de negócio

Auditores e controllers precisam analisar grandes volumes de lançamentos contábeis para identificar erros e fraudes. Processos manuais são lentos e sujeitos a falhas. Este projeto demonstra como scripts em Python podem automatizar verificações básicas em planilhas de lançamentos sintéticos, reduzindo o tempo de análise e servindo de base para soluções mais completas.

## Tecnologias usadas

- Python 3
- pandas e NumPy para manipulação de dados
- matplotlib e seaborn para visualizações
- SciPy ou implementações simples para a lei de Benford
- Jupyter Notebook para prototipagem
- Git

## Estrutura de pastas

```
/
├── README.md
├── DISCLAIMER.md
├── LICENSE
├── CITATION.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── generate_synthetic_data.py
│   ├── audit_checks.py
│   └── report.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── data/
│   └── README.md
└── tests/
    └── test_audit_checks.py
```

- `src/` contém scripts para geração de dados sintéticos e verificações de auditoria.
- `notebooks/` armazena notebooks para exploração de dados e demonstrações.
- `data/` inclui um README explicando o uso de dados sintéticos; os datasets reais não são incluídos.
- `tests/` contém testes de unidade simples.

## Como executar

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Gere um dataset sintético:
   ```bash
   python src/generate_synthetic_data.py --output data/synthetic_journal.csv
   ```
4. Execute as verificações de auditoria:
   ```bash
   python src/audit_checks.py --input data/synthetic_journal.csv --report reports/audit_report.md
   ```
5. Abra `reports/audit_report.md` para ver o relatório com achados e gráficos.

## Exemplo de saída

Um relatório em Markdown com tabelas resumindo:
- Duplicidades detectadas
- Lançamentos fora de padrão
- Fornecedores com alta concentração de despesas
- Distribuição dos dígitos iniciais para a lei de Benford

## Resultados esperados

Demonstrar como ferramentas simples de análise de dados podem automatizar partes do processo de auditoria. Recrutadores podem ver habilidades em contabilidade, auditoria, Python, manipulação de dados e geração de relatórios.

## O que este projeto demonstra para recrutadores

- Capacidade de combinar conhecimento contábil com programação.
- Uso de bibliotecas de dados para auditoria automatizada.
- Estruturação de projetos com testes, scripts, notebooks e documentação.
- Atenção a aspectos éticos e uso de dados sintéticos.

## Limitações

Este projeto utiliza dados sintéticos simplificados e regras genéricas. Não substitui auditoria profissional. Resultados não devem ser aplicados a dados reais sem adaptações.

## Créditos, fontes e licenças

Projeto inspirado em técnicas de auditoria apresentadas na literatura e exemplos de código aberto. Consulte CITATION.md para referências. Código sob licença MIT.

## Aviso ético

Este repositório utiliza apenas dados públicos ou sintéticos e não inclui informações sensíveis ou material institucional. É apenas uma demonstração educacional/profissional para portfólio.
