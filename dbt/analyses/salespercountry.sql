WITH total_value_per_country AS(
    SELECT 
    "TotalValue",
     "Country"
    FROM {{source("collect_gold","ecommerce_data_gold")}}
)

SELECT 
SUM("TotalValue") AS Total_sales_per_country, 
"Country" 
FROM total_value_per_country
GROUP BY "Country"
ORDER BY Total_sales_per_country DESC;
