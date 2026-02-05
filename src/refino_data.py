import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env localizado na raiz do projeto
load_dotenv()

# Configurações do banco PostgreSQL (agora protegidas)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Nome da tabela de origem (bronze) e destino (silver)
TABLE_ORIGEM = "ecommerce_data"
TABLE_DESTINO = "ecommerce_data_silver"

def executar_refino():
    # 1. Conectar ao banco usando f-string e as variáveis de ambiente
    connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)

    print(f"Iniciando refino: {TABLE_ORIGEM} -> {TABLE_DESTINO}...")

    # 2. Ler dados da tabela bronze
    df = pd.read_sql_table(TABLE_ORIGEM, engine)

    # 3. Aplicar schema enforcement (Essencial para seu portfólio de inventário)
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df["StockCode"] = df["StockCode"].astype(str)
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0).astype(int)
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce").fillna(0.0).astype(float)

    # 4. Remover duplicados
    df = df.drop_duplicates()

    # 5. Tratar nulos
    df = df.fillna({"Quantity": 0, "UnitPrice": 0.0})

    # 6. Filtrar valores negativos (Limpeza importante para análise de estoque)
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    # 7. Salvar na tabela silver
    df.to_sql(TABLE_DESTINO, engine, if_exists="replace", index=False)

    print(f"Dados refinados com sucesso! Conexão encerrada com segurança.")

if __name__ == "__main__":
    executar_refino()