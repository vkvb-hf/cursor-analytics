"""
Integration Tests for MCP Servers

These tests verify the MCP servers have correct structure and logic.
They use file-based validation to avoid import issues with external dependencies.

Run with: pytest tests/test_mcp_integration.py -v
Skip integration tests: pytest tests/test_mcp_integration.py -v -m "not integration"
"""
import pytest
import sys
import os
import ast
from pathlib import Path
from unittest.mock import patch

# Get paths to MCP servers
MCP_DATABRICKS_PATH = Path(__file__).parent.parent / 'mcp' / 'databricks'
MCP_SHEETS_PATH = Path(__file__).parent.parent / 'mcp' / 'google_sheets'
CORE_PATH = Path(__file__).parent.parent / 'core'


# =============================================================================
# DATABRICKS MCP INTEGRATION TESTS
# =============================================================================

class TestDatabricksMCPIntegration:
    """Integration tests for Databricks MCP server"""
    
    @pytest.fixture
    def mock_databricks_env(self):
        """Set up mock environment for Databricks"""
        env_vars = {
            'DATABRICKS_HOST': 'https://test.cloud.databricks.com',
            'DATABRICKS_TOKEN': 'test-token-12345',
            'DATABRICKS_HTTP_PATH': '/sql/1.0/warehouses/test',
            'DATABRICKS_SERVER_HOSTNAME': 'test.cloud.databricks.com',
            'CLUSTER_ID': 'test-cluster-123'
        }
        with patch.dict(os.environ, env_vars, clear=False):
            yield env_vars
    
    @pytest.mark.integration
    def test_databricks_mcp_server_structure(self):
        """Test Databricks MCP server has correct structure (imports from core/)"""
        server_path = MCP_DATABRICKS_PATH / 'server.py'
        assert server_path.exists()
        
        content = server_path.read_text()
        
        # Verify it imports from core/ (refactored architecture)
        assert 'from core.connection_pool import' in content
        assert 'from core.databricks_job_runner import' in content
        assert 'execute_sql' in content
        assert 'create_notebook' in content
        assert 'run_notebook' in content
    
    @pytest.mark.integration
    def test_databricks_client_methods(self, mock_databricks_env):
        """Test DatabricksJobRunner (in core/) has all required methods"""
        # Check core/databricks_job_runner.py instead of MCP server
        runner_path = CORE_PATH / 'databricks_job_runner.py'
        content = runner_path.read_text()
        
        required_methods = [
            'def create_notebook',
            'def create_job',
            'def run_job',
            'def get_run_status',
        ]
        
        for method in required_methods:
            assert method in content, f"Missing method: {method}"
    
    @pytest.mark.integration
    def test_connection_pool_structure(self, mock_databricks_env):
        """Test ConnectionPool (in core/) has correct structure"""
        pool_path = CORE_PATH / 'connection_pool.py'
        content = pool_path.read_text()
        
        assert 'def get_connection' in content
        assert 'def execute' in content
        assert 'def close' in content
    
    @pytest.mark.integration
    def test_all_tools_defined(self, mock_databricks_env):
        """Test all expected tools are defined (FastMCP pattern)"""
        server_path = MCP_DATABRICKS_PATH / 'server.py'
        content = server_path.read_text()
        
        expected_tools = [
            'execute_sql',
            'run_sql_file',
            'create_notebook',
            'run_notebook',
            'get_job_status',
            'sync_to_workspace',
            'sync_from_workspace'
        ]
        
        # FastMCP pattern uses `def tool_name` with @mcp.tool() decorator
        for tool in expected_tools:
            assert f'def {tool}' in content, f"Missing tool function: {tool}"
        
        # Verify FastMCP decorator is used
        assert '@mcp.tool()' in content, "Should use @mcp.tool() decorator"
    
    @pytest.mark.integration
    def test_tools_have_type_hints(self, mock_databricks_env):
        """Test that tool functions have proper type hints"""
        server_path = MCP_DATABRICKS_PATH / 'server.py'
        content = server_path.read_text()
        
        # Parse the AST
        tree = ast.parse(content)
        
        tool_functions = [
            'execute_sql', 'run_sql_file', 'create_notebook',
            'run_notebook', 'get_job_status', 'sync_to_workspace', 'sync_from_workspace'
        ]
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in tool_functions:
                # Check return annotation exists
                assert node.returns is not None, f"Function {node.name} should have return type hint"
    
    @pytest.mark.integration
    def test_tools_return_dict(self, mock_databricks_env):
        """Test that all tools return dict type"""
        server_path = MCP_DATABRICKS_PATH / 'server.py'
        content = server_path.read_text()
        
        # All tool functions should return dict[str, Any]
        assert 'dict[str, Any]' in content, "Tools should return dict[str, Any]"


# =============================================================================
# GOOGLE SHEETS MCP INTEGRATION TESTS (File-based)
# =============================================================================

class TestGoogleSheetsMCPIntegration:
    """Integration tests for Google Sheets MCP server (file-based validation)"""
    
    @pytest.mark.integration
    def test_google_sheets_server_exists(self):
        """Test Google Sheets MCP server exists"""
        server_path = MCP_SHEETS_PATH / 'server.py'
        assert server_path.exists(), "Google Sheets MCP server.py should exist"
    
    @pytest.mark.integration
    def test_google_sheets_uses_fastmcp(self):
        """Test Google Sheets server uses FastMCP pattern"""
        server_path = MCP_SHEETS_PATH / 'server.py'
        content = server_path.read_text()
        
        assert 'from mcp.server.fastmcp import FastMCP' in content
        assert 'FastMCP(' in content
        assert '@mcp.tool()' in content
    
    @pytest.mark.integration
    def test_read_sheet_function_structure(self):
        """Test read_sheet function has correct structure"""
        server_path = MCP_SHEETS_PATH / 'server.py'
        content = server_path.read_text()
        tree = ast.parse(content)
        
        # Find the read_sheet function
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'read_sheet':
                # Check parameters
                args = [arg.arg for arg in node.args.args]
                assert 'spreadsheet_id' in args, "read_sheet should have spreadsheet_id parameter"
                assert 'range_name' in args, "read_sheet should have range_name parameter"
                
                # Check has docstring
                assert ast.get_docstring(node) is not None, "read_sheet should have docstring"
                return
        
        pytest.fail("read_sheet function not found")
    
    @pytest.mark.integration
    def test_get_sheet_info_function_structure(self):
        """Test get_sheet_info function has correct structure"""
        server_path = MCP_SHEETS_PATH / 'server.py'
        content = server_path.read_text()
        tree = ast.parse(content)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'get_sheet_info':
                args = [arg.arg for arg in node.args.args]
                assert 'spreadsheet_id' in args, "get_sheet_info should have spreadsheet_id parameter"
                assert ast.get_docstring(node) is not None, "get_sheet_info should have docstring"
                return
        
        pytest.fail("get_sheet_info function not found")
    
    @pytest.mark.integration
    def test_read_multiple_ranges_function_structure(self):
        """Test read_multiple_ranges function has correct structure"""
        server_path = MCP_SHEETS_PATH / 'server.py'
        content = server_path.read_text()
        tree = ast.parse(content)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'read_multiple_ranges':
                args = [arg.arg for arg in node.args.args]
                assert 'spreadsheet_id' in args
                assert 'ranges' in args
                return
        
        pytest.fail("read_multiple_ranges function not found")
    
    @pytest.mark.integration
    def test_read_comments_function_structure(self):
        """Test read_comments function has correct structure"""
        server_path = MCP_SHEETS_PATH / 'server.py'
        content = server_path.read_text()
        tree = ast.parse(content)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'read_comments':
                args = [arg.arg for arg in node.args.args]
                assert 'spreadsheet_id' in args
                return
        
        pytest.fail("read_comments function not found")
    
    @pytest.mark.integration
    def test_response_structure_patterns(self):
        """Test response patterns are consistent"""
        server_path = MCP_SHEETS_PATH / 'server.py'
        content = server_path.read_text()
        
        # All responses should have success key
        assert '"success": True' in content or "'success': True" in content
        assert '"success": False' in content or "'success': False" in content
        
        # Error responses should have error key
        assert '"error"' in content or "'error'" in content
    
    @pytest.mark.integration
    def test_error_handling_present(self):
        """Test error handling is present"""
        server_path = MCP_SHEETS_PATH / 'server.py'
        content = server_path.read_text()
        
        # Should handle HttpError from Google API
        assert 'except HttpError' in content
        # Should have general exception handler
        assert 'except Exception' in content


# =============================================================================
# CROSS-MCP INTEGRATION TESTS
# =============================================================================

class TestCrossMCPIntegration:
    """Tests that verify consistency across MCP servers"""
    
    @pytest.mark.integration
    def test_both_servers_use_fastmcp(self):
        """Test both MCP servers use FastMCP pattern"""
        for server_name, server_path in [
            ('databricks', MCP_DATABRICKS_PATH / 'server.py'),
            ('google_sheets', MCP_SHEETS_PATH / 'server.py')
        ]:
            content = server_path.read_text()
            assert 'FastMCP' in content, f"{server_name} should use FastMCP"
            assert '@mcp.tool()' in content, f"{server_name} should use @mcp.tool() decorator"
    
    @pytest.mark.integration
    def test_both_servers_have_main_block(self):
        """Test both servers have proper main entry point"""
        for server_name, server_path in [
            ('databricks', MCP_DATABRICKS_PATH / 'server.py'),
            ('google_sheets', MCP_SHEETS_PATH / 'server.py')
        ]:
            content = server_path.read_text()
            assert 'if __name__ ==' in content, f"{server_name} should have main block"
            assert 'mcp.run()' in content, f"{server_name} should call mcp.run()"
    
    @pytest.mark.integration
    def test_env_examples_exist(self):
        """Test environment example files exist for both servers"""
        for server_name, server_path in [
            ('databricks', MCP_DATABRICKS_PATH / 'env.example'),
            ('google_sheets', MCP_SHEETS_PATH / 'env.example')
        ]:
            assert server_path.exists(), f"{server_name} should have env.example"
    
    @pytest.mark.integration
    def test_consistent_response_format(self):
        """Test both servers use consistent response format"""
        for server_path in [MCP_DATABRICKS_PATH / 'server.py', MCP_SHEETS_PATH / 'server.py']:
            content = server_path.read_text()
            
            # All should return success field
            assert '"success"' in content, f"{server_path.name} should return success field"


# =============================================================================
# CORE MODULE INTEGRATION TESTS
# =============================================================================

class TestCoreModulesIntegration:
    """Integration tests for core modules"""
    
    @pytest.mark.integration
    def test_core_init_exports(self):
        """Test core/__init__.py exports all required classes"""
        init_path = CORE_PATH / '__init__.py'
        content = init_path.read_text()
        
        expected_exports = [
            'ConnectionPool',
            'DatabricksJobRunner',
            'TableInspector',
            'WorkspaceSync',
            'get_config',
        ]
        
        for export in expected_exports:
            assert export in content, f"core/__init__.py should export {export}"
    
    @pytest.mark.integration
    def test_config_validates_env_vars(self):
        """Test config module validates environment variables"""
        config_path = CORE_PATH / '_config.py'
        content = config_path.read_text()
        
        # Should check for missing config
        assert 'missing' in content.lower() or 'Missing' in content
        # Should print warning
        assert 'WARNING' in content or 'warning' in content.lower()
    
    @pytest.mark.integration
    def test_workspace_sync_has_methods(self):
        """Test WorkspaceSync has required methods"""
        sync_path = CORE_PATH / 'workspace_sync.py'
        content = sync_path.read_text()
        
        required_methods = [
            'sync_to_workspace',
            'sync_from_workspace',
        ]
        
        for method in required_methods:
            assert f'def {method}' in content, f"WorkspaceSync should have {method}"
    
    @pytest.mark.integration
    def test_table_inspector_has_methods(self):
        """Test TableInspector has required methods"""
        inspector_path = CORE_PATH / 'table_inspector.py'
        content = inspector_path.read_text()
        
        required_methods = [
            'get_table_schema',
            'get_table_stats',
            'check_duplicates_by_column',
            'inspect_table',
        ]
        
        for method in required_methods:
            assert f'def {method}' in content, f"TableInspector should have {method}"
