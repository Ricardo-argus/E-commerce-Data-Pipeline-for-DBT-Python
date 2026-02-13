# Projeto dbt - Ecommerce Data

Este repositório documenta a parte de **transformação de dados com dbt** (data build tool), organizada para garantir qualidade, rastreabilidade e documentação clara dos modelos de dados.

---

##  Visão Geral

O objetivo deste projeto é transformar dados de ecommerce em camadas **silver** e **gold**, aplicando testes de qualidade e boas práticas de engenharia de dados.  
Toda a lógica de transformação está centralizada no dbt, permitindo versionamento, documentação e execução automatizada.

---

##  Estrutura de Diretórios

- **models/**
  - **silver/** → modelos de limpeza e padronização  
    Exemplos: `avg_quantity.sql`, `meanvaluepercustomer.sql`, `null_prices.sql`, `row_counts.sql`, `totalquantity_per_country.sql`, `schema.yml`
  - **gold/** → modelos analíticos prontos para consumo  
    Exemplos: `src_ecommerce_gold.yml`
- **tests/** → testes de qualidade customizados  
  Exemplos: `notnull_customers.sql`, `preco_maior_que_zero.sql`
- **seeds/** → dados estáticos  
  Exemplos: `paises.csv`
- **snapshots/** → controle de histórico  
  Exemplos: `clientes_snapshot.sql`
- **macros/** → funções reutilizáveis
- **analyses/** → queries exploratórias
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

### testes:

    ```dbt test```

### Rodar Modelos:

    ```dbt run```
    ```dbt run -select avg_quantity ```

### Criar Lineage DAG e Documentação:

    ``` dbt docs generate```
    ``` dbt docs serve ```


*** Visualize a Lineage Graph (DAG) mostrando a relação entre os modelos criados nesse link abaixo:**

![DAG dos modelos dbt](data/LinearGraphdbt.png)



