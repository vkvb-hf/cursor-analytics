# Debug Notebooks

Temporary debug notebooks for investigating steering report issues.

## test_bucket_bug.py

Tests the suspected bug in `bucket_by_percentage` function where:
- `'abs_rel_change' in row` checks VALUES instead of INDEX
- This causes the condition to always be False

Results are saved to `hive_metastore.visal_debug.bucket_bug_test`
