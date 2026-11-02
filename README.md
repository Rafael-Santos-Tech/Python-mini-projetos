# 🚀 Portfólio Python: Análise de Dados & API REST

Este repositório reúne projetos práticos desenvolvidos em Python, com foco em manipulação estruturada de dados e desenvolvimento de aplicações Back-end (APIs RESTful). O objetivo é demonstrar a aplicação de lógica de programação, processamento de arquivos e persistência de dados.

## 📁 Estrutura do Repositório

O repositório está dividido em dois projetos centrais e independentes:

### 1. 📊 Analisador de Dados via CLI (Pandas)
Um sistema interativo de terminal projetado para leitura, processamento e exportação de métricas a partir de arquivos CSV.
* **Tecnologias:** Python 3, biblioteca `pandas`.
* **Principais Funcionalidades:**
  * Menu interativo de navegação no terminal via CLI.
  * Cálculos de faturamento utilizando o método vetorizado de alta performance do Pandas.
  * Lógica condicional para classificar e sinalizar o desempenho de vendas dos produtos.
  * Exportação automatizada dos dados limpos e atualizados para novos arquivos CSV.

### 2. 🎮 API RESTful - Infinite Play (Flask)
Back-end completo para o gerenciamento do catálogo de jogos da loja Infinite Play.
* **Tecnologias:** Python 3, `Flask`, manipulação nativa de JSON.
* **Principais Funcionalidades:**
  * **Arquitetura REST:** Rotas unificadas executando ações específicas através de verbos HTTP (`GET`, `POST`, `PUT`, `DELETE`).
  * **Operações CRUD Completas:** Sistema preparado para cadastrar, listar, buscar por ID, atualizar e remover jogos.
  * **Persistência de Dados:** O catálogo é salvo dinamicamente no arquivo físico `catalogo.json`, garantindo a integridade e retenção dos dados sempre que o servidor reinicia.

---

## 💻 Como Executar na Sua Máquina

Para rodar qualquer um dos projetos localmente, certifique-se de ter o Python instalado.

**Clonando o repositório:**
```bash
git clone https://github.com/Rafael-Santos-Tech/Python-mini-projetos.git
````

1. Navegue até a pasta do projeto de dados.
2. Instale a biblioteca Pandas:
```bash
pip install pandas
```

3. Navegue até a pasta da API.
4.Instale o framework Flask:
```bash
pip install flask
```

5. A API estará rodando localmente em 'http://127.0.0.1:5000'. Você pode testar as rotas utilizando softwares como **Thunder Client**, **Postman** ou o próprio **PowerShell**.

*Desenvolvido por **Rafael Dos Santos Ferreira Lima** - Estudante de Análise e Desenvolvimento de Sistemas (ADS).*
