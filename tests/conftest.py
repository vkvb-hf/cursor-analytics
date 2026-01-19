"""
Pytest configuration and fixtures

This module provides shared fixtures for all tests in cursor-analytics.
Fixtures are automatically discovered by pytest.

Usage:
    def test_something(mock_config, mock_sql_connection):
        # Use fixtures directly as function parameters
        pass
"""
import pytest
import sys
import os
import tempfile
from pathlib import Path
from unittest.mock import Mock, MagicMock, patch
from typing import Dict, Any, Tuple
from collections import namedtuple

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# =============================================================================
# CONFIGURATION FIXTURES
# =============================================================================

@pytest.fixture
def mock_config():
    """Mock configuration values as dictionary"""
    return {
        'SERVER_HOSTNAME': 'test-workspace.cloud.databricks.com',
        'HTTP_PATH': 'sql/protocolv1/o/test/test',
        'TOKEN': 'test_token',
        'DATABRICKS_HOST': 'https://test-workspace.cloud.databricks.com',
        'CLUSTER_ID': 'test-cluster-id'
    }


@pytest.fixture
def mock_env_vars():
    """Set up mock environment variables for tests"""
    env_vars = {
        'DATABRICKS_HOST': 'https://test.cloud.databricks.com',
        'DATABRICKS_TOKEN': 'test-token-12345',
        'DATABRICKS_HTTP_PATH': '/sql/1.0/warehouses/test',
        'DATABRICKS_SERVER_HOSTNAME': 'test.cloud.databricks.com',
        'CLUSTER_ID': 'test-cluster-123'
    }
    with patch.dict(os.environ, env_vars, clear=False):
        yield env_vars


@pytest.fixture
def reset_connection_pool_singleton():
    """Reset the ConnectionPool singleton between tests"""
    from core.connection_pool import ConnectionPool
    original_instance = ConnectionPool._instance
    ConnectionPool._instance = None
    yield
    ConnectionPool._instance = original_instance


# =============================================================================
# DATABASE CONNECTION FIXTURES
# =============================================================================

@pytest.fixture
def mock_sql_connection() -> Tuple[MagicMock, MagicMock]:
    """Mock Databricks SQL connection and cursor"""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    # Mock cursor description (column metadata)
    mock_cursor.description = [
        ('column1', 'string', None, None, None, None, None),
        ('column2', 'int', None, None, None, None, None)
    ]
    
    # Mock fetchall with namedtuple results
    Row = namedtuple('Row', ['column1', 'column2'])
    mock_cursor.fetchall.return_value = [
        Row('value1', 123),
        Row('value2', 456)
    ]
    
    # Setup context manager
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_conn.cursor.return_value.__exit__.return_value = None
    
    return mock_conn, mock_cursor


@pytest.fixture
def mock_connection_pool(mock_sql_connection):
    """Mock the entire connection pool"""
    mock_conn, mock_cursor = mock_sql_connection
    
    with patch('core.connection_pool.ConnectionPool') as MockPool:
        mock_instance = MagicMock()
        mock_instance.execute.return_value = mock_cursor.fetchall.return_value
        mock_instance.get_connection.return_value = mock_conn
        MockPool.get_instance.return_value = mock_instance
        MockPool._instance = mock_instance
        yield mock_instance


# =============================================================================
# HTTP/API FIXTURES
# =============================================================================

@pytest.fixture
def mock_requests_response():
    """Mock requests response for API calls"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'success': True}
    mock_response.text = '{"success": true}'
    mock_response.raise_for_status = MagicMock()
    return mock_response


@pytest.fixture
def mock_requests_error_response():
    """Mock requests error response"""
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.json.return_value = {'error': 'Internal Server Error'}
    mock_response.text = '{"error": "Internal Server Error"}'
    mock_response.raise_for_status.side_effect = Exception("500 Server Error")
    return mock_response


# =============================================================================
# SAMPLE DATA FIXTURES
# =============================================================================

@pytest.fixture
def sample_table_data():
    """Sample table data for testing"""
    return [
        {'id': 1, 'name': 'Test 1', 'value': 100},
        {'id': 2, 'name': 'Test 2', 'value': 200},
        {'id': 3, 'name': 'Test 3', 'value': 300}
    ]


@pytest.fixture
def sample_query_results():
    """Sample query results as namedtuples"""
    Row = namedtuple('Row', ['id', 'name', 'value', 'created_at'])
    return [
        Row(1, 'Alice', 100.50, '2024-01-15'),
        Row(2, 'Bob', 200.75, '2024-01-16'),
        Row(3, 'Charlie', 300.00, '2024-01-17'),
    ]


@pytest.fixture
def sample_schema_data():
    """Sample table schema data"""
    return [
        {'column': 'id', 'data_type': 'bigint', 'comment': 'Primary key'},
        {'column': 'name', 'data_type': 'string', 'comment': 'User name'},
        {'column': 'email', 'data_type': 'string', 'comment': 'Email address'},
        {'column': 'created_at', 'data_type': 'timestamp', 'comment': 'Creation time'},
    ]


@pytest.fixture
def sample_notebook_content():
    """Sample Databricks notebook content"""
    return """# Databricks notebook source
# MAGIC %md
# MAGIC # Test Notebook
# MAGIC 
# MAGIC This is a test notebook.

# COMMAND ----------

print("Hello, Databricks!")

# COMMAND ----------

df = spark.sql("SELECT * FROM test_table LIMIT 10")
display(df)
"""


# =============================================================================
# FILE SYSTEM FIXTURES
# =============================================================================

@pytest.fixture
def temp_directory():
    """Create a temporary directory for tests"""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def temp_sql_file(temp_directory):
    """Create a temporary SQL file"""
    sql_file = temp_directory / "test_query.sql"
    sql_file.write_text("SELECT id, name FROM users WHERE active = true LIMIT 100")
    return sql_file


@pytest.fixture
def temp_python_files(temp_directory):
    """Create temporary Python files for sync tests"""
    files = []
    for i in range(3):
        py_file = temp_directory / f"script_{i}.py"
        py_file.write_text(f"# Script {i}\nprint('Hello from script {i}')")
        files.append(py_file)
    return files


# =============================================================================
# MCP SERVER FIXTURES
# =============================================================================

@pytest.fixture
def mock_databricks_job_runner():
    """Mock DatabricksJobRunner for MCP tests"""
    with patch('core.databricks_job_runner.DatabricksJobRunner') as MockRunner:
        mock_runner = MagicMock()
        mock_runner.create_notebook.return_value = True
        mock_runner.create_job.return_value = 123
        mock_runner.run_job.return_value = 456
        mock_runner.get_run_status.return_value = {
            'state': {
                'life_cycle_state': 'TERMINATED',
                'result_state': 'SUCCESS'
            }
        }
        MockRunner.return_value = mock_runner
        yield mock_runner


@pytest.fixture
def mock_workspace_sync():
    """Mock WorkspaceSync for MCP tests"""
    with patch('core.workspace_sync.WorkspaceSync') as MockSync:
        mock_sync = MagicMock()
        mock_sync.sync_to_workspace.return_value = {
            'success': True,
            'total': 1,
            'success': [{'file': 'test.py'}],
            'failed': []
        }
        mock_sync.sync_from_workspace.return_value = {
            'success': True,
            'files_synced': 1
        }
        MockSync.return_value = mock_sync
        yield mock_sync


# =============================================================================
# PYTEST CONFIGURATION
# =============================================================================

def pytest_configure(config):
    """Configure pytest markers"""
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests (may require mocked services)"
    )
    config.addinivalue_line(
        "markers", "slow: marks tests as slow running"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection based on markers"""
    # Add skip marker for integration tests if --skip-integration is passed
    if config.getoption("--skip-integration", default=False):
        skip_integration = pytest.mark.skip(reason="--skip-integration option provided")
        for item in items:
            if "integration" in item.keywords:
                item.add_marker(skip_integration)


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--skip-integration",
        action="store_true",
        default=False,
        help="Skip integration tests"
    )

