"""
Data Transforming - Data transformation utilities and aggregation functions.
"""

from datetime import date, timedelta
from typing import Optional

import pandas as pd
import streamlit as st


@st.cache_data(ttl=300)
def get_list_from_df(df: pd.DataFrame, column: str) -> list[str]:
    """Extract unique values from a DataFrame column."""
    if column not in df.columns:
        return []
    return sorted(df[column].dropna().unique().tolist())


@st.cache_data(ttl=300)
def get_base_alerts_df(
    default_df: pd.DataFrame,
    start_date: date,
    end_date: date,
    monitors: list[str],
    metrics: list[str],
    severities: list[str],
) -> pd.DataFrame:
    """
    Filter alerts DataFrame based on selected filters.

    Args:
        default_df: Full alerts DataFrame
        start_date: Start date filter
        end_date: End date filter
        monitors: List of monitor names to include
        metrics: List of metric names to include
        severities: List of severities to include

    Returns:
        Filtered DataFrame
    """
    if default_df.empty:
        return default_df

    df = default_df.copy()

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"]).dt.date
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    if monitors and "monitor_name" in df.columns:
        df = df[df["monitor_name"].isin(monitors)]

    if metrics and "metric_name" in df.columns:
        df = df[df["metric_name"].isin(metrics)]

    if severities and "severity" in df.columns:
        df = df[df["severity"].isin(severities)]

    return df


@st.cache_data(ttl=300)
def get_base_metrics_df(
    default_df: pd.DataFrame,
    start_date: date,
    end_date: date,
    monitors: list[str],
    metrics: list[str],
    dimension_keys: list[str],
    dimension_values: list[str],
) -> pd.DataFrame:
    """
    Filter metrics DataFrame based on selected filters.

    Args:
        default_df: Full metrics DataFrame
        start_date: Start date filter
        end_date: End date filter
        monitors: List of monitor names to include
        metrics: List of metric names to include
        dimension_keys: List of dimension keys to include
        dimension_values: List of dimension values to include

    Returns:
        Filtered DataFrame
    """
    if default_df.empty:
        return default_df

    df = default_df.copy()

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"]).dt.date
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    if monitors and "monitor_name" in df.columns:
        df = df[df["monitor_name"].isin(monitors)]

    if metrics and "metric_name" in df.columns:
        df = df[df["metric_name"].isin(metrics)]

    if dimension_keys and "dimension_key" in df.columns:
        df = df[df["dimension_key"].isin(dimension_keys)]

    if dimension_values and "dimension_value" in df.columns:
        df = df[df["dimension_value"].isin(dimension_values)]

    return df


@st.cache_data(ttl=300)
def get_alerts_summary(df: pd.DataFrame) -> dict[str, int]:
    """
    Get alert counts by severity.

    Args:
        df: Alerts DataFrame

    Returns:
        Dictionary with severity counts
    """
    if df.empty or "severity" not in df.columns:
        return {"critical": 0, "warning": 0, "info": 0}

    counts = df["severity"].value_counts().to_dict()
    return {
        "critical": counts.get("critical", 0),
        "warning": counts.get("warning", 0),
        "info": counts.get("info", 0),
    }


@st.cache_data(ttl=300)
def get_time_series_df(
    df: pd.DataFrame,
    metric_name: str,
    dimension_key: Optional[str] = None,
    dimension_value: Optional[str] = None,
) -> pd.DataFrame:
    """
    Prepare data for time series visualization.

    Args:
        df: Metrics DataFrame
        metric_name: Name of metric to plot
        dimension_key: Optional dimension key filter
        dimension_value: Optional dimension value filter

    Returns:
        DataFrame with date and metric_value columns, one row per date
    """
    if df.empty:
        return pd.DataFrame(columns=["date", "metric_value"])

    filtered = df[df["metric_name"] == metric_name].copy()

    if dimension_key and "dimension_key" in filtered.columns:
        filtered = filtered[filtered["dimension_key"] == dimension_key]

    if dimension_value and "dimension_value" in filtered.columns:
        filtered = filtered[filtered["dimension_value"] == dimension_value]

    if filtered.empty:
        return pd.DataFrame(columns=["date", "metric_value"])

    filtered["date"] = pd.to_datetime(filtered["date"])
    
    # Aggregate by date to ensure one value per date
    result = filtered.groupby("date", as_index=False)["metric_value"].mean()
    result = result.sort_values("date")

    return result


@st.cache_data(ttl=300)
def get_pop_reference(df: pd.DataFrame, period_days: int = 7) -> Optional[float]:
    """
    Calculate period-over-period reference value.

    Args:
        df: Time series DataFrame with date and metric_value
        period_days: Number of days for the period

    Returns:
        Average metric value for the period, or None if insufficient data
    """
    if df.empty or len(df) < period_days:
        return None

    recent = df.tail(period_days)
    return recent["metric_value"].mean()


@st.cache_data(ttl=300)
def get_yoy_reference(
    df: pd.DataFrame,
    target_date: date,
) -> Optional[float]:
    """
    Get year-over-year reference value.

    Args:
        df: Metrics DataFrame with yoy_value column
        target_date: Date to get YoY value for

    Returns:
        YoY metric value, or None if not available
    """
    if df.empty or "yoy_value" not in df.columns:
        return None

    df_copy = df.copy()
    df_copy["date"] = pd.to_datetime(df_copy["date"]).dt.date

    row = df_copy[df_copy["date"] == target_date]
    if row.empty:
        return None

    yoy_val = row["yoy_value"].iloc[0]
    return yoy_val if pd.notna(yoy_val) else None


@st.cache_data(ttl=300)
def get_heatmap_df(
    df: pd.DataFrame,
    metric_name: str,
    row_dimension: str,
    col_dimension: str,
    target_date: Optional[date] = None,
) -> pd.DataFrame:
    """
    Prepare data for heatmap visualization.

    Pivots metrics data to create a matrix of row_dimension x col_dimension.

    Args:
        df: Metrics DataFrame
        metric_name: Name of metric to display
        row_dimension: Dimension for rows (e.g., 'country')
        col_dimension: Dimension for columns (e.g., 'payment_method')
        target_date: Optional specific date to show (defaults to most recent)

    Returns:
        Pivoted DataFrame suitable for heatmap
    """
    if df.empty:
        return pd.DataFrame()

    filtered = df[df["metric_name"] == metric_name].copy()

    if filtered.empty:
        return pd.DataFrame()

    combined_key = f"{row_dimension},{col_dimension}"
    filtered = filtered[filtered["dimension_key"] == combined_key]

    if filtered.empty:
        return pd.DataFrame()

    if target_date:
        filtered["date"] = pd.to_datetime(filtered["date"]).dt.date
        filtered = filtered[filtered["date"] == target_date]
    else:
        filtered["date"] = pd.to_datetime(filtered["date"])
        max_date = filtered["date"].max()
        filtered = filtered[filtered["date"] == max_date]

    if filtered.empty:
        return pd.DataFrame()

    def split_dimension_value(val):
        if pd.isna(val):
            return None, None
        parts = str(val).split(",", 1)
        if len(parts) == 2:
            return parts[0].strip(), parts[1].strip()
        return parts[0].strip(), None

    filtered[["row_val", "col_val"]] = filtered["dimension_value"].apply(
        lambda x: pd.Series(split_dimension_value(x))
    )

    pivot = filtered.pivot_table(
        index="row_val",
        columns="col_val",
        values="metric_value",
        aggfunc="mean",
    )

    return pivot


@st.cache_data(ttl=300)
def get_available_dimensions(df: pd.DataFrame) -> list[str]:
    """
    Get list of available dimension keys from metrics data.

    Args:
        df: Metrics DataFrame

    Returns:
        List of unique dimension keys
    """
    if df.empty or "dimension_key" not in df.columns:
        return []

    dimensions = df["dimension_key"].dropna().unique().tolist()
    all_dims = set()
    for dim_key in dimensions:
        if dim_key:
            for dim in dim_key.split(","):
                all_dims.add(dim.strip())

    return sorted(list(all_dims))


@st.cache_data(ttl=300)
def get_dimension_values_for_key(
    df: pd.DataFrame,
    dimension_key: str,
) -> list[str]:
    """
    Get available dimension values for a specific dimension key.

    Args:
        df: Metrics DataFrame
        dimension_key: The dimension key to get values for

    Returns:
        List of unique dimension values
    """
    if df.empty or "dimension_key" not in df.columns:
        return []

    filtered = df[df["dimension_key"] == dimension_key]
    if filtered.empty:
        return []

    return sorted(filtered["dimension_value"].dropna().unique().tolist())
