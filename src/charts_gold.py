# create charts using data from database and from analysys , producing advanced informations about ABC Curves, Forward Curves and anything else
import pandas as pd
from config import get_db_config
from sqlalchemy import create_engine, Numeric

from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env localizado na raiz do projeto
db_config = get_db_config()

TABLE_ORIGEM = "ecommerce_data_gold"


# 1. Conectar ao banco usando f-string e as variáveis de ambiente
connection_string = (
        f"postgresql+psycopg2://{db_config['DB_USER']}:{db_config['DB_PASSWORD']}"
        f"@{db_config['DB_HOST']}:{db_config['DB_PORT']}/{db_config['DB_NAME']}"
    )
engine = create_engine(connection_string)
df = pd.read_sql_table(TABLE_ORIGEM, engine)

#ABC PRODUCT CURVE

products_abc_curve = df.groupby("StockCode").agg(
    TotalValue = ("TotalValue", "sum"),
    qtd_faturas=("InvoiceNo", "nunique"))

products_abc_curve = products_abc_curve.sort_values(
    by = "TotalValue", ascending=False
)

products_abc_curve["Perc"] = (
    products_abc_curve["TotalValue"] / products_abc_curve["TotalValue"].sum()
)
products_abc_curve["Perc_Acumulado"] = products_abc_curve["Perc"].cumsum()

def classificar(p): 
    if p <= 0.8:
        return "A"
    elif p <= 0.95:
        return "B"
    else:
        return "C"

products_abc_curve["Classe"] = products_abc_curve["Perc_Acumulado"].apply(classificar)

import matplotlib.pyplot as plt

# Ordenar pelo valor total
products_abc_curve = products_abc_curve.sort_values(by="TotalValue", ascending=False)

# Selecionar apenas os 20 primeiros
top20 = products_abc_curve.head(20)

# Plot
fig, ax1 = plt.subplots(figsize=(12,6))

# Barras: valor total por produto
ax1.bar(top20.index, top20["TotalValue"], color="skyblue")
ax1.set_ylabel("Valor Total")
ax1.set_xticklabels(top20.index, rotation=90)

# Linha: percentual acumulado
ax2 = ax1.twinx()
ax2.plot(top20.index, top20["Perc_Acumulado"], color="red", marker="o")
ax2.set_ylabel("Percentual Acumulado")

plt.title("Curva ABC - Top 20 Produtos")
plt.show()


# Totalvalue by Country - Top Ten 

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


country_totalvalue_plot = df.groupby("Country").agg(
    TotalValue=("TotalValue", "sum")
)

sorted_countries = country_totalvalue_plot.sort_values(by="TotalValue", ascending=False)

top10countries = sorted_countries.head(10).reset_index()

plt.figure(figsize=(12,6))
sns.barplot(
    data=top10countries,
    x="Country",
    y="TotalValue",
    palette="Blues_r"
)
plt.xticks(rotation = 45)
plt.ylabel("Valor Total")
plt.title("Top 10 Países por Valor")

plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
plt.show()







