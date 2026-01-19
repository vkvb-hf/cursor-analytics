"""
Configuration loader for cursor-analytics

This module provides a clean way to load configuration that works both:
1. When the package is installed (pip install -e .)
2. When running scripts directly from the repo

Usage in core modules:
    from core._config import get_config
    config = get_config()
    # Then use config.SERVER_HOSTNAME, config.TOKEN, etc.

Or for backward compatibility:
    from core._config import SERVER_HOSTNAME, HTTP_PATH, TOKEN, DATABRICKS_HOST, CLUSTER_ID
"""
import os
import sys
from pathlib import Path
from typing import NamedTuple

class DatabricksConfig(NamedTuple):
    """Configuration container for Databricks connection"""
    SERVER_HOSTNAME: str
    HTTP_PATH: str
    TOKEN: str
    DATABRICKS_HOST: str
    CLUSTER_ID: str


def _load_dotenv():
    """Load .env file if python-dotenv is available"""
    try:
        from dotenv import load_dotenv
        # Try multiple locations for .env
        possible_paths = [
            Path(__file__).parent.parent / '.env',  # repo root
            Path.cwd() / '.env',  # current directory
        ]
        for env_path in possible_paths:
            if env_path.exists():
                load_dotenv(env_path)
                return True
    except ImportError:
        pass
    return False


def get_config() -> DatabricksConfig:
    """
    Get Databricks configuration from environment variables.
    
    All configuration values MUST be set via environment variables or .env file.
    No defaults are provided for security reasons.
    
    Required environment variables:
        - DATABRICKS_TOKEN: Personal access token
        - DATABRICKS_SERVER_HOSTNAME: Workspace hostname (e.g., your-workspace.cloud.databricks.com)
        - DATABRICKS_HTTP_PATH: SQL warehouse HTTP path
        - DATABRICKS_HOST: Full workspace URL (e.g., https://your-workspace.cloud.databricks.com)
        - CLUSTER_ID: Cluster ID for notebook jobs
    
    Returns:
        DatabricksConfig namedtuple with all connection settings
    
    Raises:
        ValueError: If required configuration is missing
    """
    _load_dotenv()
    
    # Check for required configuration
    missing = []
    
    token = os.getenv('DATABRICKS_TOKEN')
    if not token:
        missing.append('DATABRICKS_TOKEN')
    
    server_hostname = os.getenv('DATABRICKS_SERVER_HOSTNAME')
    if not server_hostname:
        missing.append('DATABRICKS_SERVER_HOSTNAME')
    
    http_path = os.getenv('DATABRICKS_HTTP_PATH')
    if not http_path:
        missing.append('DATABRICKS_HTTP_PATH')
    
    databricks_host = os.getenv('DATABRICKS_HOST')
    if not databricks_host:
        missing.append('DATABRICKS_HOST')
    
    cluster_id = os.getenv('CLUSTER_ID')
    if not cluster_id:
        missing.append('CLUSTER_ID')
    
    if missing:
        print(f"⚠️  WARNING: Missing required configuration: {', '.join(missing)}", file=sys.stderr)
        print("   Create a .env file or set environment variables.", file=sys.stderr)
        print("   See docs/SETUP.md for configuration instructions.", file=sys.stderr)
    
    return DatabricksConfig(
        SERVER_HOSTNAME=server_hostname or '',
        HTTP_PATH=http_path or '',
        TOKEN=token or '',
        DATABRICKS_HOST=databricks_host or '',
        CLUSTER_ID=cluster_id or '',
    )


# For backward compatibility - load config on import
_config = get_config()
SERVER_HOSTNAME = _config.SERVER_HOSTNAME
HTTP_PATH = _config.HTTP_PATH
TOKEN = _config.TOKEN
DATABRICKS_HOST = _config.DATABRICKS_HOST
CLUSTER_ID = _config.CLUSTER_ID
