#!/usr/bin/env python3
"""
Test script to verify imports and actual function functionality.
This tests both imports and actual function execution with sample data.
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all imports work"""
    print("=" * 80)
    print("TESTING IMPORTS")
    print("=" * 80)
    
    errors = []
    
    try:
        # Test core package imports
        print("\n1. Testing core package imports...")
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
        print("   ✅ Core package imports successful")
    except Exception as e:
        print(f"   ❌ Core package import failed: {e}")
        errors.append(f"Core package: {e}")
    
    try:
        # Test individual module imports
        print("\n2. Testing individual module imports...")
        from core.databricks_job_runner import DatabricksJobRunner
        from core.table_inspector import TableInspector
        from core.query_util import run_query, print_table, format_value
        from core.run_sql_file import run_sql_file
        from core.interactive_sql import main as interactive_sql_main
        from core.databricks_workspace import create_workspace_directory, upload_csv_to_workspace
        from core.csv_to_table import create_table_from_csvs
        from core.create_table import create_table
        print("   ✅ Individual module imports successful")
    except Exception as e:
        print(f"   ❌ Individual module import failed: {e}")
        errors.append(f"Individual modules: {e}")
    
    return len(errors) == 0, errors


def test_format_value_function():
    """Test format_value function with actual data"""
    print("\n" + "=" * 80)
    print("TESTING format_value FUNCTION")
    print("=" * 80)
    
    try:
        from core.query_util import format_value
        
        test_cases = [
            (None, 'NULL'),
            (123, '123'),
            (1234567, '1,234,567'),
            (123.45, '123.45'),
            ('test', 'test'),
            (True, 'True'),
            (False, 'False'),
        ]
        
        all_passed = True
        for value, expected in test_cases:
            result = format_value(value)
            if result == expected:
                print(f"   ✅ format_value({repr(value)}) = {repr(result)}")
            else:
                print(f"   ❌ format_value({repr(value)}) = {repr(result)}, expected {repr(expected)}")
                all_passed = False
        
        return all_passed
    except Exception as e:
        print(f"   ❌ Error testing format_value: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_print_table_function():
    """Test print_table function with sample data"""
    print("\n" + "=" * 80)
    print("TESTING print_table FUNCTION")
    print("=" * 80)
    
    try:
        from core.query_util import print_table
        
        # Create mock row objects
        class MockRow:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)
        
        sample_data = [
            MockRow(id=1, name='Alice', value=100.50),
            MockRow(id=2, name='Bob', value=200.75),
            MockRow(id=3, name='Charlie', value=300.00),
        ]
        
        print("\n   Sample table output:")
        print("   " + "-" * 76)
        print_table(sample_data, column_names=['id', 'name', 'value'], limit=10, title="Test Table")
        print("   " + "-" * 76)
        print("   ✅ print_table function executed successfully")
        
        return True
    except Exception as e:
        print(f"   ❌ Error testing print_table: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_databricks_job_runner_initialization():
    """Test DatabricksJobRunner can be initialized"""
    print("\n" + "=" * 80)
    print("TESTING DatabricksJobRunner INITIALIZATION")
    print("=" * 80)
    
    try:
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
        
        print("   ✅ DatabricksJobRunner initialized successfully")
        print(f"   ✅ Host: {runner.host}")
        print(f"   ✅ Headers configured: {list(runner.headers.keys())}")
        
        return True
    except Exception as e:
        print(f"   ❌ Error initializing DatabricksJobRunner: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_table_inspector_initialization():
    """Test TableInspector can be initialized"""
    print("\n" + "=" * 80)
    print("TESTING TableInspector INITIALIZATION")
    print("=" * 80)
    
    try:
        from core.table_inspector import TableInspector
        
        inspector = TableInspector(
            server_hostname='test-host',
            http_path='test-path',
            token='test-token'
        )
        
        assert inspector.server_hostname == 'test-host'
        assert inspector.http_path == 'test-path'
        assert inspector.token == 'test-token'
        
        print("   ✅ TableInspector initialized successfully")
        print(f"   ✅ Server hostname: {inspector.server_hostname}")
        print(f"   ✅ HTTP path: {inspector.http_path}")
        
        return True
    except Exception as e:
        print(f"   ❌ Error initializing TableInspector: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_sql_query_functionality():
    """Test SQL query functionality with a sample query (mocked)"""
    print("\n" + "=" * 80)
    print("TESTING SQL QUERY FUNCTIONALITY")
    print("=" * 80)
    
    try:
        from core.query_util import run_query, print_table
        from unittest.mock import patch, MagicMock
        
        # Check if config exists
        try:
            from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
            has_config = True
            print("   ℹ️  Config file found - will attempt real connection test")
        except ImportError:
            has_config = False
            print("   ℹ️  No config file - testing with mock connection")
        
        if has_config and SERVER_HOSTNAME != 'your-workspace.cloud.databricks.com':
            # Try actual connection (will fail gracefully if not configured)
            print("\n   Attempting to test with actual Databricks connection...")
            print("   (This will fail if credentials are not configured)")
            try:
                # Use a simple query that should work
                result = run_query("SELECT 1 as test_value, 'Hello' as test_string", limit=1)
                if result:
                    print("   ✅ Real SQL query executed successfully!")
                    print("   ✅ Connection to Databricks works!")
                    return True
                else:
                    print("   ⚠️  Query returned None (connection may have failed)")
            except Exception as e:
                print(f"   ⚠️  Real connection test failed (expected if not configured): {e}")
                print("   ℹ️  This is normal if Databricks credentials are not set up")
        
        # Test with mock
        print("\n   Testing with mock connection...")
        with patch('core.query_util.sql.connect') as mock_connect:
            mock_conn = MagicMock()
            mock_cursor = MagicMock()
            
            # Mock cursor description
            mock_cursor.description = [
                ('test_value', 'int', None, None, None, None, None),
                ('test_string', 'string', None, None, None, None, None)
            ]
            
            # Mock fetchall result
            class MockRow:
                def __init__(self, test_value, test_string):
                    self.test_value = test_value
                    self.test_string = test_string
            
            mock_cursor.fetchall.return_value = [
                MockRow(1, 'Hello'),
                MockRow(2, 'World')
            ]
            
            mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
            mock_connect.return_value.__enter__.return_value = mock_conn
            
            result = run_query("SELECT 1 as test_value, 'Hello' as test_string", limit=2)
            
            if result:
                print("   ✅ Mock SQL query executed successfully!")
                print(f"   ✅ Query returned {len(result)} rows")
                print("   ✅ Function works correctly with mocked connection")
                return True
            else:
                print("   ❌ Mock query returned None")
                return False
                
    except Exception as e:
        print(f"   ❌ Error testing SQL query functionality: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("\n" + "=" * 80)
    print("COMPREHENSIVE FUNCTIONALITY TEST")
    print("=" * 80)
    print("\nThis script tests:")
    print("  1. All imports work correctly")
    print("  2. Functions can be called and work with sample data")
    print("  3. SQL query functionality (with mock or real connection)")
    print()
    
    results = {}
    
    # Test imports
    imports_ok, import_errors = test_imports()
    results['imports'] = imports_ok
    
    if not imports_ok:
        print("\n" + "=" * 80)
        print("❌ IMPORT TESTS FAILED")
        print("=" * 80)
        print("\nErrors:")
        for error in import_errors:
            print(f"  - {error}")
        print("\nPlease install dependencies:")
        print("  pip install requests databricks-sql-connector pandas")
        return 1
    
    # Test functions
    results['format_value'] = test_format_value_function()
    results['print_table'] = test_print_table_function()
    results['job_runner'] = test_databricks_job_runner_initialization()
    results['table_inspector'] = test_table_inspector_initialization()
    results['sql_query'] = test_sql_query_functionality()
    
    # Summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {test_name:20s} {status}")
    
    print("\n" + "=" * 80)
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 80)
    
    if passed == total:
        print("\n✅ All tests passed! Functions are working correctly.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. See details above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

