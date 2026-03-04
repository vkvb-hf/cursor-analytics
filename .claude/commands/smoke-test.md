Run smoke tests to validate repo health. Arguments: $ARGUMENTS

## Quick Mode (default)
Run these in sequence:

1. **Smoke test**: `python scripts/smoke_test.py --quick`
2. **File placement validation**: `python scripts/validate_file_placement.py`

Report pass/fail for each step with any error output.

## Full Mode (if arguments contain "full")
Run everything from quick mode, plus:

3. **Full test suite**: `pytest tests/ -v`

Report pass/fail for each step. If any test fails, show the failure details and suggest fixes.

## Summary
Present results as:

| Check | Status | Details |
|-------|--------|---------|
| Smoke test | PASS/FAIL | ... |
| File placement | PASS/FAIL | ... |
| Test suite (full only) | PASS/FAIL | N passed, N failed |
