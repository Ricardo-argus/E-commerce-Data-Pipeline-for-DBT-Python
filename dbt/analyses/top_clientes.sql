SELECT "CustomerID", "mean_unitprice"
FROM {{ ref('meanticketpercustomer') }}
ORDER BY "mean_unitprice" DESC
LIMIT 10