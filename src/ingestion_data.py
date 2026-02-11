import pandas as pd
import os
from config import get_db_config
from sqlalchemy import create_engine


# Carrega as variáveis do arquivo .env
db_config = get_db_config()


connection_string = (
        f"postgresql+psycopg2://{db_config['DB_USER']}:{db_config['DB_PASSWORD']}"
        f"@{db_config['DB_HOST']}:{db_config['DB_PORT']}/{db_config['DB_NAME']}"
    )

# Busca as variáveis de ambiente
CSV_PATH = os.getenv("CSV_PATH")


def carregar_csv_para_postgres():
    # Ler o CSV com encoding correto
    if not os.path.exists(CSV_PATH):
        print(f"❌ Erro: O arquivo {CSV_PATH} não foi encontrado.")
        return

    df = pd.read_csv(CSV_PATH, encoding="latin1")

    # Criar conexão com PostgreSQL usando as variáveis protegidas
    connection_string = (
        f"postgresql+psycopg2://{db_config['DB_USER']}:{db_config['DB_PASSWORD']}"
        f"@{db_config['DB_HOST']}:{db_config['DB_PORT']}/{db_config['DB_NAME']}"
    )
    engine = create_engine(connection_string)

    # Gravar no banco
    df.to_sql({db_config['DB_NAME']}, engine, if_exists="replace", index=False)

if __name__ == "__main__":
    carregar_csv_para_postgres()