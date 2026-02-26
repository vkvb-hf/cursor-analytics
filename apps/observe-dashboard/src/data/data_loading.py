"""
Data Loading - Database connections and cached data retrieval.
"""

from datetime import date, timedelta
from typing import Optional

import numpy as np
import pandas as pd
import streamlit as st

from utils.databricks_reader import DatabricksReader
import data.query_bank as qb


def get_connection():
    """Get Databricks connection (cached in session state)."""
    try:
        reader = DatabricksReader()
        return reader.get_connection()
    except Exception as e:
        st.warning(f"⚠️ Could not connect to Databricks: {e}. Using mock data.")
        return None


@st.cache_data(ttl=300)
def get_data(_connection, query: str) -> pd.DataFrame:
    """Get data with caching."""
    if _connection is None:
        return pd.DataFrame()
    return DatabricksReader.get_data_to_pandas(_connection, query)


def _generate_mock_alerts(start_date: date, end_date: date) -> pd.DataFrame:
    """Generate mock alerts data for demo purposes."""
    np.random.seed(42)
    
    monitors = ["verifications_overall", "verifications_by_dimension", "checkout_funnel_overall"]
    metrics = ["verification_count", "tokenisation_success_rate", "payment_page_visit", "select_to_success"]
    severities = ["critical", "warning", "info"]
    rules = ["period_over_period", "day_over_year", "data_presence"]
    countries = ["DE", "NL", "US", "UK", "AT", "BE"]
    
    num_days = (end_date - start_date).days + 1
    num_alerts = min(num_days * 3, 50)
    
    data = []
    for i in range(num_alerts):
        alert_date = start_date + timedelta(days=np.random.randint(0, num_days))
        severity = np.random.choice(severities, p=[0.1, 0.3, 0.6])
        current_val = np.random.uniform(0.7, 0.95)
        expected_val = np.random.uniform(0.85, 0.95)
        deviation = (current_val - expected_val) / expected_val
        
        data.append({
            "date": alert_date,
            "monitor_name": np.random.choice(monitors),
            "metric_name": np.random.choice(metrics),
            "rule_name": np.random.choice(rules),
            "severity": severity,
            "dimension_key": "country",
            "dimension_value": np.random.choice(countries),
            "current_value": current_val,
            "expected_value": expected_val,
            "deviation_pct": deviation,
            "message": f"Metric deviated by {deviation:.1%} from expected value",
        })
    
    return pd.DataFrame(data).sort_values("date", ascending=False)


def _generate_mock_metrics(start_date: date, end_date: date) -> pd.DataFrame:
    """Generate mock metrics data for demo purposes."""
    np.random.seed(42)
    
    monitors = ["verifications_overall", "checkout_funnel_overall"]
    metrics_config = {
        "verification_count": (10000, 2000),
        "tokenisation_success_rate": (0.92, 0.03),
        "payment_page_visit": (50000, 5000),
        "select_to_success": (0.85, 0.05),
    }
    countries = ["DE", "NL", "US", "UK", "AT", "BE"]
    payment_methods = ["card", "paypal", "sepa", "klarna"]
    
    num_days = (end_date - start_date).days + 1
    dates = [start_date + timedelta(days=i) for i in range(num_days)]
    
    data = []
    
    for d in dates:
        for monitor in monitors:
            for metric_name, (mean, std) in metrics_config.items():
                trend = 0.001 * (d - start_date).days
                value = mean * (1 + trend) + np.random.normal(0, std)
                if "rate" in metric_name or "success" in metric_name:
                    value = np.clip(value, 0, 1)
                
                data.append({
                    "date": d,
                    "monitor_name": monitor,
                    "metric_name": metric_name,
                    "dimension_key": "",
                    "dimension_value": "",
                    "metric_value": value,
                })
                
                for country in countries:
                    country_factor = {"DE": 1.0, "NL": 0.95, "US": 0.9, "UK": 0.92, "AT": 0.88, "BE": 0.85}[country]
                    c_value = value * country_factor + np.random.normal(0, std * 0.5)
                    if "rate" in metric_name or "success" in metric_name:
                        c_value = np.clip(c_value, 0, 1)
                    
                    data.append({
                        "date": d,
                        "monitor_name": monitor,
                        "metric_name": metric_name,
                        "dimension_key": "country",
                        "dimension_value": country,
                        "metric_value": c_value,
                    })
                
                for country in countries[:3]:
                    for pm in payment_methods[:3]:
                        pm_factor = {"card": 1.0, "paypal": 0.95, "sepa": 0.9, "klarna": 0.85}[pm]
                        country_factor = {"DE": 1.0, "NL": 0.95, "US": 0.9}[country]
                        cp_value = value * country_factor * pm_factor + np.random.normal(0, std * 0.3)
                        if "rate" in metric_name or "success" in metric_name:
                            cp_value = np.clip(cp_value, 0, 1)
                        
                        data.append({
                            "date": d,
                            "monitor_name": monitor,
                            "metric_name": metric_name,
                            "dimension_key": "country,payment_method",
                            "dimension_value": f"{country},{pm}",
                            "metric_value": cp_value,
                        })
    
    return pd.DataFrame(data)


@st.cache_data(ttl=300)
def get_alerts_data(
    _connection,
    start_date: date,
    end_date: date,
) -> pd.DataFrame:
    """
    Get alerts data for date range.

    Args:
        _connection: Databricks connection (underscore prefix for cache)
        start_date: Start date for query
        end_date: End date for query

    Returns:
        DataFrame with alerts data
    """
    if _connection is None:
        return _generate_mock_alerts(start_date, end_date)
    
    query = qb.get_alerts_query(
        start_date=start_date.strftime("%Y-%m-%d"),
        end_date=end_date.strftime("%Y-%m-%d"),
    )
    return get_data(_connection, query)


@st.cache_data(ttl=300)
def get_metrics_data(
    _connection,
    start_date: date,
    end_date: date,
) -> pd.DataFrame:
    """
    Get metrics data for date range.

    Args:
        _connection: Databricks connection (underscore prefix for cache)
        start_date: Start date for query
        end_date: End date for query

    Returns:
        DataFrame with metrics data
    """
    if _connection is None:
        return _generate_mock_metrics(start_date, end_date)
    
    query = qb.get_metrics_query(
        start_date=start_date.strftime("%Y-%m-%d"),
        end_date=end_date.strftime("%Y-%m-%d"),
    )
    return get_data(_connection, query)


@st.cache_data(ttl=300)
def get_metrics_with_yoy_data(
    _connection,
    start_date: date,
    end_date: date,
) -> pd.DataFrame:
    """
    Get metrics data with YoY comparison for date range.

    Args:
        _connection: Databricks connection (underscore prefix for cache)
        start_date: Start date for query
        end_date: End date for query

    Returns:
        DataFrame with metrics data including YoY values
    """
    if _connection is None:
        df = _generate_mock_metrics(start_date, end_date)
        df["yoy_value"] = df["metric_value"] * np.random.uniform(0.9, 1.1, len(df))
        return df
    
    query = qb.get_metrics_with_yoy_query(
        start_date=start_date.strftime("%Y-%m-%d"),
        end_date=end_date.strftime("%Y-%m-%d"),
    )
    return get_data(_connection, query)
