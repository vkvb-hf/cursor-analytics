# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.2.0] - 2026-01-19

### Security
- **BREAKING**: Moved credentials from hardcoded `config.py` to environment variables
- Added `.env` file support using `python-dotenv`
- Updated `.gitignore` to protect `.env` and credential files

### Added
- `.env.example` - Template for environment configuration
- `python-dotenv` dependency for loading environment variables

### Changed
- `config.py` - Now loads all credentials from environment variables with fallback defaults
- `requirements.txt` - Added `python-dotenv>=1.0.0`
- `.gitignore` - Added protection for `.env`, `.env.local`, `.env.*.local`, `*.pem`, `*.key`

### Optimized
- `mcp_server_optimized.py` - Reduced from 16 tools to 7 tools (56% reduction)
  - Removed redundant SQL wrapper tools: `list_tables`, `describe_table`, `sample_table`, `find_duplicates`, `profile_column`, `create_dashboard_table`
  - Removed template generators: `create_exploratory_notebook`, `create_pipeline_notebook`
  - Kept core tools: `execute_sql`, `run_sql_file`, `create_notebook`, `run_notebook`, `get_job_status`, `sync_to_workspace`, `sync_from_workspace`

### Removed
- Hardcoded credentials from `config.py`

## [0.1.0] - Initial Release

### Added
- Initial Databricks MCP server implementation
- Core utilities for SQL execution, notebook management, and workspace sync
- 16 MCP tools for various Databricks operations
