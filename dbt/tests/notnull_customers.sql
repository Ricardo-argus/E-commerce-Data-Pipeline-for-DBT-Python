SELECT "CustomerID"
FROM {{ source('collect_gold', "ecommerce_data_gold") }}
WHERE "CustomerID" IS NULL