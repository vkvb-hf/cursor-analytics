# Repository Reorganization Plan

**Date**: 2025-01-XX  
**Purpose**: Optimize repository structure for AI accessibility and maintainability  
**Status**: Planning Phase

## Current State Analysis

### Root Directory Issues
The root directory contains **40+ files**, making it difficult for:
- AI models to understand the repository structure
- Developers to find relevant files
- Maintaining clear separation of concerns

### File Categories in Root

#### ✅ **KEEP IN ROOT** (Essential Entry Points)
These are the main entry points and should remain in root:
- `config.py` - Configuration (required by all modules)
- `config.py.example` - Template
- `README.md` - Main documentation
- `databricks_api.py` - Main Python API entry point
- `databricks_cli.py` - Main CLI entry point
- `requirements.txt` - Dependencies
- `requirements-test.txt` - Test dependencies

#### 📁 **MOVE TO ORGANIZED DIRECTORIES**

##### 1. Test Files → `tests/`
**Current location**: Root  
**Target location**: `tests/`

Files to move:
- `test_all_core_functions.py` → `tests/test_all_core_functions.py` (if not duplicate)
- `test_functions_direct.py` → `tests/test_functions_direct.py` (if not duplicate)
- `test_imports_and_functions.py` → `tests/test_imports_and_functions.py` (if not duplicate)
- `test_imports_simple.py` → `tests/test_imports_simple.py` (if not duplicate)

**Rationale**: All test files should be in `tests/` directory for consistency.

##### 2. Documentation Files → `docs/`
**Current location**: Root  
**Target location**: `docs/`

Files to move:
- `AI_DATASET_EXPLORATION_GUIDELINES.md` → `docs/guidelines/AI_DATASET_EXPLORATION_GUIDELINES.md`
- `ARCHITECTURE.md` → `docs/ARCHITECTURE.md`
- `CLEANUP_COMPLETE.md` → `docs/status/CLEANUP_COMPLETE.md`
- `CLEANUP_SUMMARY.md` → `docs/status/CLEANUP_SUMMARY.md`
- `CORE_FUNCTIONS_LIST.md` → `docs/reference/CORE_FUNCTIONS_LIST.md`
- `CSV_UPLOAD_README.md` → `docs/guides/CSV_UPLOAD_README.md`
- `CURSOR_USAGE.md` → `docs/guides/CURSOR_USAGE.md`
- `FUNCTIONS_TEST_SUMMARY.md` → `docs/status/FUNCTIONS_TEST_SUMMARY.md`
- `HOW_TO_CREATE_AND_RUN_NOTEBOOKS.md` → `docs/guides/HOW_TO_CREATE_AND_RUN_NOTEBOOKS.md`
- `HOW_TO_USE.md` → `docs/guides/HOW_TO_USE.md`
- `INSTRUCTIONS.md` → `docs/guides/INSTRUCTIONS.md`
- `MIGRATION_GUIDE.md` → `docs/guides/MIGRATION_GUIDE.md`
- `PROJECT_STRUCTURE.md` → `docs/reference/PROJECT_STRUCTURE.md`
- `QUICK_REFERENCE.md` → `docs/guides/QUICK_REFERENCE.md`
- `QUICK_START.md` → `docs/guides/QUICK_START.md`
- `QUICK_START_NOTEBOOKS.md` → `docs/guides/QUICK_START_NOTEBOOKS.md`
- `REPO_CLEANUP_STATUS.md` → `docs/status/REPO_CLEANUP_STATUS.md`
- `SETUP.md` → `docs/guides/SETUP.md`
- `SOLUTION_NOTE.md` → `docs/notes/SOLUTION_NOTE.md`
- `SUMMARY.md` → `docs/notes/SUMMARY.md`
- `TEST_AFTER_CLEANUP.md` → `docs/status/TEST_AFTER_CLEANUP.md`
- `TEST_RESULTS_REPORT.md` → `docs/status/TEST_RESULTS_REPORT.md`
- `TESTING.md` → `docs/guides/TESTING.md`
- `TESTING_COMPLETE.md` → `docs/status/TESTING_COMPLETE.md`
- `USAGE_EXAMPLE.md` → `docs/examples/USAGE_EXAMPLE.md`

**Rationale**: 
- Centralizes all documentation
- Creates clear subdirectories: `guides/`, `reference/`, `status/`, `notes/`, `examples/`
- Makes it easier for AI to find relevant documentation

##### 3. Example/Template Files → `examples/`
**Current location**: Root  
**Target location**: `examples/`

Files to move:
- `example_notebook_with_output.py` → `examples/example_notebook_with_output.py`
- `example_query.py` → `examples/example_query.py`
- `notebook_template.py` → `examples/notebook_template.py`

**Rationale**: Examples should be in a dedicated directory for easy discovery.

##### 4. Utility Scripts → Appropriate Directories
**Current location**: Root  
**Target locations**: Various

Files to move:
- `export_cluster_to_csv.py` → `projects/adhoc/export_cluster_to_csv.py` (investigation-related)
- `run_ascs_analysis.py` → `projects/adhoc/run_ascs_analysis.py` (project-specific)
- `run_query_now.py` → `scripts/run_query_now.py` (utility script)
- `verify_setup.py` → `scripts/verify_setup.py` (setup utility)

**Rationale**: 
- Investigation scripts go to `projects/adhoc/`
- General utility scripts go to `scripts/`

##### 5. Data Files → `data/`
**Current location**: Root  
**Target location**: `data/`

Files to move:
- `cluster_US_548_US_20251113_101410.csv` → `data/cluster_US_548_US_20251113_101410.csv`

**Rationale**: Data files should be in a dedicated directory, separate from code.

## Proposed New Structure

```
cursor_databricks/
├── config.py                    # ✅ KEEP - Essential config
├── config.py.example            # ✅ KEEP - Template
├── README.md                    # ✅ KEEP - Main entry point
├── databricks_api.py            # ✅ KEEP - Main API entry point
├── databricks_cli.py            # ✅ KEEP - Main CLI entry point
├── requirements.txt             # ✅ KEEP - Dependencies
├── requirements-test.txt        # ✅ KEEP - Test dependencies
│
├── core/                        # 🔧 Core utilities (unchanged)
├── scripts/                     # 🚀 CLI scripts
│   ├── run_query_now.py        # ← MOVED from root
│   └── verify_setup.py         # ← MOVED from root
│
├── examples/                    # 📝 Examples (NEW)
│   ├── example_notebook_with_output.py
│   ├── example_query.py
│   └── notebook_template.py
│
├── docs/                        # 📚 Documentation (REORGANIZED)
│   ├── AI_UTILITY_GUIDE.md     # Existing
│   ├── ARCHITECTURE.md          # ← MOVED from root
│   ├── guides/                  # NEW - User guides
│   │   ├── CSV_UPLOAD_README.md
│   │   ├── CURSOR_USAGE.md
│   │   ├── HOW_TO_CREATE_AND_RUN_NOTEBOOKS.md
│   │   ├── HOW_TO_USE.md
│   │   ├── INSTRUCTIONS.md
│   │   ├── MIGRATION_GUIDE.md
│   │   ├── QUICK_REFERENCE.md
│   │   ├── QUICK_START.md
│   │   ├── QUICK_START_NOTEBOOKS.md
│   │   ├── SETUP.md
│   │   └── TESTING.md
│   ├── reference/               # NEW - Reference docs
│   │   ├── CORE_FUNCTIONS_LIST.md
│   │   └── PROJECT_STRUCTURE.md
│   ├── status/                  # NEW - Status/cleanup docs
│   │   ├── CLEANUP_COMPLETE.md
│   │   ├── CLEANUP_SUMMARY.md
│   │   ├── FUNCTIONS_TEST_SUMMARY.md
│   │   ├── REPO_CLEANUP_STATUS.md
│   │   ├── TEST_AFTER_CLEANUP.md
│   │   ├── TEST_RESULTS_REPORT.md
│   │   └── TESTING_COMPLETE.md
│   ├── notes/                   # NEW - Notes/notes
│   │   ├── SOLUTION_NOTE.md
│   │   └── SUMMARY.md
│   ├── examples/                # NEW - Example docs
│   │   └── USAGE_EXAMPLE.md
│   ├── guidelines/              # NEW - Guidelines
│   │   └── AI_DATASET_EXPLORATION_GUIDELINES.md
│   └── test_archive/            # Existing
│
├── data/                        # 📊 Data files (NEW)
│   └── cluster_US_548_US_20251113_101410.csv
│
├── tests/                       # 🧪 Tests
│   └── [existing test files]
│   └── test_all_core_functions.py  # ← MOVED from root (if not duplicate)
│   └── test_functions_direct.py     # ← MOVED from root (if not duplicate)
│   └── test_imports_and_functions.py # ← MOVED from root (if not duplicate)
│   └── test_imports_simple.py      # ← MOVED from root (if not duplicate)
│
├── projects/                    # 💼 Projects
│   └── adhoc/                   # Investigation scripts
│       ├── export_cluster_to_csv.py  # ← MOVED from root
│       └── run_ascs_analysis.py      # ← MOVED from root
│
├── notebooks/                   # 📓 Notebook utilities (unchanged)
├── queries/                     # 📊 SQL queries (unchanged)
├── exploration/                 # 🔍 Exploration (unchanged)
└── utils/                       # 🔧 Utils (unchanged)
```

## Benefits of This Reorganization

### For AI Models
1. **Clear Structure**: Root directory only contains essential entry points
2. **Logical Grouping**: Files organized by purpose (docs, examples, data, tests)
3. **Easy Discovery**: AI can quickly find relevant files by category
4. **Consistent Patterns**: Similar files grouped together

### For Developers
1. **Reduced Clutter**: Root directory has ~7 files instead of 40+
2. **Clear Intent**: Directory names indicate purpose
3. **Easy Navigation**: Find files by category, not by scanning root
4. **Better Maintainability**: Related files grouped together

### For Repository Health
1. **Scalability**: Easy to add new files without cluttering root
2. **Documentation**: All docs in one place with clear organization
3. **Testing**: All tests in one place
4. **Examples**: Clear examples directory for learning

## Migration Steps

1. **Create new directories**:
   ```bash
   mkdir -p docs/guides docs/reference docs/status docs/notes docs/examples docs/guidelines
   mkdir -p examples data
   ```

2. **Move files** (preserve git history):
   ```bash
   git mv <old_path> <new_path>
   ```

3. **Update imports/references**:
   - Update any hardcoded paths in code
   - Update documentation links
   - Update README.md references

4. **Verify functionality**:
   - Run tests
   - Verify imports work
   - Check documentation links

5. **Update documentation**:
   - Update README.md
   - Update PROJECT_STRUCTURE.md
   - Update any guides that reference file locations

## Files to Update After Migration

### Code Files
- Any files that import from moved modules
- `databricks_api.py` (if it references moved files)
- `databricks_cli.py` (if it references moved files)

### Documentation Files
- `README.md` - Update file structure section
- `PROJECT_STRUCTURE.md` - Update structure diagram
- All guides that reference file paths

## Risk Assessment

### Low Risk
- Moving documentation files (no code dependencies)
- Moving example files (standalone)
- Moving data files (no code dependencies)

### Medium Risk
- Moving test files (need to verify test discovery)
- Moving utility scripts (need to verify imports)

### Mitigation
- Use `git mv` to preserve history
- Run full test suite after migration
- Update import paths systematically
- Keep backup branch during migration

## Next Steps

1. ✅ Create this reorganization plan
2. ⏳ Review and approve plan
3. ⏳ Create new directory structure
4. ⏳ Move files systematically
5. ⏳ Update all references
6. ⏳ Test and verify
7. ⏳ Update documentation
8. ⏳ Commit changes

## Notes

- This reorganization maintains backward compatibility for essential entry points
- All moved files will be accessible via their new paths
- Documentation will be updated to reflect new structure
- Git history will be preserved using `git mv`

