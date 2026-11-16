from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

def reais(valor, pos=None):
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "_").replace(".", ",").replace("_", ".")

def gerar_dashboard(dados, pasta_saida):
    if dados.empty:
        print("Não há dados para gerar o dashboard.")
        return

    df = dados.copy()
    df["faturamento"] = df["preco"] * df["vendas_mes"]

    faturamento_total = df["faturamento"].sum()
    vendas_totais = df["vendas_mes"].sum()

    plt.style.use("ggplot")

    fig, eixos = plt.subplots(
        2, 2, figsize=(13, 8), layout="constrained"
    )

    fig.suptitle(
        "Dashboard de produtos\n"
        f"Faturamento: {reais(faturamento_total)} | "
        f"Unidades vendidas {vendas_totais:.0f}",
        fontsize=15,
    )

    ranking = df.sort_values("faturamento")

    ax = eixos[0, 0]

    barras = ax.barh(
        ranking["produto"], ranking["faturamento"], color="#2563eb"
    )

    ax.set_title("Faturamento mensal por produto")
    ax.set_xlabel("faturamento (R$)")

    ax.xaxis.set_major_formatter(FuncFormatter(reais))

    ax.bar_label(
        barras,
        labels=[reais(valor) for valor in ranking["faturamento"]],
        padding=3,
        fontsize=9,
    )

    ax.margins(x=0.35)

    ax = eixos[0, 1]

    barras = ax.bar(
        df["produto"], df["vendas_mes"], color="#16a34a"
    )

    ax.set_title("Vendas do mês por produto")
    ax.set_ylabel("Unidades vendidas")
    ax.bar_label(barras, padding=3)
    ax.margins(y=0.15)

    ax = eixos [1, 0]

    barras = ax.bar(
        df["produto"], df["quantidade"], color="#f59e0b"
    )

    ax.set_title("Quantidade por produto")
    ax.set_ylabel("Unidades")
    ax.bar_label(barras, padding=3)
    ax.margins(y=0.15)

    contagem = df["Status"].value_counts().reindex(
        ["Normal", "Caro/Baixa saída", "Sem vendas"],
        fill_value=0,
    )

    ax = eixos[1, 1]

    ax.pie(
        contagem, 
        labels=contagem.index,
        autopct="%1.0f%%",
        colors=["#16a34a", "#ef4444", "#2563eb"],
        startangle=90,
    )

    ax.set_title("Classificação dos produtos")

    caminho_png = Path(pasta_saida) / "dashboard.png"

    fig.savefig(caminho_png, dpi=150)

    print(f"Dashboard salvo em: {caminho_png}")

    plt.show()

    plt.close(fig)

    return caminho_png