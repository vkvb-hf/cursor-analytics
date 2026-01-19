# Test Suite

This directory contains comprehensive tests for cursor-analytics.

## Test Categories

### Unit Tests (Fast, No External Dependencies)
- `test_mcp_helpers.py` - Helper functions for MCP tools
- `test_query_util.py` - Query formatting utilities
- `test_connection_pool.py` - Connection pool logic

### Integration Tests (Mocked External Services)
- `test_mcp_tools_execution.py` - MCP tool execution with mocked backends
- `test_core_integration.py` - Core module integration
- `test_mcp_integration.py` - MCP server structure validation
- `test_table_inspector.py` - Table inspection with mocked DB
- `test_databricks_job_runner.py` - Job runner with mocked API

### Error Handling Tests
- `test_error_handling.py` - Error scenarios across all modules

### Structure Validation Tests
- `test_mcp_databricks.py` - Databricks MCP structure
- `test_mcp_google_sheets.py` - Google Sheets MCP structure

## Running Tests

```bash
# Install test dependencies
pip install -e ".[test]"

# Run all tests
pytest tests/ -v

# Run only unit tests (fast)
pytest tests/ -v -m "not integration"

# Run only integration tests
pytest tests/ -v -m "integration"

# Run with coverage
pytest tests/ --cov=core --cov=mcp --cov-report=html

# Run specific test file
pytest tests/test_mcp_tools_execution.py -v

# Run specific test class
pytest tests/test_mcp_tools_execution.py::TestExecuteSQLTool -v

# Run specific test
pytest tests/test_mcp_tools_execution.py::TestExecuteSQLTool::test_execute_sql_returns_structured_response -v

# Run tests matching a pattern
pytest tests/ -v -k "error"

# Run with verbose output and show print statements
pytest tests/ -v -s
```

## Test Structure

```
tests/
├── conftest.py                    # Shared fixtures
├── README.md                      # This file
│
├── # Unit Tests
├── test_mcp_helpers.py            # MCP helper functions
├── test_query_util.py             # Query utilities
├── test_connection_pool.py        # Connection pool
│
├── # Integration Tests
├── test_mcp_tools_execution.py    # MCP tool execution
├── test_core_integration.py       # Core module integration
├── test_mcp_integration.py        # MCP structure validation
├── test_table_inspector.py        # Table inspector
├── test_databricks_job_runner.py  # Job runner
├── test_run_sql_file.py           # SQL file execution
│
├── # Error Handling
├── test_error_handling.py         # Error scenarios
│
├── # Structure Validation
├── test_mcp_databricks.py         # Databricks MCP structure
├── test_mcp_google_sheets.py      # Google Sheets MCP structure
│
└── # Legacy/Other
    ├── test_all_functions_integration.py
    ├── test_functions_direct.py
    └── test_imports_simple.py
```

## Writing New Tests

### Test Naming Convention
- Test files: `test_<module_name>.py`
- Test classes: `Test<FeatureName>`
- Test methods: `test_<scenario>_<expected_behavior>`

### Example Test Structure

```python
"""
Tests for <module_name>

Run with: pytest tests/test_<module_name>.py -v
"""
import pytest
from unittest.mock import Mock, MagicMock, patch

class TestFeatureName:
    """Tests for <feature>"""
    
    @pytest.fixture
    def setup_fixture(self):
        """Setup for tests"""
        yield some_value
    
    def test_happy_path(self, setup_fixture):
        """Test normal operation"""
        result = function_under_test()
        assert result['success'] is True
    
    def test_error_case(self, setup_fixture):
        """Test error handling"""
        with pytest.raises(ExpectedException):
            function_under_test(invalid_input)
    
    @pytest.mark.integration
    def test_with_mocked_service(self, setup_fixture):
        """Test with mocked external service"""
        with patch('module.external_service') as mock_service:
            mock_service.return_value = expected_value
            result = function_under_test()
            assert result == expected_value
```

### Fixtures

Common fixtures are defined in `conftest.py`:

- `mock_config` - Mock Databricks configuration
- `mock_sql_connection` - Mock SQL connection and cursor
- `mock_requests_response` - Mock HTTP response
- `sample_table_data` - Sample data for testing
- `sample_notebook_content` - Sample notebook content

### Markers

- `@pytest.mark.integration` - Tests that require mocked external services
- `@pytest.mark.slow` - Tests that take longer to run

## Coverage Goals

| Module | Target Coverage |
|--------|-----------------|
| `core/connection_pool.py` | 90% |
| `core/databricks_job_runner.py` | 85% |
| `core/table_inspector.py` | 85% |
| `core/query_util.py` | 90% |
| `core/workspace_sync.py` | 80% |
| `mcp/databricks/server.py` | 85% |
| `mcp/google_sheets/server.py` | 80% |

## Continuous Integration

Tests are run automatically on:
- Every push to `main`
- Every pull request

The CI pipeline runs:
1. Syntax validation (smoke test)
2. Unit tests
3. Integration tests with mocked services
4. Coverage report generation

## Troubleshooting

### Import Errors
```bash
# Ensure package is installed in development mode
pip install -e .
```

### Missing Dependencies
```bash
# Install test dependencies
pip install -e ".[test]"
```

### Fixture Not Found
- Check that `conftest.py` is in the tests directory
- Ensure the fixture is defined or imported correctly

### Mock Not Working
- Verify the patch path matches the import path in the module under test
- Use `patch('module.where.used.function')` not `patch('module.where.defined.function')`
