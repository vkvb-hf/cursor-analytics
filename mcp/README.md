# MCP Servers

This folder contains all Model Context Protocol (MCP) servers used with Cursor IDE.

## Overview

| MCP Server | Type | Tools | Status |
|------------|------|-------|--------|
| [Databricks](databricks/) | Local Python | 7 tools | Active |
| [Google Sheets](google_sheets/) | Local Python | 4 tools | Active |
| [Tableau](tableau/) | Pre-built Node.js | 12 tools | Active |
| [Atlassian](atlassian/) | Remote SaaS | 28 tools | Active |
| [Atlan](atlan/) | Remote SaaS | 12 tools | Active |
| [GitHub](github/) | NPM Package | 26 tools | Active |

## Quick Setup

### Local MCPs (Databricks, Google Sheets)

1. Copy the example config:
   ```bash
   cp mcp/databricks/env.example mcp/databricks/.env
   cp mcp/google_sheets/env.example mcp/google_sheets/.env
   ```

2. Edit `.env` files with your credentials

3. Add to `~/.cursor/mcp.json`:
   ```json
   {
     "mcpServers": {
       "databricks": {
         "command": "python",
         "args": ["/path/to/cursor-analytics/mcp/databricks/server.py"],
         "cwd": "/path/to/cursor-analytics/mcp/databricks"
       },
       "google-sheets": {
         "command": "python",
         "args": ["/path/to/cursor-analytics/mcp/google_sheets/server.py"],
         "cwd": "/path/to/cursor-analytics/mcp/google_sheets"
       }
     }
   }
   ```

### Pre-built MCPs (Tableau)

No build required - just configure:

```json
{
  "mcpServers": {
    "tableau": {
      "command": "node",
      "args": ["/path/to/cursor-analytics/mcp/tableau/index.js"],
      "env": {
        "SERVER": "https://tableau.hellofresh.io",
        "SITE_NAME": "",
        "PAT_NAME": "Cursor MCP",
        "PAT_VALUE": "your-pat-token-here"
      }
    }
  }
}
```

See [Tableau README](tableau/README.md) for PAT setup instructions.

### External MCPs (Atlassian, Atlan, GitHub)

See individual README files for setup:
- [Atlassian Setup](atlassian/README.md)
- [Atlan Setup](atlan/README.md)
- [GitHub Setup](github/README.md)

## Full Configuration Example

Complete `~/.cursor/mcp.json` with all MCPs:

```json
{
  "mcpServers": {
    "databricks": {
      "command": "python",
      "args": ["/path/to/cursor-analytics/mcp/databricks/server.py"],
      "cwd": "/path/to/cursor-analytics/mcp/databricks"
    },
    "google-sheets": {
      "command": "python",
      "args": ["/path/to/cursor-analytics/mcp/google_sheets/server.py"],
      "cwd": "/path/to/cursor-analytics/mcp/google_sheets",
      "env": {
        "GOOGLE_SERVICE_ACCOUNT_FILE": "/path/to/service-account.json"
      }
    },
    "tableau": {
      "command": "node",
      "args": ["/path/to/cursor-analytics/mcp/tableau/index.js"],
      "env": {
        "SERVER": "https://tableau.hellofresh.io",
        "SITE_NAME": "",
        "PAT_NAME": "Cursor MCP",
        "PAT_VALUE": "your-pat-token-here"
      }
    },
    "atlassian": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"]
    },
    "Atlan": {
      "url": "https://your-workspace.atlan.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ATLAN_API_TOKEN"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

## Local vs External MCPs

### Local MCPs (code in this repo)
- **Databricks**: Custom server for SQL, notebooks, workspace sync
- **Google Sheets**: Custom server for reading spreadsheets

These use the `FastMCP` pattern and import from `core/` modules.

### External MCPs (hosted services or npm packages)
- **Atlassian**: Hosted by Atlassian at `mcp.atlassian.com`
- **Atlan**: Hosted by Atlan at `your-workspace.atlan.com/mcp`
- **GitHub**: NPM package `@modelcontextprotocol/server-github`

## Adding a New MCP

### Local MCP (Python)

1. Create folder: `mcp/your_mcp/`
2. Create `server.py` using FastMCP pattern:
   ```python
   from mcp.server.fastmcp import FastMCP
   
   mcp = FastMCP("Your MCP Name")
   
   @mcp.tool()
   def your_tool(param: str) -> dict:
       """Tool description."""
       return {"success": True, "data": ...}
   
   if __name__ == "__main__":
       mcp.run()
   ```
3. Create `env.example` with required configuration
4. Create `README.md` with setup instructions
5. Add to `~/.cursor/mcp.json`
6. Restart Cursor

### External MCP (Documentation only)

1. Create folder: `mcp/your_mcp/`
2. Create `README.md` with:
   - Setup instructions
   - Available tools
   - Example usage
   - Troubleshooting

## Testing MCPs

### Verify Local MCP Syntax
```bash
python -m py_compile mcp/databricks/server.py
python -m py_compile mcp/google_sheets/server.py
```

### Test MCP Server Directly
```bash
cd mcp/databricks
python server.py
# Server will start and wait for MCP protocol messages
```

### Run Full Test Suite
```bash
pytest tests/test_mcp_databricks.py -v
pytest tests/test_mcp_google_sheets.py -v
```

## Troubleshooting

### MCP Not Loading in Cursor
1. Check `~/.cursor/mcp.json` syntax (valid JSON)
2. Verify Python path is correct
3. Check MCP server logs in Cursor Developer Tools
4. Restart Cursor IDE

### Connection Issues
1. Verify environment variables are set
2. Check network connectivity
3. Verify credentials are valid

### Import Errors
1. Ensure virtual environment is activated
2. Run `pip install -e .` from repo root
3. Check that `mcp` package is installed: `pip install mcp`
