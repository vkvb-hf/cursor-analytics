"""
Steering Dashboard - Main Application

A Streamlit dashboard for viewing weekly steering reports and
triggering AI-powered metric diagnosis using Bedrock Claude.
"""

import os
from pathlib import Path
from typing import Dict, List, Optional

import streamlit as st

from utils.report_loader import list_available_weeks, load_report, load_metrics_data
from utils.diagnosis_agent import (
    DiagnosisAgent,
    check_aws_credentials,
    check_databricks_connection,
)

# =============================================================================
# PAGE CONFIG & CSS
# =============================================================================

st.set_page_config(
    page_title="Steering Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
/* Layout */
.block-container { padding-top: 1.5rem; padding-bottom: 1rem; }
[data-testid="stSidebar"] { background-color: #0e1117; }

/* Hide branding */
#MainMenu, footer { visibility: hidden; }

/* Typography */
h1 { font-size: 2.2rem !important; font-weight: 700 !important; }
h3 { font-size: 1.15rem !important; font-weight: 600 !important; color: #fff !important; margin-bottom: 0.5rem !important; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 2rem; border-bottom: 2px solid #262730; }
.stTabs [data-baseweb="tab"] { font-size: 1rem; font-weight: 500; color: #808495; }
.stTabs [aria-selected="true"] { color: #fff; border-bottom: 2px solid #ff4b4b; }

/* Buttons */
.stButton > button { font-size: 0.85rem; }
.stButton > button[kind="primary"] { background-color: #ff4b4b; border: none; }
.stButton > button[kind="primary"]:hover { background-color: #ff6b6b; }

/* Text area */
.stTextArea textarea { background-color: #1a1c23; border: 1px solid #262730; font-size: 0.95rem; }
.stTextArea textarea:focus { border-color: #ff4b4b; }

/* Expander styling */
.streamlit-expanderHeader { font-size: 0.9rem !important; font-weight: 500 !important; }

/* Component styling */
.comp-week [data-testid="stVerticalBlockBorderWrapper"] > div {
    border-left: 4px solid #3b82f6 !important;
}
.comp-insights [data-testid="stVerticalBlockBorderWrapper"] > div {
    border-left: 4px solid #8b5cf6 !important;
}
.comp-quarter [data-testid="stVerticalBlockBorderWrapper"] > div {
    border-left: 4px solid #10b981 !important;
}
.comp-yoy [data-testid="stVerticalBlockBorderWrapper"] > div {
    border-left: 4px solid #f59e0b !important;
}

/* Component headers */
.comp-header {
    font-size: 0.85rem;
    font-weight: 600;
    padding: 0.4rem 0.6rem;
    margin: -1rem -1rem 0.75rem -1rem;
    border-radius: 4px 4px 0 0;
}
.comp-header-week { background: linear-gradient(90deg, #3b82f6 0%, #1e3a5f 100%); }
.comp-header-insights { background: linear-gradient(90deg, #8b5cf6 0%, #4c1d95 100%); }
.comp-header-quarter { background: linear-gradient(90deg, #10b981 0%, #064e3b 100%); }
.comp-header-yoy { background: linear-gradient(90deg, #f59e0b 0%, #78350f 100%); }

/* Metric title */
h3 { font-size: 1.5rem !important; font-weight: 700 !important; color: #fff !important; margin-bottom: 0.75rem !important; }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# SESSION STATE
# =============================================================================

def init_session_state():
    defaults = {
        "diagnosing": {},  # {metric, cluster, query, status, report, week}
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

# =============================================================================
# SIDEBAR
# =============================================================================

def render_sidebar() -> Optional[str]:
    with st.sidebar:
        st.markdown("#### Steering Week")
        weeks = list_available_weeks()
        if not weeks:
            st.error("No reports found.")
            return None
        
        selected_week = st.selectbox("Week", weeks, label_visibility="collapsed")
        
        st.markdown("---")
        st.caption("CONNECTIONS")
        aws_ok, _ = check_aws_credentials()
        db_ok, _ = check_databricks_connection()
        st.markdown(f"{'✓' if aws_ok else '✗'} AWS Bedrock")
        st.markdown(f"{'✓' if db_ok else '✗'} Databricks")
        
        if not aws_ok or not db_ok:
            with st.expander("Help"):
                if not aws_ok:
                    st.code("aws sso login --profile sso-bedrock")
                if not db_ok:
                    st.caption("Check ~/.databrickscfg")
        
        return selected_week

# =============================================================================
# HELPERS
# =============================================================================

def fmt_vol(vol: float) -> str:
    if vol >= 1_000_000:
        return f"{vol/1_000_000:.1f}M"
    if vol >= 1_000:
        return f"{vol/1_000:.1f}K"
    return f"{vol:.0f}"

def fmt_pct(val: float, metric_type: str) -> str:
    if metric_type == "dollar-ratio":
        return f"€{val:.2f}"
    return f"{val*100:.2f}%"

def get_change_color(change_pct: float) -> str:
    """Red for negative, green for positive, gray for zero."""
    if change_pct < 0:
        return "#ff4b4b"
    elif change_pct > 0:
        return "#00d26a"
    return "#808495"

# =============================================================================
# REPORT TAB
# =============================================================================

def render_report_tab(week: str):
    # Clear diagnosis if week changed
    diag = st.session_state.get("diagnosing", {})
    if diag and diag.get("week") != week:
        st.session_state.diagnosing = {}
    
    data = load_metrics_data(week)
    if not data:
        st.info("No structured data. Showing raw markdown.")
        st.markdown(load_report(week), unsafe_allow_html=True)
        return
    
    metrics = data.get("metrics", [])
    periods = data.get("periods", {})
    
    st.caption(
        f"**{periods.get('latest_week', '')}** vs {periods.get('prev_week', '')} | "
        f"YoY: {periods.get('prev_year_week', '')} | Quarter: {periods.get('quarter_range', '')}"
    )
    
    # Group by focus group
    groups: Dict[str, List[Dict]] = {}
    for m in metrics:
        fg = m.get("focus_group", "Other")
        groups.setdefault(fg, []).append(m)
    
    for fg_name, fg_metrics in groups.items():
        st.markdown(f"## {fg_name}")
        for metric in fg_metrics:
            render_metric(metric, week, periods)

def render_metric(metric: Dict, week: str, periods: Dict):
    name = metric.get("name", "Unknown")
    mtype = metric.get("metric_type", "ratio")
    threshold = metric.get("threshold", 2.5)
    
    clusters = metric.get("week_comparison", {}).get("clusters", [])
    insights = metric.get("week_comparison", {}).get("deep_insights", {})
    quarter = metric.get("long_term", {}).get("quarter", {})
    yoy = metric.get("long_term", {}).get("yoy", {})
    
    # Extract period info
    latest_week = periods.get("latest_week", "")
    prev_week = periods.get("prev_week", "")
    prev_year_week = periods.get("prev_year_week", "")
    quarter_range = periods.get("quarter_range", "")
    
    # Format week header: "2026 W10 vs W11" or "2025 W52 vs 2026 W01" if year changes
    def format_week_comparison(w1: str, w2: str) -> str:
        """w1 is latest_week, w2 is prev_week. Show prev vs current."""
        if not w1 or not w2:
            return "WEEK"
        y1, wk1 = w1.split("-") if "-" in w1 else ("", w1)
        y2, wk2 = w2.split("-") if "-" in w2 else ("", w2)
        # Show prev vs current (w2 vs w1)
        if y1 == y2:
            return f"{y2} {wk2} vs {wk1}"
        return f"{y2} {wk2} vs {y1} {wk1}"
    
    # Format quarter header - use as-is from data, it's pre-formatted
    def format_quarter_range(qr: str) -> str:
        if not qr:
            return "QUARTER"
        return qr
    
    # Format YoY: just show year
    def format_yoy(prev_yr_wk: str) -> str:
        if not prev_yr_wk:
            return "YOY"
        yr = prev_yr_wk.split("-")[0] if "-" in prev_yr_wk else prev_yr_wk
        return f"YOY (vs {yr})"
    
    week_header = f"📊 {format_week_comparison(latest_week, prev_week)}"
    insights_header = "🔎 INSIGHTS"
    quarter_header = "📈 Last 13 Weeks"
    yoy_header = f"📅 {format_yoy(prev_year_week)}"
    
    st.markdown(f"### {name}")
    
    # 4 columns
    c1, c2, c3, c4 = st.columns(4)
    
    # Column 1: Week Comparison (blue)
    with c1:
        st.markdown('<div class="comp-week">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(f'<div class="comp-header comp-header-week">{week_header}</div>', unsafe_allow_html=True)
            for cl in clusters:
                render_cluster(cl, name, mtype, threshold, week)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Column 2: Deep Insights (purple)
    with c2:
        st.markdown('<div class="comp-insights">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(f'<div class="comp-header comp-header-insights">{insights_header}</div>', unsafe_allow_html=True)
            render_insights(insights)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Column 3: Long-term Quarter (green)
    with c3:
        st.markdown('<div class="comp-quarter">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(f'<div class="comp-header comp-header-quarter">{quarter_header}</div>', unsafe_allow_html=True)
            if quarter:
                render_period(quarter)
            else:
                st.caption("No data")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Column 4: YoY (amber)
    with c4:
        st.markdown('<div class="comp-yoy">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(f'<div class="comp-header comp-header-yoy">{yoy_header}</div>', unsafe_allow_html=True)
            if yoy:
                render_period(yoy)
            else:
                st.caption("No data")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Inline diagnosis section
    diag = st.session_state.get("diagnosing", {})
    if diag.get("metric") == name:
        render_inline_diagnosis(diag, week)
    
    st.markdown("---")

def render_cluster(cl: Dict, metric_name: str, mtype: str, threshold: float, week: str):
    name = cl.get("cluster", "?")
    prev_v = cl.get("previous", 0)
    curr_v = cl.get("current", 0)
    change = cl.get("change_pct", 0)
    is_sig = cl.get("is_significant", False)
    vol = cl.get("volume", 0)
    
    color = get_change_color(change)
    arrow = "↓" if change < 0 else "↑"
    
    # Significance dot: red for negative sig, green for positive sig
    sig_dot = ""
    if is_sig:
        dot_color = "#ff4b4b" if change < 0 else "#00d26a"
        sig_dot = f" <span style='color:{dot_color}'>●</span>"
    
    # Row with cluster info and diagnose button
    col_info, col_btn = st.columns([4, 1])
    
    with col_info:
        st.markdown(
            f"<span style='font-weight:600;color:{color}'>{name}</span> · "
            f"<span style='color:{color};font-weight:500'>{arrow}{abs(change):.2f}%</span>{sig_dot}",
            unsafe_allow_html=True
        )
        st.caption(f"{fmt_pct(prev_v, mtype)} → {fmt_pct(curr_v, mtype)} · {fmt_vol(vol)}")
    
    with col_btn:
        key = f"dx_{metric_name}_{name}_{week}".replace(" ", "_").replace("(", "").replace(")", "")
        if st.button("🔍", key=key, help="Diagnose"):
            # Check if another diagnosis is running
            diag = st.session_state.get("diagnosing", {})
            if diag.get("status") == "running":
                st.warning("Diagnosis in progress. Please wait.")
            else:
                query = f"{metric_name}: {name}: {fmt_pct(prev_v, mtype)} to {fmt_pct(curr_v, mtype)} ({change:+.2f}%)"
                st.session_state.diagnosing = {
                    "metric": metric_name,
                    "cluster": name,
                    "query": query,
                    "status": "running",
                    "report": None,
                    "week": week,
                }
                st.rerun()

def render_insights(insights: Dict):
    """Render deep insights grouped by cluster."""
    bu = insights.get("business_units", {})
    dim = insights.get("dimensions", {})
    low_vol = insights.get("low_volume_count", 0)
    
    has_bu = any(bu.values())
    has_dim = any(dim.values())
    
    if not has_bu and not has_dim:
        st.caption("No significant changes")
        return
    
    if has_bu:
        with st.expander("Business Units", expanded=True):
            # Group items by cluster
            cluster_groups = group_by_cluster(bu)
            render_cluster_groups(cluster_groups)
    
    if has_dim:
        with st.expander("Dimensions", expanded=True):
            # Group items by cluster + dimension
            dim_groups = group_by_cluster_dimension(dim)
            render_dimension_groups(dim_groups)
    
    if low_vol > 0:
        st.caption(f"Low volume excluded: {low_vol}")


def group_by_cluster(buckets: Dict) -> Dict[str, List[tuple]]:
    """Group business unit items by cluster. Returns {cluster: [(value, change, bucket), ...]}"""
    cluster_items = {}
    for bucket, items in buckets.items():
        for it in items:
            cluster = it.get("cluster", "?")
            value = it.get("value", "?")
            change = it.get("change_pct", 0)
            cluster_items.setdefault(cluster, []).append((value, change, bucket))
    return cluster_items


def group_by_cluster_dimension(buckets: Dict) -> Dict[str, Dict[str, List[tuple]]]:
    """Group dimension items by cluster then dimension. Returns {cluster: {dimension: [(value, change, bucket), ...]}}"""
    result = {}
    for bucket, items in buckets.items():
        for it in items:
            cluster = it.get("cluster", "?")
            dimension = it.get("dimension", "?")
            value = it.get("value", "?")
            change = it.get("change_pct", 0)
            result.setdefault(cluster, {}).setdefault(dimension, []).append((value, change, bucket))
    return result


def render_cluster_groups(cluster_groups: Dict[str, List[tuple]]):
    """Render: WL: CG (-4%), ER (-3%)"""
    for cluster, items in cluster_groups.items():
        parts = []
        for value, change, _ in items[:5]:
            color = "#ff4b4b" if change < 0 else "#00d26a"
            parts.append(f"{value} (<span style='color:{color}'>{change:+d}%</span>)")
        line = f"<b>{cluster}</b>: " + ", ".join(parts)
        if len(items) > 5:
            line += f" +{len(items)-5} more"
        st.markdown(line, unsafe_allow_html=True)


def render_dimension_groups(dim_groups: Dict[str, Dict[str, List[tuple]]]):
    """Render: HF-INTL - PaymentMethod: Credit Card (+3%), Others (+11%)"""
    for cluster, dimensions in dim_groups.items():
        for dimension, items in dimensions.items():
            parts = []
            for value, change, _ in items[:5]:
                color = "#ff4b4b" if change < 0 else "#00d26a"
                parts.append(f"{value} (<span style='color:{color}'>{change:+d}%</span>)")
            line = f"<b>{cluster}</b> - {dimension}: " + ", ".join(parts)
            if len(items) > 5:
                line += f" +{len(items)-5} more"
            st.markdown(line, unsafe_allow_html=True)


def render_period(data: Dict):
    change = data.get("overall_change_pct", 0)
    vol = data.get("volume", 0)
    insights = data.get("deep_insights", {})
    
    color = "#ff4b4b" if change < 0 else "#00d26a" if change > 0 else "#808495"
    arrow = "↓" if change < 0 else "↑"
    
    st.markdown(f"<span style='font-size:1.3rem;color:{color};font-weight:600'>{arrow}{abs(change):.2f}%</span>", unsafe_allow_html=True)
    st.caption(f"vol: {fmt_vol(vol)}")
    
    if insights:
        render_insights(insights)

# =============================================================================
# INLINE DIAGNOSIS
# =============================================================================

def render_inline_diagnosis(diag: Dict, week: str):
    """Render diagnosis inline under the metric card."""
    cluster = diag.get("cluster", "")
    query = diag.get("query", "")
    status = diag.get("status", "")
    report = diag.get("report", "")
    metric = diag.get("metric", "")
    
    st.markdown("---")
    
    # Header row with descriptive title
    col_title, col_close = st.columns([6, 1])
    with col_title:
        st.markdown(f"**🔍 DIAGNOSIS:** {query}")
    with col_close:
        if st.button("✕ Close", key="close_diagnosis"):
            st.session_state.diagnosing = {}
            st.rerun()
    
    if status == "running":
        run_diagnosis(query, week)
    elif status == "done" and report:
        # Download button
        col1, col2 = st.columns([1, 5])
        with col1:
            safe = "".join(c if c.isalnum() or c in " _-" else "_" for c in query[:50]).replace(" ", "_").lower()
            st.download_button(
                "📥 Download",
                report,
                f"{safe}_{week.replace('-','').lower()}_diagnosis.md",
                "text/markdown",
                key="download_diagnosis"
            )
        
        # Show report in expander
        with st.expander("View Full Report", expanded=True):
            st.markdown(report)


def run_diagnosis(query: str, week: str):
    """Execute the diagnosis agent and update session state."""
    progress = st.empty()
    progress.info(f"Diagnosing... (2-5 min)")
    
    msgs = []
    def cb(msg: str, i: int):
        msgs.append(f"[{i}] {msg}")
        progress.text("\n".join(msgs[-5:]))
    
    agent = DiagnosisAgent()
    try:
        result = agent.diagnose(metric_query=query, week=week, progress_callback=cb)
    finally:
        agent.close()
    
    if result["success"]:
        st.session_state.diagnosing["status"] = "done"
        st.session_state.diagnosing["report"] = result["report"]
        progress.success(f"Done — {result['iterations']} iterations, {result['queries_run']} queries")
        
        # Save to file
        safe = "".join(c if c.isalnum() or c in " _-" else "_" for c in query[:50]).replace(" ", "_").lower()
        path = Path(os.path.expanduser("~/Documents/temp")) / f"{safe}_{week.replace('-','').lower()}_diagnosis.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(result["report"])
        st.caption(f"Saved: `{path}`")
        
        st.rerun()
    else:
        st.session_state.diagnosing["status"] = "error"
        progress.error(f"Failed: {result.get('error', 'Unknown')}")

# =============================================================================
# MAIN
# =============================================================================

def main():
    init_session_state()
    week = render_sidebar()
    if not week:
        st.stop()
    
    st.markdown("# Steering Dashboard")
    render_report_tab(week)

if __name__ == "__main__":
    main()
