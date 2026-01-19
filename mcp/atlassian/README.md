# Atlassian MCP Configuration

Atlassian provides a hosted MCP server for Jira and Confluence operations.

## Setup

### 1. Authenticate with Atlassian

The Atlassian MCP uses OAuth authentication. No API token is required - you'll authenticate via browser.

### 2. Configure in Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"]
    }
  }
}
```

### 3. Restart Cursor

Restart Cursor IDE. On first use, you'll be prompted to authenticate via browser.

## Available Tools (28)

### Jira Tools

| Tool | Description |
|------|-------------|
| `jira_search` | Search issues using JQL |
| `jira_get_issue` | Get details of a specific issue |
| `jira_create_issue` | Create a new issue |
| `jira_update_issue` | Update an existing issue |
| `jira_add_comment` | Add a comment to an issue |
| `jira_transition_issue` | Change issue status |
| `jira_assign_issue` | Assign issue to a user |
| `jira_get_transitions` | Get available transitions |
| `jira_get_projects` | List available projects |
| `jira_get_issue_types` | Get issue types for a project |
| `jira_get_priorities` | Get available priorities |
| `jira_get_statuses` | Get available statuses |
| `jira_link_issues` | Link two issues together |
| `jira_get_worklogs` | Get work logs for an issue |
| `jira_add_worklog` | Add work log to an issue |

### Confluence Tools

| Tool | Description |
|------|-------------|
| `confluence_search` | Search pages and content |
| `confluence_get_page` | Get page content |
| `confluence_create_page` | Create a new page |
| `confluence_update_page` | Update page content |
| `confluence_get_spaces` | List available spaces |
| `confluence_get_space` | Get space details |
| `confluence_get_children` | Get child pages |
| `confluence_get_ancestors` | Get parent pages |
| `confluence_add_comment` | Add comment to a page |
| `confluence_get_comments` | Get page comments |
| `confluence_get_attachments` | Get page attachments |
| `confluence_add_label` | Add label to a page |
| `confluence_get_labels` | Get page labels |

## Example Usage

### Jira

```
# Search for open bugs assigned to me
Use jira_search with jql: "assignee = currentUser() AND type = Bug AND status != Done"

# Create a new task
Use jira_create_issue with:
  project: "PROJ"
  summary: "Implement feature X"
  description: "Details here..."
  issuetype: "Task"

# Add a comment
Use jira_add_comment with:
  issue_key: "PROJ-123"
  body: "Investigation complete. Root cause identified."
```

### Confluence

```
# Search for documentation
Use confluence_search with query: "API documentation"

# Get page content
Use confluence_get_page with page_id: "123456"

# Create a new page
Use confluence_create_page with:
  space_key: "DOCS"
  title: "New Feature Guide"
  body: "<p>Content here...</p>"
```

## JQL Quick Reference

Common JQL queries for Jira:

```sql
-- My open issues
assignee = currentUser() AND status != Done

-- Recent bugs in a project
project = PROJ AND type = Bug AND created >= -7d

-- High priority unassigned
priority in (High, Highest) AND assignee is EMPTY

-- Issues updated this week
updated >= startOfWeek()

-- Sprint backlog
sprint in openSprints() AND status = "To Do"
```

## Troubleshooting

### Authentication Issues
- Clear browser cookies for atlassian.com
- Try re-authenticating by restarting Cursor
- Ensure you have access to the Jira/Confluence instance

### Permission Denied
- Verify you have access to the project/space
- Check if the issue/page is restricted
- Contact your Atlassian admin for permissions

### Rate Limiting
- Atlassian may rate limit requests
- Add delays between bulk operations
- Consider batching requests where possible
