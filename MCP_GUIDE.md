# MCP Server Guide for Product Analytics

This guide explains when and how to use each MCP (Model Context Protocol) server for product analytics tasks.

---

## Quick Reference: Which MCP to Use?

| Task | MCP Server | Why |
|------|------------|-----|
| Run SQL queries | **Databricks** | Direct SQL execution on data warehouse |
| Find table schema/columns | **Databricks** or **Atlan** | Databricks for quick check, Atlan for full lineage |
| Understand data lineage | **Atlan** | Data catalog with lineage tracking |
| Find existing SQL/code | **GitHub** | Search across all repositories |
| Check Jira tickets | **Atlassian** | Access to Jira issues and Confluence |
| Read spreadsheet data | **Google Sheets** | Access to Google Sheets |
| Create/run notebooks | **Databricks** | Notebook creation and job execution |
| Sync files to Databricks | **Databricks** | Upload local files to workspace |

---

## MCP Servers Available

### 1. Databricks MCP (`databricks`)

**Purpose**: Execute SQL, manage notebooks, sync files to/from Databricks workspace.

**Tools**:
| Tool | Use When |
|------|----------|
| `execute_sql` | Running any SQL query - SELECT, DESCRIBE, SHOW, CREATE, etc. |
| `run_sql_file` | Executing SQL from a local `.sql` file |
| `create_notebook` | Creating a Python notebook in Databricks |
| `run_notebook` | Running a notebook as a job and getting output |
| `get_job_status` | Checking status of a running job |
| `sync_to_workspace` | Uploading local files to Databricks workspace |
| `sync_from_workspace` | Downloading workspace files locally |

**Common Patterns**:
```sql
-- List tables in a schema
SHOW TABLES IN schema_name

-- Describe table structure
DESCRIBE TABLE database.schema.table_name

-- Sample data
SELECT * FROM table LIMIT 10

-- Check data freshness
SELECT MAX(partition_date) FROM table
```

---

### 2. Atlan MCP (`Atlan`)

**Purpose**: Data catalog, metadata, lineage, and data discovery.

**Use When**:
- Understanding where data comes from (lineage)
- Finding which tables contain specific columns
- Discovering related tables/datasets
- Understanding data definitions and business glossary
- Finding data owners/stewards

**Tools**:
| Tool | Use When |
|------|----------|
| `search_assets` | Finding tables, columns, dashboards by name or description |
| `get_asset_lineage` | Understanding upstream/downstream dependencies |
| `get_asset_details` | Getting full metadata for a specific asset |
| `get_glossary_terms` | Finding business definitions |

---

### 3. GitHub MCP (`github`)

**Purpose**: Search code, read files, manage PRs across HelloFresh repositories.

**Use When**:
- Finding existing SQL queries or analysis code
- Understanding how a metric is calculated in production
- Searching for implementation details
- Reading pipeline code
- Finding template queries

**Tools**:
| Tool | Use When |
|------|----------|
| `search_code` | Finding code containing specific text/patterns |
| `search_repositories` | Finding repos by name or topic |
| `get_file_contents` | Reading specific files from repos |
| `list_commits` | Checking recent changes |
| `create_or_update_file` | Making changes to files |

**Key Repositories**:
- `hellofresh/pa-scripts` - Product analytics scripts and templates
- `hellofresh/ddi-pays-pipelines` - Payment data pipelines
- `hellofresh/tardis-community` - Data transformation logic
- `hellofresh/matviews-community` - Materialized view definitions

---

### 4. Atlassian MCP (`atlassian`)

**Purpose**: Access Jira tickets and Confluence documentation.

**Use When**:
- Understanding ticket requirements
- Finding analysis documentation
- Checking experiment specifications
- Reading runbooks or guides

**Tools**:
| Tool | Use When |
|------|----------|
| `get_issue` | Reading Jira ticket details |
| `search_issues` | Finding related tickets |
| `get_page` | Reading Confluence pages |
| `search_pages` | Finding documentation |

---

### 5. Google Sheets MCP (`google-sheets`)

**Purpose**: Read data from Google Sheets.

**Use When**:
- Reading input data from spreadsheets
- Accessing shared team data
- Reading experiment configurations from sheets

**Tools**:
| Tool | Use When |
|------|----------|
| `read_sheet` | Reading data from a sheet |
| `get_sheet_info` | Getting sheet metadata |
| `read_multiple_ranges` | Reading multiple ranges at once |
| `read_comments` | Reading cell comments |

---

## Decision Tree: Choosing the Right MCP

```
START: What do you need to do?
│
├── Execute SQL / Query Data
│   └── Use: Databricks MCP → execute_sql
│
├── Find Table/Column Information
│   ├── Quick schema check → Databricks MCP → DESCRIBE TABLE
│   └── Full lineage/metadata → Atlan MCP → search_assets, get_asset_lineage
│
├── Find Existing Code/Queries
│   └── Use: GitHub MCP → search_code
│       Key repos: pa-scripts, ddi-pays-pipelines, tardis-community
│
├── Understand Ticket/Requirements
│   └── Use: Atlassian MCP → get_issue
│
├── Read Spreadsheet Data
│   └── Use: Google Sheets MCP → read_sheet
│
├── Create/Run Databricks Notebook
│   └── Use: Databricks MCP → create_notebook, run_notebook
│
└── Sync Files to/from Databricks
    └── Use: Databricks MCP → sync_to_workspace, sync_from_workspace
```

---

## Workflow Examples

### Example 1: Analyze a Metric

1. **Understand the ask** → Read Jira ticket (Atlassian MCP)
2. **Find existing implementation** → Search code (GitHub MCP)
3. **Understand data lineage** → Check catalog (Atlan MCP)
4. **Verify table exists** → DESCRIBE TABLE (Databricks MCP)
5. **Run analysis** → Execute SQL (Databricks MCP)

### Example 2: Debug Data Issue

1. **Check data freshness** → `SELECT MAX(partition_date)` (Databricks MCP)
2. **Understand lineage** → Get upstream dependencies (Atlan MCP)
3. **Find pipeline code** → Search repo (GitHub MCP)
4. **Check pipeline status** → Look at job runs (Databricks MCP)

### Example 3: Create New Analysis

1. **Find template** → Search pa-scripts (GitHub MCP)
2. **Verify tables** → DESCRIBE TABLE (Databricks MCP)
3. **Test query** → Execute with LIMIT (Databricks MCP)
4. **Document** → Create notebook (Databricks MCP)

---

## Best Practices

### 1. Always Verify Before Executing
```
❌ Wrong: Assume table exists, write query, fail
✅ Right: DESCRIBE TABLE first, then write query
```

### 2. Search Before Creating
```
❌ Wrong: Write analysis from scratch
✅ Right: Search GitHub for existing templates first
```

### 3. Understand Lineage for Complex Data
```
❌ Wrong: Use table without understanding source
✅ Right: Check Atlan for lineage, understand transformations
```

### 4. Test Queries Before Providing
```
❌ Wrong: Generate SQL, give to user untested
✅ Right: Execute with LIMIT 10, verify works, then provide
```

---

## MCP Server Status Check

If an MCP server isn't responding:
1. Check if Cursor needs restart
2. Verify credentials in `~/.cursor/mcp.json`
3. Check network connectivity
4. Look at MCP server logs

---

## Configuration Location

MCP servers are configured in: `~/.cursor/mcp.json`

Current servers:
- `databricks` - Databricks SQL and workspace operations
- `Atlan` - Data catalog and lineage
- `github` - Code search and repository access
- `atlassian` - Jira and Confluence
- `google-sheets` - Google Sheets access
