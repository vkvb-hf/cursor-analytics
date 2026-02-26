"""
Filters - Sidebar filter components for the dashboard.
"""

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional

import pandas as pd
import streamlit as st

from data.data_transforming import get_list_from_df, get_available_dimensions


def _multiselect_with_all(
    label: str,
    options: list[str],
    default: Optional[list[str]] = None,
    key: Optional[str] = None,
) -> list[str]:
    """
    Create a multiselect with an 'All' option.

    When 'All' is selected (or nothing is selected), returns all options.

    Args:
        label: Label for the multiselect
        options: List of options to choose from
        default: Default selected values
        key: Streamlit widget key

    Returns:
        List of selected values (all options if 'All' selected)
    """
    all_option = "All"
    options_with_all = [all_option] + list(options)

    if default is None:
        default = [all_option]

    selected = st.multiselect(
        label,
        options=options_with_all,
        default=default,
        key=key,
    )

    if all_option in selected or not selected:
        return list(options)

    return selected


@dataclass
class AlertFilters:
    """Container for alert filter selections."""

    start_date: date
    end_date: date
    monitors: list[str]
    metrics: list[str]
    severities: list[str]


@dataclass
class MetricFilters:
    """Container for metric filter selections."""

    start_date: date
    end_date: date
    monitors: list[str]
    metrics: list[str]
    dimension_key: Optional[str]
    dimension_value: Optional[str]


def create_date_filter(
    default_start: Optional[date] = None,
    default_end: Optional[date] = None,
    key_prefix: str = "",
) -> tuple[date, date]:
    """
    Create date range filter in sidebar.

    Args:
        default_start: Default start date
        default_end: Default end date
        key_prefix: Prefix for widget keys

    Returns:
        Tuple of (start_date, end_date)
    """
    if default_start is None:
        default_start = date.today() - timedelta(days=30)
    if default_end is None:
        default_end = date.today() - timedelta(days=1)

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input(
            "Start Date",
            value=default_start,
            key=f"{key_prefix}start_date",
        )
    with col2:
        end_date = st.date_input(
            "End Date",
            value=default_end,
            key=f"{key_prefix}end_date",
        )

    return start_date, end_date


def create_alert_filters(
    alerts_df: pd.DataFrame,
    default_start: Optional[date] = None,
    default_end: Optional[date] = None,
) -> AlertFilters:
    """
    Create filter components for alerts page.

    Args:
        alerts_df: DataFrame with alerts data to extract filter options
        default_start: Default start date
        default_end: Default end date

    Returns:
        AlertFilters dataclass with selected values
    """
    st.sidebar.header("🔍 Filters")

    start_date, end_date = create_date_filter(
        default_start=default_start,
        default_end=default_end,
        key_prefix="alert_",
    )

    monitors = get_list_from_df(alerts_df, "monitor_name")
    selected_monitors = _multiselect_with_all(
        "Monitor",
        monitors,
        key="alert_monitors",
    )

    metrics = get_list_from_df(alerts_df, "metric_name")
    selected_metrics = _multiselect_with_all(
        "Metric",
        metrics,
        key="alert_metrics",
    )

    severities = ["critical", "warning", "info"]
    selected_severities = _multiselect_with_all(
        "Severity",
        severities,
        key="alert_severities",
    )

    return AlertFilters(
        start_date=start_date,
        end_date=end_date,
        monitors=selected_monitors,
        metrics=selected_metrics,
        severities=selected_severities,
    )


def create_metric_filters(
    metrics_df: pd.DataFrame,
    default_start: Optional[date] = None,
    default_end: Optional[date] = None,
    preselected_monitor: Optional[str] = None,
    preselected_metric: Optional[str] = None,
    preselected_dimension_key: Optional[str] = None,
    preselected_dimension_value: Optional[str] = None,
) -> MetricFilters:
    """
    Create filter components for metrics explorer page.

    Args:
        metrics_df: DataFrame with metrics data to extract filter options
        default_start: Default start date
        default_end: Default end date
        preselected_monitor: Pre-selected monitor (from navigation)
        preselected_metric: Pre-selected metric (from navigation)
        preselected_dimension_key: Pre-selected dimension key
        preselected_dimension_value: Pre-selected dimension value

    Returns:
        MetricFilters dataclass with selected values
    """
    st.sidebar.header("🔍 Filters")

    start_date, end_date = create_date_filter(
        default_start=default_start,
        default_end=default_end,
        key_prefix="metric_",
    )

    monitors = get_list_from_df(metrics_df, "monitor_name")
    default_monitor = preselected_monitor if preselected_monitor in monitors else None
    selected_monitor = st.sidebar.selectbox(
        "Monitor",
        options=monitors,
        index=monitors.index(default_monitor) if default_monitor else 0,
        key="metric_monitor",
    )

    monitor_df = metrics_df[metrics_df["monitor_name"] == selected_monitor] if selected_monitor else metrics_df
    metrics = get_list_from_df(monitor_df, "metric_name")
    default_metric = preselected_metric if preselected_metric in metrics else None
    selected_metric = st.sidebar.selectbox(
        "Metric",
        options=metrics,
        index=metrics.index(default_metric) if default_metric else 0,
        key="metric_metric",
    )

    metric_df = monitor_df[monitor_df["metric_name"] == selected_metric] if selected_metric else monitor_df
    dimension_keys = get_list_from_df(metric_df, "dimension_key")
    
    # Default to 'global' if available, otherwise first option
    default_dim_key = "global" if "global" in dimension_keys else (dimension_keys[0] if dimension_keys else None)
    if preselected_dimension_key and preselected_dimension_key in dimension_keys:
        default_dim_key = preselected_dimension_key
    
    selected_dimension_key = st.sidebar.selectbox(
        "Dimension",
        options=dimension_keys,
        index=dimension_keys.index(default_dim_key) if default_dim_key and default_dim_key in dimension_keys else 0,
        key="metric_dimension_key",
    )

    selected_dimension_value = None
    if selected_dimension_key:
        dim_df = metric_df[metric_df["dimension_key"] == selected_dimension_key]
        dimension_values = get_list_from_df(dim_df, "dimension_value")
        if dimension_values:
            # Default to 'global' if available for global dimension
            default_dim_val = None
            if selected_dimension_key == "global" and "global" in dimension_values:
                default_dim_val = "global"
            if preselected_dimension_value and preselected_dimension_value in dimension_values:
                default_dim_val = preselected_dimension_value
            
            selected_dimension_value = st.sidebar.selectbox(
                "Dimension Value",
                options=dimension_values,
                index=dimension_values.index(default_dim_val) if default_dim_val and default_dim_val in dimension_values else 0,
                key="metric_dimension_value",
            )

    return MetricFilters(
        start_date=start_date,
        end_date=end_date,
        monitors=[selected_monitor] if selected_monitor else [],
        metrics=[selected_metric] if selected_metric else [],
        dimension_key=selected_dimension_key if selected_dimension_key else None,
        dimension_value=selected_dimension_value,
    )
