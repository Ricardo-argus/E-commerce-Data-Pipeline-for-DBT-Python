WITH most_sold AS (
    SELECT 
    "StockCode",
    "Description",
    "Quantity"
    FROM {{source("collect_gold","ecommerce_data_gold")}}
    WHERE "Date" BETWEEN '2024-01-01' AND '2024-12-31'
)

SELECT "StockCode", "Description", SUM("Quantity") AS Total_of_products_sold FROM most_sold
GROUP BY "StockCode", "Description"
ORDER BY Total_of_products_sold DESC