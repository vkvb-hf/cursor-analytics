#!/usr/bin/env python3
"""
Verification script to check if everything is set up correctly.

Run this to verify:
1. All imports work
2. Configuration is set up
3. Core utilities are accessible
4. API and CLI are functional

Usage: python verify_setup.py
"""
import sys
import os

def check_imports():
    """Check if all core modules can be imported"""
    print("=" * 80)
    print("Checking imports...")
    print("=" * 80)
    
    try:
        from core import DatabricksJobRunner, TableInspector
        print("✓ Core utilities imported")
    except Exception as e:
        print(f"✗ Failed to import core utilities: {e}")
        return False
    
    try:
        from core.query_util import run_query, print_table
        print("✓ Query utilities imported")
    except Exception as e:
        print(f"✗ Failed to import query utilities: {e}")
        return False
    
    try:
        from databricks_api import DatabricksAPI, sql, inspect, notebook
        print("✓ Databricks API imported")
    except Exception as e:
        print(f"✗ Failed to import databricks_api: {e}")
        return False
    
    try:
        import databricks_cli
        print("✓ Databricks CLI imported")
    except Exception as e:
        print(f"✗ Failed to import databricks_cli: {e}")
        return False
    
    return True


def check_config():
    """Check if configuration is set up"""
    print("\n" + "=" * 80)
    print("Checking configuration...")
    print("=" * 80)
    
    try:
        from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN, DATABRICKS_HOST
        
        config_ok = True
        
        if SERVER_HOSTNAME == 'your-workspace.cloud.databricks.com':
            print("⚠️  SERVER_HOSTNAME is not configured (using default)")
            config_ok = False
        else:
            print(f"✓ SERVER_HOSTNAME: {SERVER_HOSTNAME}")
        
        if HTTP_PATH == 'sql/protocolv1/o/YOUR_ORG_ID/YOUR_CLUSTER_ID':
            print("⚠️  HTTP_PATH is not configured (using default)")
            config_ok = False
        else:
            print(f"✓ HTTP_PATH: configured")
        
        if TOKEN == 'dapi...':
            print("⚠️  TOKEN is not configured (using default)")
            config_ok = False
        else:
            print(f"✓ TOKEN: configured")
        
        if DATABRICKS_HOST == 'https://your-workspace.cloud.databricks.com':
            print("⚠️  DATABRICKS_HOST is not configured (using default)")
            config_ok = False
        else:
            print(f"✓ DATABRICKS_HOST: configured")
        
        if not config_ok:
            print("\n⚠️  Configuration not fully set up. Edit config.py with your credentials.")
            return False
        
        return True
        
    except ImportError as e:
        print(f"✗ Failed to import config: {e}")
        print("   Make sure config.py exists (copy from config.py.example)")
        return False


def check_api_functionality():
    """Check if API can be instantiated"""
    print("\n" + "=" * 80)
    print("Checking API functionality...")
    print("=" * 80)
    
    try:
        from databricks_api import DatabricksAPI
        
        # Try to create API instance (won't connect without real config)
        api = DatabricksAPI()
        print("✓ DatabricksAPI can be instantiated")
        
        # Check if methods exist
        assert hasattr(api, 'run_sql')
        assert hasattr(api, 'inspect_table')
        assert hasattr(api, 'create_notebook')
        assert hasattr(api, 'run_notebook_job')
        print("✓ All API methods are available")
        
        return True
        
    except Exception as e:
        print(f"✗ API functionality check failed: {e}")
        return False


def check_cli_functionality():
    """Check if CLI can be imported and has required functions"""
    print("\n" + "=" * 80)
    print("Checking CLI functionality...")
    print("=" * 80)
    
    try:
        import databricks_cli
        
        # Check if main function exists
        assert hasattr(databricks_cli, 'main')
        print("✓ CLI main function available")
        
        # Check if command functions exist
        assert hasattr(databricks_cli, 'sql_command')
        assert hasattr(databricks_cli, 'notebook_command')
        assert hasattr(databricks_cli, 'table_command')
        print("✓ All CLI command functions available")
        
        return True
        
    except Exception as e:
        print(f"✗ CLI functionality check failed: {e}")
        return False


def check_tests():
    """Check if tests can be run"""
    print("\n" + "=" * 80)
    print("Checking test suite...")
    print("=" * 80)
    
    try:
        import pytest
        print("✓ pytest is installed")
    except ImportError:
        print("⚠️  pytest is not installed (install with: pip install pytest pytest-mock)")
        return False
    
    # Check if test files exist
    test_files = [
        'tests/test_query_util.py',
        'tests/test_databricks_job_runner.py',
        'tests/test_table_inspector.py',
        'tests/test_databricks_api.py',
        'tests/test_databricks_cli.py',
    ]
    
    all_exist = True
    for test_file in test_files:
        if os.path.exists(test_file):
            print(f"✓ {test_file} exists")
        else:
            print(f"✗ {test_file} not found")
            all_exist = False
    
    return all_exist


def main():
    """Run all verification checks"""
    print("\n" + "=" * 80)
    print("DATABRICKS TOOLKIT - SETUP VERIFICATION")
    print("=" * 80 + "\n")
    
    results = []
    
    results.append(("Imports", check_imports()))
    results.append(("Configuration", check_config()))
    results.append(("API Functionality", check_api_functionality()))
    results.append(("CLI Functionality", check_cli_functionality()))
    results.append(("Test Suite", check_tests()))
    
    print("\n" + "=" * 80)
    print("VERIFICATION SUMMARY")
    print("=" * 80)
    
    all_passed = True
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {name}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 80)
    if all_passed:
        print("✓ All checks passed! You're ready to use the toolkit.")
        print("\nQuick start:")
        print("  from databricks_api import sql, inspect, notebook")
        print("  results = sql('SELECT 1')")
        return 0
    else:
        print("⚠️  Some checks failed. Please review the output above.")
        print("\nNext steps:")
        print("  1. Make sure config.py is set up (copy from config.py.example)")
        print("  2. Install dependencies: pip install databricks-sql-connector requests")
        print("  3. Install test dependencies: pip install pytest pytest-mock")
        return 1


if __name__ == "__main__":
    sys.exit(main())

