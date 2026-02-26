"""
Observe Dashboard - Main Entry Point

A Streamlit dashboard for visualizing the Observe monitoring system data.
Provides alerts overview and metrics exploration capabilities.
"""

import os
from datetime import datetime, timedelta

import streamlit as st

from data.data_loading import get_connection, get_alerts_data, get_metrics_data
import data.query_bank as qb


def init_session_state():
    """Initialize default session state values."""
    if "connection" not in st.session_state:
        st.session_state.connection = get_connection()

    if "start_date" not in st.session_state:
        st.session_state.start_date = datetime.now().date() - timedelta(days=30)

    if "end_date" not in st.session_state:
        st.session_state.end_date = datetime.now().date() - timedelta(days=1)

    if "selected_monitor" not in st.session_state:
        st.session_state.selected_monitor = None

    if "selected_metric" not in st.session_state:
        st.session_state.selected_metric = None

    if "selected_dimension_key" not in st.session_state:
        st.session_state.selected_dimension_key = None

    if "selected_dimension_value" not in st.session_state:
        st.session_state.selected_dimension_value = None


def validate_environment():
    """Validate required environment variables."""
    alerts_table = os.getenv("OBSERVE_ALERTS_TABLE", "payments_hf.observe_alerts_daily")
    metrics_table = os.getenv("OBSERVE_METRICS_TABLE", "payments_hf.observe_metrics_daily")

    if not alerts_table or not metrics_table:
        st.error("❌ Required table environment variables are not set.")
        st.stop()

    return alerts_table, metrics_table


def main():
    """Main application entry point."""
    init_session_state()
    alerts_table, metrics_table = validate_environment()

    alerts_page = st.Page(
        "ui/pages/alerts_overview.py",
        title="Alerts Overview",
        icon="🚨",
        default=True,
    )
    metrics_page = st.Page(
        "ui/pages/metrics_explorer.py",
        title="Metrics Explorer",
        icon="📊",
    )

    pg = st.navigation([alerts_page, metrics_page])
    st.set_page_config(
        page_title="Observe Dashboard",
        page_icon="📊",
        layout="wide",
    )
    pg.run()


if __name__ == "__main__":
    main()
