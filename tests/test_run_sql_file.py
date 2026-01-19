"""
Tests for run_sql_file.py
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch
from pathlib import Path
from collections import namedtuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestRunSQLFile:
    """Tests for run_sql_file function"""
    
    @patch('databricks.sql.connect')
    def test_run_sql_file_success(self, mock_connect, tmp_path):
        from core.run_sql_file import run_sql_file
        
        # Create a temporary SQL file
        sql_file = tmp_path / "test.sql"
        sql_file.write_text("SELECT 1 as test")
        
        # Setup mock cursor
        mock_cursor = MagicMock()
        Row = namedtuple('Row', ['test'])
        mock_cursor.fetchall.return_value = [Row(1)]
        mock_cursor.description = [('test', None, None, None, None, None, None)]
        
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        # Should not raise an exception
        run_sql_file(str(sql_file), output_format='show', limit=10)
        
        mock_cursor.execute.assert_called_once()
    
    def test_run_sql_file_not_found(self, tmp_path):
        from core.run_sql_file import run_sql_file
        
        non_existent_file = tmp_path / "nonexistent.sql"
        
        # Should exit with code 1
        with pytest.raises(SystemExit) as exc_info:
            run_sql_file(str(non_existent_file), output_format='show', limit=10)
        
        assert exc_info.value.code == 1
    
    @patch('databricks.sql.connect')
    @patch('pandas.DataFrame.to_csv')
    def test_run_sql_file_output_csv(self, mock_to_csv, mock_connect, tmp_path):
        from core.run_sql_file import run_sql_file
        
        sql_file = tmp_path / "test.sql"
        sql_file.write_text("SELECT 1 as test")
        
        # Setup mock cursor
        mock_cursor = MagicMock()
        Row = namedtuple('Row', ['test'])
        mock_cursor.fetchall.return_value = [Row(1)]
        mock_cursor.description = [('test', None, None, None, None, None, None)]
        
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        # Change to tmp_path so CSV is written there
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        try:
            run_sql_file(str(sql_file), output_format='csv', limit=10)
            mock_to_csv.assert_called_once()
        finally:
            os.chdir(original_cwd)
