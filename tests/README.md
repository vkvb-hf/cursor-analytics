# Test Suite

This directory contains unit tests for all Databricks utilities.

## Running Tests

```bash
# Install pytest if not already installed
pip install pytest pytest-mock

# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_query_util.py

# Run with verbose output
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=core --cov=databricks_api --cov=databricks_cli
```

## Test Structure

- `conftest.py` - Shared fixtures and configuration
- `test_query_util.py` - Tests for query execution utilities
- `test_databricks_job_runner.py` - Tests for job runner
- `test_table_inspector.py` - Tests for table inspection
- `test_databricks_api.py` - Tests for Python API
- `test_databricks_cli.py` - Tests for CLI tool
- `test_run_sql_file.py` - Tests for SQL file execution

## Test Coverage

The tests use mocks to avoid requiring actual Databricks connections. All tests should pass without real credentials.

## Adding New Tests

When adding new functionality:
1. Add corresponding test file
2. Use fixtures from `conftest.py`
3. Mock external dependencies (Databricks API, file I/O)
4. Test both success and error cases

