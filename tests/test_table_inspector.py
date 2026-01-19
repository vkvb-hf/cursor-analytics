"""
Tests for table_inspector.py
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch, PropertyMock
from collections import namedtuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.table_inspector import TableInspector


class TestTableInspector:
    """Tests for TableInspector class"""
    
    @pytest.fixture
    def inspector(self):
        return TableInspector(
            server_hostname='test-host',
            http_path='test-path',
            token='test-token'
        )
    
    @patch('core.table_inspector.sql.connect')
    def test_get_table_schema(self, mock_connect, inspector):
        # Create proper mock cursor with named tuple results
        mock_cursor = MagicMock()
        Row = namedtuple('Row', ['col_name', 'data_type', 'comment'])
        mock_cursor.fetchall.return_value = [
            Row('id', 'bigint', None),
            Row('name', 'string', 'User name')
        ]
        
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        schema = inspector.get_table_schema('schema.table')
        
        assert schema is not None
        assert len(schema) == 2
        assert schema[0]['column'] == 'id'
        assert schema[1]['column'] == 'name'
    
    @patch('core.table_inspector.sql.connect')
    def test_get_table_stats(self, mock_connect, inspector):
        # Create proper mock cursor
        mock_cursor = MagicMock()
        
        # fetchone returns a tuple-like object for COUNT(*)
        mock_cursor.fetchone.return_value = (100,)
        
        # fetchall for schema query
        Row = namedtuple('Row', ['col_name', 'data_type', 'comment'])
        mock_cursor.fetchall.return_value = [
            Row('id', 'bigint', None),
            Row('name', 'string', None)
        ]
        
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        stats = inspector.get_table_stats('schema.table')
        
        assert stats is not None
        assert stats['total_rows'] == 100
        assert stats['column_count'] == 2
    
    @patch('core.table_inspector.sql.connect')
    def test_inspect_table(self, mock_connect, inspector):
        """Test the main inspect_table method"""
        mock_cursor = MagicMock()
        
        # Schema query result
        Row = namedtuple('Row', ['col_name', 'data_type', 'comment'])
        mock_cursor.fetchall.return_value = [
            Row('id', 'bigint', None),
            Row('name', 'string', None)
        ]
        
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        result = inspector.inspect_table('schema.table')
        
        assert result is not None
    
    @patch('core.table_inspector.sql.connect')
    def test_check_duplicates_by_column(self, mock_connect, inspector):
        """Test duplicate checking"""
        mock_cursor = MagicMock()
        Row = namedtuple('Row', ['key_column', 'count'])
        mock_cursor.fetchall.return_value = [
            Row('value1', 2),
            Row('value2', 3)
        ]
        
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        duplicates = inspector.check_duplicates_by_column('schema.table', 'key_column')
        
        assert duplicates is not None
