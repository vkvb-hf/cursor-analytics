# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.3.1] - 2026-01-19

### Added
- `MCP_GUIDE.md` - Comprehensive guide for all MCP servers
  - Quick reference table: task-to-MCP mapping
  - Decision tree for choosing the right MCP server
  - Workflow examples for common analysis tasks
  - Best practices for MCP usage

### Documentation
- Updated `.cursorrules` with MCP selection logic (Section 0)
- Added MCP tool reference table to Section 8

## [0.3.0] - 2026-01-19

### Added
- `mcp_server_standalone.py` - Completely self-contained MCP server with NO external dependencies
  - All functionality inlined (no imports from `core/` modules)
  - Config loaded directly from environment variables
  - DatabricksClient class with all REST API operations
  - ConnectionPool for efficient SQL execution
  - WorkspaceSync operations for file synchronization

### Changed
- MCP server no longer requires `PYTHONPATH` environment variable
- Removed `sys.path.insert` hack - proper Python module structure
- Simplified mcp.json configuration (just command, args, cwd)

### Architecture
- Phase 1 complete: MCP server is now fully isolated and portable
- Can be moved to any location without breaking imports
- Ready for Phase 2: Clean repo structure

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
