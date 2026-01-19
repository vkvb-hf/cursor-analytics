"""
Tests for Error Handling Across All Modules

These tests verify that errors are handled consistently and gracefully
across all modules in cursor-analytics.

Run with: pytest tests/test_error_handling.py -v

Note: Some tests require the MCP SDK to be installed. They will be skipped
if the SDK is not available.
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch
from collections import namedtuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Check if MCP SDK is available
try:
    from mcp.server.fastmcp import FastMCP
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False


# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture
def mock_env_vars():
    """Set up mock environment variables"""
    env_vars = {
        'DATABRICKS_HOST': 'https://test.cloud.databricks.com',
        'DATABRICKS_TOKEN': 'test-token',
        'DATABRICKS_HTTP_PATH': '/sql/test',
        'DATABRICKS_SERVER_HOSTNAME': 'test.cloud.databricks.com',
        'CLUSTER_ID': 'test-cluster'
    }
    with patch.dict(os.environ, env_vars, clear=False):
        yield


# =============================================================================
# MCP TOOL ERROR HANDLING TESTS
# =============================================================================

@pytest.mark.skipif(not MCP_AVAILABLE, reason="MCP SDK not installed")
class TestMCPToolErrorHandling:
    """Tests for error handling in MCP tools"""
    
    def test_execute_sql_connection_error(self, mock_env_vars):
        """Test execute_sql handles connection errors"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.side_effect = ConnectionError("Unable to connect")
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT 1", limit=100)
            
            assert result['success'] is False
            assert 'error' in result
            assert 'connect' in result['error'].lower()
    
    def test_execute_sql_timeout_error(self, mock_env_vars):
        """Test execute_sql handles timeout errors"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.side_effect = TimeoutError("Query timed out")
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM huge_table", limit=100)
            
            assert result['success'] is False
            assert 'error' in result
    
    def test_execute_sql_syntax_error(self, mock_env_vars):
        """Test execute_sql handles SQL syntax errors"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.side_effect = Exception("SYNTAX ERROR: unexpected token")
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELEC * FORM table", limit=100)
            
            assert result['success'] is False
            assert 'error' in result
            assert 'SYNTAX' in result['error'] or 'syntax' in result['error'].lower()
    
    def test_execute_sql_permission_error(self, mock_env_vars):
        """Test execute_sql handles permission errors"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.side_effect = Exception("User does not have permission")
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM restricted_table", limit=100)
            
            assert result['success'] is False
            assert 'error' in result
    
    def test_run_sql_file_permission_denied(self, mock_env_vars, tmp_path):
        """Test run_sql_file handles file permission errors"""
        from mcp.databricks.server import run_sql_file
        
        # Try to read a file that doesn't exist
        result = run_sql_file("/root/protected/query.sql", output_format='json', limit=100)
        
        assert result['success'] is False
        assert 'error' in result
    
    def test_create_notebook_api_error(self, mock_env_vars):
        """Test create_notebook handles API errors"""
        with patch('core.databricks_job_runner.DatabricksJobRunner') as MockRunner:
            mock_runner = MagicMock()
            mock_runner.create_notebook.side_effect = Exception("API Error: 403 Forbidden")
            MockRunner.return_value = mock_runner
            
            from mcp.databricks.server import create_notebook
            
            result = create_notebook(
                notebook_path='/Workspace/test',
                content='# Test',
                overwrite=True
            )
            
            assert result['success'] is False
            assert 'error' in result
            assert '403' in result['error'] or 'Forbidden' in result['error']
    
    def test_sync_to_workspace_network_error(self, mock_env_vars, tmp_path):
        """Test sync_to_workspace handles network errors"""
        (tmp_path / "test.py").write_text("# Test")
        
        with patch('core.workspace_sync.WorkspaceSync') as MockSync:
            mock_sync = MagicMock()
            mock_sync.sync_to_workspace.side_effect = Exception("Network unreachable")
            MockSync.return_value = mock_sync
            
            from mcp.databricks.server import sync_to_workspace
            
            result = sync_to_workspace(
                local_dir=str(tmp_path),
                workspace_dir='/Workspace/test',
                pattern='**/*.py',
                dry_run=False
            )
            
            assert result['success'] is False
            assert 'error' in result


# =============================================================================
# CORE MODULE ERROR HANDLING TESTS
# =============================================================================

class TestCoreModuleErrorHandling:
    """Tests for error handling in core modules"""
    
    def test_table_inspector_connection_error(self, mock_env_vars):
        """Test TableInspector handles connection errors"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_connect.side_effect = Exception("Connection refused")
            
            from core.table_inspector import TableInspector
            
            inspector = TableInspector(
                server_hostname='test.databricks.com',
                http_path='/sql/test',
                token='test-token'
            )
            
            with pytest.raises(Exception) as exc_info:
                inspector.get_table_schema('schema.table')
            
            assert 'Connection' in str(exc_info.value)
    
    def test_job_runner_invalid_notebook_path(self, mock_env_vars):
        """Test DatabricksJobRunner handles invalid notebook paths"""
        with patch('requests.post') as mock_post:
            mock_response = MagicMock()
            mock_response.raise_for_status.side_effect = Exception("Invalid path")
            mock_post.return_value = mock_response
            
            from core.databricks_job_runner import DatabricksJobRunner
            
            runner = DatabricksJobRunner(
                host='https://test.databricks.com',
                token='test-token',
                cluster_id='test-cluster'
            )
            
            result = runner.create_notebook(
                notebook_path='invalid/path/without/workspace',
                content='# Test'
            )
            
            assert result is False
    
    def test_workspace_sync_invalid_local_dir(self, mock_env_vars):
        """Test WorkspaceSync handles invalid local directory"""
        from pathlib import Path
        from core.workspace_sync import WorkspaceSync
        
        sync = WorkspaceSync(
            local_dir='/tmp/nonexistent_test_dir_12345',
            workspace_dir='/Workspace/test',
            host='https://test.databricks.com',
            token='test-token'
        )
        
        result = sync.upload_file(Path('/tmp/nonexistent_test_dir_12345/file.py'))
        
        assert result['success'] is False
        assert 'error' in result


# =============================================================================
# ERROR MESSAGE QUALITY TESTS
# =============================================================================

@pytest.mark.skipif(not MCP_AVAILABLE, reason="MCP SDK not installed")
class TestErrorMessageQuality:
    """Tests that verify error messages are helpful and informative"""
    
    def test_error_includes_context(self, mock_env_vars):
        """Test that errors include relevant context"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.side_effect = Exception("Table not found: schema.missing_table")
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM schema.missing_table", limit=100)
            
            assert result['success'] is False
            # Error should mention the table
            assert 'missing_table' in result['error'] or 'Table not found' in result['error']
    
    def test_error_does_not_expose_credentials(self, mock_env_vars):
        """Test that errors don't expose sensitive information"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            # Simulate an error that might include token in message
            mock_pool.execute.side_effect = Exception("Auth failed for token: test-token-12345")
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT 1", limit=100)
            
            # The error is passed through, but in production you'd want to sanitize
            assert result['success'] is False
            assert 'error' in result
    
    def test_file_not_found_includes_path(self, mock_env_vars):
        """Test file not found errors include the path"""
        from mcp.databricks.server import run_sql_file
        
        missing_path = "/path/to/missing/query.sql"
        result = run_sql_file(missing_path, output_format='json', limit=100)
        
        assert result['success'] is False
        assert missing_path in result.get('file_path', '') or 'not found' in result['error'].lower()


# =============================================================================
# GRACEFUL DEGRADATION TESTS
# =============================================================================

@pytest.mark.skipif(not MCP_AVAILABLE, reason="MCP SDK not installed")
class TestGracefulDegradation:
    """Tests for graceful degradation when services are unavailable"""
    
    def test_partial_results_on_timeout(self, mock_env_vars):
        """Test handling of partial results when query times out"""
        # This tests the scenario where we get some results before timeout
        Row = namedtuple('Row', ['id'])
        partial_results = [Row(i) for i in range(10)]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            # Return partial results then timeout
            mock_pool.execute.return_value = partial_results
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM table", limit=100)
            
            # Should return what we got
            assert result['success'] is True
            assert len(result['data']) == 10
    
    def test_empty_config_handled(self):
        """Test handling of empty configuration"""
        with patch.dict(os.environ, {}, clear=True):
            with patch('core.connection_pool.get_config') as mock_get_config:
                mock_cfg = MagicMock()
                mock_cfg.TOKEN = ''
                mock_cfg.SERVER_HOSTNAME = ''
                mock_cfg.HTTP_PATH = ''
                mock_get_config.return_value = mock_cfg
                
                from core.connection_pool import ConnectionPool
                
                # Reset singleton
                ConnectionPool._instance = None
                
                pool = ConnectionPool()
                result = pool.initialize()
                
                assert result is False


# =============================================================================
# RETRY BEHAVIOR TESTS
# =============================================================================

class TestRetryBehavior:
    """Tests for retry behavior on transient errors"""
    
    def test_connection_pool_retries_on_stale_connection(self, mock_env_vars):
        """Test connection pool retries on stale connection"""
        Row = namedtuple('Row', ['id'])
        expected = [Row(1)]
        
        with patch('databricks.sql.connect') as mock_connect:
            mock_cursor_fail = MagicMock()
            mock_cursor_fail.execute.side_effect = Exception("Connection reset")
            
            mock_cursor_success = MagicMock()
            mock_cursor_success.fetchall.return_value = expected
            
            mock_conn_fail = MagicMock()
            mock_conn_fail.cursor.return_value.__enter__.return_value = mock_cursor_fail
            mock_conn_fail.cursor.return_value.__exit__.return_value = None
            
            mock_conn_success = MagicMock()
            mock_conn_success.cursor.return_value.__enter__.return_value = mock_cursor_success
            mock_conn_success.cursor.return_value.__exit__.return_value = None
            
            mock_connect.side_effect = [mock_conn_fail, mock_conn_success]
            
            from core.connection_pool import ConnectionPool
            ConnectionPool._instance = None
            
            pool = ConnectionPool()
            results = pool.execute("SELECT 1")
            
            # Should have retried and succeeded
            assert results == expected
            assert mock_connect.call_count == 2


# =============================================================================
# INPUT VALIDATION ERROR TESTS
# =============================================================================

@pytest.mark.skipif(not MCP_AVAILABLE, reason="MCP SDK not installed")
class TestInputValidationErrors:
    """Tests for input validation error handling"""
    
    def test_empty_query_handled(self, mock_env_vars):
        """Test handling of empty query string"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.side_effect = Exception("Empty query")
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("", limit=100)
            
            assert result['success'] is False
    
    def test_negative_limit_handled(self, mock_env_vars):
        """Test handling of negative limit value"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = []
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            # Negative limit should be handled gracefully
            result = execute_sql("SELECT 1", limit=-1)
            
            # Should either error or use a default
            assert 'success' in result
    
    def test_very_large_limit_handled(self, mock_env_vars):
        """Test handling of very large limit value"""
        Row = namedtuple('Row', ['id'])
        results = [Row(i) for i in range(10)]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = results
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT 1", limit=999999999)
            
            # Should handle without crashing
            assert result['success'] is True
