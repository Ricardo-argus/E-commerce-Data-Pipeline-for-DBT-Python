{% macro calc_growth(current_value, previous_value) %}
    CASE
        WHEN {{ previous_value }} IS NULL OR {{ previous_value }} = 0 THEN NULL
        ELSE ROUND((({{current_value}} - {{previous_value}}) :: numeric / {{ previous_value }}::numeric) * 100, 2)
    END
{% endmacro %}