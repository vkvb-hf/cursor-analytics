"""
Steering Dashboard - Main Application

A Streamlit dashboard for viewing weekly steering reports and
triggering AI-powered metric diagnosis using Bedrock Claude.
"""

import os
from datetime import datetime
from pathlib import Path

import streamlit as st

from utils.report_loader import list_available_weeks, load_report
from utils.diagnosis_agent import (
    DiagnosisAgent,
    check_aws_credentials,
    check_databricks_connection,
)

st.set_page_config(
    page_title="Steering Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better visual hierarchy and readability
st.markdown("""
<style>
/* Remove default padding bloat */
.block-container {
    padding-top: 2rem;
    padding-bottom: 1rem;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #0e1117;
}

/* Week selector - prominent with depth */
[data-testid="stSidebar"] .stSelectbox > div > div {
    background-color: #1e2130;
    border: 1px solid #3d4155;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
[data-testid="stSidebar"] .stSelectbox > div > div:hover {
    border-color: #ff4b4b;
}

/* Connection status styling */
[data-testid="stSidebar"] .stCaption {
    color: #606580;
    font-size: 0.7rem;
    letter-spacing: 1px;
    margin-top: 1rem;
}

/* Connection status - inline and minimal */
.connection-status {
    display: flex;
    gap: 1rem;
    padding: 0.5rem 0;
    font-size: 0.8rem;
}
.connection-ok { color: #00d26a; }
.connection-fail { color: #ff4b4b; }

/* Tabs - more prominent */
.stTabs [data-baseweb="tab-list"] {
    gap: 2rem;
    border-bottom: 2px solid #262730;
}
.stTabs [data-baseweb="tab"] {
    font-size: 1rem;
    font-weight: 500;
    padding: 0.75rem 0;
    color: #808495;
}
.stTabs [aria-selected="true"] {
    color: #ffffff;
    border-bottom: 2px solid #ff4b4b;
}

/* Tables - better readability with responsive font */
.stMarkdown table {
    width: 100%;
    border-collapse: collapse;
    font-size: clamp(0.8rem, 1.2vw, 1rem); /* Responsive: min 12.8px, scales with viewport, max 16px */
}
.stMarkdown table th {
    background-color: #1a1c23;
    color: #808495;
    font-weight: 600;
    text-transform: uppercase;
    font-size: clamp(0.7rem, 1vw, 0.875rem); /* Responsive: min 11.2px, max 14px */
    letter-spacing: 0.5px;
    padding: 0.75rem 1rem;
    text-align: left;
    border-bottom: 2px solid #262730;
    white-space: nowrap;
}
.stMarkdown table td {
    padding: 0.6rem 1rem;
    border-bottom: 1px solid #262730;
    vertical-align: top;
    line-height: 1.5;
}
.stMarkdown table tr:hover {
    background-color: #1a1c23;
}

/* Alternating row colors */
.stMarkdown table tbody tr:nth-child(even) {
    background-color: rgba(255,255,255,0.02);
}

/* Headers - clear hierarchy */
h1 {
    font-size: 2.5rem !important;
    font-weight: 700 !important;
    margin-bottom: 1rem !important;
    letter-spacing: -0.5px;
}
h2 {
    font-size: 1.25rem !important;
    font-weight: 500 !important;
    color: #ffffff !important;
    margin-top: 1.5rem !important;
}
h3 {
    font-size: 1rem !important;
    font-weight: 500 !important;
    color: #808495 !important;
}

/* Metric highlights - color coding */
.metric-drop { color: #ff4b4b; font-weight: 600; }
.metric-rise { color: #00d26a; font-weight: 600; }

/* Cards for sections */
.report-section {
    background-color: #1a1c23;
    border-radius: 8px;
    padding: 1.25rem;
    margin-bottom: 1rem;
    border: 1px solid #262730;
}

/* Diagnosis input area */
.stTextArea textarea {
    background-color: #1a1c23;
    border: 1px solid #262730;
    border-radius: 6px;
    font-size: 0.9rem;
}
.stTextArea textarea:focus {
    border-color: #ff4b4b;
    box-shadow: 0 0 0 1px #ff4b4b;
}

/* Primary button */
.stButton > button[kind="primary"] {
    background-color: #ff4b4b;
    border: none;
    font-weight: 500;
}
.stButton > button[kind="primary"]:hover {
    background-color: #ff6b6b;
}

/* Progress/status messages */
.stAlert {
    border-radius: 6px;
    font-size: 0.85rem;
}

/* Hide streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Week badge */
.week-badge {
    display: inline-block;
    background-color: #262730;
    color: #ffffff;
    padding: 0.25rem 0.75rem;
    border-radius: 4px;
    font-size: 0.85rem;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)


def init_session_state():
    """Initialize session state variables."""
    if "diagnosis_report" not in st.session_state:
        st.session_state.diagnosis_report = None
    if "diagnosis_running" not in st.session_state:
        st.session_state.diagnosis_running = False
    if "diagnosis_progress" not in st.session_state:
        st.session_state.diagnosis_progress = []
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "report"


def render_sidebar():
    """Render the sidebar with week selector and connection status."""
    with st.sidebar:
        st.markdown("#### Steering Week")
        
        weeks = list_available_weeks()
        if not weeks:
            st.error("No steering reports found.")
            return None

        # Styled week selector
        selected_week = st.selectbox(
            "Steering Week",
            weeks,
            label_visibility="collapsed"
        )

        st.markdown("---")
        st.caption("CONNECTIONS")
        
        aws_ok, aws_msg = check_aws_credentials()
        db_ok, db_msg = check_databricks_connection()
        
        if aws_ok:
            st.markdown("✓ AWS Bedrock")
        else:
            st.markdown("✗ AWS Bedrock")
            
        if db_ok:
            st.markdown("✓ Databricks")
        else:
            st.markdown("✗ Databricks")

        if not aws_ok or not db_ok:
            with st.expander("Help"):
                if not aws_ok:
                    st.code("aws sso login --profile sso-bedrock", language="bash")
                if not db_ok:
                    st.caption("Check ~/.databrickscfg")

        return selected_week


def save_diagnosis_report(report: str, metric_query: str, week: str) -> str:
    """Save diagnosis report to file and return the path."""
    safe_query = "".join(c if c.isalnum() or c in " _-" else "_" for c in metric_query[:50])
    safe_query = safe_query.replace(" ", "_").lower()
    week_formatted = week.replace("-", "").lower()

    filename = f"{safe_query}_{week_formatted}_diagnosis.md"
    output_dir = Path(os.path.expanduser("~/Documents/temp"))
    output_dir.mkdir(parents=True, exist_ok=True)

    filepath = output_dir / filename
    filepath.write_text(report)

    return str(filepath)


def run_diagnosis(metric_query: str, week: str, progress_placeholder) -> dict:
    """Run the diagnosis and update progress."""
    progress_messages = []

    def progress_callback(message: str, iteration: int):
        progress_messages.append(f"[{iteration}] {message}")
        progress_placeholder.text("\n".join(progress_messages[-5:]))

    agent = DiagnosisAgent()
    try:
        result = agent.diagnose(
            metric_query=metric_query,
            week=week,
            progress_callback=progress_callback,
        )
        return result
    finally:
        agent.close()


def render_report_tab(selected_week: str):
    """Render the steering report view."""
    # Clean header without redundant info
    content = load_report(selected_week)
    st.markdown(content, unsafe_allow_html=True)


def render_diagnosis_tab(selected_week: str):
    """Render the diagnosis view."""
    st.markdown(f'<span class="week-badge">Week {selected_week}</span>', unsafe_allow_html=True)
    st.markdown("")
    
    diagnosis_query = st.text_area(
        "Describe the metric anomaly to investigate",
        placeholder="Example: Acceptance LL0 dropped from 90.28% to 88.18% in HF-INTL",
        height=80,
        label_visibility="visible"
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        diagnose_clicked = st.button(
            "Run Diagnosis",
            type="primary",
            use_container_width=True,
            disabled=st.session_state.diagnosis_running
        )
    with col2:
        if st.session_state.diagnosis_report:
            st.download_button(
                label="Download Report",
                data=st.session_state.diagnosis_report,
                file_name=f"diagnosis_{selected_week}.md",
                mime="text/markdown"
            )

    if diagnose_clicked and diagnosis_query.strip():
        st.session_state.diagnosis_running = True
        st.session_state.diagnosis_report = None

        st.markdown("---")
        progress_placeholder = st.empty()
        progress_placeholder.info("Starting diagnosis... (2-5 min)")

        result = run_diagnosis(diagnosis_query, selected_week, progress_placeholder)

        st.session_state.diagnosis_running = False

        if result["success"]:
            st.session_state.diagnosis_report = result["report"]
            progress_placeholder.success(
                f"Complete — {result['iterations']} iterations, {result['queries_run']} queries"
            )
            filepath = save_diagnosis_report(result["report"], diagnosis_query, selected_week)
            st.caption(f"Saved: `{filepath}`")
        else:
            progress_placeholder.error(f"Failed: {result.get('error', 'Unknown error')}")

    if st.session_state.diagnosis_report:
        st.markdown("---")
        st.markdown(st.session_state.diagnosis_report)


def main():
    """Main application entry point."""
    init_session_state()

    selected_week = render_sidebar()
    if not selected_week:
        st.stop()

    # Big title
    st.markdown("# Steering Dashboard")

    tab_report, tab_diagnosis = st.tabs(["Weekly Report", "Diagnosis"])

    with tab_report:
        render_report_tab(selected_week)

    with tab_diagnosis:
        render_diagnosis_tab(selected_week)


if __name__ == "__main__":
    main()
