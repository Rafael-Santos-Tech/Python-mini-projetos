import pandas as pd
from pathlib import Path

pasta_projeto = Path(__file__).resolve().parent

caminho_csv = pasta_projeto / "dados.csv"

if not caminho_csv.exists():
    print(f"Arquivo não encontrado: {caminho_csv}")
    exit()

df = pd.read_csv(caminho_csv)

while True: 
    print("\n" + "=" * 50)
    print("📊 MENU DO ANALISADOR DE DADOS")
    print("=" * 50)
    print("1 - Ver visão Geral, Estrutura e Estatísticas")
    print("2 - Filtrar Produtos acima de R$300")
    print("3 - Filtrar Produtos abaixo de R$300")
    print("4 - Gerar Análise de Desempenho e Atualizar Tabela")
    print("0 - Sair do Programa")
    print("=" * 50)

    opcao = input("Escolha uma opção (0 a 4): ")

    if opcao == '1':
        print("--- Visão Geral ---")
        print(df.head())

        print("\n--- Estrutura do Arquivo ---")
        df.info()

        print("\n--- Estatísticas Automáticas ---")
        print(df.describe())

    elif opcao == '2': 
        print("\n--- Produtos custando mais de R$ 300 ---")
        for indice, linha in df.iterrows():
            if linha['preco'] > 300:
                print(f"Produto: [{linha['produto']}] | Preço: [{linha['preco']}]")

    elif opcao == '3': 
        print("\n--- Produtos custando menos de R$ 300 ---")
        for indice, linha in df.iterrows():
            if linha['preco'] < 300:
                print(f"Produto: [{linha['produto']}] | Preço: [{linha['preco']}]")

    elif opcao == '4': 
        df['faturamento'] = df['preco'] * df['vendas_mes']

        print("\n--- Análise de Desempenho de Produtos e Atualização da Tabela com Nova Coluna ---")
        for indice, linha in df.iterrows():
            if linha['preco'] > 200 and linha['vendas_mes'] < 10:
                print(f"Produto: {linha['produto']} R$ [{linha['preco']}] | {linha['vendas_mes']} vendas -> Alerta: Caro e com pouca saída")
                df.loc[indice, 'Status'] = 'Caro/Baixa saída'
            else:
                print(f"Produto: {linha['produto']} R$ [{linha['preco']}] | {linha['vendas_mes']} vendas -> Alerta: Vendas normais")
                df.loc[indice, 'Status'] = 'Normal'

        print("\n--- Salvando Tabela Atualizada ---")
        caminho_atualizado = pasta_projeto / "dados_atualizados.csv"
        df.to_csv(caminho_atualizado, index=False)
        print("\nArquivo 'dados_atualizados.csv' criado com sucesso na pasta do projeto!")

        print("\n--- Exibindo o Novo Arquivo ---")      
        df_novo_arquivo = pd.read_csv(caminho_atualizado)
        print(df_novo_arquivo)

    elif opcao == '0':
        print("\nEncerrando o programa. Até logo! 🚀")
        break

    else: 
        print("\n❌ Opção inválida! Por favor, digite um número correspondente ao menu.")