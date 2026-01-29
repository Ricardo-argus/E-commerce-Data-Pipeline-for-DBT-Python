import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Busca as variáveis de ambiente
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
CSV_PATH = os.getenv("CSV_PATH")
TABLE_NAME = "ecommerce_data" # Mantendo o nome que o dbt espera

def carregar_csv_para_postgres():
    # Ler o CSV com encoding correto
    if not os.path.exists(CSV_PATH):
        print(f"❌ Erro: O arquivo {CSV_PATH} não foi encontrado.")
        return

    df = pd.read_csv(CSV_PATH, encoding="latin1")

    # Criar conexão com PostgreSQL usando as variáveis protegidas
    connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)

    # Gravar no banco
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)

    print(f"✅ Dados gravados com sucesso na tabela '{TABLE_NAME}'. Credenciais protegidas!")

if __name__ == "__main__":
    carregar_csv_para_postgres()