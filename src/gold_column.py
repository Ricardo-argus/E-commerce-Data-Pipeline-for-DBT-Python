import pandas as pd
from config import get_db_config
from sqlalchemy import create_engine

# Carrega as variáveis do arquivo .env localizado na raiz do projeto
db_config = get_db_config()

# Nome da tabela de origem (bronze) e destino (silver)
TABLE_ORIGEM = "ecommerce_data_silver"
TABLE_DESTINO = "ecommerce_data_gold"

def executar_updates():
    # 1. Conectar ao banco usando f-string e as variáveis de ambiente
    connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)

    df = pd.read_sql_table(TABLE_ORIGEM, engine)


    #new analysys

    # New column total_value
    df["TotalValue"] = df["Quantity"] * df["UnitPrice"]

# New column for Region

    country_to_region = {
    "Argentina": "South America",
    "Australia": "Oceania",
    "Austria": "Europe",
    "Bahrain": "Europe",
    "Belgium": "Europe",
    "Brazil": "South America",
    "Canada": "North America",
    "Channel Islands": "Europe",
    "Chile": "South America",
    "China": "Asia",
    "Cyprus": "Europe",
    "Czech Republic": "Europe",
    "Denmark": "Europe",
    "EIRE": "Europe",
    "European Community": "Europe",
    "Finland": "Europe",
    "France": "Europe",
    "Germany": "Europe",
    "Greece": "Europe",
    "Iceland": "Europe",
    "Israel": "Middle East",
    "Italy": "Europe",
    "Japan": "Asia",
    "Lebanon": "Middle East",
    "Lithuania": "Europe",
    "Malta": "Europe",
    "Netherlands": "Europe",
    "Norway": "Europe",
    "Peru": "South America",
    "Poland": "Europe",
    "Portugal": "Europe",
    "RSA": "Africa", 
    "Saudi Arabia": "Middle East",
    "Singapore": "Asia",
    "Spain": "Europe",
    "Sweden": "Europe",
    "Switzerland": "Europe",
    "Turkey": "Europe",
    "United Arab Emirates": "Middle East",
    "United Kingdom": "Europe",
    "USA": "North America"
    }

    df["Region"] = df["Country"].map(country_to_region).fillna("Other")



    #Save new updates on table Gold
    df.to_sql(TABLE_DESTINO, engine, if_exists="replace", index=False)


if __name__ == "__main__":
    executar_updates()