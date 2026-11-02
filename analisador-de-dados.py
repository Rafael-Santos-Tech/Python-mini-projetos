import pandas as pd

df = pd.read_csv('dados.csv')

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
        df.to_csv('dados_atualizados.csv', index=False)
        print("\nArquivo 'dados_atualizados.csv' criado com sucesso na pasta do projeto!")

        print("\n--- Exibindo o Novo Arquivo ---")      
        df_novo_arquivo = pd.read_csv('dados_atualizados.csv')
        print(df_novo_arquivo)

    elif opcao == '0':
        print("\nEncerrando o programa. Até logo! 🚀")
        break

    else: 
        print("\n❌ Opção inválida! Por favor, digite um número correspondente ao menu.")