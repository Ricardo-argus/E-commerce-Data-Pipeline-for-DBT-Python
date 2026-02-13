
-- Total Quantity Percentage by Source

SELECT 
    "source_sales_channel",
    SUM("Quantity") Total_Quantidades_Vendidas,
    {{ calc_percent('"Quantity"') }} AS Percentage_by_Source
FROM "ecommerce_data_gold"
GROUP BY "source_sales_channel"
ORDER BY Percentage_by_Source DESC


