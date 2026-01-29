-- models/silver/avg_quantity.sql
SELECT 
    AVG("Quantity") AS media_quantidade 
FROM {{ source('collect_silver', 'ecommerce_data_silver') }}