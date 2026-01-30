-- models/meanticketpercustomer.sql

WITH mean_valuecustom AS (
    SELECT
        "UnitPrice",
        "CustomerID"
    FROM {{ source("collect_silver", "ecommerce_data_silver") }}
)

SELECT 
    "CustomerID",
    AVG("UnitPrice") AS mean_unitprice
FROM mean_valuecustom
GROUP BY "CustomerID"
HAVING AVG("UnitPrice") > 5
ORDER BY mean_unitprice DESC


