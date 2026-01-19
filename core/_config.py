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
    
    Returns:
        DatabricksConfig namedtuple with all connection settings
    """
    _load_dotenv()
    
    token = os.getenv('DATABRICKS_TOKEN')
    if not token:
        print("⚠️  WARNING: DATABRICKS_TOKEN not set!", file=sys.stderr)
        print("   Create a .env file with your token or set the environment variable.", file=sys.stderr)
    
    return DatabricksConfig(
        SERVER_HOSTNAME=os.getenv('DATABRICKS_SERVER_HOSTNAME', 'hf-gp.cloud.databricks.com'),
        HTTP_PATH=os.getenv('DATABRICKS_HTTP_PATH', 'sql/protocolv1/o/4157495209488006/0319-154505-47yntzz2'),
        TOKEN=token or '',
        DATABRICKS_HOST=os.getenv('DATABRICKS_HOST', 'https://hf-gp.cloud.databricks.com'),
        CLUSTER_ID=os.getenv('CLUSTER_ID', '0319-154505-47yntzz2'),
    )


# For backward compatibility - load config on import
_config = get_config()
SERVER_HOSTNAME = _config.SERVER_HOSTNAME
HTTP_PATH = _config.HTTP_PATH
TOKEN = _config.TOKEN
DATABRICKS_HOST = _config.DATABRICKS_HOST
CLUSTER_ID = _config.CLUSTER_ID
