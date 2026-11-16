# Analisador de Dados com MySQL

Aplicação de terminal em Python para gerenciar produtos e analisar suas vendas do mês. Os dados ficam no MySQL, as consultas são carregadas com Pandas e o dashboard é gerado com Matplotlib.

## Preparar o banco de dados

Com o MySQL Server em execução, abra uma conexão no MySQL Workbench ou em outro cliente SQL e rode o script abaixo para criar a estrutura usada pelo programa.

```sql
CREATE DATABASE IF NOT EXISTS analise_vendas
    CHARACTER SET utf8mb4;

USE analise_vendas;

CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(150) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    quantidade INT NOT NULL,
    vendas_mes INT NOT NULL
);
```

O arquivo `banco.py` configura a conexão com `localhost`, porta `3306`, usuário `root` e banco `analise_vendas`. Se seu MySQL usa outro usuário ou porta, ajuste esses valores em `banco.py`. O programa pede a senha do MySQL no terminal ao iniciar.

## Como executar no Windows

Com o Python 3 instalado, abra o PowerShell na pasta `analisador_MySQL` e execute os comandos abaixo.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Se a tabela estiver vazia, cadastre o primeiro produto pela opção `8`. Use a opção `5` para visualizar o dashboard e salvar `dashboard.png` na pasta do projeto.

## Opções do menu

| Opção | Ação |
| --- | --- |
| `1` | Mostra os produtos, a estrutura dos dados e as estatísticas descritivas. |
| `2` | Lista produtos com preço acima de R$ 300. |
| `3` | Lista produtos com preço abaixo de R$ 300. |
| `4` | Exibe o faturamento e a classificação de cada produto. |
| `5` | Gera o dashboard com faturamento, vendas, quantidade e classificação dos produtos. |
| `6` | Atualiza nome, preço, quantidade ou vendas do mês de um produto pelo ID. |
| `7` | Exclui um produto pelo ID após a confirmação no terminal. |
| `8` | Cadastra um produto e mostra o ID gerado. |
| `0` | Encerra o programa. |

O faturamento de cada produto é `preco × vendas_mes`. A classificação é `Sem vendas` para zero unidades vendidas, `Caro/Baixa saída` para preço acima de R$ 300 com 1 a 9 unidades vendidas no mês e `Normal` nos demais casos.

## Arquivos principais

| Arquivo | Função |
| --- | --- |
| `main.py` | Exibe o menu e valida os dados informados no terminal. |
| `banco.py` | Abre a conexão com SQLAlchemy e PyMySQL e executa as operações no MySQL. |
| `dashboard.py` | Gera e salva os gráficos com Matplotlib. |

A [versão CSV](../analisador_CSV/) usa um arquivo local como fonte de dados.
