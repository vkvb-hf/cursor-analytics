"""
Tests for databricks_api.py
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from databricks_api import DatabricksAPI, sql, inspect, notebook


class TestDatabricksAPI:
    """Tests for DatabricksAPI class"""
    
    @pytest.fixture
    def api(self):
        return DatabricksAPI(
            server_hostname='test-host',
            http_path='test-path',
            token='test-token',
            databricks_host='https://test.databricks.com',
            cluster_id='test-cluster'
        )
    
    @patch('databricks_api.run_query_with_display')
    def test_run_sql_display(self, mock_run, api):
        mock_run.return_value = [Mock(col1='val1')]
        
        result = api.run_sql("SELECT * FROM test", display=True)
        
        assert result is not None
        mock_run.assert_called_once()
    
    @patch('databricks_api.sql.connect')
    def test_run_sql_no_display(self, mock_connect, api, mock_sql_connection):
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        result = api.run_sql("SELECT * FROM test", display=False)
        
        assert result is not None
        mock_cursor.execute.assert_called_once()
    
    @patch.object(DatabricksAPI, 'table_inspector')
    def test_inspect_table(self, mock_inspector, api):
        mock_inspector.get_table_schema.return_value = "schema_info"
        mock_inspector.get_table_stats.return_value = "stats_info"
        mock_inspector.get_table_sample.return_value = [Mock(id=1)]
        
        result = api.inspect_table('schema.table', sample_rows=10)
        
        assert 'schema' in result
        assert 'stats' in result
        assert 'sample' in result
    
    @patch.object(DatabricksAPI, 'job_runner')
    def test_create_notebook(self, mock_runner, api):
        mock_runner.create_notebook.return_value = True
        
        result = api.create_notebook('/Workspace/test', '# Test', overwrite=True)
        
        assert result is True
        mock_runner.create_notebook.assert_called_once()
    
    @patch.object(DatabricksAPI, 'job_runner')
    def test_run_notebook_job(self, mock_runner, api):
        mock_runner.create_and_run.return_value = {'job_id': 123, 'run_id': 456}
        
        result = api.run_notebook_job('/Workspace/test', '# Test', 'my-job')
        
        assert result is not None
        assert result['job_id'] == 123


class TestConvenienceFunctions:
    """Tests for convenience functions"""
    
    @patch('databricks_api.DatabricksAPI')
    def test_sql_function(self, mock_api_class):
        mock_api = MagicMock()
        mock_api.run_sql.return_value = [Mock(test=1)]
        mock_api_class.return_value = mock_api
        
        result = sql("SELECT 1")
        
        assert result is not None
        mock_api.run_sql.assert_called_once()
    
    @patch('databricks_api.DatabricksAPI')
    def test_inspect_function(self, mock_api_class):
        mock_api = MagicMock()
        mock_api.inspect_table.return_value = {'schema': 'test'}
        mock_api_class.return_value = mock_api
        
        result = inspect('schema.table', sample=10)
        
        assert result is not None
        mock_api.inspect_table.assert_called_once()

