# Projeto dbt - Ecommerce Data

Este repositório documenta a parte de **transformação de dados com dbt** (data build tool), organizada para garantir qualidade, rastreabilidade e documentação clara dos modelos de dados.

---

##  Visão Geral

O objetivo deste projeto é transformar dados de ecommerce em camadas **silver** e **gold**, aplicando testes de qualidade e boas práticas de engenharia de dados.  
Toda a lógica de transformação está centralizada no dbt, permitindo versionamento, documentação e execução automatizada.

---

##  Estrutura de Diretórios

- **models/**
  - **silver/** → modelos de dados brutos e criação de seed 
    Exemplos: `count_null.sql`, `paises_seedmodel.sql`
  - **silver/** → modelos de limpeza e padronização  
    Exemplos: `avg_quantity.sql`, `meanvaluepercustomer.sql`, `null_prices.sql`, `row_counts.sql`, `totalquantity_per_country.sql`
  - **gold/** → modelos analíticos prontos para consumo  
    Exemplos: `mean_ticket_per_region_2025.sql`, `percentage_meanprice_month.sql`, `most_sold_products_2024`
- **tests/** → testes de qualidade customizados  
  Exemplos: `notnull_customers.sql`, `preco_maior_que_zero.sql`
- **seeds/** → dados estáticos  
  Exemplos: `paises.csv`
- **snapshots/** → controle de histórico  
  Exemplos: `clientes_snapshot.sql`
- **macros/** → funções reutilizáveis
  Exemplos: `calc_growth.sql`, `fill_null.sql`
- **analyses/** → queries exploratórias
  Exemplos: `salespercountry.sql`, `top_clientes.sql`
- **dbt_project.yml** → arquivo principal de configuração

---

##  Configuração de Fontes

As fontes são definidas em arquivos YAML, como:
- `src_ecommerce_silver.yml`
- `src_ecommerce_gold.yml`
- `src_ecommerce_bronze.yml`

## Exemplo de referência a uma fonte:

```sql
SELECT "CustomerID"
FROM {{ source("collect_gold", "ecommerce_data_gold") }}
WHERE "CustomerID" IS NULL
```

## Como rodar aplicacao, testes e  documentação 

### Testes:

```bash
    dbt test
```

# Rodar Modelos:

    ```bash
    dbt run
    ```

    ```bash
    dbt run -select avg_quantity 
    ```

### Criar Lineage DAG e Documentação:

    ```bash
    dbt docs generate
    ```

    ```bash
    dbt docs serve 
    ```
*** Visualize a Lineage Graph (DAG) mostrando a relação entre os modelos criados abaixo:**

![DAG dos modelos dbt](DAG_image/LinearGraphdbt.png)



