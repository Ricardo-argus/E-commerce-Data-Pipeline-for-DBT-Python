{% snapshot clientes_snapshot %}
{{
    config(
        target_schema='snapshots',
        unique_key='"CustomerID"',
        strategy='check',
        check_cols=['Country']
    )
}}

SELECT "CustomerID", "Country"
FROM {{ source('collect_silver', 'ecommerce_data_silver') }}

{% endsnapshot %}
