import pandas as pd
import numpy as np
import datetime
from config import get_db_config
from sqlalchemy import create_engine, Numeric

# Carrega as variáveis do arquivo .env localizado na raiz do projeto
db_config = get_db_config()

TABLE_ORIGEM = "ecommerce_data_gold"

def update_gold_table():
    # 1. Conectar ao banco usando f-string e as variáveis de ambiente
    connection_string = (
        f"postgresql+psycopg2://{db_config['DB_USER']}:{db_config['DB_PASSWORD']}"
        f"@{db_config['DB_HOST']}:{db_config['DB_PORT']}/{db_config['DB_NAME']}"
    )
    engine = create_engine(connection_string)
    df = pd.read_sql_table(TABLE_ORIGEM, engine)

    #Convert UnitPrice to Numeric
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors='coerce')

    # Convert TotalValues to Numeric
    df["TotalValue"] = pd.to_numeric(df["TotalValue"], errors='coerce')

    #Update TOTALVALUE FOR 2 DECIMAL PLACES

    df["TotalValue"] = df["TotalValue"].round(2)

    # Add date column between 2023 and 2025

    start = datetime.date(2023, 1, 1)
    end = datetime.date(2025, 12, 31)
    delta_days = (end - start).days

    random_days = np.random.randint(0, delta_days + 1, size=len(df))
    df["Date"] = [start + datetime.timedelta(days=int(d)) for d in random_days ]


    df.to_sql("ecommerce_data_gold", engine, if_exists="replace", index=False,
          dtype={"TotalValue": Numeric(10,2), "UnitPrice": Numeric(10,2)}
    )
    
if __name__ == "__main__":
    update_gold_table()








