"""
Tests for Databricks MCP Server (mcp/databricks/server.py)

Tests the MCP server components without requiring actual connections.
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch
from pathlib import Path
from collections import namedtuple

# Get the path to the MCP server
MCP_PATH = Path(__file__).parent.parent / 'mcp' / 'databricks'


class TestDatabricksMCPServerSyntax:
    """Test that the MCP server has valid syntax and structure"""
    
    def test_server_file_exists(self):
        """Test server.py exists"""
        server_path = MCP_PATH / 'server.py'
        assert server_path.exists(), f"Server file not found at {server_path}"
    
    def test_server_syntax_valid(self):
        """Test server.py has valid Python syntax"""
        import ast
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # This will raise SyntaxError if invalid
        ast.parse(content)
    
    def test_server_has_required_components(self):
        """Test server.py contains required MCP components"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Check for key components
        assert 'class ConnectionPool' in content
        assert 'class DatabricksClient' in content
        assert 'def list_tools' in content
        assert 'def call_tool' in content
        assert 'execute_sql' in content
        assert 'run_notebook' in content
        assert 'sync_to_workspace' in content


class TestDatabricksClientUnit:
    """Unit tests for DatabricksClient class (no actual connections)"""
    
    def test_client_class_exists(self):
        """Test DatabricksClient class can be imported"""
        # Read the server file and extract the class
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        assert 'class DatabricksClient' in content
    
    def test_client_has_required_methods(self):
        """Test DatabricksClient has required methods"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        required_methods = [
            'def create_notebook',
            'def create_job',
            'def run_job',
            'def get_run_status',
            'def upload_file',
            'def download_file',
            'def sync_to_workspace',
            'def sync_from_workspace',
        ]
        
        for method in required_methods:
            assert method in content, f"Missing method: {method}"


class TestMCPToolDefinitions:
    """Test MCP tool definitions"""
    
    def test_all_tools_defined(self):
        """Test all expected tools are defined in server"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        expected_tools = [
            'execute_sql',
            'run_sql_file',
            'create_notebook',
            'run_notebook',
            'get_job_status',
            'sync_to_workspace',
            'sync_from_workspace'
        ]
        
        for tool in expected_tools:
            assert f'name="{tool}"' in content, f"Missing tool definition: {tool}"
    
    def test_tool_descriptions_exist(self):
        """Test tools have descriptions"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Each Tool should have a description
        assert content.count('description=') >= 7, "Not all tools have descriptions"


class TestConnectionPoolUnit:
    """Unit tests for ConnectionPool class"""
    
    def test_connection_pool_class_exists(self):
        """Test ConnectionPool class exists"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        assert 'class ConnectionPool' in content
    
    def test_connection_pool_has_required_methods(self):
        """Test ConnectionPool has required methods"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        required_methods = [
            'def get_connection',
            'def execute_query',
            'def close',
        ]
        
        for method in required_methods:
            assert method in content, f"Missing method: {method}"


class TestConfigLoading:
    """Test configuration loading logic"""
    
    def test_config_function_exists(self):
        """Test load_config function exists"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        assert 'def load_config' in content
    
    def test_config_reads_env_vars(self):
        """Test config reads expected environment variables"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        expected_vars = [
            'DATABRICKS_HOST',
            'DATABRICKS_TOKEN',
            'DATABRICKS_HTTP_PATH',
            'CLUSTER_ID',
        ]
        
        for var in expected_vars:
            assert var in content, f"Missing env var: {var}"
