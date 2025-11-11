"""
Pytest configuration and fixtures
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch
from typing import Dict, Any

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def mock_config():
    """Mock configuration values"""
    return {
        'SERVER_HOSTNAME': 'test-workspace.cloud.databricks.com',
        'HTTP_PATH': 'sql/protocolv1/o/test/test',
        'TOKEN': 'test_token',
        'DATABRICKS_HOST': 'https://test-workspace.cloud.databricks.com',
        'CLUSTER_ID': 'test-cluster-id'
    }


@pytest.fixture
def mock_sql_connection():
    """Mock Databricks SQL connection"""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    # Mock cursor description
    mock_cursor.description = [
        ('column1', 'string', None, None, None, None, None),
        ('column2', 'int', None, None, None, None, None)
    ]
    
    # Mock fetchall
    mock_cursor.fetchall.return_value = [
        Mock(column1='value1', column2=123),
        Mock(column1='value2', column2=456)
    ]
    
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_conn.cursor.return_value.__exit__.return_value = None
    
    return mock_conn, mock_cursor


@pytest.fixture
def mock_requests_response():
    """Mock requests response"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'success': True}
    mock_response.text = '{"success": true}'
    return mock_response


@pytest.fixture
def sample_table_data():
    """Sample table data for testing"""
    return [
        {'id': 1, 'name': 'Test 1', 'value': 100},
        {'id': 2, 'name': 'Test 2', 'value': 200},
        {'id': 3, 'name': 'Test 3', 'value': 300}
    ]


@pytest.fixture
def sample_notebook_content():
    """Sample notebook content"""
    return """# Databricks notebook source
# MAGIC %md
# MAGIC # Test Notebook
# MAGIC 
# MAGIC This is a test notebook.

# COMMAND ----------

print("Hello, Databricks!")
"""


