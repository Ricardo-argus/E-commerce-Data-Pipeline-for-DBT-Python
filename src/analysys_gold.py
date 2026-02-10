import pandas as pd
import os
from sqlalchemy import create_engine, Numeric

from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env localizado na raiz do projeto
load_dotenv()

# Configurações do banco PostgreSQL (agora protegidas)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


TABLE_ORIGEM = "ecommerce_data_gold"


# 1. Conectar ao banco usando f-string e as variáveis de ambiente
connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)
df = pd.read_sql_table(TABLE_ORIGEM, engine)

# CREATE ANALYSYS WITH DATA 
    
#Quantity of Invoice By Customer (INVOICE NO BY CUSTOMER)
inv_by_custom = (
    df.groupby("CustomerID")["InvoiceNo"].count()
    .reset_index()
    .rename(columns={"InvoiceNo": "Qtd_Faturas"})
    .sort_values(by="Qtd_Faturas", ascending=False)
    .head(10)
)
print(inv_by_custom)

# CREATE TOTAL VALUE BY REGION

totalvalue_byreg = (
    df.groupby("Region")["TotalValue"].sum()
    .reset_index()
    .rename(columns={"TotalValue": "Valor_Total_por_Regiao"})
    .sort_values(by="Valor_Total_por_Regiao", ascending=False)
    .head(10)
)
print(totalvalue_byreg)


# AVG_Quantity by Region

avg_quantity_byregion = (
    df.groupby("Region")["Quantity"].mean()
    .reset_index()
    .rename(columns={"Quantity": "Media_quantidade"})
    .sort_values(by="Media_quantidade", ascending=False)
    .head(10)
)
print(avg_quantity_byregion)


#identify all boxes on DESCRIPTION, ALL ROSES and say what type of product has more quantity 

qtd_box = df["Description"].str.contains("\\bbox(es)?\\b", case=False, na=False)

country_countsbox = df[qtd_box].groupby("Country").size()
print("Quantidade de Boxes por Pais:",country_countsbox)


france_boxes = (df[qtd_box & (df["Country"] == "France")]).shape[0]
print("Quantidade de Boxes para França:",france_boxes)

total_boxes = qtd_box.sum()

#Identify all roses on Description, calculate by Country and after compare quantity with box

qtd_rose = df["Description"].str.contains("\\brose(s)?\\b", case=False, na=False)

country_countsroses = df[qtd_rose].groupby("Country").size()
print("Quantidade de Roses por Pais:",country_countsroses)


max_country = country_countsroses.idxmax()
max_roses = country_countsroses.max()

print(f"Pais com maior quantidade de Roses: {max_country} ({max_roses})")






