-- models\silver\null_prices

SELECT {{ fill_null('"UnitPrice"', 0) }} as unit_price
FROM {{ source('collect_silver', 'ecommerce_data_silver') }}
