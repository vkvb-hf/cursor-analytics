#!/usr/bin/env python3
"""
GitHub Analytics MCP Server

Tools:
- get_pr_build_status: Check if PR build/release workflow is complete

Configuration:
- GITHUB_TOKEN: Personal access token with repo scope
"""

import os
import sys
import requests
from pathlib import Path
from typing import Any

try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("MCP SDK not installed. Install with: pip install mcp", file=sys.stderr)
    sys.exit(1)

mcp = FastMCP("GitHub Analytics MCP")


def get_github_token() -> str:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable not set")
    return token


def github_api_request(endpoint: str, params: dict = None) -> dict:
    token = get_github_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(f"https://api.github.com{endpoint}", headers=headers, params=params)
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_pr_build_status(
    owner: str,
    repo: str,
    pull_number: int,
    check_name: str = "Release"
) -> dict[str, Any]:
    """
    Check if a PR's build/release workflow is complete.
    
    This is useful for checking if a PR is ready to be merged or if you can
    trigger downstream processes that depend on the build.
    
    The default check_name "Release" matches the "PR: Test and Release / Release" 
    workflow used in ddi-pays-pipelines and similar repos.

    Args:
        owner: Repository owner (e.g., "hellofresh")
        repo: Repository name (e.g., "ddi-pays-pipelines")
        pull_number: Pull request number
        check_name: Name of the check to look for (default: "Release")

    Returns:
        JSON with: 
        - success: bool
        - build_complete: bool (True if the specified check completed successfully)
        - build_status: str ("success", "failure", "in_progress", "pending", "not_found")
        - check_name: str
        - conclusion: str (if completed)
        - all_checks_passed: bool
        - checks_summary: dict with counts by status
        - details: list of relevant check runs
    """
    try:
        pr_data = github_api_request(f"/repos/{owner}/{repo}/pulls/{pull_number}")
        head_sha = pr_data["head"]["sha"]
        
        check_runs_data = github_api_request(
            f"/repos/{owner}/{repo}/commits/{head_sha}/check-runs",
            params={"per_page": 100}
        )
        
        check_runs = check_runs_data.get("check_runs", [])
        
        # Find the target check
        target_check = None
        for check in check_runs:
            if check["name"] == check_name:
                target_check = check
                break
        
        # Summarize all checks
        summary = {"total": len(check_runs), "completed": 0, "in_progress": 0, 
                   "queued": 0, "success": 0, "failure": 0, "skipped": 0, "neutral": 0}
        
        all_passed = True
        for check in check_runs:
            status = check["status"]
            conclusion = check.get("conclusion")
            
            if status == "completed":
                summary["completed"] += 1
                if conclusion == "success":
                    summary["success"] += 1
                elif conclusion == "failure":
                    summary["failure"] += 1
                    all_passed = False
                elif conclusion == "skipped":
                    summary["skipped"] += 1
                elif conclusion == "neutral":
                    summary["neutral"] += 1
                else:
                    all_passed = False
            elif status == "in_progress":
                summary["in_progress"] += 1
                all_passed = False
            else:
                summary["queued"] += 1
                all_passed = False
        
        # Determine build status
        if target_check is None:
            build_status, build_complete, conclusion = "not_found", False, None
        elif target_check["status"] == "completed":
            conclusion = target_check["conclusion"]
            build_complete, build_status = True, conclusion or "completed"
        else:
            build_status, build_complete, conclusion = target_check["status"], False, None
        
        # Important checks only (non-skipped, non-neutral, or still running)
        details = [
            {"name": c["name"], "status": c["status"], "conclusion": c.get("conclusion")}
            for c in check_runs
            if c.get("conclusion") not in ["skipped", "neutral"] or c["status"] != "completed"
        ]
        
        return {
            "success": True,
            "build_complete": build_complete and conclusion == "success",
            "build_status": build_status,
            "check_name": check_name,
            "conclusion": conclusion,
            "all_checks_passed": all_passed,
            "checks_summary": summary,
            "pr_number": pull_number,
            "head_sha": head_sha[:8],
            "details": details
        }
        
    except requests.exceptions.HTTPError as e:
        error_msg = str(e)
        try:
            error_msg = e.response.json().get("message", str(e))
        except:
            pass
        return {"success": False, "build_complete": False, "build_status": "error", 
                "error": error_msg, "pr_number": pull_number}
    except Exception as e:
        return {"success": False, "build_complete": False, "build_status": "error",
                "error": str(e), "pr_number": pull_number}


if __name__ == "__main__":
    mcp.run()
