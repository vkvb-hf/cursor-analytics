"""
Databricks Reader - Low-level database connection utilities.
"""

import configparser
import os
from pathlib import Path
from typing import Optional

import pandas as pd
from databricks import sql

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def _load_databricks_config() -> tuple[Optional[str], Optional[str]]:
    """Load host and token from ~/.databrickscfg if available."""
    config_path = Path.home() / ".databrickscfg"
    if not config_path.exists():
        return None, None

    config = configparser.ConfigParser()
    config.read(config_path)

    if "DEFAULT" in config:
        host = config["DEFAULT"].get("host", "").strip()
        token = config["DEFAULT"].get("token", "").strip()
        return host, token

    return None, None


class DatabricksReader:
    """Database connection and query execution for Databricks."""

    def __init__(
        self,
        host: Optional[str] = None,
        token: Optional[str] = None,
        http_path: Optional[str] = None,
    ):
        cfg_host, cfg_token = _load_databricks_config()

        self.host = host or os.getenv("DATABRICKS_HOST") or cfg_host
        self.token = token or os.getenv("DATABRICKS_TOKEN") or cfg_token
        self.http_path = http_path or os.getenv("DATABRICKS_HTTP_PATH")
        
        self.server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME")
        if not self.server_hostname and self.host:
            self.server_hostname = self.host.replace("https://", "").replace("http://", "").rstrip("/")

    def get_connection(self):
        """Establish connection to Databricks SQL warehouse."""
        if not all([self.server_hostname, self.token, self.http_path]):
            missing = []
            if not self.server_hostname:
                missing.append("DATABRICKS_SERVER_HOSTNAME or DATABRICKS_HOST")
            if not self.token:
                missing.append("DATABRICKS_TOKEN")
            if not self.http_path:
                missing.append("DATABRICKS_HTTP_PATH")
            raise ValueError(
                f"Missing Databricks credentials: {', '.join(missing)}. "
                "Set environment variables or create a .env file."
            )

        return sql.connect(
            server_hostname=self.server_hostname,
            http_path=self.http_path,
            access_token=self.token,
        )

    @staticmethod
    def get_data_to_pandas(connection, query: str) -> pd.DataFrame:
        """Execute query and return DataFrame."""
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            return pd.DataFrame(data, columns=columns)
        finally:
            cursor.close()
