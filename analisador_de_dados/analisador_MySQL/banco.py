from getpass import getpass

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

def criar_engine():
    url = URL.create(
        drivername="mysql+pymysql",
        username="root",
        password=getpass("Senha do MySQL: "),
        host="localhost",
        port=3306,
        database="analise_vendas",
        query={"charset": "utf8mb4"},
    )

    return create_engine(url, pool_pre_ping=True)

def consultar_produtos(
    engine, produto_id=None, preco_minimo=None, preco_maximo=None
):

    consulta = text("""
        SELECT
            id,
            produto,
            preco,
            quantidade,
            vendas_mes,
            preco * vendas_mes AS faturamento,
            CASE
                WHEN vendas_mes = 0
                THEN 'Sem vendas'

                WHEN preco > 300 AND vendas_mes < 10
                THEN 'Caro/Baixa saída'
                ELSE 'Normal'
            END AS Status
        FROM produtos
        WHERE (:produto_id IS NULL OR id = :produto_id)
        AND (:minimo IS NULL OR preco > :minimo)
        AND (:maximo IS NULL OR preco < :maximo)
        ORDER BY id
    """)

    parametros = {
        "produto_id": produto_id,
        "minimo": preco_minimo,
        "maximo": preco_maximo,
    }
 
    with engine.connect() as conexao:
        return pd.read_sql_query(
            consulta, 
            conexao,
            params=parametros,
            )

def atualizar_produto(
    engine, produto_id, campo, valor
):
    campos_permitidos = {
        "produto",
        "preco",
        "quantidade",
        "vendas_mes",
    }

    if campo not in campos_permitidos:
        raise ValueError("Campo inválido para atualização.")

    comando = text(
        f"UPDATE produtos SET {campo} = :valor "
        "WHERE id = :produto_id"
    )

    parametros = {
        "produto_id": produto_id,
        "valor": valor,
    }

    with engine.begin() as conexao:
        resultado = conexao.execute(comando, parametros)
        return resultado.rowcount

def excluir_produto(engine, produto_id):
    comando = text("""
        DELETE FROM produtos
        WHERE id = :produto_id
    """)

    with engine.begin() as conexao:
        resultado = conexao.execute(
            comando, 
            {"produto_id": produto_id},
        )
        return resultado.rowcount

def adicionar_produto(
        engine, produto, preco, quantidade, vendas_mes
):
    comando = text("""
        INSERT INTO produtos (
            produto,
            preco,
            quantidade,
            vendas_mes
        )
        VALUES (
            :produto,
            :preco,
            :quantidade,
            :vendas_mes
        )
    """)

    parametros = {
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade,
        "vendas_mes": vendas_mes,
    }

    with engine.begin() as conexao:
        resultado = conexao.execute(comando, parametros)
        return resultado.lastrowid
    