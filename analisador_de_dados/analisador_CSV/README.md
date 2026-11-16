# 📊 Analisador de Dados com Python e Pandas

## 📌 Sobre o Projeto

O **Analisador de Dados** é uma aplicação desenvolvida em Python que utiliza a biblioteca **Pandas** para realizar a leitura, manipulação, análise e exportação de dados comerciais armazenados em arquivos CSV.

O projeto possui uma interface de linha de comando (CLI), permitindo que o usuário explore informações de produtos, aplique filtros de preços, visualize estatísticas e gere análises de desempenho de forma interativa.

O principal objetivo é aplicar conceitos de **análise de dados, lógica de programação, automação de processos e manipulação de arquivos**, simulando situações reais de processamento de informações comerciais.

---

## 🚀 Funcionalidades

O sistema disponibiliza um menu interativo com quatro funcionalidades principais.

### 1. 📋 Visão Geral e Estatísticas

Permite visualizar as principais informações do conjunto de dados utilizando funcionalidades nativas do Pandas.

- Exibição das primeiras linhas com `df.head()`.
- Identificação das colunas e dos tipos de dados com `df.info()`.
- Geração de estatísticas descritivas com `df.describe()`.
- Visualização da estrutura geral do arquivo CSV.

### 2. 💰 Filtragem de Produtos Acima de R$ 300

Realiza uma consulta ao DataFrame, identificando os produtos cujo preço é superior a R$ 300,00.

Essa funcionalidade demonstra a utilização de filtros condicionais para selecionar registros com base em critérios comerciais.

### 3. 🏷️ Filtragem de Produtos Abaixo de R$ 300

Permite consultar produtos com valores inferiores a R$ 300,00, facilitando a segmentação dos dados por faixa de preço.

### 4. 📈 Análise de Desempenho e Atualização de Dados

Executa operações para analisar o desempenho comercial dos produtos.

- Processamento de informações utilizando Pandas.
- Aplicação de cálculos e regras condicionais.
- Análise de métricas de faturamento e desempenho.
- Atualização dos dados processados.
- Exportação dos resultados para arquivos CSV.

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

**Python 3:** linguagem principal utilizada no desenvolvimento da aplicação.

**Pandas:** biblioteca responsável pela leitura, manipulação, filtragem e análise dos dados.

**CSV:** formato utilizado para armazenar e exportar informações tabulares.

**CLI (Command-Line Interface):** interface de interação com o usuário por meio do terminal.

---

## 📁 Estrutura do Projeto

```text
analisador_de-dados/
│
├── analisador.py
│   └── Código principal do sistema
│
├── dados.csv
│   └── Base de dados utilizada nas análises
│
├── README.md
│   └── Documentação do projeto
│
└── arquivos CSV gerados
    └── Resultados das análises
```

**Observação:** `analisador.py` é um nome sugerido para o arquivo principal. Caso o arquivo existente possua outro nome, utilize o nome correspondente nos comandos.

---

## 💻 Instalação e Execução

### 1. Pré-requisitos

Para executar o projeto, é necessário possuir:

- Python 3 instalado.
- Biblioteca Pandas.
- Git para clonar o repositório.
- Terminal, PowerShell ou Visual Studio Code.

### 2. Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/Rafael-Santos-Tech/Python-mini-projetos.git
```

Acesse a pasta do projeto:

```bash
cd Python-mini-projetos/analisador_de-dados
```

### 3. Instalar as dependências

Execute o comando:

```bash
python -m pip install pandas
```

### 4. Executar o programa

Com os arquivos necessários disponíveis, execute:

```bash
python analisador.py
```

Substitua `analisador.py` pelo nome real do arquivo principal, caso seja diferente.

### 5. Configuração do arquivo CSV

O programa utiliza um arquivo chamado `dados.csv` para carregar as informações.

```python
import pandas as pd

df = pd.read_csv("dados.csv")
```

O arquivo deve estar no diretório de execução esperado pelo programa.

Caso o arquivo não seja encontrado, será necessário verificar seu caminho.

---

## 🖥️ Exemplo de Funcionamento

Ao iniciar a aplicação, o usuário encontra o seguinte menu:

```text
==================================================
📊 MENU DO ANALISADOR DE DADOS
==================================================
1 - Ver visão Geral, Estrutura e Estatísticas
2 - Filtrar Produtos acima de R$300
3 - Filtrar Produtos abaixo de R$300
4 - Gerar Análise de Desempenho e Atualizar Tabela
0 - Sair do Programa
==================================================

Escolha uma opção (0 a 4):
```

### Exemplo: Consultando estatísticas

Ao selecionar a opção `1`, o sistema executa:

```python
print("--- Visão Geral ---")
print(df.head())

print("\n--- Estrutura do Arquivo ---")
df.info()

print("\n--- Estatísticas Automáticas ---")
print(df.describe())
```

Essa operação permite compreender a estrutura do conjunto de dados, identificar valores numéricos e visualizar informações estatísticas relevantes.

### Exemplo: Filtrando produtos

Um filtro condicional com Pandas pode ser implementado da seguinte forma:

```python
produtos_filtrados = df[df["Preco"] > 300]

print(produtos_filtrados)
```

O exemplo considera uma coluna chamada `Preco`. O nome deve corresponder à coluna existente no arquivo CSV.

---

## 🧠 Conceitos Aplicados

Durante o desenvolvimento, foram utilizados conhecimentos de programação e análise de dados, incluindo:

- Estruturas condicionais `if`, `elif` e `else`.
- Estruturas de repetição com `while`.
- Entrada de dados com `input()`.
- Manipulação de DataFrames.
- Leitura e escrita de arquivos CSV.
- Filtragem e seleção de registros.
- Estatísticas descritivas.
- Operações vetorizadas com Pandas.
- Organização de menus interativos.
- Processamento e exportação de informações.

---

## 🔮 Possíveis Melhorias Futuras

O projeto poderá receber novas funcionalidades, como:

- Geração de gráficos utilizando Matplotlib.
- Exportação de relatórios para Excel.
- Implementação de filtros personalizados.
- Tratamento de erros para arquivos inexistentes ou inválidos.
- Validação de colunas e tipos de dados.
- Criação de dashboards interativos.
- Integração com bancos de dados SQL.
- Automatização de relatórios comerciais.

---

## 🎯 Objetivo Educacional

Este projeto foi desenvolvido para consolidar conhecimentos em **Python e análise de dados**, demonstrando como informações armazenadas em arquivos CSV podem ser processadas e transformadas em resultados úteis.

A aplicação também contribui para o desenvolvimento de habilidades relacionadas à resolução de problemas, organização de código e utilização de bibliotecas amplamente empregadas no mercado de tecnologia.

---

## 👨‍💻 Desenvolvedor

**Rafael dos Santos Ferreira Lima**

Estudante de **Análise e Desenvolvimento de Sistemas (ADS)**, com interesse em desenvolvimento de software, Python, análise de dados e tecnologias Back-end.

**GitHub:** [Rafael-Santos-Tech](https://github.com/Rafael-Santos-Tech)

**Repositório:** [Python-mini-projetos](https://github.com/Rafael-Santos-Tech/Python-mini-projetos)

---

⭐ Se este projeto foi útil ou interessante, considere deixar uma estrela no repositório!

*Desenvolvido para fins educacionais e aprimoramento de habilidades em programação e análise de dados.*