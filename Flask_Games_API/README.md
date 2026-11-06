# 🎮 Infinite Play | API RESTful com Python e Flask

## 📌 Sobre o Projeto

O **Infinite Play** é uma API RESTful desenvolvida em **Python**, utilizando o framework **Flask**, com o objetivo de gerenciar um catálogo de jogos digitais.

A aplicação implementa as quatro operações fundamentais de um sistema CRUD (*Create, Read, Update e Delete*), permitindo cadastrar, consultar, atualizar e remover jogos por meio de requisições HTTP.

O projeto utiliza arquivos JSON para persistência de dados, garantindo que as informações cadastradas sejam mantidas mesmo após o encerramento e a reinicialização do servidor.

O principal objetivo é aplicar conhecimentos de **desenvolvimento Back-end, arquitetura REST, manipulação de dados JSON, métodos HTTP e persistência de informações**, simulando o funcionamento de um sistema de gerenciamento de catálogo de jogos.

---

## 🚀 Funcionalidades

A API disponibiliza funcionalidades para gerenciamento completo de um catálogo de jogos digitais.

### 📋 1. Listagem de Jogos

Permite consultar todos os jogos cadastrados no sistema por meio de uma requisição `GET`.

Cada jogo possui as seguintes informações:

- **ID:** identificador numérico do jogo.
- **Título:** nome do jogo.
- **Gênero:** categoria do jogo.
- **Preço:** valor comercial do jogo.
- **Avaliação:** nota atribuída ao jogo.

### 🔎 2. Consulta por ID

Permite localizar um jogo específico utilizando seu identificador.

Caso o ID informado não exista, a API retorna uma mensagem de erro acompanhada do código HTTP `404 Not Found`.

### ➕ 3. Cadastro de Jogos

Permite cadastrar novos jogos por meio de requisições `POST`, enviando as informações em formato JSON.

O sistema gera automaticamente um identificador para o novo registro e atualiza o arquivo de armazenamento.

### ✏️ 4. Atualização de Jogos

Permite modificar informações de jogos existentes utilizando o método `PUT`.

Os campos podem ser atualizados individualmente, preservando os valores anteriores dos atributos que não forem enviados na requisição.

### 🗑️ 5. Exclusão de Jogos

Permite remover jogos cadastrados utilizando o método `DELETE`.

Após a exclusão, o arquivo JSON é atualizado para refletir as alterações realizadas.

### 💾 6. Persistência de Dados

O sistema utiliza o arquivo `catalogo.json` como mecanismo de armazenamento local.

- Carrega automaticamente os dados ao iniciar o servidor.
- Cria um catálogo inicial caso o arquivo não exista.
- Salva alterações após cadastros, atualizações e exclusões.
- Mantém os dados entre diferentes execuções da aplicação.

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

**Python 3:** linguagem principal utilizada no desenvolvimento da API.

**Flask:** framework responsável pela criação do servidor e gerenciamento das rotas HTTP.

**JSON:** formato utilizado para comunicação entre cliente e servidor e armazenamento dos dados.

**Biblioteca OS:** utilizada para verificar a existência do arquivo de armazenamento.

**HTTP:** protocolo utilizado para realizar as operações de consulta e gerenciamento de registros.

---

## 📁 Estrutura do Projeto

```text
Flask_Games_API/
│
├── app.py
│   └── Código principal da API Flask
│
├── catalogo.json
│   └── Arquivo de armazenamento dos jogos
│
├── requirements.txt
│   └── Dependências do projeto
│
└── README.md
    └── Documentação da aplicação
```

**Observação:** a estrutura acima é uma organização recomendada. O arquivo `catalogo.json` é criado automaticamente na primeira execução, caso não exista. Os nomes dos demais arquivos devem corresponder aos utilizados no repositório.

---

## 🌐 Endpoints da API

A aplicação disponibiliza os seguintes endpoints:

| Método HTTP | Endpoint | Descrição |
|---|---|---|
| GET | `/api/jogos` | Lista todos os jogos |
| GET | `/api/jogos/{id}` | Consulta um jogo pelo ID |
| POST | `/api/jogos` | Cadastra um novo jogo |
| PUT | `/api/jogos/{id}` | Atualiza um jogo existente |
| DELETE | `/api/jogos/{id}` | Remove um jogo do catálogo |

**URL base local:**

```text
http://127.0.0.1:5000
```

---

## 📡 Exemplos de Requisições e Respostas

### 1. GET — Listar todos os jogos

**Requisição:**

```http
GET /api/jogos
```

**Exemplo de resposta:**

```json
[
    {
        "id": 1,
        "titulo": "Minecraft",
        "genero": "Aventura",
        "preco": 99.90,
        "avaliacao": 4.9
    },
    {
        "id": 2,
        "titulo": "Hollow Knight",
        "genero": "Aventura",
        "preco": 39.99,
        "avaliacao": 4.9
    }
]
```

**Código HTTP:** `200 OK`

A resposta contém todos os registros presentes no catálogo.

### 2. GET — Consultar jogo por ID

**Requisição:**

```http
GET /api/jogos/1
```

**Resposta esperada após a correção do retorno JSON:**

```json
{
    "id": 1,
    "titulo": "Minecraft",
    "genero": "Aventura",
    "preco": 99.90,
    "avaliacao": 4.9
}
```

**Código HTTP:** `200 OK`

Caso o jogo não exista:

```json
{
    "erro": "Jogo não encontrado no sistema"
}
```

**Código HTTP:** `404 Not Found`

### 3. POST — Cadastrar novo jogo

**Requisição:**

```http
POST /api/jogos
Content-Type: application/json
```

**Corpo da requisição:**

```json
{
    "titulo": "Stardew Valley",
    "genero": "Simulação",
    "preco": 24.99,
    "avaliacao": 4.9
}
```

**Exemplo de resposta:**

```json
{
    "id": 16,
    "titulo": "Stardew Valley",
    "genero": "Simulação",
    "preco": 24.99,
    "avaliacao": 4.9
}
```

**Código HTTP:** `201 Created`

O ID `16` é ilustrativo e considera que o catálogo inicial contém 15 jogos.

### 4. PUT — Atualizar informações de um jogo

**Requisição:**

```http
PUT /api/jogos/1
Content-Type: application/json
```

**Corpo da requisição:**

```json
{
    "preco": 79.90,
    "avaliacao": 5.0
}
```

**Exemplo de resposta:**

```json
{
    "mensagem": "Jogo atualizado com sucesso!",
    "jogo": {
        "id": 1,
        "titulo": "Minecraft",
        "genero": "Aventura",
        "preco": 79.90,
        "avaliacao": 5.0
    }
}
```

**Código HTTP:** `200 OK`

Os atributos não informados permanecem com seus valores anteriores.

### 5. DELETE — Excluir jogo

**Requisição:**

```http
DELETE /api/jogos/1
```

**Exemplo de resposta:**

```json
{
    "mensagem": "O jogo 'Minecraft' foi removido com sucesso!"
}
```

**Código HTTP:** `200 OK`

Após a operação, o jogo é removido do catálogo e o arquivo JSON é atualizado.

---

## 💻 Instalação e Execução

### 1. Pré-requisitos

Para executar o projeto, é necessário possuir:

- Python 3 instalado.
- Git instalado.
- Terminal ou PowerShell.
- Editor de código, como Visual Studio Code.
- Uma ferramenta de testes HTTP, como Postman ou Thunder Client (opcional).

### 2. Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/Rafael-Santos-Tech/Python-mini-projetos.git
```

Acesse a pasta da API:

```bash
cd Python-mini-projetos/Flask_Games_API
```

### 3. Criar um ambiente virtual (recomendado)

```bash
python -m venv .venv
```

No Windows PowerShell, ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
python -m pip install flask
```

Caso o projeto possua um arquivo `requirements.txt`, também é possível instalar as dependências utilizando:

```bash
python -m pip install -r requirements.txt
```

### 5. Executar a API

Execute o arquivo principal:

```bash
python app.py
```

Se o arquivo principal possuir outro nome, substitua `app.py` pelo nome correspondente.

Após iniciar o servidor, a aplicação estará disponível, na configuração padrão, em:

```text
http://127.0.0.1:5000
```

Para visualizar o catálogo, acesse:

```text
http://127.0.0.1:5000/api/jogos
```

**Importante:** o servidor de desenvolvimento do Flask deve ser utilizado apenas em ambientes locais de desenvolvimento e testes.

---

## 🧪 Como Testar a API

As requisições podem ser realizadas utilizando ferramentas como **Postman, Thunder Client ou PowerShell**.

### Exemplo utilizando PowerShell

Listar os jogos:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/jogos" -Method GET
```

Cadastrar um jogo:

```powershell
$dados = @{
    titulo = "Celeste"
    genero = "Plataforma"
    preco = 36.99
    avaliacao = 4.9
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/api/jogos" `
    -Method POST `
    -ContentType "application/json" `
    -Body $dados
```

A API retornará os dados do jogo cadastrado, incluindo o identificador gerado automaticamente.

---

## 🗂️ Armazenamento de Dados

A aplicação utiliza um arquivo JSON como alternativa simples a um banco de dados tradicional.

O processo de persistência funciona da seguinte maneira:

1. O servidor verifica se o arquivo `catalogo.json` existe.
2. Caso exista, os dados são carregados para a memória.
3. Caso não exista, um catálogo inicial é criado.
4. As requisições modificam os registros armazenados em memória.
5. Após operações de escrita, os dados são salvos no arquivo JSON.

Essa abordagem é adequada para fins educacionais e aplicações locais de pequeno porte.

Para sistemas maiores, recomenda-se utilizar bancos de dados como SQLite, PostgreSQL ou MySQL.

---

## 🧠 Conceitos Aplicados

Durante o desenvolvimento da aplicação, foram trabalhados conceitos como:

- Desenvolvimento Back-end com Python.
- Criação de servidores utilizando Flask.
- Arquitetura de APIs RESTful.
- Operações CRUD.
- Métodos HTTP: GET, POST, PUT e DELETE.
- Manipulação e serialização de arquivos JSON.
- Estruturas condicionais e de repetição.
- Funções e organização de código.
- Persistência de dados.
- Códigos de status HTTP.
- Comunicação entre cliente e servidor.
- Testes de endpoints.

---

## 🔮 Possíveis Melhorias Futuras

O projeto poderá evoluir com a implementação de novas funcionalidades:

- Validação dos dados enviados nas requisições.
- Tratamento de erros e exceções.
- Integração com banco de dados SQL.
- Autenticação e autorização de usuários.
- Sistema de busca por título e gênero.
- Filtros por preço e avaliação.
- Paginação dos resultados.
- Documentação interativa com Swagger/OpenAPI.
- Testes automatizados utilizando Pytest.
- Organização do código em módulos e Blueprints.
- Implantação da API em serviços de hospedagem.

---

## ⚠️ Limitações da Versão Atual

O projeto foi desenvolvido para fins educacionais e apresenta algumas limitações:

- O armazenamento utiliza um arquivo JSON local.
- Não possui autenticação de usuários.
- Ainda não implementa validação completa dos dados recebidos.
- Não possui mecanismos de controle de acesso concorrente ao arquivo.
- A geração de IDs considera o último registro da lista, podendo produzir identificadores repetidos em determinadas situações após exclusões.
- A consulta individual precisa retornar diretamente o dicionário do jogo por meio de `jsonify(jogo)`.

Esses pontos representam oportunidades de aprimoramento em futuras versões.

---

## 🎯 Objetivo Educacional

Este projeto foi desenvolvido para consolidar conhecimentos adquiridos durante os estudos em **Análise e Desenvolvimento de Sistemas (ADS)**.

A aplicação demonstra como construir uma API RESTful utilizando Python e Flask, compreender o funcionamento das requisições HTTP e implementar operações de gerenciamento de informações com persistência de dados.

Além disso, contribui para o desenvolvimento de habilidades relacionadas à lógica de programação, organização de sistemas Back-end e integração entre aplicações.

---

## 👨‍💻 Desenvolvedor

**Rafael dos Santos Ferreira Lima**

Estudante de **Análise e Desenvolvimento de Sistemas (ADS)**, com interesse em desenvolvimento Back-end, Python, APIs RESTful, bancos de dados e engenharia de software.

**GitHub:** [Rafael-Santos-Tech](https://github.com/Rafael-Santos-Tech)

**Repositório:** [Python-mini-projetos](https://github.com/Rafael-Santos-Tech/Python-mini-projetos)

---

⭐ Se este projeto foi útil ou interessante, considere deixar uma estrela no repositório!

*Desenvolvido para fins educacionais e aprimoramento prático em desenvolvimento Back-end com Python.*