"""
Tests for table_inspector.py
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch

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
    def test_get_table_schema(self, mock_connect, inspector, mock_sql_connection):
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        # Mock DESCRIBE query result
        mock_cursor.fetchall.return_value = [
            Mock(col_name='id', data_type='bigint', comment=None),
            Mock(col_name='name', data_type='string', comment=None)
        ]
        
        schema = inspector.get_table_schema('schema.table')
        
        assert schema is not None
        mock_cursor.execute.assert_called()
    
    @patch('core.table_inspector.sql.connect')
    def test_get_table_stats(self, mock_connect, inspector, mock_sql_connection):
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        # Mock stats query result
        mock_cursor.fetchall.return_value = [
            Mock(count=100, size_bytes=1024)
        ]
        
        stats = inspector.get_table_stats('schema.table')
        
        assert stats is not None
    
    @patch('core.table_inspector.sql.connect')
    def test_get_table_sample(self, mock_connect, inspector, mock_sql_connection):
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        mock_cursor.fetchall.return_value = [
            Mock(id=1, name='test1'),
            Mock(id=2, name='test2')
        ]
        
        sample = inspector.get_table_sample('schema.table', limit=2)
        
        assert sample is not None
        assert len(sample) == 2
    
    @patch('core.table_inspector.sql.connect')
    def test_find_duplicates(self, mock_connect, inspector, mock_sql_connection):
        mock_conn, mock_cursor = mock_sql_connection
        mock_connect.return_value.__enter__.return_value = mock_conn
        
        mock_cursor.fetchall.return_value = [
            Mock(key_column='value1', count=2),
            Mock(key_column='value2', count=3)
        ]
        
        duplicates = inspector.find_duplicates('schema.table', 'key_column', limit=10)
        
        assert duplicates is not None


