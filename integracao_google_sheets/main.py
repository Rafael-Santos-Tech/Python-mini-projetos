import os
import gspread
import math
from gspread.utils import ValueRenderOption

cliente = gspread.oauth(
    credentials_filename="credentials.json",
    authorized_user_filename="authorized_user.json"
)

url = os.getenv("GOOGLE_SHEETS_URL", "").strip()
if not url:
    raise SystemExit("Defina GOOGLE_SHEETS_URL no terminal com o link da sua planilha.")
planilha = cliente.open_by_url(url)
aba = planilha.sheet1

def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")

    return f"R$ {texto}"

def carregar_vendas():

    linha = aba.get(
        "A1:E",
        value_render_option=ValueRenderOption.unformatted
    )

    vendas = []

    for numero_linha, dados in enumerate(linha[1:], start=2):

        if len(dados) < 5:
            continue

        try:
            venda = {
                "linha": numero_linha,
                "id": int(dados[0]),
                "produto": str(dados[1]),
                "quantidade": int(dados[2]),
                "valor": float(dados[3]),
                "total": float(dados[4])
            }

            vendas.append(venda)

        except(ValueError, TypeError):
            continue

    return vendas

def cadastrar_vendas():

    print("\n--- Cadastro de Vendas ---")

    produto = input("Nome do Produto: ").strip()

    if not produto:
        print("Erro: o nome do produto não pode estar vazio!")
        return

    try: 
        quantidade = int(input("Quantidade: "))

        valor = float(
            input("Valor unitário: R$ ").replace(",", ".")
        )

    except ValueError:
        print("Erro: digite número válidos!")
        return

    if quantidade <= 0 or not math.isfinite(valor) or valor < 0:
        print("Erro: quantidade ou valor inválido!")
        return

    total = round(quantidade * valor, 2)

    if not math.isfinite(total):
        print("Erro: valor total inválido!")
        return

    vendas = carregar_vendas()

    proximo_id = max(
        (venda["id"] for venda in vendas),
        default=0
    ) + 1

    aba.append_row(
        [proximo_id, produto, quantidade, valor, total],
        value_input_option="RAW"
    ) 

    print(f"\nVenda cadastrada com sucesso!\nID:{proximo_id}\nProduto:{produto}\nQuantidade:{quantidade}\nValor unitário: {formatar_moeda(valor)}\nTotal: {formatar_moeda(total)}")

def consultar_vendas():

    print("--- Consultar Vendas ---")

    vendas = carregar_vendas()

    if not vendas:
        print("\nNenhuma venda cadastrada!")
        return

    print("-" * 78)

    print(
        f"{'ID':<5}"
        f"{'PRODUTO':<23}"
        f"{'QUANTIDADE':<8}"
        f"{'VALOR UNITÁRIO':<20}"
        f"{'TOTAL':<20}"
    )

    print("-" * 78)

    for venda in vendas:

        print(
            f"{venda['id']:<5}"
            f"{venda['produto'][:22]:<23}"
            f"{venda['quantidade']:<8}"
            f"{formatar_moeda(venda['valor']):<20}"
            f"{formatar_moeda(venda['total']):<20}"
        )

    print("-" * 78)

    total_geral = sum(
        venda["total"] for venda in vendas
    )

    print(f"\nTotal de vendas cadastradas: {len(vendas)}\nFaturamento total: {formatar_moeda(total_geral)}")


def buscar_venda():

    try:
        id_venda = int(input("Digite o ID da venda: "))

    except ValueError:
        print("\nErro: digite um ID válido!")
        return None

    vendas = carregar_vendas()

    for venda in vendas:

        if venda["id"] == id_venda:
            return venda

    print("\nVenda não encontrada!")
    return None

def atualizar_venda():

    print("--- Atualizar venda ---")

    venda = buscar_venda()

    if venda is None:
        return

    print(f"\nDados atuais:\nID: {venda['id']}\nProduto: {venda['produto']}\nQuantidade: {venda['quantidade']}\nValor: {formatar_moeda(venda['valor'])}\nTotal: {formatar_moeda(venda['total'])}\n\nPressione ENTER para manter um valor atual.")

    novo_produto = input("Novo produto: ").strip()

    if novo_produto:
        produto = novo_produto
    else:
        produto = venda["produto"]

    nova_quantidade = input("Nova quantidade: ").strip()

    if nova_quantidade:

        try:
            quantidade = int(nova_quantidade)

        except ValueError:
            print("\nErro: quantidade inválida!")
            return

    else:
        quantidade = venda["quantidade"]

    novo_valor = input("Novo valor unitário: R$ ").strip()

    if novo_valor:

        try:
            valor = float(novo_valor.replace(",", "."))

        except ValueError:
            print("\nErro: valor inválido!")
            return

    else:
        valor = venda["valor"]

    if quantidade <= 0 or not math.isfinite(valor) or valor < 0:
        print("\nErro: dados inválidos!")
        return

    total = round(quantidade * valor, 2)

    if not math.isfinite(total):
        print("\nErro: valor total inválido!")
        return

    linha = venda["linha"]

    aba.update(
        range_name = f"A{linha}:E{linha}",
        values=[[
            venda["id"],
            produto,
            quantidade,
            valor,
            total
        ]],
        value_input_option="RAW"
    )

    print(f"\nVenda atualizada com sucesso!\nID: {venda['id']}\nProduto: {produto}\nQuantidade: {quantidade}\nTotal: {formatar_moeda(total)}")

def excluir_venda():

    print("\n--- Excluir venda ---")

    venda = buscar_venda()

    if venda is None:
        return

    print(f"\nVenda encontrada:\nID: {venda['id']}\nProduto: {venda['produto']}\nQuantidade: {venda['quantidade']}\nValor: {formatar_moeda(venda['valor'])}\nTotal: {formatar_moeda(venda['total'])}")

    confirmar = input(
        "\nDeseja realmente excluir esta venda? (S/N): "
    ).strip().upper()

    if confirmar != "S":
        print("Exclusão cancelada!")
        return

    linha = venda["linha"]

    aba.delete_rows(linha)

    print("\nVenda excluída com sucesso!")

def exibir_menu():

    print("\n--- Sistema de Vendas ---\n\n1 - Cadastrar venda\n2 - Consultar vendas\n3 - Atualizar venda\n4 - Excluir venda\n5 - Sair")

def menu_principal():

    while True:

        exibir_menu()

        opcao = input("Escolha uma opção: ").strip()

        try:

            if opcao == "1":
                cadastrar_vendas()

            elif opcao == "2":
                consultar_vendas()

            elif opcao == "3":
                atualizar_venda()

            elif opcao == "4":
                excluir_venda()

            elif opcao == "5":
                print("\nSistema encerrado com sucesso!")
                break

            else:
                print("\nOpção inválida! Tente novamente.")

        except gspread.exceptions.APIError as erro:
            print("\nErro na comunicação com o Google Sheets!")
            print(erro)


if __name__ == "__main__":
    menu_principal()