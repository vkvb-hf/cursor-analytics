"""
Tests for MCP Tool Execution

These tests verify that MCP tools execute correctly with mocked backends.
Unlike the existing tests that only check file structure, these tests
actually invoke the tool functions and verify their behavior.

Run with: pytest tests/test_mcp_tools_execution.py -v

Note: These tests require the MCP SDK to be installed. They will be skipped
if the SDK is not available.
"""
import pytest
import sys
import os
import json
from unittest.mock import Mock, MagicMock, patch, PropertyMock
from collections import namedtuple
from pathlib import Path

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Check if MCP SDK is available
try:
    from mcp.server.fastmcp import FastMCP
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False

# Skip all tests in this module if MCP is not available
pytestmark = pytest.mark.skipif(
    not MCP_AVAILABLE,
    reason="MCP SDK not installed. Install with: pip install mcp"
)


# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture
def mock_env_vars():
    """Set up mock environment variables for all tests"""
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
def mock_connection_pool():
    """Mock the connection pool for SQL execution tests"""
    with patch('core.connection_pool.ConnectionPool') as MockPool:
        mock_instance = MagicMock()
        MockPool.get_instance.return_value = mock_instance
        MockPool._instance = mock_instance
        yield mock_instance


@pytest.fixture
def sample_query_results():
    """Sample query results for testing"""
    Row = namedtuple('Row', ['id', 'name', 'value', 'created_at'])
    return [
        Row(1, 'Alice', 100.50, '2024-01-15'),
        Row(2, 'Bob', 200.75, '2024-01-16'),
        Row(3, 'Charlie', 300.00, '2024-01-17'),
    ]


# =============================================================================
# EXECUTE_SQL TOOL TESTS
# =============================================================================

class TestExecuteSQLTool:
    """Tests for the execute_sql MCP tool"""
    
    def test_execute_sql_returns_structured_response(self, mock_env_vars):
        """Test execute_sql returns properly structured JSON"""
        Row = namedtuple('Row', ['id', 'name'])
        mock_results = [Row(1, 'test')]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = mock_results
            mock_get_pool.return_value = mock_pool
            
            # Import after patching
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM test_table", limit=100)
            
            # Verify response structure
            assert isinstance(result, dict)
            assert 'success' in result
            assert 'row_count' in result or 'error' in result
    
    def test_execute_sql_adds_limit_to_select(self, mock_env_vars):
        """Test that LIMIT is added to SELECT queries without one"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = []
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql, add_limit_if_needed
            
            # Test the helper function directly
            query_without_limit = "SELECT * FROM table"
            modified = add_limit_if_needed(query_without_limit, 100)
            assert "LIMIT 100" in modified
            
            # Query with existing LIMIT should not be modified
            query_with_limit = "SELECT * FROM table LIMIT 50"
            not_modified = add_limit_if_needed(query_with_limit, 100)
            assert "LIMIT 100" not in not_modified
            assert "LIMIT 50" in not_modified
    
    def test_execute_sql_does_not_add_limit_to_non_select(self, mock_env_vars):
        """Test that LIMIT is not added to non-SELECT queries"""
        from mcp.databricks.server import add_limit_if_needed
        
        queries = [
            "SHOW TABLES IN schema",
            "DESCRIBE table_name",
            "CREATE TABLE test AS SELECT 1",
            "INSERT INTO table VALUES (1)",
        ]
        
        for query in queries:
            modified = add_limit_if_needed(query, 100)
            # Non-SELECT queries should not have LIMIT added
            if not query.upper().startswith("SELECT"):
                assert modified == query or "LIMIT" not in modified.replace(query, "")
    
    def test_execute_sql_handles_empty_results(self, mock_env_vars):
        """Test execute_sql handles empty result sets"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = []
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM empty_table", limit=100)
            
            assert result['success'] is True
            assert result['row_count'] == 0
            assert result['data'] == []
    
    def test_execute_sql_handles_connection_error(self, mock_env_vars):
        """Test execute_sql handles connection errors gracefully"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.side_effect = Exception("Connection refused")
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM table", limit=100)
            
            assert result['success'] is False
            assert 'error' in result
            assert 'Connection refused' in result['error']
    
    def test_execute_sql_truncates_long_queries_in_response(self, mock_env_vars):
        """Test that very long queries are truncated in the response"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = []
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            long_query = "SELECT " + ", ".join([f"col{i}" for i in range(100)]) + " FROM table"
            result = execute_sql(long_query, limit=100)
            
            # Query in response should be truncated
            if 'query' in result:
                assert len(result['query']) <= 210  # 200 + "..."


# =============================================================================
# RUN_SQL_FILE TOOL TESTS
# =============================================================================

class TestRunSQLFileTool:
    """Tests for the run_sql_file MCP tool"""
    
    def test_run_sql_file_reads_and_executes(self, mock_env_vars, tmp_path):
        """Test run_sql_file reads file and executes SQL"""
        # Create test SQL file
        sql_file = tmp_path / "test_query.sql"
        sql_file.write_text("SELECT id, name FROM users WHERE active = true")
        
        Row = namedtuple('Row', ['id', 'name'])
        mock_results = [Row(1, 'Alice'), Row(2, 'Bob')]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = mock_results
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import run_sql_file
            
            result = run_sql_file(str(sql_file), output_format='json', limit=100)
            
            assert result['success'] is True
            assert result['file_path'] == str(sql_file)
    
    def test_run_sql_file_handles_missing_file(self, mock_env_vars):
        """Test run_sql_file handles missing file gracefully"""
        from mcp.databricks.server import run_sql_file
        
        result = run_sql_file("/nonexistent/path/query.sql", output_format='json', limit=100)
        
        assert result['success'] is False
        assert 'error' in result
        assert 'not found' in result['error'].lower() or 'No such file' in result['error']
    
    def test_run_sql_file_text_output_format(self, mock_env_vars, tmp_path):
        """Test run_sql_file with text output format"""
        sql_file = tmp_path / "test.sql"
        sql_file.write_text("SELECT 1 as test")
        
        Row = namedtuple('Row', ['test'])
        mock_results = [Row(1)]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = mock_results
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import run_sql_file
            
            result = run_sql_file(str(sql_file), output_format='show', limit=100)
            
            assert result['success'] is True
            assert result['output_format'] == 'text'
            assert 'output' in result


# =============================================================================
# CREATE_NOTEBOOK TOOL TESTS
# =============================================================================

class TestCreateNotebookTool:
    """Tests for the create_notebook MCP tool"""
    
    def test_create_notebook_success(self, mock_env_vars):
        """Test create_notebook creates notebook successfully"""
        with patch('core.databricks_job_runner.DatabricksJobRunner') as MockRunner:
            mock_runner = MagicMock()
            mock_runner.create_notebook.return_value = True
            MockRunner.return_value = mock_runner
            
            from mcp.databricks.server import create_notebook
            
            result = create_notebook(
                notebook_path='/Workspace/Users/test@example.com/my_notebook',
                content='# Test notebook\nprint("Hello")',
                overwrite=True
            )
            
            assert result['success'] is True
            assert result['notebook_path'] == '/Workspace/Users/test@example.com/my_notebook'
            assert result['action'] == 'created'
    
    def test_create_notebook_failure(self, mock_env_vars):
        """Test create_notebook handles failure"""
        with patch('core.databricks_job_runner.DatabricksJobRunner') as MockRunner:
            mock_runner = MagicMock()
            mock_runner.create_notebook.return_value = False
            MockRunner.return_value = mock_runner
            
            from mcp.databricks.server import create_notebook
            
            result = create_notebook(
                notebook_path='/Workspace/test',
                content='# Test',
                overwrite=True
            )
            
            assert result['success'] is False
            assert result['action'] == 'failed'
    
    def test_create_notebook_handles_exception(self, mock_env_vars):
        """Test create_notebook handles exceptions gracefully"""
        with patch('core.databricks_job_runner.DatabricksJobRunner') as MockRunner:
            mock_runner = MagicMock()
            mock_runner.create_notebook.side_effect = Exception("API Error: Unauthorized")
            MockRunner.return_value = mock_runner
            
            from mcp.databricks.server import create_notebook
            
            result = create_notebook(
                notebook_path='/Workspace/test',
                content='# Test',
                overwrite=True
            )
            
            assert result['success'] is False
            assert 'error' in result
            assert 'Unauthorized' in result['error']


# =============================================================================
# GET_JOB_STATUS TOOL TESTS
# =============================================================================

class TestGetJobStatusTool:
    """Tests for the get_job_status MCP tool"""
    
    def test_get_job_status_running(self, mock_env_vars):
        """Test get_job_status for a running job"""
        with patch('core.databricks_job_runner.DatabricksJobRunner') as MockRunner:
            mock_runner = MagicMock()
            mock_runner.get_run_status.return_value = {
                'state': {
                    'life_cycle_state': 'RUNNING',
                    'result_state': None,
                    'state_message': 'Job is running'
                }
            }
            MockRunner.return_value = mock_runner
            
            from mcp.databricks.server import get_job_status
            
            result = get_job_status(run_id=12345)
            
            assert result['success'] is True
            assert result['is_running'] is True
            assert result['is_complete'] is False
            assert result['life_cycle_state'] == 'RUNNING'
    
    def test_get_job_status_completed_success(self, mock_env_vars):
        """Test get_job_status for a successfully completed job"""
        with patch('core.databricks_job_runner.DatabricksJobRunner') as MockRunner:
            mock_runner = MagicMock()
            mock_runner.get_run_status.return_value = {
                'state': {
                    'life_cycle_state': 'TERMINATED',
                    'result_state': 'SUCCESS',
                    'state_message': 'Job completed successfully'
                }
            }
            MockRunner.return_value = mock_runner
            
            from mcp.databricks.server import get_job_status
            
            result = get_job_status(run_id=12345)
            
            assert result['success'] is True
            assert result['is_running'] is False
            assert result['is_complete'] is True
            assert result['is_success'] is True
    
    def test_get_job_status_completed_failed(self, mock_env_vars):
        """Test get_job_status for a failed job"""
        with patch('core.databricks_job_runner.DatabricksJobRunner') as MockRunner:
            mock_runner = MagicMock()
            mock_runner.get_run_status.return_value = {
                'state': {
                    'life_cycle_state': 'TERMINATED',
                    'result_state': 'FAILED',
                    'state_message': 'Job failed with error'
                }
            }
            MockRunner.return_value = mock_runner
            
            from mcp.databricks.server import get_job_status
            
            result = get_job_status(run_id=12345)
            
            assert result['success'] is True
            assert result['is_complete'] is True
            assert result['is_success'] is False
            assert result['result_state'] == 'FAILED'
    
    def test_get_job_status_not_found(self, mock_env_vars):
        """Test get_job_status for non-existent job"""
        with patch('core.databricks_job_runner.DatabricksJobRunner') as MockRunner:
            mock_runner = MagicMock()
            mock_runner.get_run_status.return_value = None
            MockRunner.return_value = mock_runner
            
            from mcp.databricks.server import get_job_status
            
            result = get_job_status(run_id=99999)
            
            assert result['success'] is False
            assert 'error' in result


# =============================================================================
# SYNC TOOLS TESTS
# =============================================================================

class TestSyncTools:
    """Tests for sync_to_workspace and sync_from_workspace tools"""
    
    def test_sync_to_workspace_dry_run(self, mock_env_vars, tmp_path):
        """Test sync_to_workspace in dry run mode"""
        # Create test files
        (tmp_path / "test.py").write_text("# Test file")
        
        with patch('core.workspace_sync.WorkspaceSync') as MockSync:
            mock_sync = MagicMock()
            mock_sync.sync_to_workspace.return_value = {
                'success': True,
                'total': 1,
                'success': [{'file': 'test.py', 'dry_run': True}],
                'failed': []
            }
            MockSync.return_value = mock_sync
            
            from mcp.databricks.server import sync_to_workspace
            
            result = sync_to_workspace(
                local_dir=str(tmp_path),
                workspace_dir='/Workspace/test',
                pattern='**/*.py',
                dry_run=True
            )
            
            assert result['success'] is True
            assert result['dry_run'] is True
    
    def test_sync_from_workspace_success(self, mock_env_vars, tmp_path):
        """Test sync_from_workspace downloads files"""
        with patch('core.workspace_sync.WorkspaceSync') as MockSync:
            mock_sync = MagicMock()
            mock_sync.sync_from_workspace.return_value = {
                'success': True,
                'files_synced': 3
            }
            MockSync.return_value = mock_sync
            
            from mcp.databricks.server import sync_from_workspace
            
            result = sync_from_workspace(
                local_dir=str(tmp_path),
                workspace_dir='/Workspace/test',
                dry_run=False
            )
            
            assert result['success'] is True
            assert result['action'] == 'sync_from_workspace'


# =============================================================================
# RESPONSE FORMAT VALIDATION TESTS
# =============================================================================

class TestResponseFormatValidation:
    """Tests that verify response formats match documentation"""
    
    def test_execute_sql_response_has_required_fields(self, mock_env_vars):
        """Test execute_sql response has all documented fields"""
        Row = namedtuple('Row', ['id', 'name'])
        mock_results = [Row(1, 'test')]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = mock_results
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM test", limit=100)
            
            # Required fields per documentation
            required_fields = ['success', 'row_count', 'columns', 'data']
            for field in required_fields:
                assert field in result, f"Missing required field: {field}"
    
    def test_error_response_has_required_fields(self, mock_env_vars):
        """Test error responses have required fields"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.side_effect = Exception("Test error")
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM test", limit=100)
            
            assert result['success'] is False
            assert 'error' in result
    
    def test_data_field_is_list_of_dicts(self, mock_env_vars):
        """Test that data field contains list of dictionaries"""
        Row = namedtuple('Row', ['id', 'name'])
        mock_results = [Row(1, 'Alice'), Row(2, 'Bob')]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = mock_results
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM test", limit=100)
            
            assert isinstance(result['data'], list)
            if result['data']:
                assert isinstance(result['data'][0], dict)


# =============================================================================
# EDGE CASE TESTS
# =============================================================================

class TestEdgeCases:
    """Tests for edge cases and boundary conditions"""
    
    def test_execute_sql_with_special_characters(self, mock_env_vars):
        """Test execute_sql handles special characters in queries"""
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = []
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            # Query with special characters
            query = "SELECT * FROM table WHERE name = 'O''Brien' AND status = \"active\""
            result = execute_sql(query, limit=100)
            
            # Should not crash
            assert 'success' in result
    
    def test_execute_sql_with_unicode(self, mock_env_vars):
        """Test execute_sql handles unicode in results"""
        Row = namedtuple('Row', ['name', 'city'])
        mock_results = [Row('José García', 'São Paulo'), Row('北京', '東京')]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = mock_results
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM international_users", limit=100)
            
            assert result['success'] is True
            # Data should be serializable
            json.dumps(result)  # Should not raise
    
    def test_execute_sql_with_null_values(self, mock_env_vars):
        """Test execute_sql handles NULL values correctly"""
        Row = namedtuple('Row', ['id', 'name', 'email'])
        mock_results = [Row(1, None, 'test@example.com'), Row(2, 'Bob', None)]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = mock_results
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM users", limit=100)
            
            assert result['success'] is True
            # Should be JSON serializable with nulls
            json_str = json.dumps(result)
            assert 'null' in json_str or result['data'][0].get('name') is None
    
    def test_execute_sql_with_large_numbers(self, mock_env_vars):
        """Test execute_sql handles large numbers correctly"""
        from decimal import Decimal
        
        Row = namedtuple('Row', ['id', 'amount'])
        mock_results = [
            Row(1, Decimal('999999999999.99')),
            Row(2, 12345678901234567890)
        ]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = mock_results
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM transactions", limit=100)
            
            assert result['success'] is True
            # Should be JSON serializable
            json.dumps(result)  # Should not raise
    
    def test_execute_sql_respects_limit(self, mock_env_vars):
        """Test execute_sql respects the limit parameter"""
        Row = namedtuple('Row', ['id'])
        mock_results = [Row(i) for i in range(1000)]
        
        with patch('core.connection_pool.get_pool') as mock_get_pool:
            mock_pool = MagicMock()
            mock_pool.execute.return_value = mock_results
            mock_get_pool.return_value = mock_pool
            
            from mcp.databricks.server import execute_sql
            
            result = execute_sql("SELECT * FROM large_table", limit=50)
            
            assert result['success'] is True
            assert len(result['data']) <= 50
            assert result['truncated'] is True
