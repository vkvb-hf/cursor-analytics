"""
Time Series - Time series visualization with reference lines.
"""

from typing import Optional

import pandas as pd
import plotly.graph_objects as go
import streamlit as st


@st.cache_data(ttl=300)
def create_time_series_chart(
    df: pd.DataFrame,
    metric_name: str,
    pop_value: Optional[float] = None,
    yoy_df: Optional[pd.DataFrame] = None,
    show_pop: bool = True,
    show_yoy: bool = True,
) -> go.Figure:
    """
    Create time series chart with optional reference lines.

    Args:
        df: DataFrame with 'date' and 'metric_value' columns
        metric_name: Name of the metric for title
        pop_value: Period-over-period average value for reference line
        yoy_df: DataFrame with YoY values (date, yoy_value columns)
        show_pop: Whether to show PoP reference line
        show_yoy: Whether to show YoY reference line

    Returns:
        Plotly figure
    """
    fig = go.Figure()

    if df.empty:
        fig.add_annotation(
            text="No data available",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=16),
        )
        return fig

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["metric_value"],
            mode="lines+markers",
            name="Current",
            line=dict(color="#1f77b4", width=2),
            marker=dict(size=6),
        )
    )

    if show_pop and pop_value is not None:
        fig.add_hline(
            y=pop_value,
            line_dash="dash",
            line_color="#ff7f0e",
            annotation_text=f"PoP Avg: {pop_value:.4f}",
            annotation_position="top right",
        )

    if show_yoy and yoy_df is not None and not yoy_df.empty:
        fig.add_trace(
            go.Scatter(
                x=yoy_df["date"],
                y=yoy_df["yoy_value"],
                mode="lines",
                name="YoY",
                line=dict(color="#2ca02c", width=1, dash="dot"),
                opacity=0.7,
            )
        )

    fig.update_layout(
        title=dict(
            text=metric_name,
            font=dict(size=18),
        ),
        xaxis_title="Date",
        yaxis_title="Value",
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        margin=dict(l=60, r=40, t=80, b=60),
    )

    return fig


def display_time_series(
    df: pd.DataFrame,
    metric_name: str,
    pop_value: Optional[float] = None,
    yoy_df: Optional[pd.DataFrame] = None,
    show_pop: bool = True,
    show_yoy: bool = True,
) -> None:
    """
    Display time series chart in Streamlit.

    Args:
        df: DataFrame with 'date' and 'metric_value' columns
        metric_name: Name of the metric for title
        pop_value: Period-over-period average value
        yoy_df: DataFrame with YoY values
        show_pop: Whether to show PoP reference line
        show_yoy: Whether to show YoY reference line
    """
    fig = create_time_series_chart(
        df=df,
        metric_name=metric_name,
        pop_value=pop_value,
        yoy_df=yoy_df,
        show_pop=show_pop,
        show_yoy=show_yoy,
    )

    st.plotly_chart(fig, use_container_width=True)
