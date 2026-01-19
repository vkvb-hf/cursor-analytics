"""
Tests for Databricks MCP Server (mcp/databricks/server.py)

Tests the MCP server components without requiring actual connections.
Updated to reflect the FastMCP architecture.
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch
from pathlib import Path
from collections import namedtuple

# Get paths
MCP_PATH = Path(__file__).parent.parent / 'mcp' / 'databricks'
CORE_PATH = Path(__file__).parent.parent / 'core'


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
    
    def test_server_uses_fastmcp(self):
        """Test server.py uses FastMCP pattern"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Check for FastMCP pattern
        assert 'from mcp.server.fastmcp import FastMCP' in content, "Should import FastMCP"
        assert 'mcp = FastMCP' in content, "Should initialize FastMCP"
        assert '@mcp.tool()' in content, "Should use @mcp.tool() decorator"
    
    def test_server_has_required_tools(self):
        """Test server.py contains all required tool definitions"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        required_tools = [
            'def execute_sql',
            'def run_sql_file',
            'def create_notebook',
            'def run_notebook',
            'def get_job_status',
            'def sync_to_workspace',
            'def sync_from_workspace'
        ]
        
        for tool in required_tools:
            assert tool in content, f"Missing tool: {tool}"
    
    def test_server_imports_from_core(self):
        """Test server imports from core modules"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        expected_imports = [
            'from core._config import',
            'from core.connection_pool import',
            'from core.databricks_job_runner import',
            'from core.workspace_sync import',
        ]
        
        for imp in expected_imports:
            assert imp in content, f"Missing import: {imp}"


class TestCoreModulesExist:
    """Test that core modules have required classes"""
    
    def test_connection_pool_exists(self):
        """Test ConnectionPool class exists in core/"""
        pool_path = CORE_PATH / 'connection_pool.py'
        assert pool_path.exists(), "core/connection_pool.py should exist"
        
        with open(pool_path, 'r') as f:
            content = f.read()
        
        assert 'class ConnectionPool' in content
    
    def test_connection_pool_has_required_methods(self):
        """Test ConnectionPool has required methods"""
        pool_path = CORE_PATH / 'connection_pool.py'
        with open(pool_path, 'r') as f:
            content = f.read()
        
        required_methods = [
            'def get_connection',
            'def execute',
            'def close',
            'def initialize',
        ]
        
        for method in required_methods:
            assert method in content, f"Missing method in ConnectionPool: {method}"
    
    def test_job_runner_exists(self):
        """Test DatabricksJobRunner class exists in core/"""
        runner_path = CORE_PATH / 'databricks_job_runner.py'
        assert runner_path.exists(), "core/databricks_job_runner.py should exist"
        
        with open(runner_path, 'r') as f:
            content = f.read()
        
        assert 'class DatabricksJobRunner' in content
    
    def test_job_runner_has_required_methods(self):
        """Test DatabricksJobRunner has required methods"""
        runner_path = CORE_PATH / 'databricks_job_runner.py'
        with open(runner_path, 'r') as f:
            content = f.read()
        
        required_methods = [
            'def create_notebook',
            'def create_job',
            'def run_job',
            'def get_run_status',
        ]
        
        for method in required_methods:
            assert method in content, f"Missing method in DatabricksJobRunner: {method}"


class TestConfigLoading:
    """Test configuration loading logic"""
    
    def test_config_module_exists(self):
        """Test _config.py exists in core/"""
        config_path = CORE_PATH / '_config.py'
        assert config_path.exists(), "core/_config.py should exist"
    
    def test_config_has_get_config(self):
        """Test get_config function exists"""
        config_path = CORE_PATH / '_config.py'
        with open(config_path, 'r') as f:
            content = f.read()
        
        assert 'def get_config' in content
    
    def test_config_reads_env_vars(self):
        """Test config reads expected environment variables"""
        config_path = CORE_PATH / '_config.py'
        with open(config_path, 'r') as f:
            content = f.read()
        
        expected_vars = [
            'DATABRICKS_HOST',
            'DATABRICKS_TOKEN',
            'DATABRICKS_HTTP_PATH',
            'CLUSTER_ID',
        ]
        
        for var in expected_vars:
            assert var in content, f"Missing env var: {var}"
    
    def test_config_no_hardcoded_defaults(self):
        """Test config doesn't have hardcoded sensitive defaults"""
        config_path = CORE_PATH / '_config.py'
        with open(config_path, 'r') as f:
            content = f.read()
        
        # Should NOT contain hardcoded workspace URLs or IDs
        assert 'hf-gp.cloud.databricks.com' not in content, "Should not have hardcoded hostname"
        assert '4157495209488006' not in content, "Should not have hardcoded workspace ID"


class TestMCPServerNoCodeDuplication:
    """Test that MCP server doesn't duplicate code from core/"""
    
    def test_no_duplicated_classes(self):
        """Test server doesn't duplicate classes from core/"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # These should NOT be in the MCP server (they're in core/)
        assert 'class ConnectionPool:' not in content, "ConnectionPool should be imported, not defined"
        assert 'class DatabricksJobRunner:' not in content, "DatabricksJobRunner should be imported, not defined"
        assert 'class WorkspaceSync:' not in content, "WorkspaceSync should be imported, not defined"


class TestEnvExampleExists:
    """Test that environment example files exist"""
    
    def test_databricks_env_example_exists(self):
        """Test env.example exists for Databricks MCP"""
        env_example = MCP_PATH / 'env.example'
        assert env_example.exists(), "mcp/databricks/env.example should exist"
    
    def test_env_example_has_required_vars(self):
        """Test env.example contains all required variables"""
        env_example = MCP_PATH / 'env.example'
        with open(env_example, 'r') as f:
            content = f.read()
        
        required_vars = [
            'DATABRICKS_HOST',
            'DATABRICKS_TOKEN',
            'DATABRICKS_HTTP_PATH',
            'DATABRICKS_SERVER_HOSTNAME',
            'CLUSTER_ID',
        ]
        
        for var in required_vars:
            assert var in content, f"Missing variable in env.example: {var}"
