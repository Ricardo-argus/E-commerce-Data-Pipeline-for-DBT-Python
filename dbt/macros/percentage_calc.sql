{% macro calc_percent(column_name) %}
    ROUND(SUM({{ column_name }}) * 100.0 / SUM(SUM({{ column_name }})) OVER (), 2)
{% endmacro %}