#!/usr/bin/env python3
"""
Smoke Test for cursor-analytics

Run this after ANY change to verify nothing is broken.
This tests all critical import paths and basic functionality.

Usage:
    python scripts/smoke_test.py           # Run all tests
    python scripts/smoke_test.py --quick   # Skip dependency-heavy tests

Exit codes:
    0 - All tests passed
    1 - Some tests failed
"""
import sys
import os
import ast

# Add parent directory to path (this is the pattern we're testing works)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

# Track results
results = []
warnings = []

def test(name, func, critical=True):
    """Run a test and record result"""
    try:
        func()
        results.append((name, True, None, critical))
        print(f"  ✅ {name}")
    except Exception as e:
        results.append((name, False, str(e), critical))
        if critical:
            print(f"  ❌ {name}: {e}")
        else:
            print(f"  ⚠️  {name}: {e} (non-critical)")

def check_syntax(filepath):
    """Check if a Python file has valid syntax"""
    full_path = os.path.join(ROOT_DIR, filepath)
    if os.path.exists(full_path):
        with open(full_path, 'r') as f:
            ast.parse(f.read())
    else:
        raise FileNotFoundError(f"{filepath} not found")

def main():
    quick_mode = '--quick' in sys.argv
    
    print("\n" + "="*60)
    print("CURSOR-ANALYTICS SMOKE TEST")
    if quick_mode:
        print("(Quick mode - skipping dependency tests)")
    print("="*60 + "\n")
    
    # =========================================
    # PHASE 1: File Structure (CRITICAL)
    # =========================================
    print("📁 Testing Directory Structure (CRITICAL)...")
    
    required_dirs = ['core', 'scripts', 'tests', 'docs', 'mcp', 'use_cases', 'archive']
    for dir_name in required_dirs:
        def make_dir_test(d):
            def test_func():
                dir_path = os.path.join(ROOT_DIR, d)
                assert os.path.isdir(dir_path), f"Directory {d} not found"
            return test_func
        test(f"Directory exists: {dir_name}/", make_dir_test(dir_name), critical=True)
    
    # =========================================
    # PHASE 2: Key Files Exist (CRITICAL)
    # =========================================
    print("\n📄 Testing Key Files (CRITICAL)...")
    
    key_files = [
        'README.md',
        'requirements.txt',
        'databricks_api.py',
        'databricks_cli.py',
        'mcp/databricks/server.py',
        'core/__init__.py',
        'config.py.example',
    ]
    
    for file_name in key_files:
        def make_file_test(f):
            def test_func():
                file_path = os.path.join(ROOT_DIR, f)
                assert os.path.exists(file_path), f"File {f} not found"
            return test_func
        test(f"File exists: {file_name}", make_file_test(file_name), critical=True)
    
    # =========================================
    # PHASE 3: Python Syntax Validation (CRITICAL)
    # =========================================
    print("\n🐍 Testing Python Syntax (CRITICAL)...")
    
    critical_python_files = [
        'databricks_api.py',
        'databricks_cli.py',
        'mcp/databricks/server.py',
        'core/__init__.py',
        'core/databricks_job_runner.py',
        'core/table_inspector.py',
        'core/query_util.py',
        'core/workspace_sync.py',
        'core/run_sql_file.py',
    ]
    
    for py_file in critical_python_files:
        def make_syntax_test(filepath):
            def test_func():
                check_syntax(filepath)
            return test_func
        test(f"Syntax valid: {py_file}", make_syntax_test(py_file), critical=True)
    
    # =========================================
    # PHASE 4: Import Tests (Non-critical without deps)
    # =========================================
    if not quick_mode:
        print("\n📦 Testing Imports (requires dependencies)...")
        
        # These may fail if databricks-sql-connector not installed
        test("Import core package", lambda: __import__('core'), critical=False)
        
        def test_databricks_api_class():
            from databricks_api import DatabricksAPI
            assert DatabricksAPI is not None
        test("Import DatabricksAPI class", test_databricks_api_class, critical=False)
        
        test("Import databricks_cli module", lambda: __import__('databricks_cli'), critical=False)
    
    # =========================================
    # PHASE 5: MCP Server Syntax
    # =========================================
    print("\n🔌 Testing MCP Server Files...")
    
    mcp_files = ['mcp/databricks/server.py']
    # Check if Google Sheets MCP exists
    if os.path.exists(os.path.join(ROOT_DIR, 'mcp/google_sheets/server.py')):
        mcp_files.append('mcp/google_sheets/server.py')
    
    for mcp_file in mcp_files:
        def make_mcp_test(filepath):
            def test_func():
                check_syntax(filepath)
            return test_func
        test(f"MCP syntax valid: {mcp_file}", make_mcp_test(mcp_file), critical=True)
    
    # =========================================
    # PHASE 6: Archive Structure Sanity
    # =========================================
    print("\n📂 Testing Archive Structure...")
    
    # Check that archive directories exist
    archive_dirs = ['archive/projects', 'archive/core_unused', 'archive/core_notebook_output']
    for arch_dir in archive_dirs:
        def make_arch_test(d):
            def test_func():
                dir_path = os.path.join(ROOT_DIR, d)
                if not os.path.isdir(dir_path):
                    raise FileNotFoundError(f"Archive directory {d} not found")
            return test_func
        test(f"Archive exists: {arch_dir}", make_arch_test(arch_dir), critical=False)
    
    # =========================================
    # RESULTS SUMMARY
    # =========================================
    print("\n" + "="*60)
    print("RESULTS SUMMARY")
    print("="*60)
    
    critical_passed = sum(1 for _, success, _, critical in results if success and critical)
    critical_failed = sum(1 for _, success, _, critical in results if not success and critical)
    non_critical_passed = sum(1 for _, success, _, critical in results if success and not critical)
    non_critical_failed = sum(1 for _, success, _, critical in results if not success and not critical)
    total = len(results)
    
    print(f"\n  Total Tests:      {total}")
    print(f"  Critical Passed:  {critical_passed} ✅")
    print(f"  Critical Failed:  {critical_failed} ❌")
    print(f"  Optional Passed:  {non_critical_passed} ✅")
    print(f"  Optional Failed:  {non_critical_failed} ⚠️")
    
    if critical_failed > 0:
        print("\n🚨 CRITICAL FAILURES:")
        for name, success, error, critical in results:
            if not success and critical:
                print(f"    - {name}: {error}")
        print("\n❌ SMOKE TEST FAILED - Do not proceed with refactor!")
        return 1
    elif non_critical_failed > 0:
        print("\n⚠️  NON-CRITICAL ISSUES (can proceed with caution):")
        for name, success, error, critical in results:
            if not success and not critical:
                print(f"    - {name}: {error}")
        print("\n✅ CRITICAL TESTS PASSED - Safe to proceed (fix optional issues when possible)")
        return 0
    else:
        print("\n✅ ALL TESTS PASSED - Safe to proceed!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
