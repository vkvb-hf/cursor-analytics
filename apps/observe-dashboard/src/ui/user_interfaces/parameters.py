"""
Parameters - Sidebar parameter components for visualizations.
"""

from dataclasses import dataclass
from typing import Optional

import pandas as pd
import streamlit as st

from data.data_transforming import get_available_dimensions


@dataclass
class HeatmapParameters:
    """Container for heatmap parameter selections."""

    row_dimension: str
    col_dimension: str


def create_heatmap_parameters(
    metrics_df: pd.DataFrame,
    default_row: Optional[str] = None,
    default_col: Optional[str] = None,
) -> HeatmapParameters:
    """
    Create parameter controls for heatmap visualization.

    Args:
        metrics_df: DataFrame with metrics data to extract dimension options
        default_row: Default row dimension
        default_col: Default column dimension

    Returns:
        HeatmapParameters dataclass with selected values
    """
    st.sidebar.header("📊 Heatmap Parameters")

    dimensions = get_available_dimensions(metrics_df)

    if not dimensions:
        st.sidebar.warning("No dimensions available for heatmap")
        return HeatmapParameters(row_dimension="", col_dimension="")

    if len(dimensions) < 2:
        st.sidebar.warning("Need at least 2 dimensions for heatmap")
        return HeatmapParameters(
            row_dimension=dimensions[0] if dimensions else "",
            col_dimension="",
        )

    default_row_idx = 0
    if default_row and default_row in dimensions:
        default_row_idx = dimensions.index(default_row)

    row_dimension = st.sidebar.selectbox(
        "Row Dimension",
        options=dimensions,
        index=default_row_idx,
        key="heatmap_row_dim",
    )

    col_options = [d for d in dimensions if d != row_dimension]
    default_col_idx = 0
    if default_col and default_col in col_options:
        default_col_idx = col_options.index(default_col)

    col_dimension = st.sidebar.selectbox(
        "Column Dimension",
        options=col_options,
        index=default_col_idx,
        key="heatmap_col_dim",
    )

    return HeatmapParameters(
        row_dimension=row_dimension,
        col_dimension=col_dimension,
    )


@dataclass
class TimeSeriesParameters:
    """Container for time series parameter selections."""

    show_pop_reference: bool
    show_yoy_reference: bool
    pop_period_days: int


def create_time_series_parameters() -> TimeSeriesParameters:
    """
    Create parameter controls for time series visualization.

    Returns:
        TimeSeriesParameters dataclass with selected values
    """
    st.sidebar.header("📈 Time Series Parameters")

    show_pop = st.sidebar.checkbox(
        "Show PoP Reference",
        value=True,
        key="ts_show_pop",
        help="Show period-over-period average line",
    )

    pop_days = 7
    if show_pop:
        pop_days = st.sidebar.slider(
            "PoP Period (days)",
            min_value=3,
            max_value=30,
            value=7,
            key="ts_pop_days",
        )

    show_yoy = st.sidebar.checkbox(
        "Show YoY Reference",
        value=True,
        key="ts_show_yoy",
        help="Show year-over-year comparison line",
    )

    return TimeSeriesParameters(
        show_pop_reference=show_pop,
        show_yoy_reference=show_yoy,
        pop_period_days=pop_days,
    )
