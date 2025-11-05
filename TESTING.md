# Testing Guide

## Unit Tests Location

All unit tests are located in the `tests/` directory:

```
tests/
├── __init__.py
├── conftest.py                    # Shared fixtures and mocks
├── test_query_util.py             # Tests for query execution
├── test_databricks_job_runner.py  # Tests for job runner
├── test_table_inspector.py        # Tests for table inspection
├── test_databricks_api.py         # Tests for Python API
├── test_databricks_cli.py         # Tests for CLI tool
├── test_run_sql_file.py           # Tests for SQL file execution
└── test_manual.py                 # Manual tests (no pytest required)
```

## Test Coverage

### Test Files and Coverage

| Test File | Tests | Coverage |
|-----------|-------|----------|
| `test_query_util.py` | 8 tests | Query formatting, execution, error handling |
| `test_databricks_job_runner.py` | 5 tests | Job creation, execution, status checking |
| `test_table_inspector.py` | 4 tests | Schema, stats, samples, duplicates |
| `test_databricks_api.py` | 7 tests | API initialization, methods, convenience functions |
| `test_databricks_cli.py` | 6 tests | CLI commands (sql, notebook, table) |
| `test_run_sql_file.py` | 3 tests | SQL file execution, error handling |

**Total: 37+ test cases**

## Running Tests

### Option 1: Using pytest (Recommended)

```bash
# Install pytest if not already installed
pip install pytest pytest-mock

# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_query_util.py

# Run specific test
pytest tests/test_query_util.py::TestFormatValue::test_format_int

# Run with coverage
pytest tests/ --cov=core --cov=databricks_api --cov=databricks_cli
```

### Option 2: Manual Tests (No pytest required)

```bash
# Run manual tests that don't require pytest
python tests/test_manual.py
```

This will test:
- All imports work
- Basic functionality
- API initialization
- Core utilities

### Option 3: Verify Setup Script

```bash
# Run the verification script
python verify_setup.py
```

## Test Structure

### Fixtures (conftest.py)

Shared fixtures for all tests:
- `mock_config` - Mock configuration values
- `mock_sql_connection` - Mock Databricks SQL connection
- `mock_requests_response` - Mock HTTP responses
- `sample_table_data` - Sample data for testing
- `sample_notebook_content` - Sample notebook content

### Test Categories

1. **Unit Tests** - Test individual functions/classes
2. **Integration Tests** - Test interactions between components
3. **Mock Tests** - Use mocks to avoid real Databricks connections

## What's Tested

### ✅ Core Utilities
- [x] Query formatting (`format_value`)
- [x] Query execution (`run_query`)
- [x] Table printing (`print_table`)
- [x] Job runner initialization
- [x] Job creation and execution
- [x] Table inspection (schema, stats, samples)
- [x] Duplicate detection

### ✅ API Layer
- [x] API initialization
- [x] SQL execution (with/without display)
- [x] Table inspection
- [x] Notebook creation
- [x] Job management
- [x] Convenience functions

### ✅ CLI Layer
- [x] SQL command
- [x] Notebook commands (create, run, status)
- [x] Table commands (inspect, duplicates)
- [x] Interactive mode

## Test Results

Run the tests to see current status:

```bash
# Quick check
python tests/test_manual.py

# Full suite (requires pytest)
pytest tests/ -v
```

## Writing New Tests

When adding new functionality:

1. **Create test file** in `tests/` directory
2. **Use fixtures** from `conftest.py`
3. **Mock external dependencies** (Databricks API, file I/O)
4. **Test both success and error cases**
5. **Follow naming**: `test_*.py` for test files, `test_*` for test functions

Example:
```python
def test_my_new_function():
    """Test my new function"""
    from core.my_module import my_function
    
    # Test success case
    result = my_function(input)
    assert result == expected
    
    # Test error case
    with pytest.raises(ValueError):
        my_function(invalid_input)
```

## Continuous Testing

To ensure tests always pass:

```bash
# Run tests before committing
pytest tests/

# Run with coverage
pytest tests/ --cov=core --cov-report=html
```

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'pytest'`
**Solution:** Install pytest: `pip install pytest pytest-mock`

### Issue: Tests fail with import errors
**Solution:** Make sure you're running from the project root directory

### Issue: Tests fail with connection errors
**Solution:** Tests use mocks - they shouldn't need real connections. Check that mocks are set up correctly.

## Current Test Status

To see the current test status, run:

```bash
python tests/test_manual.py
```

Or with pytest:

```bash
pytest tests/ -v
```

