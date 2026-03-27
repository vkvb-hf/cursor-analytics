# Google Drive MCP

MCP server for reading Google Drive files (Docs, Sheets, Slides, etc.) directly from Cursor.

## Features

- **Read any Google Drive file** by URL or file ID
- **Automatic URL parsing** - paste full Google Docs/Sheets URLs
- **List files** in Drive or specific folders
- **Search files** by name
- **Get file metadata** without downloading content

## Tools

| Tool | Description |
|------|-------------|
| `gdrive_read` | Read content of a file by ID or URL |
| `gdrive_list` | List files in Drive or a folder |
| `gdrive_search` | Search files by name |
| `gdrive_get_info` | Get file metadata |

## Setup

### 1. Get OAuth2 Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project or select existing one
3. Enable the **Google Drive API**
4. Go to **Credentials** → **Create Credentials** → **OAuth client ID**
5. Select **Desktop app**
6. Download the JSON file and save as `credentials.json` in this folder

### 2. Copy Credentials

If you already have credentials from `daily_context_updater`:

```bash
cp /Users/visal.kumar/Documents/daily_context_updater/credentials.json .
cp /Users/visal.kumar/Documents/daily_context_updater/token.json .
```

### 3. Add to MCP Config

Add to `~/.cursor/mcp.json` or the project's `.mcp.json`:

```json
{
  "mcpServers": {
    "gdrive": {
      "type": "stdio",
      "command": "/Users/visal.kumar/Documents/databricks/databricks_env/bin/python",
      "args": ["/Users/visal.kumar/Documents/databricks/cursor-analytics/mcp/gdrive/server.py"],
      "cwd": "/Users/visal.kumar/Documents/databricks/cursor-analytics/mcp/gdrive"
    }
  }
}
```

### 4. Restart Cursor

Restart Cursor IDE to load the new MCP server.

## Usage Examples

### Read a Google Doc by URL

```
gdrive_read("https://docs.google.com/document/d/1xTymhg4_zU4XPDy9XJYXCsaeZmKVCkFUJRr5bvzFNf0/edit")
```

### Read by File ID

```
gdrive_read("1xTymhg4_zU4XPDy9XJYXCsaeZmKVCkFUJRr5bvzFNf0")
```

### List Recent Docs

```
gdrive_list(file_type="doc", page_size=10)
```

### Search for Files

```
gdrive_search("Q4 report")
```

### Get File Info

```
gdrive_get_info("https://docs.google.com/spreadsheets/d/abc123/edit")
```

## Supported File Types

| Type | Read As |
|------|---------|
| Google Docs | Plain text |
| Google Sheets | CSV |
| Google Slides | Plain text |
| Text files (.txt, .md, .py, etc.) | Plain text |
| Binary files | Error (not supported) |

## Troubleshooting

### "credentials.json not found"

Copy credentials from an existing setup or create new OAuth2 credentials in Google Cloud Console.

### "Token expired"

Delete `token.json` and restart. You'll be prompted to re-authenticate.

### "Access denied"

Make sure the file is shared with your Google account or you own it.
