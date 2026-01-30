-- tests/preco_maior_que_zero.sql
SELECT *
FROM {{ ref('meanticketpercustomer') }}
WHERE mean_unitprice <= 0
