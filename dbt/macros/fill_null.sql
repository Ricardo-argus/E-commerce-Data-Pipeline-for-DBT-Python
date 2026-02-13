{% macro fill_null(column, default_value) %}
        coalesce({{column }}, {{ default_value }})
{% endmacro %}