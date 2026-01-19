# Google Sheets MCP Server

A Model Context Protocol server for reading Google Sheets.

## Tools

| Tool | Description |
|------|-------------|
| `read_sheet` | Read data from a Google Sheet |
| `get_sheet_info` | Get spreadsheet metadata (sheet names, dimensions) |
| `read_multiple_ranges` | Read multiple ranges at once |
| `read_comments` | Read comments/notes from cells |

## Configuration

### 1. Create Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable the Google Sheets API
4. Create a Service Account
5. Download the JSON key file
6. Share your spreadsheets with the service account email

### 2. Setup Credentials

Place your `service-account.json` in this directory (it's gitignored).

### 3. Cursor Configuration

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "google-sheets": {
      "command": "/path/to/python",
      "args": ["/path/to/cursor-analytics/mcp/google_sheets/server.py"],
      "cwd": "/path/to/cursor-analytics/mcp/google_sheets",
      "env": {
        "GOOGLE_SERVICE_ACCOUNT_FILE": "/path/to/service-account.json"
      }
    }
  }
}
```

## Dependencies

```bash
pip install mcp google-auth google-api-python-client
```

## Usage Examples

### Read a Sheet
```
Use read_sheet with:
- spreadsheet_id: 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
- range_name: Sheet1!A1:D10
```

### Get Sheet Info
```
Use get_sheet_info with:
- spreadsheet_id: 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
```

## Finding Spreadsheet ID

The spreadsheet ID is in the URL:
```
https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit
```
