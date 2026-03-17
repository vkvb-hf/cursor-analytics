"""
Diagnosis Agent - LLM tool loop for steering metric diagnosis.

Uses AWS Bedrock Claude with a SQL tool to iteratively diagnose metric changes.
"""

import json
import os
from datetime import datetime
from typing import Any, Callable, Optional

import boto3
import pandas as pd

from utils.databricks_reader import DatabricksReader
from utils.diagnosis_prompts import SYSTEM_PROMPT, SQL_TOOL_DEFINITION, get_user_prompt


class DiagnosisAgent:
    """Agent that performs iterative diagnosis using Bedrock Claude and Databricks SQL."""

    def __init__(
        self,
        aws_profile: Optional[str] = None,
        aws_region: Optional[str] = None,
        model_id: Optional[str] = None,
        max_iterations: int = 30,
    ):
        self.aws_profile = aws_profile or os.getenv("AWS_PROFILE", "sso-bedrock")
        self.aws_region = aws_region or os.getenv("AWS_REGION", "eu-west-1")
        self.model_id = model_id or os.getenv(
            "BEDROCK_MODEL_ID",
            "eu.anthropic.claude-sonnet-4-20250514-v1:0"
        )
        self.max_iterations = max_iterations

        self._bedrock_client = None
        self._db_reader = None

    def _get_bedrock_client(self):
        """Get or create Bedrock client."""
        if self._bedrock_client is None:
            session = boto3.Session(profile_name=self.aws_profile)
            self._bedrock_client = session.client(
                "bedrock-runtime",
                region_name=self.aws_region
            )
        return self._bedrock_client

    def _get_db_reader(self):
        """Get or create Databricks reader."""
        if self._db_reader is None:
            self._db_reader = DatabricksReader()
        return self._db_reader

    def _execute_sql(self, sql: str, description: str = "") -> str:
        """Execute SQL query and return results as markdown table."""
        try:
            reader = self._get_db_reader()
            df = reader.execute_query(sql)

            if df.empty:
                return "Query returned no results."

            return df.to_markdown(index=False)

        except Exception as e:
            return f"SQL Error: {str(e)}"

    def _call_bedrock(
        self,
        messages: list[dict],
        system: str,
        tools: list[dict],
    ) -> dict:
        """Call Bedrock Claude API."""
        client = self._get_bedrock_client()

        response = client.converse(
            modelId=self.model_id,
            system=[{"text": system}],
            messages=messages,
            toolConfig={"tools": [{"toolSpec": t} for t in tools]},
            inferenceConfig={
                "maxTokens": 8192,
                "temperature": 0.0,
            }
        )

        return response

    def _process_tool_use(self, tool_use: dict) -> str:
        """Process a tool use request and return the result."""
        tool_name = tool_use.get("name")
        tool_input = tool_use.get("input", {})

        if tool_name == "run_sql":
            sql = tool_input.get("sql", "")
            description = tool_input.get("description", "")
            return self._execute_sql(sql, description)
        else:
            return f"Unknown tool: {tool_name}"

    def _extract_text_from_response(self, response: dict) -> str:
        """Extract text content from Bedrock response."""
        output = response.get("output", {})
        message = output.get("message", {})
        content = message.get("content", [])

        text_parts = []
        for block in content:
            if "text" in block:
                text_parts.append(block["text"])

        return "\n".join(text_parts)

    def _extract_tool_uses(self, response: dict) -> list[dict]:
        """Extract tool use blocks from Bedrock response."""
        output = response.get("output", {})
        message = output.get("message", {})
        content = message.get("content", [])

        tool_uses = []
        for block in content:
            if "toolUse" in block:
                tool_uses.append(block["toolUse"])

        return tool_uses

    def diagnose(
        self,
        metric_query: str,
        week: str,
        progress_callback: Optional[Callable[[str, int], None]] = None,
    ) -> dict:
        """
        Run iterative diagnosis and return the result.

        Args:
            metric_query: User's description of what to diagnose
            week: The week to analyze (e.g., "2026-W09")
            progress_callback: Optional callback(message, iteration) for progress updates

        Returns:
            dict with keys:
                - success: bool
                - report: str (markdown report if successful)
                - error: str (error message if failed)
                - iterations: int (number of tool loop iterations)
                - queries_run: int (number of SQL queries executed)
        """
        messages = [
            {
                "role": "user",
                "content": [{"text": get_user_prompt(metric_query, week)}]
            }
        ]

        tools = [SQL_TOOL_DEFINITION]
        iteration = 0
        queries_run = 0
        final_report = ""

        try:
            while iteration < self.max_iterations:
                iteration += 1

                if progress_callback:
                    progress_callback(f"Iteration {iteration}: Calling LLM...", iteration)

                response = self._call_bedrock(messages, SYSTEM_PROMPT, tools)

                stop_reason = response.get("stopReason", "")
                text_content = self._extract_text_from_response(response)
                tool_uses = self._extract_tool_uses(response)

                if text_content:
                    final_report = text_content

                if stop_reason == "end_turn" and not tool_uses:
                    if progress_callback:
                        progress_callback("Diagnosis complete!", iteration)
                    break

                if tool_uses:
                    assistant_content = []
                    if text_content:
                        assistant_content.append({"text": text_content})
                    for tu in tool_uses:
                        assistant_content.append({"toolUse": tu})

                    messages.append({
                        "role": "assistant",
                        "content": assistant_content
                    })

                    tool_results = []
                    for tu in tool_uses:
                        tool_id = tu.get("toolUseId")
                        tool_name = tu.get("name")
                        tool_input = tu.get("input", {})

                        if progress_callback:
                            desc = tool_input.get("description", "Running SQL query")
                            progress_callback(f"Iteration {iteration}: {desc}", iteration)

                        result = self._process_tool_use(tu)
                        queries_run += 1

                        tool_results.append({
                            "toolResult": {
                                "toolUseId": tool_id,
                                "content": [{"text": result}]
                            }
                        })

                    messages.append({
                        "role": "user",
                        "content": tool_results
                    })

                elif stop_reason == "end_turn":
                    break

            return {
                "success": True,
                "report": final_report,
                "iterations": iteration,
                "queries_run": queries_run,
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "iterations": iteration,
                "queries_run": queries_run,
            }

    def close(self):
        """Close resources (no-op for Statement Execution API)."""
        self._db_reader = None


def check_aws_credentials(profile: str = "sso-bedrock") -> tuple[bool, str]:
    """Check if AWS credentials are valid."""
    try:
        session = boto3.Session(profile_name=profile)
        sts = session.client("sts")
        identity = sts.get_caller_identity()
        return True, f"Authenticated as {identity.get('Arn', 'unknown')}"
    except Exception as e:
        return False, str(e)


def check_databricks_connection() -> tuple[bool, str]:
    """Check if Databricks connection is valid."""
    from utils.databricks_reader import check_databricks_connection as db_check
    return db_check()
