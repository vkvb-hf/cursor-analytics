"""
Query Bank - SQL query templates for Observe Dashboard.

Contains all SQL queries used to fetch data from Databricks.
"""

import os


def build_query(query_template: str, values: dict) -> str:
    """Build query from template and values."""
    return query_template.format(**values)


def get_alerts_table() -> str:
    """Get the alerts table name from environment."""
    return os.getenv("OBSERVE_ALERTS_TABLE", "payments_hf.observe_alerts_daily")


def get_metrics_table() -> str:
    """Get the metrics table name from environment."""
    return os.getenv("OBSERVE_METRICS_TABLE", "payments_hf.observe_metrics_daily")


ALERTS_QUERY_TEMPLATE = """
SELECT
    date,
    monitor_name,
    metric_name,
    rule_name,
    severity,
    dimension_key,
    dimension_value,
    current_value,
    expected_value,
    deviation_pct,
    message
FROM {table_name}
WHERE date BETWEEN '{start_date}' AND '{end_date}'
ORDER BY date DESC, severity DESC
"""


METRICS_QUERY_TEMPLATE = """
SELECT
    date,
    monitor_name,
    metric_name,
    dimension_key,
    dimension_value,
    metric_value
FROM {table_name}
WHERE date BETWEEN '{start_date}' AND '{end_date}'
ORDER BY date DESC
"""


METRICS_WITH_YOY_QUERY_TEMPLATE = """
WITH current_period AS (
    SELECT
        date,
        monitor_name,
        metric_name,
        dimension_key,
        dimension_value,
        metric_value
    FROM {table_name}
    WHERE date BETWEEN '{start_date}' AND '{end_date}'
),
yoy_period AS (
    SELECT
        date,
        DATE_ADD(date, 365) as yoy_date,
        monitor_name,
        metric_name,
        dimension_key,
        dimension_value,
        metric_value as yoy_value
    FROM {table_name}
    WHERE date BETWEEN DATE_SUB('{start_date}', 365) AND DATE_SUB('{end_date}', 365)
)
SELECT
    c.date,
    c.monitor_name,
    c.metric_name,
    c.dimension_key,
    c.dimension_value,
    c.metric_value,
    y.yoy_value
FROM current_period c
LEFT JOIN yoy_period y
    ON c.date = y.yoy_date
    AND c.monitor_name = y.monitor_name
    AND c.metric_name = y.metric_name
    AND c.dimension_key = y.dimension_key
    AND c.dimension_value = y.dimension_value
ORDER BY c.date DESC
"""


def get_alerts_query(start_date: str, end_date: str) -> str:
    """Build alerts query for date range."""
    return build_query(
        ALERTS_QUERY_TEMPLATE,
        {
            "table_name": get_alerts_table(),
            "start_date": start_date,
            "end_date": end_date,
        },
    )


def get_metrics_query(start_date: str, end_date: str) -> str:
    """Build metrics query for date range."""
    return build_query(
        METRICS_QUERY_TEMPLATE,
        {
            "table_name": get_metrics_table(),
            "start_date": start_date,
            "end_date": end_date,
        },
    )


def get_metrics_with_yoy_query(start_date: str, end_date: str) -> str:
    """Build metrics query with YoY comparison for date range."""
    return build_query(
        METRICS_WITH_YOY_QUERY_TEMPLATE,
        {
            "table_name": get_metrics_table(),
            "start_date": start_date,
            "end_date": end_date,
        },
    )
