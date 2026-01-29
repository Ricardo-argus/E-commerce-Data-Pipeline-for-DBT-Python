import pandas as pd
from sqlalchemy import create_engine

DB_USER = "ricardo"
DB_PASSWORD = "Ric2026$"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "python_projeto"

CSV_PATH = "C:/pythonproj/src/data.csv"
TABLE_NAME = "ecommerce_data"

def carregar_csv_para_postgres():
    # Ler o CSV com encoding correto
    df = pd.read_csv(CSV_PATH, encoding="latin1")

    # Criar conexão com PostgreSQL
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    # Gravar no banco
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)

    print(f"✅ Dados do CSV '{CSV_PATH}' gravados na tabela '{TABLE_NAME}' do banco {DB_NAME}.")

if __name__ == "__main__":
    carregar_csv_para_postgres()