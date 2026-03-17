"""
Databricks Reader - Database connection utilities using Statement Execution API.

Uses the Databricks Statement Execution API (same as MCP) for SQL queries.
"""

import configparser
import json
import os
import time
from pathlib import Path
from typing import Any, Optional

import pandas as pd
import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def _load_databricks_config() -> tuple[Optional[str], Optional[str], Optional[str]]:
    """Load host, token, and warehouse_id from ~/.databrickscfg if available."""
    config_path = Path.home() / ".databrickscfg"
    if not config_path.exists():
        return None, None, None

    config = configparser.ConfigParser()
    config.read(config_path)

    if "DEFAULT" in config:
        host = config["DEFAULT"].get("host", "").strip().rstrip("/")
        token = config["DEFAULT"].get("token", "").strip()
        warehouse_id = config["DEFAULT"].get("warehouse_id", "").strip()
        return host, token, warehouse_id

    return None, None, None


class DatabricksReader:
    """Database connection and query execution for Databricks using Statement Execution API."""

    def __init__(
        self,
        host: Optional[str] = None,
        token: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ):
        cfg_host, cfg_token, cfg_warehouse_id = _load_databricks_config()

        self.host = host or os.getenv("DATABRICKS_HOST") or cfg_host
        self.token = token or os.getenv("DATABRICKS_TOKEN") or cfg_token
        self.warehouse_id = warehouse_id or os.getenv("DATABRICKS_WAREHOUSE_ID") or cfg_warehouse_id

        if self.host:
            self.host = self.host.rstrip("/")

    def _get_headers(self) -> dict:
        """Get request headers with authorization."""
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def execute_query(self, query: str, timeout_seconds: int = 300) -> pd.DataFrame:
        """
        Execute SQL query using Statement Execution API and return DataFrame.
        
        Args:
            query: SQL query to execute
            timeout_seconds: Maximum time to wait for query completion
            
        Returns:
            pandas DataFrame with query results
        """
        if not all([self.host, self.token]):
            missing = []
            if not self.host:
                missing.append("DATABRICKS_HOST")
            if not self.token:
                missing.append("DATABRICKS_TOKEN")
            raise ValueError(
                f"Missing Databricks credentials: {', '.join(missing)}. "
                "Set environment variables or create ~/.databrickscfg"
            )

        url = f"{self.host}/api/2.0/sql/statements"
        
        payload = {
            "statement": query,
            "wait_timeout": "50s",
            "on_wait_timeout": "CONTINUE",
        }
        
        if self.warehouse_id:
            payload["warehouse_id"] = self.warehouse_id

        response = requests.post(url, headers=self._get_headers(), json=payload)
        response.raise_for_status()
        result = response.json()

        statement_id = result.get("statement_id")
        status = result.get("status", {}).get("state")

        start_time = time.time()
        while status in ("PENDING", "RUNNING"):
            if time.time() - start_time > timeout_seconds:
                raise TimeoutError(f"Query timed out after {timeout_seconds} seconds")
            
            time.sleep(2)
            
            poll_url = f"{self.host}/api/2.0/sql/statements/{statement_id}"
            poll_response = requests.get(poll_url, headers=self._get_headers())
            poll_response.raise_for_status()
            result = poll_response.json()
            status = result.get("status", {}).get("state")

        if status == "FAILED":
            error = result.get("status", {}).get("error", {})
            raise RuntimeError(f"Query failed: {error.get('message', 'Unknown error')}")

        if status != "SUCCEEDED":
            raise RuntimeError(f"Unexpected query status: {status}")

        return self._result_to_dataframe(result)

    def _result_to_dataframe(self, result: dict) -> pd.DataFrame:
        """Convert Statement Execution API result to pandas DataFrame."""
        manifest = result.get("manifest", {})
        schema = manifest.get("schema", {})
        columns = schema.get("columns", [])
        
        column_names = [col.get("name") for col in columns]
        
        data_result = result.get("result", {})
        data_array = data_result.get("data_array", [])
        
        return pd.DataFrame(data_array, columns=column_names)

    def test_connection(self) -> tuple[bool, str]:
        """Test the database connection."""
        try:
            df = self.execute_query("SELECT 1 as test")
            return True, "Connected to Databricks"
        except Exception as e:
            return False, str(e)


def check_databricks_connection() -> tuple[bool, str]:
    """Check if Databricks connection is valid."""
    try:
        reader = DatabricksReader()
        return reader.test_connection()
    except Exception as e:
        return False, str(e)
