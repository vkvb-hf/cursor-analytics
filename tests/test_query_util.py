"""
Tests for query_util.py
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch
from io import StringIO

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.query_util import format_value, print_table, run_query


class TestFormatValue:
    """Tests for format_value function"""
    
    def test_format_none(self):
        assert format_value(None) == 'NULL'
    
    def test_format_int(self):
        assert format_value(123) == '123'
        assert format_value(1234567) == '1,234,567'
    
    def test_format_float(self):
        assert format_value(123.45) == '123.45'
        assert format_value(123.456789) == '123.46'
    
    def test_format_string(self):
        assert format_value('test') == 'test'
    
    def test_format_bool(self):
        assert format_value(True) == 'True'
        assert format_value(False) == 'False'


class TestPrintTable:
    """Tests for print_table function"""
    
    def test_print_empty_results(self, capsys):
        print_table([])
        captured = capsys.readouterr()
        assert "No results returned" in captured.out
    
    def test_print_table_with_results(self, capsys):
        results = [
            Mock(column1='value1', column2=123),
            Mock(column1='value2', column2=456)
        ]
        print_table(results, column_names=['column1', 'column2'], limit=10)
        captured = capsys.readouterr()
        assert 'column1' in captured.out
        assert 'column2' in captured.out
    
    def test_print_table_with_limit(self, capsys):
        results = [Mock(col=i) for i in range(100)]
        print_table(results, column_names=['col'], limit=5)
        captured = capsys.readouterr()
        assert "Showing 5 of 100 rows" in captured.out


class TestRunQuery:
    """Tests for run_query function"""
    
    @patch('core.query_util.sql.connect')
    @patch('core.query_util.SERVER_HOSTNAME', 'test-host')
    @patch('core.query_util.HTTP_PATH', 'test-path')
    @patch('core.query_util.TOKEN', 'test-token')
    def test_run_query_success(self, mock_connect, mock_sql_connection):
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        result = run_query("SELECT * FROM test", limit=10)
        
        assert result is not None
        mock_cursor.execute.assert_called_once_with("SELECT * FROM test")
    
    @patch('core.query_util.sql.connect')
    @patch('core.query_util.SERVER_HOSTNAME', 'test-host')
    @patch('core.query_util.HTTP_PATH', 'test-path')
    @patch('core.query_util.TOKEN', 'test-token')
    def test_run_query_error(self, mock_connect):
        mock_connect.side_effect = Exception("Connection failed")
        
        result = run_query("SELECT * FROM test")
        
        assert result is None

