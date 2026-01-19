#!/usr/bin/env python3
"""
Simple import test that checks what dependencies are needed
"""
import sys
import os

# Add parent directory to path (since we're now in tests/ subdirectory)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_dependencies():
    """Check which dependencies are installed"""
    print("=" * 80)
    print("CHECKING DEPENDENCIES")
    print("=" * 80)
    
    dependencies = {
        'requests': 'requests',
        'databricks-sql-connector': 'databricks',
        'pandas': 'pandas'
    }
    
    missing = []
    installed = []
    
    for package_name, import_name in dependencies.items():
        try:
            __import__(import_name)
            installed.append(package_name)
            print(f"  ✅ {package_name} installed")
        except ImportError:
            missing.append(package_name)
            print(f"  ❌ {package_name} NOT installed")
    
    print("\n" + "=" * 80)
    if missing:
        print(f"Missing dependencies: {', '.join(missing)}")
        print("\nTo install:")
        print(f"  pip install {' '.join(missing)}")
        print("\nOr install all requirements:")
        print("  pip install -r requirements.txt")
        assert False
    else:
        print("✅ All dependencies installed!")
        assert True


def test_imports_with_graceful_failure():
    """Test imports, showing what fails gracefully"""
    print("\n" + "=" * 80)
    print("TESTING IMPORTS (with graceful failure handling)")
    print("=" * 80)
    
    results = {}
    
    # Test format_value (no external deps)
    try:
        from core.query_util import format_value
        print("  ✅ format_value imported (no external dependencies)")
        results['format_value'] = True
        
        # Test it works
        assert format_value(None) == 'NULL'
        assert format_value(123) == '123'
        print("  ✅ format_value function works correctly")
    except Exception as e:
        print(f"  ❌ format_value failed: {e}")
        results['format_value'] = False
    
    # Test imports that require requests
    try:
        from core.databricks_job_runner import DatabricksJobRunner
        print("  ✅ DatabricksJobRunner imported")
        results['job_runner'] = True
        
        # Test initialization
        runner = DatabricksJobRunner(host='test', token='test')
        assert runner.host == 'test'
        print("  ✅ DatabricksJobRunner can be initialized")
    except ImportError as e:
        if 'requests' in str(e):
            print("  ⚠️  DatabricksJobRunner requires 'requests' package")
        else:
            print(f"  ❌ DatabricksJobRunner import failed: {e}")
        results['job_runner'] = False
    except Exception as e:
        print(f"  ❌ DatabricksJobRunner error: {e}")
        results['job_runner'] = False
    
    # Test imports that require databricks-sql-connector
    try:
        from core.query_util import run_query, print_table
        print("  ✅ query_util functions imported")
        results['query_util'] = True
    except ImportError as e:
        if 'databricks' in str(e):
            print("  ⚠️  query_util requires 'databricks-sql-connector' package")
        else:
            print(f"  ❌ query_util import failed: {e}")
        results['query_util'] = False
    except Exception as e:
        print(f"  ❌ query_util error: {e}")
        results['query_util'] = False
    
    # Test table_inspector
    try:
        from core.table_inspector import TableInspector
        print("  ✅ TableInspector imported")
        results['table_inspector'] = True
        
        # Test initialization
        inspector = TableInspector(server_hostname='test', http_path='test', token='test')
        assert inspector.server_hostname == 'test'
        print("  ✅ TableInspector can be initialized")
    except ImportError as e:
        if 'databricks' in str(e):
            print("  ⚠️  TableInspector requires 'databricks-sql-connector' package")
        else:
            print(f"  ❌ TableInspector import failed: {e}")
        results['table_inspector'] = False
    except Exception as e:
        print(f"  ❌ TableInspector error: {e}")
        results['table_inspector'] = False
    
    return results


def test_functionality_with_mocks():
    """Test functions work with mocks (no real connection needed)"""
    print("\n" + "=" * 80)
    print("TESTING FUNCTIONALITY WITH MOCKS")
    print("=" * 80)
    
    try:
        from core.query_util import format_value, print_table
        
        # Test format_value with various inputs
        print("\n  Testing format_value function:")
        test_cases = [
            (None, 'NULL'),
            (123, '123'),
            (1234567, '1,234,567'),
            (123.45, '123.45'),
            ('test', 'test'),
        ]
        
        all_passed = True
        for value, expected in test_cases:
            result = format_value(value)
            if result == expected:
                print(f"    ✅ format_value({repr(value)}) = {repr(result)}")
            else:
                print(f"    ❌ format_value({repr(value)}) = {repr(result)}, expected {repr(expected)}")
                all_passed = False
        
        # Test print_table with sample data
        print("\n  Testing print_table function:")
        class MockRow:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)
        
        sample_data = [
            MockRow(id=1, name='Test 1', value=100),
            MockRow(id=2, name='Test 2', value=200),
        ]
        
        print("    Sample output:")
        print_table(sample_data, column_names=['id', 'name', 'value'], limit=5)
        print("    ✅ print_table executed successfully")
        
        assert all_passed
    except Exception as e:
        print(f"  ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        assert False


def main():
    """Main test function"""
    print("\n" + "=" * 80)
    print("SIMPLE IMPORT AND FUNCTIONALITY TEST")
    print("=" * 80)
    
    # Check dependencies
    deps_ok = check_dependencies()
    
    # Test imports
    import_results = test_imports_with_graceful_failure()
    
    # Test functionality
    if import_results.get('format_value'):
        func_ok = test_functionality_with_mocks()
    else:
        func_ok = False
        print("\n⚠️  Skipping functionality tests (format_value not available)")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    if deps_ok:
        print("✅ All dependencies installed")
    else:
        print("⚠️  Some dependencies missing - install with: pip install -r requirements.txt")
    
    print(f"\nImport results:")
    for name, result in import_results.items():
        status = "✅" if result else "❌"
        print(f"  {status} {name}")
    
    if func_ok:
        print("\n✅ Functionality tests passed")
    
    print("\n" + "=" * 80)
    
    if deps_ok and all(import_results.values()) and func_ok:
        print("✅ All tests passed!")
        return 0
    else:
        print("⚠️  Some tests failed or dependencies missing")
        print("\nTo fix:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Run full test: python test_imports_and_functions.py")
        return 1


if __name__ == "__main__":
    sys.exit(main())

