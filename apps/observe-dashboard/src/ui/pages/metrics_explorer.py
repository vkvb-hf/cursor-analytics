"""
Metrics Explorer Page - Explore metrics trends and patterns.
"""

import pandas as pd
import streamlit as st

from data.data_loading import get_metrics_data, get_metrics_with_yoy_data
from data.data_transforming import (
    get_base_metrics_df,
    get_time_series_df,
    get_pop_reference,
)
from ui.user_interfaces.filters import create_metric_filters
from ui.user_interfaces.parameters import create_time_series_parameters
from ui.views.time_series import display_time_series


st.title("📊 Metrics Explorer")

connection = st.session_state.get("connection")
if connection is None:
    st.error("❌ Database connection not available. Please check your configuration.")
    st.stop()

preselected_monitor = st.session_state.get("selected_monitor")
preselected_metric = st.session_state.get("selected_metric")
preselected_dim_key = st.session_state.get("selected_dimension_key")
preselected_dim_value = st.session_state.get("selected_dimension_value")

with st.spinner("Loading metrics data..."):
    default_metrics_df = get_metrics_data(
        connection,
        st.session_state.start_date,
        st.session_state.end_date,
    )

    metrics_with_yoy_df = get_metrics_with_yoy_data(
        connection,
        st.session_state.start_date,
        st.session_state.end_date,
    )

filters = create_metric_filters(
    metrics_df=default_metrics_df,
    default_start=st.session_state.start_date,
    default_end=st.session_state.end_date,
    preselected_monitor=preselected_monitor,
    preselected_metric=preselected_metric,
    preselected_dimension_key=preselected_dim_key,
    preselected_dimension_value=preselected_dim_value,
)

ts_params = create_time_series_parameters()

if st.session_state.get("selected_monitor"):
    st.session_state.selected_monitor = None
    st.session_state.selected_metric = None
    st.session_state.selected_dimension_key = None
    st.session_state.selected_dimension_value = None

filtered_df = get_base_metrics_df(
    default_df=default_metrics_df,
    start_date=filters.start_date,
    end_date=filters.end_date,
    monitors=filters.monitors,
    metrics=filters.metrics,
    dimension_keys=[filters.dimension_key] if filters.dimension_key else [],
    dimension_values=[filters.dimension_value] if filters.dimension_value else [],
)

st.subheader("📈 Time Series Trend")

if filters.metrics:
    metric_name = filters.metrics[0]

    time_series_df = get_time_series_df(
        df=filtered_df,
        metric_name=metric_name,
        dimension_key=filters.dimension_key,
        dimension_value=filters.dimension_value,
    )

    pop_value = None
    if ts_params.show_pop_reference:
        pop_value = get_pop_reference(time_series_df, ts_params.pop_period_days)

    yoy_df = None
    if ts_params.show_yoy_reference and not metrics_with_yoy_df.empty:
        yoy_filtered = get_base_metrics_df(
            default_df=metrics_with_yoy_df,
            start_date=filters.start_date,
            end_date=filters.end_date,
            monitors=filters.monitors,
            metrics=filters.metrics,
            dimension_keys=[filters.dimension_key] if filters.dimension_key else [],
            dimension_values=[filters.dimension_value] if filters.dimension_value else [],
        )
        if not yoy_filtered.empty and "yoy_value" in yoy_filtered.columns:
            yoy_df = yoy_filtered[["date", "yoy_value"]].copy()
            yoy_df["date"] = pd.to_datetime(yoy_df["date"])
            yoy_df = yoy_df.sort_values("date")

    display_time_series(
        df=time_series_df,
        metric_name=metric_name,
        pop_value=pop_value,
        yoy_df=yoy_df,
        show_pop=ts_params.show_pop_reference,
        show_yoy=ts_params.show_yoy_reference,
    )
else:
    st.info("Select a metric to view the time series.")
