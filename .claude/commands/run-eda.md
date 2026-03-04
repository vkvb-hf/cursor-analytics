Run a full guided EDA for: $ARGUMENTS

Follow this checklist step by step. Do NOT skip steps or make assumptions.

## 1. Understand the Data Source
- Identify the table from the user's request
- Run `DESCRIBE EXTENDED <table>` via `execute_sql`
- Run `SELECT * FROM <table> LIMIT 10` to see actual data
- Note data types, nested structs, and null patterns

## 2. Validate Field Assumptions
- Check data types: is it string `'true'` or boolean `true`?
- Check for nulls in key fields: `SELECT COUNT(*), COUNT(field) FROM table`
- Run `GROUP BY` to see distinct values for categorical fields
- Test nested struct paths: `SELECT nested.field FROM table LIMIT 1`

## 3. Clarify Business Definitions
Ask the user:
- "What defines a 'conversion' in this context?"
- "What defines 'blocked' / 'failed' / other key states?"
- "Should I use first occurrence or last occurrence?"
- "Are there any known data quirks I should watch for?"

**Wait for user response before proceeding.**

## 4. Confirm Filters
Ask the user to confirm:
- **Country** (MANDATORY — never run without this)
- **Date range** (default: last 30 days)
- **Segment filters** (customer type, payment method, etc.)
- **Exclusions** (test accounts, internal users)

**Wait for user response before proceeding.**

## 5. Prototype with Small Queries
- Test that field paths work: `SELECT field FROM table WHERE country = 'XX' LIMIT 1`
- Test filters: `SELECT COUNT(*) FROM table WHERE <all_filters>`
- Test aggregation logic on a small date range before full run

## 6. Execute Analysis
- Run the full query with confirmed filters
- Print record counts at each step
- For complex analysis requiring plots, use `run_notebook` MCP tool
- Present results with clear labels and context

## 7. Summarize
- Key findings with numbers
- Any data quality issues discovered
- Suggested follow-up analyses
