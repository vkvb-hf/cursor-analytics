# File Persistence Issue - Root Cause Analysis

## Problem

When running all three comparison types (`week_prev`, `week_yoy`, `quarter_prev`), only the last file (`quarter_prev`) persists in Databricks workspace, even though all jobs complete successfully.

## Root Cause

### Issue Identified

1. **All jobs write to the same folder**: `long-term-steering-2025-W45`
2. **Each job writes a different filename** (should coexist):
   - `detailed_summary_week_vs_prev_week.txt`
   - `detailed_summary_week_vs_prev_yr_week.txt`
   - `detailed_summary_quarter_vs_prev_quarter.txt`
3. **Jobs run sequentially** with 5-second delays
4. **Only the last file persists** in workspace

### Possible Causes

1. **Workspace Sync Timing**: Files are written but workspace doesn't sync until job completes. If jobs run too close together, earlier files might not sync properly.

2. **File System Caching**: Databricks workspace might cache file writes, and only the last write persists if there's a sync issue.

3. **Job Isolation**: Each job runs in an isolated environment. Files written in one job might not be visible to subsequent jobs until workspace syncs.

4. **Race Condition**: When multiple jobs write to the same folder, there might be a race condition where files are overwritten or deleted.

5. **Notebook Overwriting**: Each job overwrites the same notebook file, which might cause workspace sync issues.

## Solution Implemented

### Changes Made

1. **Added explicit file flush and sync**:
   ```python
   f.flush()
   os.fsync(f.fileno())  # Force write to disk
   ```

2. **Added file verification**:
   ```python
   if os.path.exists(detailed_summary_path):
       file_size = os.path.getsize(detailed_summary_path)
       print(f"  ✅ File written successfully: {detailed_summary_path} ({file_size} bytes)")
   ```

3. **Added verification after file generation**:
   - Checks file exists after writing
   - Reports file size
   - Warns if file not found

### Why This Should Help

- **Explicit flush**: Ensures data is written to buffer
- **fsync**: Forces operating system to write buffer to disk
- **Verification**: Confirms file exists before job completes
- **Logging**: Helps identify if files are actually being written

## Alternative Solutions (If Issue Persists)

### Option 1: Write to Unique Folders Per Comparison Type
```python
OUTPUT_BASE_FOLDER = f'{WORKSPACE_FOLDER}/long-term-steering-{COMPARISON_TYPE}-{latest_week_str}'
```

### Option 2: Add Delay Between Jobs
Increase the delay in `run_long_term_steering.py` from 5 seconds to 30 seconds to allow workspace sync.

### Option 3: Write to DBFS First, Then Copy to Workspace
Write files to DBFS (`/tmp/`), then explicitly copy to workspace using Databricks API.

### Option 4: Use Databricks Workspace API to Write Files
Instead of using `open()`, use Databricks Workspace API to write files directly, ensuring they persist.

## Testing

After implementing the fix:

1. Run all three comparison types
2. Check if all files persist in workspace
3. Verify file sizes match expected values
4. Check job logs for verification messages

## Expected Behavior

After fix:
- All three files should persist in workspace
- File verification messages should appear in job logs
- Files should be accessible via workspace API immediately after job completion

## Current Status

- ✅ Code updated with file flush and verification
- ⏳ Needs testing to verify fix works
- 📝 Monitoring job logs for file verification messages

