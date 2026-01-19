# Atlassian MCP Server

Remote MCP server hosted by Atlassian for Jira and Confluence operations.

## Type

**External/Remote** - No local code required. Hosted at `https://mcp.atlassian.com/v1/sse`

## Tools (28 total)

### Jira Tools
| Tool | Description |
|------|-------------|
| `createJiraIssue` | Create a new Jira issue |
| `editJiraIssue` | Edit an existing issue |
| `getJiraIssue` | Get issue details |
| `searchJiraIssuesUsingJql` | Search issues with JQL |
| `addCommentToJiraIssue` | Add a comment |
| `addWorklogToJiraIssue` | Log work time |
| `transitionJiraIssue` | Change issue status |
| `getTransitionsForJiraIssue` | Get available transitions |
| `getVisibleJiraProjects` | List accessible projects |
| `getJiraProjectIssueTypesMetadata` | Get project issue types |
| `getJiraIssueTypeMetaWithFields` | Get issue type fields |
| `getJiraIssueRemoteIssueLinks` | Get linked issues |
| `lookupJiraAccountId` | Find user account ID |

### Confluence Tools
| Tool | Description |
|------|-------------|
| `createConfluencePage` | Create a new page |
| `updateConfluencePage` | Update existing page |
| `getConfluencePage` | Get page content |
| `getConfluencePageDescendants` | Get child pages |
| `getPagesInConfluenceSpace` | List pages in space |
| `getConfluenceSpaces` | List accessible spaces |
| `createConfluenceFooterComment` | Add footer comment |
| `createConfluenceInlineComment` | Add inline comment |
| `getConfluencePageFooterComments` | Get footer comments |
| `getConfluencePageInlineComments` | Get inline comments |
| `searchConfluenceUsingCql` | Search with CQL |

### General Tools
| Tool | Description |
|------|-------------|
| `atlassianUserInfo` | Get current user info |
| `getAccessibleAtlassianResources` | List accessible resources |
| `fetch` | Generic HTTP fetch |
| `search` | General search |

## Configuration

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"],
      "env": {}
    }
  }
}
```

## Authentication

Authentication is handled through OAuth when you first use the MCP. You'll be prompted to log in to your Atlassian account.

## Usage Examples

### Create Jira Issue
```
Use createJiraIssue with:
- project: PROJ
- summary: Bug in login page
- issueType: Bug
- description: Users cannot log in with SSO
```

### Search Jira
```
Use searchJiraIssuesUsingJql with:
- jql: project = PROJ AND status = "In Progress" ORDER BY created DESC
```

### Create Confluence Page
```
Use createConfluencePage with:
- spaceKey: TEAM
- title: Meeting Notes 2024-01-15
- content: <p>Discussion points...</p>
```
