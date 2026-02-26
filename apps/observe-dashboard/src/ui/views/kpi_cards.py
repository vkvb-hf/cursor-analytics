"""
KPI Cards - Alert count cards by severity.
"""

import streamlit as st


def create_kpi_cards(alert_counts: dict[str, int]) -> None:
    """
    Display KPI cards showing alert counts by severity.

    Args:
        alert_counts: Dictionary with keys 'critical', 'warning', 'info'
    """
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🔴 Critical",
            value=alert_counts.get("critical", 0),
            delta=None,
        )

    with col2:
        st.metric(
            label="🟡 Warning",
            value=alert_counts.get("warning", 0),
            delta=None,
        )

    with col3:
        st.metric(
            label="🔵 Info",
            value=alert_counts.get("info", 0),
            delta=None,
        )


def create_kpi_cards_styled(alert_counts: dict[str, int]) -> None:
    """
    Display styled KPI cards with colored backgrounds.

    Args:
        alert_counts: Dictionary with keys 'critical', 'warning', 'info'
    """
    col1, col2, col3 = st.columns(3)

    critical_count = alert_counts.get("critical", 0)
    warning_count = alert_counts.get("warning", 0)
    info_count = alert_counts.get("info", 0)

    with col1:
        st.markdown(
            f"""
            <div style="
                background-color: #ffebee;
                border-left: 4px solid #f44336;
                padding: 1rem;
                border-radius: 4px;
            ">
                <h3 style="margin: 0; color: #c62828;">Critical</h3>
                <p style="font-size: 2rem; margin: 0; font-weight: bold; color: #c62828;">
                    {critical_count}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div style="
                background-color: #fff8e1;
                border-left: 4px solid #ff9800;
                padding: 1rem;
                border-radius: 4px;
            ">
                <h3 style="margin: 0; color: #ef6c00;">Warning</h3>
                <p style="font-size: 2rem; margin: 0; font-weight: bold; color: #ef6c00;">
                    {warning_count}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div style="
                background-color: #e3f2fd;
                border-left: 4px solid #2196f3;
                padding: 1rem;
                border-radius: 4px;
            ">
                <h3 style="margin: 0; color: #1565c0;">Info</h3>
                <p style="font-size: 2rem; margin: 0; font-weight: bold; color: #1565c0;">
                    {info_count}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
