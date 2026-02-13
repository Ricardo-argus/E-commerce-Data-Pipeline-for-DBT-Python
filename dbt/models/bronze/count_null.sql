WITH count_null_customers AS(
    SELECT 
    "CustomerID"
    FROM {{source("collect_bronze","ecommerce_data")}}
)

SELECT COUNT("CustomerID") AS Count_of_null_customers FROM count_null_customers 
WHERE "CustomerID" IS NULL