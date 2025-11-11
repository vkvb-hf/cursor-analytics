#!/usr/bin/env python3
"""
Comprehensive integration test that uses all core functions with sample use cases.

This test verifies that:
1. All imports work correctly
2. All functions can be instantiated/called
3. Functions work together in realistic scenarios
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch, call
from io import StringIO

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestAllImports:
    """Test that all imports work correctly"""
    
    def test_core_imports(self):
        """Test importing from core package"""
        from core import (
            DatabricksJobRunner,
            TableInspector,
            print_table,
            run_query,
            interactive_sql_main,
            run_sql_file,
            create_workspace_directory,
            upload_csv_to_workspace
        )
        assert DatabricksJobRunner is not None
        assert TableInspector is not None
        assert print_table is not None
        assert run_query is not None
        assert interactive_sql_main is not None
        assert run_sql_file is not None
        assert create_workspace_directory is not None
        assert upload_csv_to_workspace is not None
    
    def test_individual_module_imports(self):
        """Test importing from individual modules"""
        from core.databricks_job_runner import DatabricksJobRunner
        from core.table_inspector import TableInspector
        from core.query_util import run_query, print_table, format_value
        from core.run_sql_file import run_sql_file
        from core.interactive_sql import main as interactive_sql_main
        from core.databricks_workspace import create_workspace_directory, upload_csv_to_workspace
        from core.csv_to_table import create_table_from_csvs
        from core.create_table import create_table
        
        assert DatabricksJobRunner is not None
        assert TableInspector is not None
        assert run_query is not None
        assert print_table is not None
        assert format_value is not None
        assert run_sql_file is not None
        assert interactive_sql_main is not None
        assert create_workspace_directory is not None
        assert upload_csv_to_workspace is not None
        assert create_table_from_csvs is not None
        assert create_table is not None


class TestQueryUtilities:
    """Test query utility functions"""
    
    @patch('core.query_util.sql.connect')
    def test_run_query_function(self, mock_connect, mock_sql_connection):
        """Test run_query function with mocked connection"""
        from core.query_util import run_query
        
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        result = run_query("SELECT 1 as test", limit=10)
        
        assert result is not None
        mock_cursor.execute.assert_called_once_with("SELECT 1 as test")
    
    def test_format_value_function(self):
        """Test format_value function"""
        from core.query_util import format_value
        
        assert format_value(None) == 'NULL'
        assert format_value(123) == '123'
        assert format_value(1234567) == '1,234,567'
        assert format_value(123.45) == '123.45'
        assert format_value('test') == 'test'
        assert format_value(True) == 'True'
    
    def test_print_table_function(self, capsys):
        """Test print_table function"""
        from core.query_util import print_table
        
        # Test with empty results
        print_table([])
        captured = capsys.readouterr()
        assert "No results returned" in captured.out
        
        # Test with mock results
        results = [
            Mock(column1='value1', column2=123),
            Mock(column1='value2', column2=456)
        ]
        print_table(results, column_names=['column1', 'column2'], limit=10)
        captured = capsys.readouterr()
        assert 'column1' in captured.out
        assert 'column2' in captured.out


class TestTableInspector:
    """Test TableInspector class"""
    
    @pytest.fixture
    def inspector(self):
        from core.table_inspector import TableInspector
        return TableInspector(
            server_hostname='test-host',
            http_path='test-path',
            token='test-token'
        )
    
    @patch('core.table_inspector.sql.connect')
    def test_table_inspector_initialization(self, mock_connect, inspector, mock_sql_connection):
        """Test TableInspector can be initialized"""
        assert inspector is not None
        assert inspector.server_hostname == 'test-host'
        assert inspector.http_path == 'test-path'
        assert inspector.token == 'test-token'
    
    @patch('core.table_inspector.sql.connect')
    def test_get_table_schema(self, mock_connect, inspector, mock_sql_connection):
        """Test get_table_schema method"""
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        mock_cursor.fetchall.return_value = [
            ('id', 'bigint', None),
            ('name', 'string', None)
        ]
        
        schema = inspector.get_table_schema('schema.table')
        
        assert schema is not None
        assert len(schema) == 2
        assert schema[0]['column'] == 'id'
        assert schema[0]['data_type'] == 'bigint'
        mock_cursor.execute.assert_called()
    
    @patch('core.table_inspector.sql.connect')
    def test_get_table_stats(self, mock_connect, inspector, mock_sql_connection):
        """Test get_table_stats method"""
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        mock_cursor.fetchone.return_value = [100]
        mock_cursor.fetchall.return_value = [
            ('id', 'bigint', None),
            ('name', 'string', None)
        ]
        
        stats = inspector.get_table_stats('schema.table')
        
        assert stats is not None
        assert stats['total_rows'] == 100
        assert stats['column_count'] == 2


class TestDatabricksJobRunner:
    """Test DatabricksJobRunner class"""
    
    @pytest.fixture
    def runner(self):
        from core.databricks_job_runner import DatabricksJobRunner
        return DatabricksJobRunner(
            host='https://test.databricks.com',
            token='test-token',
            cluster_id='test-cluster'
        )
    
    def test_job_runner_initialization(self, runner):
        """Test DatabricksJobRunner can be initialized"""
        assert runner is not None
        assert runner.host == 'https://test.databricks.com'
        assert runner.token == 'test-token'
        assert runner.cluster_id == 'test-cluster'
        assert 'Authorization' in runner.headers
    
    @patch('core.databricks_job_runner.requests.post')
    def test_create_notebook(self, mock_post, runner):
        """Test create_notebook method"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        result = runner.create_notebook(
            notebook_path='/Workspace/test',
            content='# Test notebook',
            overwrite=True
        )
        
        assert result is True
        mock_post.assert_called_once()
    
    @patch('core.databricks_job_runner.requests.post')
    def test_create_job(self, mock_post, runner):
        """Test create_job method"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'job_id': 123}
        mock_post.return_value = mock_response
        
        job_id = runner.create_job(
            notebook_path='/Workspace/test',
            job_name='test-job'
        )
        
        assert job_id == 123
        mock_post.assert_called_once()


class TestWorkspaceFunctions:
    """Test workspace utility functions"""
    
    def test_create_workspace_directory_function(self):
        """Test create_workspace_directory function exists and can be called"""
        from core.databricks_workspace import create_workspace_directory
        
        assert create_workspace_directory is not None
        assert callable(create_workspace_directory)
    
    def test_upload_csv_to_workspace_function(self):
        """Test upload_csv_to_workspace function exists and can be called"""
        from core.databricks_workspace import upload_csv_to_workspace
        
        assert upload_csv_to_workspace is not None
        assert callable(upload_csv_to_workspace)


class TestRunSQLFile:
    """Test run_sql_file function"""
    
    @patch('core.run_sql_file.sql.connect')
    def test_run_sql_file_function(self, mock_connect, mock_sql_connection, tmp_path):
        """Test run_sql_file function"""
        from core.run_sql_file import run_sql_file
        
        # Create a temporary SQL file
        sql_file = tmp_path / "test.sql"
        sql_file.write_text("SELECT 1 as test")
        
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        # This should not raise an exception
        try:
            run_sql_file(str(sql_file), output_format='show', limit=10)
            assert True
        except Exception as e:
            pytest.fail(f"run_sql_file raised exception: {e}")


class TestSampleUseCase:
    """Test a realistic use case combining multiple functions"""
    
    @patch('core.query_util.sql.connect')
    @patch('core.table_inspector.sql.connect')
    def test_complete_workflow(self, mock_table_connect, mock_query_connect, 
                               mock_sql_connection):
        """Test a complete workflow using multiple utilities"""
        from core import TableInspector, run_query
        
        # Setup mocks
        mock_conn, mock_cursor = mock_sql_connection
        mock_query_connect.return_value.__enter__.return_value = mock_conn
        mock_table_connect.return_value.__enter__.return_value = mock_conn
        
        # Mock query results
        mock_cursor.fetchall.return_value = [
            Mock(id=1, name='Test 1', value=100),
            Mock(id=2, name='Test 2', value=200)
        ]
        mock_cursor.fetchone.return_value = [2]
        
        # Step 1: Inspect a table
        inspector = TableInspector(
            server_hostname='test-host',
            http_path='test-path',
            token='test-token'
        )
        
        stats = inspector.get_table_stats('schema.table')
        assert stats is not None
        
        # Step 2: Run a query
        results = run_query("SELECT * FROM schema.table LIMIT 10", limit=10)
        assert results is not None
        
        # Verify both operations were called
        assert mock_cursor.execute.call_count >= 2


class TestErrorHandling:
    """Test error handling in functions"""
    
    @patch('core.query_util.sql.connect')
    def test_run_query_handles_errors(self, mock_connect):
        """Test run_query handles connection errors gracefully"""
        from core.query_util import run_query
        
        mock_connect.side_effect = Exception("Connection failed")
        
        result = run_query("SELECT 1")
        
        # Should return None on error, not raise exception
        assert result is None
    
    @patch('core.databricks_job_runner.requests.post')
    def test_create_notebook_handles_errors(self):
        """Test create_notebook handles API errors gracefully"""
        from core.databricks_job_runner import DatabricksJobRunner
        
        runner = DatabricksJobRunner(
            host='https://test.databricks.com',
            token='test-token'
        )
        
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("API Error")
        mock_post = MagicMock(return_value=mock_response)
        
        with patch('core.databricks_job_runner.requests.post', mock_post):
            result = runner.create_notebook(
                notebook_path='/Workspace/test',
                content='# Test'
            )
            
            # Should return False on error, not raise exception
            assert result is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

