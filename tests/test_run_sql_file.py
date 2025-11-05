"""
Tests for run_sql_file.py
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.run_sql_file import run_sql_file


class TestRunSQLFile:
    """Tests for run_sql_file function"""
    
    @patch('core.run_sql_file.sql.connect')
    @patch('core.run_sql_file.SERVER_HOSTNAME', 'test-host')
    @patch('core.run_sql_file.HTTP_PATH', 'test-path')
    @patch('core.run_sql_file.TOKEN', 'test-token')
    def test_run_sql_file_success(self, mock_connect, mock_sql_connection, tmp_path):
        # Create a temporary SQL file
        sql_file = tmp_path / "test.sql"
        sql_file.write_text("SELECT 1 as test")
        
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        result = run_sql_file(str(sql_file), output_format='show', limit=10)
        
        assert result == 0
        mock_cursor.execute.assert_called_once()
    
    @patch('core.run_sql_file.sql.connect')
    def test_run_sql_file_not_found(self, tmp_path):
        non_existent_file = tmp_path / "nonexistent.sql"
        
        result = run_sql_file(str(non_existent_file), output_format='show', limit=10)
        
        assert result == 1
    
    @patch('core.run_sql_file.sql.connect')
    @patch('core.run_sql_file.print_table')
    def test_run_sql_file_output_csv(self, mock_print, mock_connect, mock_sql_connection, tmp_path):
        import pandas as pd
        
        sql_file = tmp_path / "test.sql"
        sql_file.write_text("SELECT 1 as test")
        
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        result = run_sql_file(str(sql_file), output_format='csv', limit=10)
        
        assert result == 0
        # Check if CSV file was created
        output_file = tmp_path / "test_output.csv"
        # Note: This test would need to be adjusted based on actual implementation

