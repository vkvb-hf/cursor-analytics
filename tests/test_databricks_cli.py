"""
Tests for databricks_cli.py
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch
from io import StringIO

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from databricks_cli import sql_command, notebook_command, table_command, main


class TestSQLCommand:
    """Tests for SQL command"""
    
    @patch('databricks_cli.run_query_with_display')
    def test_sql_command_with_query(self, mock_run):
        mock_run.return_value = [Mock(test=1)]
        
        args = Mock()
        args.query = ['SELECT', '1']
        args.file = None
        args.limit = 10
        args.format = 'show'
        args.title = None
        
        result = sql_command(args)
        
        assert result == 0
        mock_run.assert_called_once()
    
    @patch('databricks_cli.run_sql_file')
    def test_sql_command_with_file(self, mock_run_file):
        mock_run_file.return_value = 0
        
        args = Mock()
        args.query = None
        args.file = 'test.sql'
        args.format = 'csv'
        args.limit = 100
        
        result = sql_command(args)
        
        assert result == 0
        mock_run_file.assert_called_once_with('test.sql', 'csv', 100)
    
    def test_sql_command_no_args(self):
        args = Mock()
        args.query = None
        args.file = None
        
        result = sql_command(args)
        
        assert result == 1


class TestNotebookCommand:
    """Tests for notebook command"""
    
    @patch('databricks_cli.DatabricksJobRunner')
    def test_notebook_create(self, mock_runner_class):
        mock_runner = MagicMock()
        mock_runner.create_notebook.return_value = True
        mock_runner_class.return_value = mock_runner
        
        args = Mock()
        args.action = 'create'
        args.path = '/Workspace/test'
        args.file = 'test.py'
        args.overwrite = True
        args.job_name = None
        args.run_id = None
        
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = '# Test'
            result = notebook_command(args)
        
        assert result == 0
        mock_runner.create_notebook.assert_called_once()
    
    @patch('databricks_cli.DatabricksJobRunner')
    def test_notebook_run(self, mock_runner_class):
        mock_runner = MagicMock()
        mock_runner.create_and_run.return_value = {'job_id': 123, 'run_id': 456}
        mock_runner_class.return_value = mock_runner
        
        args = Mock()
        args.action = 'run'
        args.path = '/Workspace/test'
        args.file = 'test.py'
        args.job_name = 'my-job'
        args.run_id = None
        args.overwrite = False
        
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = '# Test'
            result = notebook_command(args)
        
        assert result == 0
        mock_runner.create_and_run.assert_called_once()


class TestTableCommand:
    """Tests for table command"""
    
    @patch('databricks_cli.TableInspector')
    def test_table_inspect(self, mock_inspector_class):
        mock_inspector = MagicMock()
        mock_inspector.get_table_schema.return_value = "schema_info"
        mock_inspector.get_table_stats.return_value = "stats_info"
        mock_inspector.get_table_sample.return_value = [Mock(id=1)]
        mock_inspector_class.return_value = mock_inspector
        
        args = Mock()
        args.action = 'inspect'
        args.table = 'schema.table'
        args.schema = True
        args.stats = True
        args.sample = 10
        args.key_column = None
        args.limit = 20
        
        result = table_command(args)
        
        assert result == 0
        mock_inspector.get_table_schema.assert_called_once()
        mock_inspector.get_table_stats.assert_called_once()
        mock_inspector.get_table_sample.assert_called_once_with('schema.table', limit=10)


class TestMain:
    """Tests for main function"""
    
    @patch('sys.argv', ['databricks_cli.py', 'sql', '--query', 'SELECT 1'])
    @patch('databricks_cli.sql_command')
    def test_main_sql_command(self, mock_sql):
        mock_sql.return_value = 0
        result = main()
        assert result == 0
    
    @patch('sys.argv', ['databricks_cli.py', 'interactive'])
    @patch('databricks_cli.interactive_sql_main')
    def test_main_interactive(self, mock_interactive):
        mock_interactive.return_value = None
        result = main()
        assert result == 0

