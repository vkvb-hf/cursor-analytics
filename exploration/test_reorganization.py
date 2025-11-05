#!/usr/bin/env python3
"""Test script to verify reorganization works correctly."""

import sys
import os

# Add root to path
sys.path.insert(0, os.path.dirname(__file__))

def test_imports():
    """Test all key imports."""
    print("=" * 80)
    print("Testing Imports")
    print("=" * 80)
    
    tests = []
    
    # Test config
    try:
        from config import SERVER_HOSTNAME, TOKEN
        tests.append(("Config import", True, None))
    except Exception as e:
        tests.append(("Config import", False, str(e)))
    
    # Test utilities
    try:
        from utils import DatabricksJobRunner
        tests.append(("DatabricksJobRunner import", True, None))
    except Exception as e:
        tests.append(("DatabricksJobRunner import", False, str(e)))
    
    try:
        from utils.table_inspector import TableInspector
        tests.append(("TableInspector import", True, None))
    except Exception as e:
        tests.append(("TableInspector import", False, str(e)))
    
    try:
        from utils.databricks_workspace import create_workspace_directory
        tests.append(("databricks_workspace import", True, None))
    except Exception as e:
        tests.append(("databricks_workspace import", False, str(e)))
    
    try:
        from utils.csv_to_table import create_table_from_csvs
        tests.append(("csv_to_table import", True, None))
    except Exception as e:
        tests.append(("csv_to_table import", False, str(e)))
    
    # Print results
    all_passed = True
    for name, passed, error in tests:
        status = "✅" if passed else "❌"
        print(f"{status} {name}")
        if not passed:
            print(f"   Error: {error}")
            all_passed = False
    
    return all_passed


def test_structure():
    """Test that structure is correct."""
    print("\n" + "=" * 80)
    print("Testing Directory Structure")
    print("=" * 80)
    
    required_dirs = [
        "utils",
        "projects/adyen_ml",
        "tests",
        "docs"
    ]
    
    required_files = [
        "utils/__init__.py",
        "utils/databricks_job_runner.py",
        "utils/table_inspector.py",
        "utils/databricks_workspace.py",
        "docs/AI_UTILITY_GUIDE.md",
        "projects/adyen_ml/README.md",
        "README.md"
    ]
    
    all_good = True
    
    print("\n📁 Directories:")
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✅ {dir_path}/")
        else:
            print(f"❌ {dir_path}/ (missing)")
            all_good = False
    
    print("\n📄 Files:")
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} (missing)")
            all_good = False
    
    return all_good


def test_project_files():
    """Test that project files are accessible."""
    print("\n" + "=" * 80)
    print("Testing Project Files")
    print("=" * 80)
    
    project_files = [
        "projects/adyen_ml/run_adyen_ml_job.py",
        "projects/adyen_ml/check_duplicates.py",
        "projects/adyen_ml/check_conflicting_attributes.py"
    ]
    
    all_good = True
    for file_path in project_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} (missing)")
            all_good = False
    
    return all_good


def main():
    """Run all tests."""
    print("\n" + "=" * 80)
    print("Reorganization Test Suite")
    print("=" * 80)
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Structure", test_structure()))
    results.append(("Project Files", test_project_files()))
    
    print("\n" + "=" * 80)
    print("Summary")
    print("=" * 80)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 80)
    if all_passed:
        print("✅ All tests passed! Reorganization successful.")
        return 0
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())


