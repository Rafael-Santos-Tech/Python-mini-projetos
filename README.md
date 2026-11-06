# 🚀 Portfólio Python | Análise de Dados, API REST & Google Sheets

Bem-vindo ao meu portfólio de projetos desenvolvidos em **Python**!

Este repositório reúne três projetos práticos voltados à análise de dados, desenvolvimento Back-end e integração com ferramentas externas.

O objetivo é aplicar conhecimentos de lógica de programação, manipulação de arquivos, automação de processos, desenvolvimento de APIs RESTful e persistência de dados, explorando diferentes aplicações da linguagem Python.

## 🛠️ Tecnologias e Ferramentas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-34A853?style=for-the-badge&logo=googlesheets&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

**Principais conhecimentos aplicados:** Python 3, Pandas, Flask, JSON, CSV, APIs REST, requisições HTTP, integração de sistemas e Git/GitHub.

---

## 📁 Estrutura do Repositório

O repositório está organizado em três projetos independentes:

```text
Python-mini-projetos/
│
├── analisador_de-dados/
│   └── Projeto de análise de dados com Pandas
│
├── Flask_Games_API/
│   └── API REST para gerenciamento de jogos
│
├── integracao_google_sheets/
│   └── Projeto de integração com Google Sheets
│
└── README.md
```

## 📊 1. Analisador de Dados via CLI — Pandas

**Diretório:** `analisador_de-dados`

Sistema interativo desenvolvido em Python para leitura, processamento, análise e exportação de dados comerciais armazenados em arquivos CSV.

O projeto utiliza a biblioteca Pandas para transformar dados brutos em informações que auxiliam na avaliação do desempenho de produtos e vendas.

### Principais funcionalidades

- Menu interativo executado diretamente no terminal (CLI).
- Leitura e processamento de arquivos CSV.
- Visualização da estrutura e das primeiras linhas dos dados.
- Geração de estatísticas descritivas com Pandas.
- Filtragem de produtos com base em faixas de preço.
- Cálculo de métricas comerciais e faturamento.
- Classificação de desempenho por meio de regras condicionais.
- Exportação de resultados para arquivos CSV atualizados.

### Tecnologias utilizadas

**Python 3 | Pandas | CSV | CLI**

### Conhecimentos desenvolvidos

Manipulação de DataFrames, filtros condicionais, processamento de dados tabulares, operações vetorizadas e automação de análises.

---

## 🎮 2. Infinite Play — API RESTful com Flask

**Diretório:** `Flask_Games_API`

Aplicação Back-end desenvolvida em Python utilizando o framework Flask para gerenciar um catálogo de jogos digitais.

O sistema disponibiliza endpoints HTTP que permitem consultar, cadastrar, atualizar e remover jogos, implementando as quatro operações fundamentais de um CRUD.

### Principais funcionalidades

- Desenvolvimento de API REST utilizando Flask.
- Listagem completa dos jogos cadastrados.
- Consulta individual de jogos por identificador (ID).
- Cadastro de novos jogos por requisições HTTP.
- Atualização de informações de jogos existentes.
- Exclusão de jogos cadastrados.
- Respostas estruturadas em formato JSON.
- Persistência local dos dados no arquivo `catalogo.json`.
- Criação automática de um catálogo inicial caso o arquivo não exista.
- Retorno de códigos HTTP conforme o resultado das operações.

### Endpoints da API

| Método | Endpoint | Funcionalidade |
|---|---|---|
| GET | `/api/jogos` | Listar todos os jogos |
| GET | `/api/jogos/1` | Consultar jogo por ID |
| POST | `/api/jogos` | Cadastrar novo jogo |
| PUT | `/api/jogos/1` | Atualizar jogo existente |
| DELETE | `/api/jogos/1` | Remover jogo do catálogo |

### Exemplo de requisição POST

```json
{
  "titulo": "Minecraft",
  "genero": "Aventura",
  "preco": 99.90,
  "avaliacao": 4.9
}
```

O sistema atribui um identificador ao novo jogo e registra as informações no catálogo.

### Tecnologias utilizadas

**Python 3 | Flask | JSON | HTTP | API REST**

### Conhecimentos desenvolvidos

Desenvolvimento Back-end, criação de endpoints, manipulação de requisições HTTP, operações CRUD, serialização JSON e persistência de dados em arquivos.

---

## 📗 3. Integração com Google Sheets

**Diretório:** `integracao_google_sheets`

Projeto dedicado ao estudo da comunicação entre aplicações Python e planilhas do Google Sheets.

A proposta é explorar a integração de dados entre sistemas externos e planilhas online, permitindo desenvolver soluções de automação e gerenciamento de informações.

### Objetivos do projeto

- Explorar a integração entre Python e Google Sheets.
- Compreender a comunicação com serviços externos.
- Trabalhar com dados organizados em planilhas.
- Estudar possibilidades de leitura, escrita e atualização automatizada de informações.
- Desenvolver conhecimentos sobre autenticação e consumo de APIs.

### Tecnologias relacionadas

**Python 3 | Google Sheets | Integração de APIs**

### Conhecimentos abordados

Integração de sistemas, comunicação com serviços externos, manipulação de dados em planilhas e automação de processos.

*As funcionalidades específicas e as dependências deste projeto devem ser consultadas diretamente em seus arquivos.*

---

## 💻 Como Executar os Projetos Localmente

### 1. Pré-requisitos

Certifique-se de possuir:

- Python 3 instalado.
- Git instalado.
- Um editor de código, como Visual Studio Code.
- Terminal ou PowerShell para executar os comandos.

### 2. Clonar o repositório

```bash
git clone https://github.com/Rafael-Santos-Tech/Python-mini-projetos.git
```

Acesse o diretório:

```bash
cd Python-mini-projetos
```

### 3. Executar o Analisador de Dados

Acesse a pasta:

```bash
cd analisador_de-dados
```

Instale a dependência:

```bash
python -m pip install pandas
```

Execute o arquivo Python principal do projeto, mantendo os arquivos CSV necessários no local esperado pelo código.

### 4. Executar a API REST

A partir da raiz do repositório:

```bash
cd Flask_Games_API
```

Instale o Flask:

```bash
python -m pip install flask
```

Se o arquivo principal estiver nomeado `app.py`, execute:

```bash
python app.py
```

Com o servidor iniciado na configuração padrão, a API poderá ser acessada em:

```text
http://127.0.0.1:5000/api/jogos
```

As requisições podem ser testadas utilizando Thunder Client, Postman ou PowerShell.

### 5. Executar a Integração com Google Sheets

Acesse a pasta:

```bash
cd integracao_google_sheets
```

Instale as dependências indicadas no código ou no arquivo `requirements.txt`, caso esteja disponível.

Configure as credenciais e permissões exigidas pela integração utilizada e execute o arquivo Python principal.

**Importante:** credenciais, tokens de acesso e chaves privadas não devem ser publicados no GitHub.

---

## 🎯 Objetivos do Portfólio

Este repositório foi criado para consolidar conhecimentos adquiridos durante os estudos em Análise e Desenvolvimento de Sistemas (ADS).

Os projetos permitem desenvolver competências em programação Python, resolução de problemas, tratamento de dados, desenvolvimento de aplicações Back-end e integração entre diferentes tecnologias.

O portfólio está em constante evolução, com foco no aprimoramento das funcionalidades, organização do código e aplicação de boas práticas de desenvolvimento.

---

## 👨‍💻 Desenvolvedor

**Rafael dos Santos Ferreira Lima**

Estudante de Análise e Desenvolvimento de Sistemas (ADS), com interesse em desenvolvimento de software, programação Python, Back-end, análise de dados e integração de sistemas.

**GitHub:** [Rafael-Santos-Tech](https://github.com/Rafael-Santos-Tech)

---

⭐ Se este repositório foi útil ou interessante, considere deixar uma estrela!

*Desenvolvido para fins educacionais e aprimoramento prático em programação.*
