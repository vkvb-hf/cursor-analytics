#!/usr/bin/env python3
"""
Manual test runner - runs tests without pytest
Use this to verify tests work without installing pytest
"""
import sys
import os
from unittest.mock import Mock, MagicMock, patch

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_format_value():
    """Test format_value function"""
    from core.query_util import format_value
    
    assert format_value(None) == 'NULL', "format_value(None) should return 'NULL'"
    assert format_value(123) == '123', "format_value(123) should return '123'"
    assert format_value(1234567) == '1,234,567', "format_value should format large numbers"
    assert format_value(123.45) == '123.45', "format_value should handle floats"
    assert format_value('test') == 'test', "format_value should handle strings"
    assert format_value(True) == 'True', "format_value should handle booleans"
    print("✓ test_format_value passed")


def test_databricks_job_runner_init():
    """Test DatabricksJobRunner initialization"""
    from core.databricks_job_runner import DatabricksJobRunner
    
    runner = DatabricksJobRunner(
        host='https://test.databricks.com',
        token='test-token',
        cluster_id='test-cluster'
    )
    
    assert runner.host == 'https://test.databricks.com'
    assert runner.token == 'test-token'
    assert runner.cluster_id == 'test-cluster'
    assert 'Authorization' in runner.headers
    print("✓ test_databricks_job_runner_init passed")


def test_databricks_api_init():
    """Test DatabricksAPI initialization"""
    from databricks_api import DatabricksAPI
    
    api = DatabricksAPI(
        server_hostname='test-host',
        http_path='test-path',
        token='test-token',
        databricks_host='https://test.databricks.com',
        cluster_id='test-cluster'
    )
    
    assert api.job_runner is not None
    assert api.table_inspector is not None
    assert hasattr(api, 'run_sql')
    assert hasattr(api, 'inspect_table')
    assert hasattr(api, 'create_notebook')
    assert hasattr(api, 'run_notebook_job')
    print("✓ test_databricks_api_init passed")


def test_imports():
    """Test that all modules can be imported"""
    try:
        # Test core package imports
        from core import (
            DatabricksJobRunner,
            TableInspector,
            print_table,
            run_query,
            interactive_sql_main,
            run_sql_file,
            create_workspace_directory,
            upload_csv_to_workspace
        )
        print("✓ Core package imports successful")
        
        # Test individual module imports
        from core.databricks_job_runner import DatabricksJobRunner
        from core.table_inspector import TableInspector
        from core.query_util import run_query, print_table, format_value
        from core.run_sql_file import run_sql_file
        from core.interactive_sql import main as interactive_sql_main
        from core.databricks_workspace import create_workspace_directory, upload_csv_to_workspace
        from core.csv_to_table import create_table_from_csvs
        from core.create_table import create_table
        print("✓ Individual module imports successful")
        
        # Test API imports (if available)
        try:
            from databricks_api import DatabricksAPI, sql, inspect, notebook
            print("✓ Databricks API imports successful")
        except ImportError:
            print("⚠ Databricks API not available (optional)")
        
        # Test CLI imports (if available)
        try:
            import databricks_cli
            print("✓ Databricks CLI imports successful")
        except ImportError:
            print("⚠ Databricks CLI not available (optional)")
        
        print("✓ All imports successful")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all manual tests"""
    print("=" * 80)
    print("MANUAL TEST RUNNER")
    print("=" * 80)
    print()
    
    tests = [
        test_imports,
        test_format_value,
        test_databricks_job_runner_init,
        test_databricks_api_init,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
        print()
    
    print("=" * 80)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 80)
    
    if failed == 0:
        print("\n✓ All manual tests passed!")
        print("\nNote: For full test suite, install pytest:")
        print("  pip install pytest pytest-mock")
        print("  pytest tests/ -v")
        return 0
    else:
        print(f"\n✗ {failed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())


