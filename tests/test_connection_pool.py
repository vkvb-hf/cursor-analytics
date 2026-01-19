"""
Tests for Connection Pool

These tests verify the ConnectionPool class handles connections correctly,
including reconnection logic, error handling, and resource cleanup.

Run with: pytest tests/test_connection_pool.py -v
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch, call
from collections import namedtuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture
def mock_config():
    """Mock configuration for connection pool"""
    with patch('core.connection_pool.get_config') as mock_get_config:
        mock_cfg = MagicMock()
        mock_cfg.SERVER_HOSTNAME = 'test.databricks.com'
        mock_cfg.HTTP_PATH = '/sql/test'
        mock_cfg.TOKEN = 'test-token'
        mock_get_config.return_value = mock_cfg
        yield mock_cfg


@pytest.fixture
def reset_singleton():
    """Reset the ConnectionPool singleton between tests"""
    from core.connection_pool import ConnectionPool
    ConnectionPool._instance = None
    yield
    ConnectionPool._instance = None


# =============================================================================
# CONNECTION POOL INITIALIZATION TESTS
# =============================================================================

class TestConnectionPoolInitialization:
    """Tests for ConnectionPool initialization"""
    
    def test_singleton_pattern(self, mock_config, reset_singleton):
        """Test ConnectionPool uses singleton pattern"""
        from core.connection_pool import ConnectionPool
        
        pool1 = ConnectionPool.get_instance()
        pool2 = ConnectionPool.get_instance()
        
        assert pool1 is pool2
    
    def test_get_pool_returns_singleton(self, mock_config, reset_singleton):
        """Test get_pool() returns the singleton instance"""
        from core.connection_pool import get_pool, ConnectionPool
        
        pool = get_pool()
        
        assert pool is ConnectionPool.get_instance()
    
    def test_initialize_with_valid_config(self, mock_config, reset_singleton):
        """Test initialization succeeds with valid config"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_conn = MagicMock()
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            result = pool.initialize()
            
            assert result is True
            assert pool._initialized is True
    
    def test_initialize_without_token_fails(self, reset_singleton):
        """Test initialization fails without token"""
        with patch('core.connection_pool.get_config') as mock_get_config:
            mock_cfg = MagicMock()
            mock_cfg.TOKEN = ''  # Empty token
            mock_cfg.SERVER_HOSTNAME = 'test.databricks.com'
            mock_cfg.HTTP_PATH = '/sql/test'
            mock_get_config.return_value = mock_cfg
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            result = pool.initialize()
            
            assert result is False
    
    def test_initialize_handles_connection_error(self, mock_config, reset_singleton):
        """Test initialization handles connection errors"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_connect.side_effect = Exception("Connection refused")
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            result = pool.initialize()
            
            assert result is False
            assert pool._initialized is False


# =============================================================================
# QUERY EXECUTION TESTS
# =============================================================================

class TestConnectionPoolExecution:
    """Tests for query execution"""
    
    def test_execute_query_success(self, mock_config, reset_singleton):
        """Test successful query execution"""
        Row = namedtuple('Row', ['id', 'name'])
        expected_results = [Row(1, 'Alice'), Row(2, 'Bob')]
        
        with patch('databricks.sql.connect') as mock_connect:
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = expected_results
            
            mock_conn = MagicMock()
            mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
            mock_conn.cursor.return_value.__exit__.return_value = None
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            results = pool.execute("SELECT * FROM users")
            
            assert results == expected_results
            mock_cursor.execute.assert_called_once_with("SELECT * FROM users")
    
    def test_execute_query_without_fetch(self, mock_config, reset_singleton):
        """Test query execution without fetching results"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_cursor = MagicMock()
            
            mock_conn = MagicMock()
            mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
            mock_conn.cursor.return_value.__exit__.return_value = None
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            results = pool.execute("CREATE TABLE test (id INT)", fetch=False)
            
            assert results == []
            mock_cursor.fetchall.assert_not_called()
    
    def test_execute_with_columns(self, mock_config, reset_singleton):
        """Test execute_with_columns returns results and column names"""
        Row = namedtuple('Row', ['id', 'name'])
        expected_results = [Row(1, 'Alice')]
        
        with patch('databricks.sql.connect') as mock_connect:
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = expected_results
            mock_cursor.description = [
                ('id', 'int', None, None, None, None, None),
                ('name', 'string', None, None, None, None, None)
            ]
            
            mock_conn = MagicMock()
            mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
            mock_conn.cursor.return_value.__exit__.return_value = None
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            results, columns = pool.execute_with_columns("SELECT * FROM users")
            
            assert results == expected_results
            assert columns == ['id', 'name']


# =============================================================================
# RECONNECTION LOGIC TESTS
# =============================================================================

class TestConnectionPoolReconnection:
    """Tests for reconnection logic"""
    
    def test_reconnect_on_stale_connection(self, mock_config, reset_singleton):
        """Test automatic reconnection when connection is stale"""
        Row = namedtuple('Row', ['id'])
        expected_results = [Row(1)]
        
        with patch('databricks.sql.connect') as mock_connect:
            mock_cursor_fail = MagicMock()
            mock_cursor_fail.execute.side_effect = Exception("Connection lost")
            
            mock_cursor_success = MagicMock()
            mock_cursor_success.fetchall.return_value = expected_results
            
            mock_conn_fail = MagicMock()
            mock_conn_fail.cursor.return_value.__enter__.return_value = mock_cursor_fail
            mock_conn_fail.cursor.return_value.__exit__.return_value = None
            
            mock_conn_success = MagicMock()
            mock_conn_success.cursor.return_value.__enter__.return_value = mock_cursor_success
            mock_conn_success.cursor.return_value.__exit__.return_value = None
            
            # First call fails, second succeeds
            mock_connect.side_effect = [mock_conn_fail, mock_conn_success]
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            results = pool.execute("SELECT 1")
            
            assert results == expected_results
            # Should have connected twice (initial + reconnect)
            assert mock_connect.call_count == 2
    
    def test_reconnect_resets_connection(self, mock_config, reset_singleton):
        """Test that reconnection properly resets the connection"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_cursor = MagicMock()
            mock_cursor.execute.side_effect = [Exception("Stale"), None]
            mock_cursor.fetchall.return_value = []
            
            mock_conn = MagicMock()
            mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
            mock_conn.cursor.return_value.__exit__.return_value = None
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            pool._connection = mock_conn  # Set initial connection
            
            # This should trigger reconnection
            pool.execute("SELECT 1")
            
            # Connection should have been reset (set to None then recreated)
            assert mock_connect.call_count >= 1


# =============================================================================
# RESOURCE CLEANUP TESTS
# =============================================================================

class TestConnectionPoolCleanup:
    """Tests for resource cleanup"""
    
    def test_close_closes_connection(self, mock_config, reset_singleton):
        """Test close() properly closes the connection"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_conn = MagicMock()
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            pool.initialize()
            pool.close()
            
            mock_conn.close.assert_called_once()
            assert pool._connection is None
            assert pool._initialized is False
    
    def test_close_handles_already_closed(self, mock_config, reset_singleton):
        """Test close() handles already closed connection"""
        from core.connection_pool import ConnectionPool
        
        pool = ConnectionPool()
        # Don't initialize - connection is None
        
        # Should not raise
        pool.close()
        
        assert pool._connection is None
    
    def test_close_handles_close_error(self, mock_config, reset_singleton):
        """Test close() handles errors during close"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_conn = MagicMock()
            mock_conn.close.side_effect = Exception("Close failed")
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            pool.initialize()
            
            # Should not raise
            pool.close()
            
            assert pool._connection is None


# =============================================================================
# MODULE-LEVEL FUNCTION TESTS
# =============================================================================

class TestModuleLevelFunctions:
    """Tests for module-level convenience functions"""
    
    def test_execute_query_function(self, mock_config, reset_singleton):
        """Test execute_query() convenience function"""
        Row = namedtuple('Row', ['id'])
        expected = [Row(1)]
        
        with patch('databricks.sql.connect') as mock_connect:
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = expected
            
            mock_conn = MagicMock()
            mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
            mock_conn.cursor.return_value.__exit__.return_value = None
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import execute_query
            
            results = execute_query("SELECT 1")
            
            assert results == expected
    
    def test_execute_query_with_columns_function(self, mock_config, reset_singleton):
        """Test execute_query_with_columns() convenience function"""
        Row = namedtuple('Row', ['id'])
        expected = [Row(1)]
        
        with patch('databricks.sql.connect') as mock_connect:
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = expected
            mock_cursor.description = [('id', 'int', None, None, None, None, None)]
            
            mock_conn = MagicMock()
            mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
            mock_conn.cursor.return_value.__exit__.return_value = None
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import execute_query_with_columns
            
            results, columns = execute_query_with_columns("SELECT 1 as id")
            
            assert results == expected
            assert columns == ['id']


# =============================================================================
# CONCURRENT ACCESS TESTS
# =============================================================================

class TestConnectionPoolConcurrency:
    """Tests for concurrent access scenarios"""
    
    def test_get_connection_creates_if_none(self, mock_config, reset_singleton):
        """Test get_connection creates connection if none exists"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_conn = MagicMock()
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            assert pool._connection is None
            
            conn = pool.get_connection()
            
            assert conn is mock_conn
            assert pool._initialized is True
    
    def test_get_connection_reuses_existing(self, mock_config, reset_singleton):
        """Test get_connection reuses existing connection"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_conn = MagicMock()
            mock_connect.return_value = mock_conn
            
            from core.connection_pool import ConnectionPool
            
            pool = ConnectionPool()
            
            conn1 = pool.get_connection()
            conn2 = pool.get_connection()
            
            assert conn1 is conn2
            # Should only connect once
            assert mock_connect.call_count == 1
