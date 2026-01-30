-- models/totalquantity_per_country

WITH count_per_country AS (
    SELECT 
    "Country",
     "Quantity"
    FROM {{source("collect_silver","ecommerce_data_silver")}}
)

SELECT 
    "Country",
    SUM("Quantity") AS total_quantity_per_country
FROM count_per_country
GROUP BY "Country"
ORDER BY total_quantity_per_country DESC
LIMIT 10

