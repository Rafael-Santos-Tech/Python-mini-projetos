# Analisador de Dados com CSV

Mini-projeto em Python que usa Pandas para analisar preços e vendas de produtos a partir de um arquivo CSV. A análise é feita pelo menu do terminal.

## Como executar no Windows

Com o Python 3 instalado, abra o PowerShell na pasta `analisador_CSV` e execute os comandos abaixo.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Mantenha `dados.csv` junto de `main.py`. Para usar sua própria base, preserve as colunas `produto`, `preco` e `vendas_mes`. Os valores de preço e vendas devem ser numéricos.

## Opções do menu

| Opção | Ação |
| --- | --- |
| `1` | Mostra uma amostra dos dados, a estrutura da tabela e as estatísticas descritivas. |
| `2` | Lista produtos com preço acima de R$ 300. |
| `3` | Lista produtos com preço abaixo de R$ 300. |
| `4` | Calcula o faturamento, classifica os produtos e grava o arquivo `dados_atualizados.csv`. |
| `0` | Encerra o programa. |

Na opção `4`, o faturamento é calculado por `preco × vendas_mes`. O produto recebe o status `Caro/Baixa saída` quando custa mais de R$ 200 e teve menos de 10 vendas no mês. Os demais recebem o status `Normal`. O resultado é salvo na pasta do projeto.

## Versão com banco de dados

A [versão MySQL](../analisador_MySQL/) amplia o projeto com cadastro, edição e exclusão de produtos e um dashboard de vendas.
