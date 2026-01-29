import pandas as pd
from sqlalchemy import create_engine

# Configurações do banco PostgreSQL
DB_USER = "ricardo"
DB_PASSWORD = "Ric2026$"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "python_projeto"

# Nome da tabela de origem (bronze) e destino (silver)
TABLE_ORIGEM = "ecommerce_data"
TABLE_DESTINO = "ecommerce_data_silver"

def executar_refino():
    # 1. Conectar ao banco
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    # 2. Ler dados da tabela bronze
    df = pd.read_sql_table(TABLE_ORIGEM, engine)

    # 3. Aplicar schema enforcement
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df["StockCode"] = df["StockCode"].astype(str)
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0).astype(int)
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce").fillna(0.0).astype(float)

    # 4. Remover duplicados
    df = df.drop_duplicates()

    # 5. Tratar nulos (já feito com fillna acima, mas pode reforçar)
    df = df.fillna({"Quantity": 0, "UnitPrice": 0.0})

    # 6. Filtrar valores negativos
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    # 7. Salvar na tabela silver
    df.to_sql(TABLE_DESTINO, engine, if_exists="replace", index=False)

    print(f"✅ Dados refinados gravados na tabela '{TABLE_DESTINO}'.")

if __name__ == "__main__":
    executar_refino()