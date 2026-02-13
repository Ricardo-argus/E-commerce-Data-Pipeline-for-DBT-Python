{{ config(materialized='view') }}

SELECT
    month,
    avg_price,
    {{ calc_growth('avg_price', 'LAG(avg_price) OVER (ORDER BY month)') }} AS growth_percent
FROM (SELECT 
        DATE_TRUNC('month', "Date") AS month,
        AVG("UnitPrice") AS avg_price
    FROM "ecommerce_data_gold"
    GROUP BY DATE_TRUNC('month', "Date")) as monthly_avg 
ORDER BY month