"""
Report loader for steering dashboard.
Loads markdown report files from local git repository.
"""

import os
import re
from pathlib import Path
from typing import List

import streamlit as st

DEFAULT_REPORTS_DIR = os.path.expanduser(
    "~/Documents/GitHub/cursor-analytics/projects/long_term_steering_report"
)


def get_reports_dir() -> Path:
    """Get the reports directory path from env var or default."""
    return Path(os.getenv("STEERING_REPORTS_DIR", DEFAULT_REPORTS_DIR))


@st.cache_data(ttl=60)
def list_available_weeks() -> List[str]:
    """
    Return list of available weeks like ['2026-W11', '2026-W10', ...].
    Sorted with most recent first.
    """
    dir_path = get_reports_dir()
    if not dir_path.exists():
        st.warning(f"Reports directory not found: {dir_path}")
        return []

    pattern = re.compile(r"(\d{4})_W(\d{2})_steering_report_v2\.md")
    weeks = []

    for f in dir_path.glob("*_steering_report_v2.md"):
        match = pattern.match(f.name)
        if match:
            weeks.append(f"{match.group(1)}-W{match.group(2)}")

    return sorted(weeks, reverse=True)


@st.cache_data(ttl=60)
def load_report(week: str) -> str:
    """
    Load markdown content for a specific week.
    
    Args:
        week: Week string like '2026-W10'
        
    Returns:
        Markdown content as string
    """
    dir_path = get_reports_dir()
    year, week_num = week.split("-W")
    filename = f"{year}_W{week_num}_steering_report_v2.md"
    filepath = dir_path / filename

    if not filepath.exists():
        return f"**Report not found:** `{filepath}`\n\nMake sure to run `git pull` in the cursor-analytics repository."

    return filepath.read_text()
