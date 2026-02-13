WITH Source_Sales AS (
    SELECT
    "source_sales_channel",
    "TotalValue",
    "Date"
    FROM "ecommerce_data_gold"
    WHERE "Date" BETWEEN '2025-01-01' AND '2025-12-31'
)

SELECT
"source_sales_channel",
SUM("TotalValue")
FROM Source_Sales
GROUP BY "source_sales_channel"