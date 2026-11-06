# Sistema de Vendas em Python + Google Sheets

Projeto acadêmico de **CRUD (Create, Read, Update, Delete)** com interface de terminal, usando Python, [gspread](https://docs.gspread.org/) e a API do Google Sheets. Os registros são armazenados em uma planilha online.

## Funcionalidades

- **Cadastrar** uma venda: produto, quantidade e preço unitário.
- **Consultar** vendas e visualizar faturamento total.
- **Atualizar** registros pelo ID.
- **Excluir** registros pelo ID, com confirmação.
- Menu interativo com validações básicas de entrada.

## Estrutura

```text
integracao_google_sheets/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

Os arquivos locais `credentials.json` e `authorized_user.json` e o diretório `.venv/` **não fazem parte do repositório**.

## Requisitos

- Python 3.10+.
- Uma conta Google e uma planilha Google Sheets própria.
- Projeto no Google Cloud com **Google Sheets API** e **Google Drive API** habilitadas.
- Cliente OAuth 2.0 do tipo **Aplicativo para computador** configurado em seu projeto. Se o aplicativo estiver no modo de teste, cadastre sua conta em **Usuários de teste**.

## Como executar localmente

1. Clone o repositório e abra a pasta do projeto.
2. Crie e ative o ambiente virtual no Windows:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   Se o PowerShell bloquear a ativação, você pode executar os comandos com `.\.venv\Scripts\python.exe` sem ativar o ambiente.
3. Instale as dependências:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Baixe **suas próprias credenciais OAuth de aplicativo para computador** do Google Cloud e salve-as localmente como `credentials.json` ao lado de `main.py`. **Nunca envie esse arquivo ao GitHub.**
5. Crie uma planilha com a primeira linha contendo exatamente:

   ```text
   ID | Produto | Quantidade | Valor Unitário | Total
   ```

6. No PowerShell, defina a variável de ambiente com o link de sua própria planilha (só ficará definida nesta sessão do terminal):

   ```powershell
   $env:GOOGLE_SHEETS_URL = "COLE_AQUI_O_LINK_DA_SUA_PLANILHA"
   ```

   Substitua pelo link real no terminal; **não coloque esse link no código publicado**.
7. Execute:

   ```powershell
   python main.py
   ```

8. Na primeira execução, conclua a autorização no navegador. O arquivo `authorized_user.json` será gerado automaticamente e deve permanecer privado.

## Tecnologias

- Python
- gspread
- Google Sheets API e Google Drive API
- OAuth 2.0

## Cuidados e limitações

- Não publique arquivos de credenciais, tokens, ambiente virtual, capturas de tela com chaves ou dados privados da planilha.
- Este projeto foi pensado para uso educacional e **um usuário por vez**. Alterações simultâneas na planilha podem produzir conflitos.
- O ID da última venda pode ser reutilizado após sua exclusão, pois o próximo ID é calculado pelo maior ID existente.
- `float` é utilizado para simplificar o aprendizado; projetos financeiros reais devem considerar `decimal.Decimal`.
- A execução depende das permissões concedidas à conta autenticada.

## Segurança

O arquivo `.gitignore` impede o versionamento das credenciais quando ainda não estão rastreadas pelo Git. Antes de publicar, confira os arquivos com `git status` e `git diff --cached --name-only`. Se alguma credencial já foi enviada ao GitHub, revogue/rotacione o acesso: remover o arquivo em um commit novo não apaga o histórico.
