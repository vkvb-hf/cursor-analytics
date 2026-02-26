"""
Heatmap - Dimension x Dimension heatmap visualization.
"""

from typing import Optional

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


@st.cache_data(ttl=300)
def create_heatmap_chart(
    df: pd.DataFrame,
    metric_name: str,
    row_dimension: str,
    col_dimension: str,
    increase_is_good: bool = True,
) -> go.Figure:
    """
    Create heatmap visualization.

    Args:
        df: Pivoted DataFrame with row dimension as index, col dimension as columns
        metric_name: Name of the metric for title
        row_dimension: Name of the row dimension
        col_dimension: Name of the column dimension
        increase_is_good: If True, higher values are green; if False, lower is green

    Returns:
        Plotly figure
    """
    if df.empty:
        fig = go.Figure()
        fig.add_annotation(
            text="No data available for heatmap",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=16),
        )
        return fig

    color_scale = "RdYlGn" if increase_is_good else "RdYlGn_r"

    fig = px.imshow(
        df,
        labels=dict(
            x=col_dimension,
            y=row_dimension,
            color=metric_name,
        ),
        aspect="auto",
        color_continuous_scale=color_scale,
        text_auto=".3f",
    )

    fig.update_layout(
        title=dict(
            text=f"{metric_name} by {row_dimension} × {col_dimension}",
            font=dict(size=18),
        ),
        xaxis_title=col_dimension,
        yaxis_title=row_dimension,
        margin=dict(l=100, r=40, t=80, b=60),
    )

    fig.update_traces(
        textfont=dict(size=10),
    )

    return fig


def display_heatmap(
    df: pd.DataFrame,
    metric_name: str,
    row_dimension: str,
    col_dimension: str,
    increase_is_good: bool = True,
) -> None:
    """
    Display heatmap chart in Streamlit.

    Args:
        df: Pivoted DataFrame with row dimension as index, col dimension as columns
        metric_name: Name of the metric for title
        row_dimension: Name of the row dimension
        col_dimension: Name of the column dimension
        increase_is_good: If True, higher values are green; if False, lower is green
    """
    if df.empty:
        st.info(
            f"No data available for heatmap with dimensions {row_dimension} × {col_dimension}. "
            "This combination may not exist in the data."
        )
        return

    fig = create_heatmap_chart(
        df=df,
        metric_name=metric_name,
        row_dimension=row_dimension,
        col_dimension=col_dimension,
        increase_is_good=increase_is_good,
    )

    st.plotly_chart(fig, use_container_width=True)


def create_simple_heatmap(
    df: pd.DataFrame,
    value_column: str,
    row_column: str,
    col_column: str,
    title: str,
    increase_is_good: bool = True,
) -> go.Figure:
    """
    Create a simple heatmap from unpivoted data.

    Args:
        df: DataFrame with row, column, and value columns
        value_column: Name of the value column
        row_column: Name of the row column
        col_column: Name of the column column
        title: Chart title
        increase_is_good: If True, higher values are green

    Returns:
        Plotly figure
    """
    if df.empty:
        fig = go.Figure()
        fig.add_annotation(
            text="No data available",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
        return fig

    pivot_df = df.pivot_table(
        index=row_column,
        columns=col_column,
        values=value_column,
        aggfunc="mean",
    )

    color_scale = "RdYlGn" if increase_is_good else "RdYlGn_r"

    fig = px.imshow(
        pivot_df,
        labels=dict(x=col_column, y=row_column, color=value_column),
        aspect="auto",
        color_continuous_scale=color_scale,
        text_auto=".3f",
    )

    fig.update_layout(
        title=title,
        margin=dict(l=100, r=40, t=80, b=60),
    )

    return fig
