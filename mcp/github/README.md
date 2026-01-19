# GitHub MCP Server

NPM-based MCP server for GitHub operations.

## Type

**NPM Package** - Uses `@modelcontextprotocol/server-github`

## Tools (26 total)

### Repository Tools
| Tool | Description |
|------|-------------|
| `create_repository` | Create a new repository |
| `fork_repository` | Fork a repository |
| `search_repositories` | Search for repositories |
| `get_file_contents` | Get file contents |
| `create_or_update_file` | Create or update a file |
| `push_files` | Push multiple files |
| `create_branch` | Create a new branch |
| `list_commits` | List commits |
| `search_code` | Search code |

### Issue Tools
| Tool | Description |
|------|-------------|
| `create_issue` | Create a new issue |
| `get_issue` | Get issue details |
| `update_issue` | Update an issue |
| `list_issues` | List issues |
| `search_issues` | Search issues |
| `add_issue_comment` | Add comment to issue |

### Pull Request Tools
| Tool | Description |
|------|-------------|
| `create_pull_request` | Create a PR |
| `get_pull_request` | Get PR details |
| `list_pull_requests` | List PRs |
| `get_pull_request_files` | Get files changed in PR |
| `get_pull_request_comments` | Get PR comments |
| `get_pull_request_reviews` | Get PR reviews |
| `get_pull_request_status` | Get PR status checks |
| `create_pull_request_review` | Create a review |
| `merge_pull_request` | Merge a PR |
| `update_pull_request_branch` | Update PR branch |

### User Tools
| Tool | Description |
|------|-------------|
| `search_users` | Search for users |

## Configuration

### 1. Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate a new token with required scopes:
   - `repo` (for private repos)
   - `public_repo` (for public repos only)
   - `read:org` (for organization access)

### 2. Cursor Configuration

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

## Dependencies

Requires Node.js and npm installed.

## Usage Examples

### Create Issue
```
Use create_issue with:
- owner: your-org
- repo: your-repo
- title: Bug: Login fails on Safari
- body: Steps to reproduce...
- labels: ["bug", "priority-high"]
```

### Create Pull Request
```
Use create_pull_request with:
- owner: your-org
- repo: your-repo
- title: feat: Add user authentication
- head: feature/auth
- base: main
- body: This PR adds...
```

### Search Code
```
Use search_code with:
- q: "def authenticate" language:python org:your-org
```

### Get File Contents
```
Use get_file_contents with:
- owner: your-org
- repo: your-repo
- path: src/main.py
```
