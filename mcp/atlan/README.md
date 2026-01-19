# Atlan MCP Configuration

Atlan provides a hosted MCP server for data catalog operations.

## Setup

### 1. Get Your Atlan API Token

1. Log in to your Atlan workspace
2. Go to **Settings** → **API Tokens**
3. Create a new token with appropriate permissions
4. Copy the token (shown only once)

### 2. Configure in Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "Atlan": {
      "url": "https://your-workspace.atlan.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ATLAN_API_TOKEN"
      }
    }
  }
}
```

Replace:
- `your-workspace` with your Atlan workspace name
- `YOUR_ATLAN_API_TOKEN` with your API token

### 3. Restart Cursor

Restart Cursor IDE to load the MCP server.

## Available Tools (12)

| Tool | Description |
|------|-------------|
| `search_assets` | Search for data assets by name, type, or metadata |
| `get_asset` | Get detailed information about a specific asset |
| `get_lineage` | Get upstream/downstream lineage for an asset |
| `get_columns` | Get column information for a table |
| `get_glossary_terms` | Search glossary terms |
| `get_classifications` | Get classification/tag information |
| `get_owners` | Get asset ownership information |
| `get_readme` | Get README/documentation for an asset |
| `search_by_query` | Advanced search with DSL query |
| `get_recent_assets` | Get recently updated assets |
| `get_popular_assets` | Get most accessed assets |
| `get_data_quality` | Get data quality metrics |

## Example Usage

```
# Search for tables containing "customer"
Use search_assets with query: "customer" and type: "Table"

# Get lineage for a specific table
Use get_lineage with qualified_name: "default/schema/table_name"

# Find glossary terms
Use get_glossary_terms with query: "revenue"
```

## Environment Variables (Alternative)

Instead of hardcoding in mcp.json, you can use environment variables:

```bash
# .env or shell profile
export ATLAN_API_TOKEN=your-token-here
export ATLAN_WORKSPACE_URL=https://your-workspace.atlan.com
```

Then reference in mcp.json:
```json
{
  "mcpServers": {
    "Atlan": {
      "url": "${ATLAN_WORKSPACE_URL}/mcp",
      "headers": {
        "Authorization": "Bearer ${ATLAN_API_TOKEN}"
      }
    }
  }
}
```

## Troubleshooting

### Connection Failed
- Verify your workspace URL is correct
- Check that your API token is valid and not expired
- Ensure your network can reach Atlan servers

### Permission Denied
- Verify your API token has the required permissions
- Check if the asset you're accessing is restricted

### Rate Limiting
- Atlan may rate limit API requests
- Add delays between bulk operations
