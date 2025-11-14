#!/usr/bin/env python3
"""
File Placement Validation Script

This script validates that files are placed correctly according to repository structure rules.
Run this after creating or moving files to ensure compliance.

Usage:
    python scripts/validate_file_placement.py
    python scripts/validate_file_placement.py --fix  # Auto-fix issues where possible
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple, Dict

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Allowed files in root directory
ALLOWED_ROOT_FILES = {
    'config.py',
    'config.py.example',
    'README.md',
    'databricks_api.py',
    'databricks_cli.py',
    'requirements.txt',
    'requirements-test.txt'
}

# Directory rules
DIRECTORY_RULES = {
    'core/': {
        'allowed_extensions': ['.py'],
        'allowed_patterns': [],
        'disallowed_patterns': ['test_', 'example_'],
        'description': 'Core reusable utilities'
    },
    'scripts/': {
        'allowed_extensions': ['.py'],
        'allowed_patterns': [],
        'disallowed_patterns': ['test_'],
        'description': 'CLI entry points'
    },
    'notebooks/': {
        'allowed_extensions': ['.py'],
        'allowed_patterns': [],
        'disallowed_patterns': ['test_', 'run_', 'verify_', 'diagnose_', 'find_', 'check_', 'delete_', 'ascs_'],
        'description': 'Reusable notebook utilities only'
    },
    'tests/': {
        'allowed_extensions': ['.py'],
        'allowed_patterns': ['test_'],
        'disallowed_patterns': [],
        'description': 'Test files'
    },
    'examples/': {
        'allowed_extensions': ['.py'],
        'allowed_patterns': ['example_', 'template'],
        'disallowed_patterns': [],
        'description': 'Example scripts and templates'
    },
    'data/': {
        'allowed_extensions': ['.csv', '.json', '.parquet', '.txt'],
        'allowed_patterns': [],
        'disallowed_patterns': ['.py', '.md'],
        'description': 'Data files'
    },
    'docs/': {
        'allowed_extensions': ['.md'],
        'allowed_patterns': [],
        'disallowed_patterns': ['.py', '.csv', '.json'],
        'description': 'Documentation'
    },
    'projects/adhoc/exploration/': {
        'allowed_extensions': ['.py', '.sql'],
        'allowed_patterns': ['test_', 'check_', 'verify_'],
        'disallowed_patterns': [],
        'description': 'Temporary exploration/test scripts'
    },
    'projects/adhoc/notebooks/': {
        'allowed_extensions': ['.py'],
        'allowed_patterns': ['run_', 'test_', 'verify_', 'diagnose_', 'find_', 'check_', 'delete_'],
        'disallowed_patterns': [],
        'description': 'One-time notebook tasks'
    },
    'projects/adhoc/queries/': {
        'allowed_extensions': ['.sql'],
        'allowed_patterns': ['check_', 'test_', 'get_'],
        'disallowed_patterns': [],
        'description': 'One-time investigation queries'
    }
}

# Files that should NOT be in root
ROOT_DISALLOWED_PATTERNS = [
    'test_', 'example_', 'check_', 'verify_', 'diagnose_', 'find_',
    'run_', 'delete_', 'ascs_', 'investigate_', 'inspect_'
]

# Files that should be in specific directories
REQUIRED_PATTERNS = {
    'test_': 'tests/',
    'example_': 'examples/',
    'template': 'examples/',
}


class ValidationError:
    """Represents a validation error"""
    def __init__(self, file_path: str, issue: str, suggestion: str = None):
        self.file_path = file_path
        self.issue = issue
        self.suggestion = suggestion

    def __str__(self):
        msg = f"❌ {self.file_path}: {self.issue}"
        if self.suggestion:
            msg += f"\n   💡 Suggestion: {self.suggestion}"
        return msg


def get_repo_root() -> Path:
    """Get the repository root directory"""
    current = Path(__file__).resolve()
    # Go up from scripts/ to root
    return current.parent.parent


def find_files_in_root(root: Path) -> List[Path]:
    """Find all files in root directory"""
    files = []
    for item in root.iterdir():
        if item.is_file() and not item.name.startswith('.'):
            files.append(item)
    return files


def check_root_directory(root: Path) -> List[ValidationError]:
    """Check root directory for violations"""
    errors = []
    root_files = find_files_in_root(root)
    
    for file in root_files:
        name = file.name
        
        # Check if file is allowed
        if name not in ALLOWED_ROOT_FILES:
            # Check if it matches disallowed patterns
            is_disallowed = any(name.startswith(pattern) for pattern in ROOT_DISALLOWED_PATTERNS)
            
            if is_disallowed or name.endswith(('.md', '.csv', '.json')) and name != 'README.md':
                # Determine where it should go
                suggestion = suggest_correct_location(name, root)
                errors.append(ValidationError(
                    file_path=name,
                    issue=f"File should not be in root directory",
                    suggestion=suggestion
                ))
    
    return errors


def suggest_correct_location(filename: str, root: Path) -> str:
    """Suggest the correct location for a file"""
    name_lower = filename.lower()
    
    # Check required patterns
    for pattern, directory in REQUIRED_PATTERNS.items():
        if filename.startswith(pattern):
            return f"Move to {directory}"
    
    # Check file extension
    if filename.endswith('.md') and filename != 'README.md':
        return "Move to docs/ (with appropriate subdirectory)"
    
    if filename.endswith(('.csv', '.json', '.parquet')):
        return "Move to data/"
    
    if filename.endswith('.py'):
        # Check patterns
        if any(filename.startswith(p) for p in ['test_', 'check_', 'verify_']):
            if 'notebook' in name_lower or 'diagnose' in name_lower or 'run_' in filename:
                return "Move to projects/adhoc/notebooks/"
            return "Move to tests/ or projects/adhoc/exploration/"
        
        if filename.startswith('example_'):
            return "Move to examples/"
        
        if any(filename.startswith(p) for p in ['run_', 'diagnose_', 'find_', 'delete_', 'ascs_']):
            return "Move to projects/adhoc/notebooks/"
        
        if filename.startswith('investigate_') or filename.startswith('inspect_'):
            return "Move to projects/adhoc/"
    
    if filename.endswith('.sql'):
        if filename.startswith('check_') or filename.startswith('test_'):
            return "Move to projects/adhoc/queries/"
    
    return "Review file organization rules in docs/AI_UTILITY_GUIDE.md"


def check_directory_structure(root: Path) -> List[ValidationError]:
    """Check directory structure for violations"""
    errors = []
    
    for dir_path, rules in DIRECTORY_RULES.items():
        full_path = root / dir_path
        if not full_path.exists():
            continue
        
        for file_path in full_path.rglob('*'):
            # Skip __pycache__ directories and hidden files
            if '__pycache__' in str(file_path) or file_path.name.startswith('.'):
                continue
            
            if file_path.is_file():
                relative_path = file_path.relative_to(root)
                errors.extend(check_file_placement(file_path, relative_path, rules, root))
    
    return errors


def check_file_placement(file_path: Path, relative_path: Path, rules: Dict, root: Path) -> List[ValidationError]:
    """Check if a file is correctly placed"""
    errors = []
    filename = file_path.name
    ext = file_path.suffix
    
    # Allow README.md files in subdirectories
    if filename == 'README.md':
        return errors
    
    # Check extension
    if ext and ext not in rules['allowed_extensions']:
        errors.append(ValidationError(
            file_path=str(relative_path),
            issue=f"File type {ext} not allowed in {relative_path.parent}/",
            suggestion=f"Move to appropriate directory for {ext} files"
        ))
    
    # Check disallowed patterns (but allow exceptions for known utilities)
    for pattern in rules['disallowed_patterns']:
        if pattern in filename:
            # Allow exceptions for known utility files
            if relative_path.parent.name == 'notebooks' and filename in ['create_and_run_databricks_job.py', 'check_job_status.py']:
                continue
            errors.append(ValidationError(
                file_path=str(relative_path),
                issue=f"File matches disallowed pattern '{pattern}' for this directory",
                suggestion=suggest_correct_location(filename, root)
            ))
    
    # Special check for notebooks/ - should only have utilities (not in adhoc subdirectory)
    if 'notebooks/' in str(relative_path) and relative_path.parent.name == 'notebooks' and 'adhoc' not in str(relative_path):
        one_time_patterns = ['run_', 'test_', 'verify_', 'diagnose_', 'find_', 'check_', 
                            'delete_', 'ascs_', 'create_checkout', 'temp']
        # Allow certain utility files even if they match patterns
        allowed_utilities = ['create_and_run_databricks_job.py', 'get_job_output.py', 
                           'get_notebook_content.py', 'get_notebook_from_job.py',
                           'get_notebook_from_url.py', 'check_job_status.py']
        if filename not in allowed_utilities and any(filename.startswith(p) for p in one_time_patterns):
            errors.append(ValidationError(
                file_path=str(relative_path),
                issue="One-time task file in notebooks/ (should only contain reusable utilities)",
                suggestion="Move to projects/adhoc/notebooks/"
            ))
    
    return errors


def count_files(root: Path) -> int:
    """Count total files in repository (excluding __pycache__ and hidden files)"""
    count = 0
    for file_path in root.rglob('*'):
        if file_path.is_file() and '__pycache__' not in str(file_path) and not file_path.name.startswith('.'):
            count += 1
    return count


def validate_repository(root: Path) -> Tuple[List[ValidationError], int]:
    """Validate entire repository structure"""
    all_errors = []
    
    print("🔍 Validating repository structure...")
    print("=" * 80)
    
    # Count total files
    total_files = count_files(root)
    
    # Check root directory
    print("\n📁 Checking root directory...")
    root_errors = check_root_directory(root)
    all_errors.extend(root_errors)
    
    # Check directory structure
    print("\n📁 Checking directory structure...")
    dir_errors = check_directory_structure(root)
    all_errors.extend(dir_errors)
    
    return all_errors, total_files


def print_summary(errors: List[ValidationError], total_files: int):
    """Print validation summary"""
    print("\n" + "=" * 80)
    print("📊 VALIDATION SUMMARY")
    print("=" * 80)
    
    if not errors:
        print("✅ All files are correctly placed!")
        print(f"✅ Validated {total_files} files")
        return
    
    print(f"\n❌ Found {len(errors)} issue(s):\n")
    
    # Group errors by type
    root_errors = [e for e in errors if '/' not in e.file_path]
    other_errors = [e for e in errors if e not in root_errors]
    
    if root_errors:
        print("📁 Root Directory Issues:")
        for error in root_errors:
            print(f"  {error}")
    
    if other_errors:
        print("\n📁 Directory Structure Issues:")
        for error in other_errors:
            print(f"  {error}")
    
    print("\n" + "=" * 80)
    print("💡 TIP: Review docs/AI_UTILITY_GUIDE.md for file organization rules")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description='Validate file placement in repository'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Auto-fix issues where possible (not implemented yet)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed output'
    )
    
    args = parser.parse_args()
    
    root = get_repo_root()
    
    if args.verbose:
        print(f"Repository root: {root}")
    
    errors, total = validate_repository(root)
    
    print_summary(errors, total)
    
    # Exit with error code if issues found
    if errors:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()

