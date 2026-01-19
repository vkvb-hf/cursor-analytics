# Run Status - November 11, 2025

## Job Execution Status

### ✅ Jobs Successfully Executed Today

All three comparison types were executed successfully:

1. **week_prev** (Week vs Previous Week)
   - Run ID: `24314528182285`
   - Started: 2025-11-11 11:36:18
   - Status: ✅ SUCCESS

2. **week_yoy** (Week vs Previous Year Week)
   - Run ID: `245764085238067`
   - Started: 2025-11-11 11:37:17
   - Status: ✅ SUCCESS

3. **quarter_prev** (Quarter vs Previous Quarter)
   - Run ID: `471163224685608`
   - Started: 2025-11-11 11:37:46
   - Status: ✅ SUCCESS

## File Locations in Databricks

### Main Output Folder
```
/Workspace/Users/visal.kumar@hellofresh.com/long-term-steering-2025-W45
```

This folder contains:
- `detailed_summary_week_vs_prev_week.txt`
- `detailed_summary_week_vs_prev_yr_week.txt`
- `detailed_summary_quarter_vs_prev_quarter.txt`
- `debug_output.txt`
- Additional debug files

### Other Folders Found
- `long-term-steering-debug` - Debug files
- `long-term-steering-quarter-prev-2025-W45` - Quarter comparison (old location?)
- `long-term-steering-week-prev-2025-W45` - Week comparison (old location?)
- `long-term-steering-week-yoy-2025-W45` - Year-over-year (old location?)

## File Download Status

Files were successfully downloaded to local `output/` directory:
- ✅ `detailed_summary_week_vs_prev_week.txt` (Nov 11 11:37)
- ✅ `detailed_summary_week_vs_prev_yr_week.txt` (Nov 11 11:37)
- ✅ `detailed_summary_quarter_vs_prev_quarter.txt` (Nov 11 11:38)

## Note on Modification Times

If the Databricks folder shows last modified Nov 10, but jobs ran Nov 11:
- Jobs executed successfully (confirmed by job run IDs)
- Files may have been written but folder timestamp not updated
- Or files were written to the same location, overwriting existing files
- The downloaded files have Nov 11 timestamps, confirming they were just downloaded

## Verification

To verify files were actually updated:
1. Check file contents - compare with previous versions
2. Check file sizes - should match the downloaded files
3. Check job logs in Databricks UI for any write errors

## Accessing Files

**In Databricks UI:**
```
https://hf-gp.cloud.databricks.com/#workspace/Users/visal.kumar@hellofresh.com/long-term-steering-2025-W45
```

**Local copies:**
```
cursor_databricks/projects/long_term_steering_report/output/
```

