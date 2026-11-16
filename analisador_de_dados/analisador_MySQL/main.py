from decimal import Decimal, InvalidOperation
from pathlib import Path

from sqlalchemy.exc import SQLAlchemyError

from banco import (
    criar_engine,
    consultar_produtos,
    atualizar_produto,
    excluir_produto,
    adicionar_produto
)
from dashboard import gerar_dashboard

from pandas.errors import DatabaseError

def ler_inteiro(mensagem, minimo=0):
    valor = int(input(mensagem))

    if valor < minimo:
        raise ValueError(
            f"Informe um inteiro maior ou igual a {minimo}."
        )

    return valor

def ler_preco():
    texto = input(
        "Novo preço, sem separador de milhar (ex.: 150,50): "
    ).strip()

    valor = Decimal(texto.replace(",", "."))

    if not valor.is_finite() or valor < 0:
        raise ValueError(
            "O preço precisa ser um número não negativo."
        )

    return valor

def main():
    pasta_projeto = Path(__file__).resolve().parent
    engine = criar_engine()

    try:
        while True:
            print("""
                1 - Visão geral e estatísticas
                2 - Produtos acima de R$ 300
                3 - Produtos abaixo de R$ 300
                4 - Análise de desempenho
                5 - Dashboard
                6 - Atualizar produto
                7 - Excluir produto
                8 - Adicionar produto
                0 - Sair
            """)

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "0":
                break

            try:
                if opcao in {"1", "2", "3", "4", "5"}:

                    df = consultar_produtos(
                        engine, 
                        preco_minimo=300 if opcao == "2" else None,
                        preco_maximo=300 if opcao == "3" else None,
                    )

                    if df.empty:
                        print("Nenhum produto encontrado.")
                        continue

                    elif opcao == "1":
                        print(df.to_string(index=False))
                        df.info()
                        print(df.describe())

                    elif opcao in {"2", "3"}:
                        print(df.to_string(index=False))

                    elif opcao == "4":
                        print(
                            df[
                                ["produto", "faturamento", "Status"]
                            ].to_string(index=False)
                        )

                    elif opcao == "5":
                        gerar_dashboard(df, pasta_projeto)

                elif opcao in {"6", "7"}:
                    produto_id = ler_inteiro(
                        "ID do produto: ",
                        minimo=1,
                    )

                    atual = consultar_produtos(
                        engine, 
                        produto_id=produto_id,
                    )

                    if atual.empty:
                        print("Produto não encontrado.")
                        continue

                    print(atual.to_string(index=False))

                    if opcao == "6":
                        print("""
                            Qual campo deseja alterar?

                            1 - Nome do produto
                            2 - Preço
                            3 - Quantidade
                            4 - Vendas do mês
                            0 - Cancelar
                        """)

                        escolha = input("Escolha uma opção: ").strip()

                        if escolha == "0":
                            print("Atualização cancelada.")
                            continue

                        if escolha == "1":
                            campo = "produto"
                            valor = input("Novo nome do produto: ").strip()

                            if not valor:
                                raise ValueError(
                                    "O nome não pode ficar vazio."
                                )

                        elif escolha == "2":
                            campo = "preco"
                            valor = ler_preco()

                        elif escolha == "3":
                            campo = "quantidade"
                            valor = ler_inteiro("Nova quantidade: ")

                        elif escolha == "4":
                            campo = "vendas_mes"
                            valor = ler_inteiro("Novas vendas do mês: ")

                        else:
                            print("Campo inválido.")
                            continue

                        linhas = atualizar_produto(
                            engine,
                            produto_id,
                            campo,
                            valor,
                        )

                        print(
                            "Produto atualizado."
                            if linhas
                            else "Produto não encontrado."
                        )

                    else:
                        confirmacao = input(
                            "Excluir este produto? Digite SIM: "
                        ).strip().upper()

                        if confirmacao == "SIM":
                            linhas = excluir_produto(
                                engine, 
                                produto_id,
                            )

                            print(
                                "Produto excluído."
                                if linhas
                                else "Produto não encontrado."
                            )

                        else:
                            print("Exclusão cancelada.")

                elif opcao == "8":
                    nome = input("Nome do produto: ").strip()

                    if not nome:
                        raise ValueError("O nome não pode ficar vazio.")

                    preco = ler_preco()
                    quantidade = ler_inteiro("Quantidade: ")
                    vendas = ler_inteiro(
                        "Vendas do mês (0 se ainda não vendeu): "
                    )

                    novo_id = adicionar_produto(
                        engine,
                        nome,
                        preco,
                        quantidade,
                        vendas,
                    )

                    print(
                        f"Produto cadastrado com sucesso! ID: {novo_id}"
                    )

                else:
                    print("Opção inválida.")

            except (ValueError, InvalidOperation) as erro:
                print(f"Entrada inválida: {erro}")

            except (SQLAlchemyError, DatabaseError) as erro:
                print(f"Erro no banco: {erro}")

    finally: 
        engine.dispose()

if __name__ == "__main__":
    main()