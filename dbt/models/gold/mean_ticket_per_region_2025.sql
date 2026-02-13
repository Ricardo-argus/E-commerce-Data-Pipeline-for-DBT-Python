SELECT
    "Region",
    ROUND(SUM("TotalValue")::numeric / COUNT(DISTINCT "InvoiceNo"),2) AS Mean_Ticket
FROM {{source('collect_gold', "ecommerce_data_gold")}}
WHERE "Date" BETWEEN '2025-01-01' AND '2025-12-31'
GROUP BY "Region"
ORDER BY Mean_Ticket DESC
