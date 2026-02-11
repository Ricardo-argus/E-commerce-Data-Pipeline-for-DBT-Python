SELECT "CustomerID", "mean_unitprice"
FROM {{ ref('meanvaluepercustomer') }}
ORDER BY "mean_unitprice" DESC
LIMIT 10