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

st.title("📊 Steering Report")


def init_session_state():
    """Initialize session state variables."""
    if "diagnosis_report" not in st.session_state:
        st.session_state.diagnosis_report = None
    if "diagnosis_running" not in st.session_state:
        st.session_state.diagnosis_running = False
    if "diagnosis_progress" not in st.session_state:
        st.session_state.diagnosis_progress = []


def render_sidebar():
    """Render the sidebar with week selector and connection status."""
    with st.sidebar:
        st.header("Settings")

        weeks = list_available_weeks()
        if not weeks:
            st.error("No steering reports found. Check STEERING_REPORTS_DIR.")
            return None

        selected_week = st.selectbox(
            "Select Week",
            weeks,
            help="Choose which week's steering report to view"
        )

        st.divider()

        st.subheader("Connection Status")

        aws_ok, aws_msg = check_aws_credentials()
        if aws_ok:
            st.success("✅ AWS Bedrock")
        else:
            st.error("❌ AWS Bedrock")
            with st.expander("Details"):
                st.caption(aws_msg)
                st.code("aws sso login --profile sso-bedrock", language="bash")

        db_ok, db_msg = check_databricks_connection()
        if db_ok:
            st.success("✅ Databricks")
        else:
            st.error("❌ Databricks")
            with st.expander("Details"):
                st.caption(db_msg)
                st.caption("Check ~/.databrickscfg or DATABRICKS_* env vars")

        st.divider()

        if st.button("🗑️ Clear Diagnosis", use_container_width=True):
            st.session_state.diagnosis_report = None
            st.session_state.diagnosis_progress = []
            st.rerun()

        return selected_week


def render_report(content: str):
    """Render the steering report markdown."""
    st.markdown(content, unsafe_allow_html=True)


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


def render_diagnosis_panel(selected_week: str):
    """Render the diagnosis input and results panel."""
    st.subheader("🔍 Diagnosis")

    diagnosis_query = st.text_area(
        "What do you want to diagnose?",
        placeholder="e.g., Acceptance LL0 dropped 2.32% in HF-INTL\n\nor\n\nWhy did Recovery W0 increase 17.61% overall?",
        height=120,
        help="Describe the metric change you want to investigate"
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        diagnose_clicked = st.button(
            "🚀 Diagnose",
            type="primary",
            use_container_width=True,
            disabled=st.session_state.diagnosis_running
        )
    with col2:
        if st.button("📋 Example", use_container_width=True):
            st.info("Try: 'Acceptance LL0 (Initial Charge) dropped from 90.28% to 88.18% in HF-INTL'")

    if diagnose_clicked and diagnosis_query.strip():
        st.session_state.diagnosis_running = True
        st.session_state.diagnosis_report = None

        st.divider()
        st.markdown(f"**Diagnosing for {selected_week}:**")
        st.markdown(f"> {diagnosis_query}")

        progress_placeholder = st.empty()
        progress_placeholder.info("Starting diagnosis... This may take 2-5 minutes.")

        result = run_diagnosis(diagnosis_query, selected_week, progress_placeholder)

        st.session_state.diagnosis_running = False

        if result["success"]:
            st.session_state.diagnosis_report = result["report"]

            progress_placeholder.success(
                f"✅ Diagnosis complete! "
                f"({result['iterations']} iterations, {result['queries_run']} queries)"
            )

            filepath = save_diagnosis_report(
                result["report"],
                diagnosis_query,
                selected_week
            )
            st.caption(f"Report saved to: `{filepath}`")

        else:
            progress_placeholder.error(f"❌ Diagnosis failed: {result.get('error', 'Unknown error')}")

    if st.session_state.diagnosis_report:
        st.divider()
        st.subheader("📄 Diagnosis Report")

        with st.container(height=600):
            st.markdown(st.session_state.diagnosis_report)

        st.download_button(
            label="📥 Download Report",
            data=st.session_state.diagnosis_report,
            file_name=f"diagnosis_{selected_week}.md",
            mime="text/markdown",
            use_container_width=True
        )


def main():
    """Main application entry point."""
    init_session_state()

    selected_week = render_sidebar()
    if not selected_week:
        st.stop()

    col_report, col_diagnosis = st.columns([3, 2])

    with col_report:
        st.subheader(f"Week {selected_week}")
        content = load_report(selected_week)
        with st.container(height=800):
            render_report(content)

    with col_diagnosis:
        render_diagnosis_panel(selected_week)


if __name__ == "__main__":
    main()
