-- tests/preco_maior_que_zero.sql
SELECT *
FROM {{ source('collect_gold', "ecommerce_data_gold") }}
WHERE mean_unitprice <= 0
