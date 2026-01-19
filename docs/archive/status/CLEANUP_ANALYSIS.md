# Directory Cleanup Analysis

## Analysis Results

### 1. `exploration/` Directory
**Status**: ✅ **TEMPORARY - Should be moved to `projects/adhoc/` or deleted**

**Evidence**:
- README explicitly states: "Files in this directory are typically temporary"
- README says: "Can be deleted after use or when no longer needed"
- Contains: test scripts, check scripts, verification scripts
- All files are one-time exploration/debugging scripts

**Files (23 total)**:
- `test_*.py` - Test scripts (temporary)
- `check_*.py` - Validation scripts (temporary)
- `verify_*.py` - Verification scripts (temporary)
- `notebook_*.py` - Test notebooks (temporary)

**Recommendation**: Move to `projects/adhoc/exploration/` or delete if no longer needed

---

### 2. `notebooks/` Directory
**Status**: ⚠️ **MIXED - Needs separation**

**Permanent Utilities** (6 files - KEEP):
- `create_and_run_databricks_job.py` - Reusable utility
- `get_job_output.py` - Reusable utility
- `get_notebook_content.py` - Reusable utility
- `get_notebook_from_job.py` - Reusable utility
- `get_notebook_from_url.py` - Reusable utility
- `check_job_status.py` - Reusable utility

**One-Time Tasks** (25+ files - MOVE TO `projects/adhoc/`):
- `ascs_cancellation_analysis.py` - One-time analysis
- `diagnose_event_date_2025_11_03.py` - One-time diagnostic
- `verify_nov3_data.py` - One-time verification
- `delete_partition_2023_12_31.py` - One-time task
- `find_affected_dates.py` - One-time investigation
- `test_*.py` - Test files (temporary)
- `run_*.py` - One-time run scripts
- All other task-specific files

**Recommendation**: 
- Keep utilities in `notebooks/` (or move to `core/notebook_utils/`)
- Move one-time tasks to `projects/adhoc/notebooks/`

---

### 3. `queries/` Directory
**Status**: ✅ **TEMPORARY - Should be moved to `projects/adhoc/`**

**Evidence**:
- All files are `check_*.sql` - investigation/debugging queries
- No production queries
- All appear to be one-time exploration queries
- Used for debugging specific issues (xbrand, matching attributes, etc.)

**Files (37 total)**:
- `check_xbrand_*.sql` - X-brand investigation queries
- `check_degree_*.sql` - Degree pattern investigation
- `check_matching_attributes_*.sql` - Matching attributes investigation
- `test_*.sql` - Test queries
- `get_customer_*.sql` - One-time customer detail queries

**Recommendation**: Move to `projects/adhoc/queries/` or delete if no longer needed

---

## Proposed Actions

### Option 1: Conservative (Move to adhoc)
1. Move `exploration/` → `projects/adhoc/exploration/`
2. Move one-time files from `notebooks/` → `projects/adhoc/notebooks/`
3. Keep utility files in `notebooks/` (or move to `core/notebook_utils/`)
4. Move `queries/` → `projects/adhoc/queries/`

### Option 2: Aggressive (Delete temporary files)
1. Delete `exploration/` (if truly one-time and no longer needed)
2. Move one-time files from `notebooks/` → `projects/adhoc/notebooks/`
3. Keep utility files in `notebooks/`
4. Delete `queries/` (if truly one-time and no longer needed)

### Option 3: Hybrid (Recommended)
1. Move `exploration/` → `projects/adhoc/exploration/` (archive)
2. Move one-time files from `notebooks/` → `projects/adhoc/notebooks/`
3. Keep utility files in `notebooks/` (or consolidate to `core/notebook_utils/`)
4. Move `queries/` → `projects/adhoc/queries/` (archive)

---

## Final Structure After Cleanup

```
cursor_databricks/
├── notebooks/                   # 📓 ONLY reusable notebook utilities
│   ├── create_and_run_databricks_job.py
│   ├── get_job_output.py
│   ├── get_notebook_content.py
│   ├── get_notebook_from_job.py
│   ├── get_notebook_from_url.py
│   └── check_job_status.py
│
├── projects/
│   └── adhoc/
│       ├── exploration/          # ✨ MOVED - Temporary exploration scripts
│       ├── notebooks/           # ✨ MOVED - One-time notebook tasks
│       └── queries/             # ✨ MOVED - One-time investigation queries
```

---

## Benefits

1. **Clear Separation**: Permanent utilities vs. temporary tasks
2. **Better Organization**: All ad-hoc work in one place
3. **Easier Cleanup**: Can delete `projects/adhoc/` contents when no longer needed
4. **Reduced Clutter**: Root-level directories only contain permanent utilities

