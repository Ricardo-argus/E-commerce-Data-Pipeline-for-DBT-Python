{% macro row_count_model(model_name) %}
    select count(*) from {{ ref(model_name) }}
{% endmacro %}

