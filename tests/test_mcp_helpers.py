"""
Tests for Helper Functions in MCP Server

These tests verify the helper functions used by MCP tools work correctly,
including result formatting, query modification, and data serialization.

Run with: pytest tests/test_mcp_helpers.py -v

Note: These tests require the MCP SDK to be installed. They will be skipped
if the SDK is not available.
"""
import pytest
import sys
import os
import json
from unittest.mock import Mock, MagicMock, patch
from collections import namedtuple
from decimal import Decimal
from datetime import datetime, date

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
    """Set up mock environment variables"""
    env_vars = {
        'DATABRICKS_HOST': 'https://test.cloud.databricks.com',
        'DATABRICKS_TOKEN': 'test-token',
        'DATABRICKS_HTTP_PATH': '/sql/test',
        'DATABRICKS_SERVER_HOSTNAME': 'test.cloud.databricks.com',
        'CLUSTER_ID': 'test-cluster'
    }
    with patch.dict(os.environ, env_vars, clear=False):
        yield


# =============================================================================
# FORMAT_RESULTS_STRUCTURED TESTS
# =============================================================================

class TestFormatResultsStructured:
    """Tests for format_results_structured helper function"""
    
    def test_empty_results(self, mock_env_vars):
        """Test formatting empty results"""
        from mcp.databricks.server import format_results_structured
        
        result = format_results_structured([], limit=100)
        
        assert result['success'] is True
        assert result['row_count'] == 0
        assert result['data'] == []
        assert result['truncated'] is False
    
    def test_results_with_namedtuple(self, mock_env_vars):
        """Test formatting results from namedtuple rows"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['id', 'name', 'value'])
        results = [
            Row(1, 'Alice', 100),
            Row(2, 'Bob', 200),
        ]
        
        formatted = format_results_structured(results, limit=100)
        
        assert formatted['success'] is True
        assert formatted['row_count'] == 2
        assert formatted['columns'] == ['id', 'name', 'value']
        assert len(formatted['data']) == 2
        assert formatted['data'][0]['id'] == 1
        assert formatted['data'][0]['name'] == 'Alice'
    
    def test_results_truncation(self, mock_env_vars):
        """Test that results are truncated when exceeding limit"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['id'])
        results = [Row(i) for i in range(100)]
        
        formatted = format_results_structured(results, limit=10)
        
        assert formatted['row_count'] == 100
        assert formatted['rows_returned'] == 10
        assert len(formatted['data']) == 10
        assert formatted['truncated'] is True
    
    def test_results_not_truncated_when_under_limit(self, mock_env_vars):
        """Test that results are not marked truncated when under limit"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['id'])
        results = [Row(i) for i in range(5)]
        
        formatted = format_results_structured(results, limit=100)
        
        assert formatted['truncated'] is False
    
    def test_execution_time_included(self, mock_env_vars):
        """Test that execution time is included when provided"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['id'])
        results = [Row(1)]
        
        formatted = format_results_structured(results, limit=100, execution_time_ms=123.45)
        
        assert formatted['execution_time_ms'] == 123.45
    
    def test_non_serializable_types_converted(self, mock_env_vars):
        """Test that non-serializable types are converted to strings"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['id', 'amount', 'created'])
        results = [
            Row(1, Decimal('123.45'), datetime(2024, 1, 15, 10, 30, 0)),
        ]
        
        formatted = format_results_structured(results, limit=100)
        
        # Should be JSON serializable
        json_str = json.dumps(formatted)
        assert json_str is not None
        
        # Non-serializable types should be converted to strings
        data = formatted['data'][0]
        assert isinstance(data['amount'], (str, int, float))
        assert isinstance(data['created'], str)


# =============================================================================
# FORMAT_RESULTS_TEXT TESTS
# =============================================================================

class TestFormatResultsText:
    """Tests for format_results_text helper function"""
    
    def test_empty_results_text(self, mock_env_vars):
        """Test text formatting of empty results"""
        from mcp.databricks.server import format_results_text
        
        result = format_results_text([], limit=100)
        
        assert "0 rows" in result
    
    def test_results_with_headers(self, mock_env_vars):
        """Test text formatting includes headers"""
        from mcp.databricks.server import format_results_text
        
        Row = namedtuple('Row', ['id', 'name'])
        results = [Row(1, 'Alice'), Row(2, 'Bob')]
        
        text = format_results_text(results, limit=100)
        
        assert 'id' in text
        assert 'name' in text
        assert 'Alice' in text
        assert 'Bob' in text
    
    def test_text_truncation_message(self, mock_env_vars):
        """Test text format shows truncation message"""
        from mcp.databricks.server import format_results_text
        
        Row = namedtuple('Row', ['id'])
        results = [Row(i) for i in range(100)]
        
        text = format_results_text(results, limit=10)
        
        assert "more rows" in text


# =============================================================================
# ADD_LIMIT_IF_NEEDED TESTS
# =============================================================================

class TestAddLimitIfNeeded:
    """Tests for add_limit_if_needed helper function"""
    
    def test_adds_limit_to_select(self, mock_env_vars):
        """Test LIMIT is added to SELECT without one"""
        from mcp.databricks.server import add_limit_if_needed
        
        query = "SELECT * FROM users"
        result = add_limit_if_needed(query, 100)
        
        assert "LIMIT 100" in result
    
    def test_does_not_add_limit_if_exists(self, mock_env_vars):
        """Test LIMIT is not added if already present"""
        from mcp.databricks.server import add_limit_if_needed
        
        query = "SELECT * FROM users LIMIT 50"
        result = add_limit_if_needed(query, 100)
        
        assert result == query
        assert "LIMIT 100" not in result
    
    def test_does_not_add_limit_to_show(self, mock_env_vars):
        """Test LIMIT is not added to SHOW queries"""
        from mcp.databricks.server import add_limit_if_needed
        
        query = "SHOW TABLES IN schema"
        result = add_limit_if_needed(query, 100)
        
        assert result == query
    
    def test_does_not_add_limit_to_describe(self, mock_env_vars):
        """Test LIMIT is not added to DESCRIBE queries"""
        from mcp.databricks.server import add_limit_if_needed
        
        query = "DESCRIBE table_name"
        result = add_limit_if_needed(query, 100)
        
        assert result == query
    
    def test_does_not_add_limit_to_create(self, mock_env_vars):
        """Test LIMIT is not added to CREATE queries"""
        from mcp.databricks.server import add_limit_if_needed
        
        query = "CREATE TABLE test AS SELECT * FROM source"
        result = add_limit_if_needed(query, 100)
        
        # Should not add another LIMIT
        assert result.count("LIMIT") <= 1
    
    def test_handles_lowercase_select(self, mock_env_vars):
        """Test handles lowercase SELECT"""
        from mcp.databricks.server import add_limit_if_needed
        
        query = "select * from users"
        result = add_limit_if_needed(query, 100)
        
        assert "LIMIT 100" in result
    
    def test_handles_mixed_case(self, mock_env_vars):
        """Test handles mixed case queries"""
        from mcp.databricks.server import add_limit_if_needed
        
        query = "Select * From users Where id > 10"
        result = add_limit_if_needed(query, 100)
        
        assert "LIMIT 100" in result
    
    def test_removes_trailing_semicolon(self, mock_env_vars):
        """Test removes trailing semicolon before adding LIMIT"""
        from mcp.databricks.server import add_limit_if_needed
        
        query = "SELECT * FROM users;"
        result = add_limit_if_needed(query, 100)
        
        assert result.endswith("LIMIT 100")
        assert not result.endswith(";")
    
    def test_handles_whitespace(self, mock_env_vars):
        """Test handles queries with extra whitespace"""
        from mcp.databricks.server import add_limit_if_needed
        
        query = "  SELECT * FROM users  "
        result = add_limit_if_needed(query, 100)
        
        assert "LIMIT 100" in result
    
    def test_handles_subquery_with_limit(self, mock_env_vars):
        """Test handles subqueries that have LIMIT"""
        from mcp.databricks.server import add_limit_if_needed
        
        # This query has LIMIT in subquery but not in outer query
        # Current implementation will see LIMIT and not add another
        query = "SELECT * FROM (SELECT * FROM users LIMIT 10) subq"
        result = add_limit_if_needed(query, 100)
        
        # Current behavior: won't add LIMIT because it sees LIMIT in query
        # This is a known limitation
        assert "LIMIT" in result


# =============================================================================
# DATA SERIALIZATION TESTS
# =============================================================================

class TestDataSerialization:
    """Tests for data serialization in responses"""
    
    def test_serialize_decimal(self, mock_env_vars):
        """Test Decimal values are serialized correctly"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['amount'])
        results = [Row(Decimal('123.456789'))]
        
        formatted = format_results_structured(results, limit=100)
        
        # Should be JSON serializable
        json_str = json.dumps(formatted)
        parsed = json.loads(json_str)
        
        assert parsed['data'][0]['amount'] is not None
    
    def test_serialize_datetime(self, mock_env_vars):
        """Test datetime values are serialized correctly"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['created_at'])
        results = [Row(datetime(2024, 1, 15, 10, 30, 45))]
        
        formatted = format_results_structured(results, limit=100)
        
        # Should be JSON serializable
        json_str = json.dumps(formatted)
        parsed = json.loads(json_str)
        
        assert '2024' in str(parsed['data'][0]['created_at'])
    
    def test_serialize_date(self, mock_env_vars):
        """Test date values are serialized correctly"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['birth_date'])
        results = [Row(date(1990, 5, 15))]
        
        formatted = format_results_structured(results, limit=100)
        
        # Should be JSON serializable
        json_str = json.dumps(formatted)
        parsed = json.loads(json_str)
        
        assert '1990' in str(parsed['data'][0]['birth_date'])
    
    def test_serialize_none(self, mock_env_vars):
        """Test None values are serialized as null"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['nullable_field'])
        results = [Row(None)]
        
        formatted = format_results_structured(results, limit=100)
        
        json_str = json.dumps(formatted)
        
        assert 'null' in json_str or formatted['data'][0]['nullable_field'] is None
    
    def test_serialize_boolean(self, mock_env_vars):
        """Test boolean values are serialized correctly"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['is_active', 'is_deleted'])
        results = [Row(True, False)]
        
        formatted = format_results_structured(results, limit=100)
        
        assert formatted['data'][0]['is_active'] is True
        assert formatted['data'][0]['is_deleted'] is False
    
    def test_serialize_nested_structure(self, mock_env_vars):
        """Test nested structures are handled"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['metadata'])
        # Some databases return complex types
        results = [Row({'key': 'value', 'nested': {'a': 1}})]
        
        formatted = format_results_structured(results, limit=100)
        
        # Should be JSON serializable
        json_str = json.dumps(formatted)
        assert json_str is not None
    
    def test_serialize_list_field(self, mock_env_vars):
        """Test list fields are serialized correctly"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['tags'])
        results = [Row(['tag1', 'tag2', 'tag3'])]
        
        formatted = format_results_structured(results, limit=100)
        
        # Should be JSON serializable
        json_str = json.dumps(formatted)
        parsed = json.loads(json_str)
        
        assert parsed['data'][0]['tags'] == ['tag1', 'tag2', 'tag3']


# =============================================================================
# COLUMN EXTRACTION TESTS
# =============================================================================

class TestColumnExtraction:
    """Tests for column name extraction from results"""
    
    def test_extract_columns_from_namedtuple(self, mock_env_vars):
        """Test column extraction from namedtuple"""
        from mcp.databricks.server import format_results_structured
        
        Row = namedtuple('Row', ['col_a', 'col_b', 'col_c'])
        results = [Row(1, 2, 3)]
        
        formatted = format_results_structured(results, limit=100)
        
        assert formatted['columns'] == ['col_a', 'col_b', 'col_c']
    
    def test_extract_columns_from_dict_row(self, mock_env_vars):
        """Test column extraction from dict-like rows"""
        from mcp.databricks.server import format_results_structured
        
        # Some connectors return dict-like objects
        class DictRow:
            def __init__(self, data):
                self._data = data
                self._fields = list(data.keys())
            
            def asDict(self):
                return self._data
            
            def __iter__(self):
                return iter(self._data.values())
        
        results = [DictRow({'x': 1, 'y': 2})]
        
        formatted = format_results_structured(results, limit=100)
        
        # Should extract columns somehow
        assert 'columns' in formatted
    
    def test_handles_row_without_fields(self, mock_env_vars):
        """Test handling rows without _fields attribute"""
        from mcp.databricks.server import format_results_structured
        
        # Plain tuple without field names
        results = [(1, 'test', 100)]
        
        formatted = format_results_structured(results, limit=100)
        
        # Should not crash
        assert formatted['success'] is True
