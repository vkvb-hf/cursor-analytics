# MCP Servers

This folder contains all Model Context Protocol (MCP) servers used with Cursor IDE.

## Overview

| MCP Server | Type | Tools | Status |
|------------|------|-------|--------|
| [Databricks](databricks/) | Local Python | 7 tools | Active |
| [Google Sheets](google_sheets/) | Local Python | 4 tools | Active |
| [Atlassian](atlassian/) | Remote SaaS | 28 tools | Active |
| [Atlan](atlan/) | Remote SaaS | 12 tools | Active |
| [GitHub](github/) | NPM Package | 26 tools | Active |

## Configuration

All MCP servers are configured in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "databricks": {
      "command": "/path/to/python",
      "args": ["/path/to/cursor-analytics/mcp/databricks/server.py"],
      "cwd": "/path/to/cursor-analytics/mcp/databricks"
    },
    "google-sheets": {
      "command": "/path/to/python",
      "args": ["/path/to/cursor-analytics/mcp/google_sheets/server.py"],
      "cwd": "/path/to/cursor-analytics/mcp/google_sheets",
      "env": {
        "GOOGLE_SERVICE_ACCOUNT_FILE": "/path/to/service-account.json"
      }
    },
    "atlassian": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"]
    },
    "Atlan": {
      "url": "https://hellofresh.atlan.com/mcp"
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token-here"
      }
    }
  }
}
```

## Local vs External MCPs

### Local MCPs (code in this repo)
- **Databricks**: Custom server for SQL, notebooks, workspace sync
- **Google Sheets**: Custom server for reading spreadsheets

### External MCPs (hosted services or npm packages)
- **Atlassian**: Hosted by Atlassian at `mcp.atlassian.com`
- **Atlan**: Hosted by Atlan at `hellofresh.atlan.com/mcp`
- **GitHub**: NPM package `@modelcontextprotocol/server-github`

## Adding a New MCP

1. Create a folder: `mcp/your_mcp/`
2. Add `server.py` (for local) or `README.md` (for external)
3. Update `~/.cursor/mcp.json`
4. Restart Cursor to load the new MCP
