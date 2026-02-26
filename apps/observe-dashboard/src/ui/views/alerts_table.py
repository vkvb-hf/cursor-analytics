"""
Alerts Table - Interactive table for displaying alerts.
"""

from typing import Optional, Callable

import pandas as pd
import streamlit as st


def format_severity(severity: str) -> str:
    """Format severity with emoji indicator."""
    severity_map = {
        "critical": "🔴 Critical",
        "warning": "🟡 Warning",
        "info": "🔵 Info",
    }
    return severity_map.get(severity.lower(), severity)


def format_deviation(deviation: float) -> str:
    """Format deviation percentage. Value is already in percentage form (e.g., -3.46 means -3.46%)."""
    if pd.isna(deviation):
        return "N/A"
    sign = "+" if deviation > 0 else ""
    return f"{sign}{deviation:.1f}%"


def create_alerts_table(
    df: pd.DataFrame,
    on_row_click: Optional[Callable] = None,
) -> Optional[dict]:
    """
    Display interactive alerts table.

    Args:
        df: DataFrame with alerts data
        on_row_click: Optional callback when row is clicked

    Returns:
        Selected row data if a row is clicked, None otherwise
    """
    if df.empty:
        st.info("No alerts found for the selected filters.")
        return None

    display_df = df.copy()

    display_columns = [
        "date",
        "severity",
        "metric_name",
        "monitor_name",
        "dimension_value",
        "deviation_pct",
    ]
    available_columns = [c for c in display_columns if c in display_df.columns]
    display_df = display_df[available_columns]

    if "severity" in display_df.columns:
        display_df["severity"] = display_df["severity"].apply(format_severity)

    column_config = {
        "date": st.column_config.DateColumn("Date", width="small"),
        "severity": st.column_config.TextColumn("Severity", width="small"),
        "metric_name": st.column_config.TextColumn("Metric", width="medium"),
        "monitor_name": st.column_config.TextColumn("Monitor", width="medium"),
        "dimension_value": st.column_config.TextColumn("Dimension", width="medium"),
        "deviation_pct": st.column_config.NumberColumn(
            "Deviation %", 
            width="small",
            format="%.1f%%",
        ),
    }

    event = st.dataframe(
        display_df,
        column_config=column_config,
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row",
    )

    if event and event.selection and event.selection.rows:
        selected_idx = event.selection.rows[0]
        return df.iloc[selected_idx].to_dict()

    return None


def create_alert_detail(alert_data: dict) -> None:
    """
    Display detailed information about a selected alert.

    Args:
        alert_data: Dictionary with alert details
    """
    st.subheader("Alert Details")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**Metric:** {alert_data.get('metric_name', 'N/A')}")
        st.markdown(f"**Monitor:** {alert_data.get('monitor_name', 'N/A')}")
        st.markdown(f"**Rule:** {alert_data.get('rule_name', 'N/A')}")
        st.markdown(f"**Severity:** {format_severity(alert_data.get('severity', 'N/A'))}")

    with col2:
        current = alert_data.get("current_value")
        expected = alert_data.get("expected_value")
        deviation = alert_data.get("deviation_pct")

        current_str = f"{current:.4f}" if current is not None else "N/A"
        expected_str = f"{expected:.4f}" if expected is not None else "N/A"
        deviation_str = format_deviation(deviation) if deviation is not None else "N/A"

        st.markdown(f"**Current Value:** {current_str}")
        st.markdown(f"**Expected Value:** {expected_str}")
        st.markdown(f"**Deviation:** {deviation_str}")

    if "dimension_key" in alert_data and "dimension_value" in alert_data:
        dim_key = alert_data.get("dimension_key", "")
        dim_value = alert_data.get("dimension_value", "")
        if dim_key and dim_value:
            st.markdown(f"**Dimension:** {dim_key} = {dim_value}")

    message = alert_data.get("message")
    if message:
        st.info(f"📝 {message}")
