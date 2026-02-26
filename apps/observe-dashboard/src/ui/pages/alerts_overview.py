"""
Alerts Overview Page - Display and filter alerts from Observe monitoring.
"""

import streamlit as st

from data.data_loading import get_alerts_data
from data.data_transforming import get_base_alerts_df, get_alerts_summary
import data.query_bank as qb
from ui.user_interfaces.filters import create_alert_filters
from ui.views.kpi_cards import create_kpi_cards_styled
from ui.views.alerts_table import create_alerts_table, create_alert_detail


def navigate_to_metrics(alert_data: dict) -> None:
    """
    Set session state for navigation to metrics explorer.

    Args:
        alert_data: Dictionary with alert details
    """
    st.session_state.selected_monitor = alert_data.get("monitor_name")
    st.session_state.selected_metric = alert_data.get("metric_name")
    st.session_state.selected_dimension_key = alert_data.get("dimension_key")
    st.session_state.selected_dimension_value = alert_data.get("dimension_value")


st.title("🚨 Alerts Overview")

connection = st.session_state.get("connection")
if connection is None:
    st.error("❌ Database connection not available. Please check your configuration.")
    st.stop()

with st.spinner("Loading alerts data..."):
    default_alerts_df = get_alerts_data(
        connection,
        st.session_state.start_date,
        st.session_state.end_date,
    )

filters = create_alert_filters(
    alerts_df=default_alerts_df,
    default_start=st.session_state.start_date,
    default_end=st.session_state.end_date,
)

filtered_df = get_base_alerts_df(
    default_df=default_alerts_df,
    start_date=filters.start_date,
    end_date=filters.end_date,
    monitors=filters.monitors,
    metrics=filters.metrics,
    severities=filters.severities,
)

st.subheader("Alert Summary")
alert_counts = get_alerts_summary(filtered_df)
create_kpi_cards_styled(alert_counts)

st.markdown("---")

st.subheader("Recent Alerts")
selected_alert = create_alerts_table(filtered_df)

if selected_alert:
    st.markdown("---")
    create_alert_detail(selected_alert)

    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("📊 View in Metrics Explorer", type="primary"):
            navigate_to_metrics(selected_alert)
            st.switch_page("ui/pages/metrics_explorer.py")
