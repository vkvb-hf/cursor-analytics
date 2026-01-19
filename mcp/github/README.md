# GitHub MCP Configuration

GitHub MCP is provided as an NPM package for repository, PR, and issue operations.

## Setup

### 1. Create a GitHub Personal Access Token

1. Go to GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Click **Generate new token (classic)**
3. Select scopes:
   - `repo` (Full control of private repositories)
   - `read:org` (Read org membership)
   - `read:user` (Read user profile)
4. Generate and copy the token (shown only once)

### 2. Configure in Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
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

Replace `ghp_your_token_here` with your actual token.

### 3. Restart Cursor

Restart Cursor IDE to load the MCP server.

## Available Tools (26)

### Repository Tools

| Tool | Description |
|------|-------------|
| `get_repository` | Get repository information |
| `list_repositories` | List repositories for a user/org |
| `search_repositories` | Search repositories |
| `get_file_contents` | Get file contents from a repo |
| `list_directory` | List directory contents |
| `get_readme` | Get repository README |
| `get_branches` | List repository branches |
| `get_commits` | Get commit history |
| `get_commit` | Get specific commit details |

### Pull Request Tools

| Tool | Description |
|------|-------------|
| `list_pull_requests` | List PRs for a repository |
| `get_pull_request` | Get PR details |
| `create_pull_request` | Create a new PR |
| `update_pull_request` | Update PR title/body |
| `merge_pull_request` | Merge a PR |
| `get_pull_request_diff` | Get PR diff |
| `get_pull_request_files` | Get files changed in PR |
| `add_pull_request_comment` | Add comment to PR |
| `request_reviewers` | Request PR reviewers |

### Issue Tools

| Tool | Description |
|------|-------------|
| `list_issues` | List repository issues |
| `get_issue` | Get issue details |
| `create_issue` | Create a new issue |
| `update_issue` | Update issue |
| `add_issue_comment` | Add comment to issue |
| `search_issues` | Search issues across repos |

### Other Tools

| Tool | Description |
|------|-------------|
| `get_user` | Get user profile |
| `search_code` | Search code across GitHub |

## Example Usage

### Repository Operations

```
# Get repository info
Use get_repository with:
  owner: "your-org"
  repo: "your-repo"

# Get file contents
Use get_file_contents with:
  owner: "your-org"
  repo: "your-repo"
  path: "src/main.py"

# Search repositories
Use search_repositories with:
  query: "language:python topic:analytics"
```

### Pull Request Operations

```
# List open PRs
Use list_pull_requests with:
  owner: "your-org"
  repo: "your-repo"
  state: "open"

# Create a PR
Use create_pull_request with:
  owner: "your-org"
  repo: "your-repo"
  title: "Add new feature"
  body: "Description of changes..."
  head: "feature-branch"
  base: "main"

# Get PR diff
Use get_pull_request_diff with:
  owner: "your-org"
  repo: "your-repo"
  pull_number: 123
```

### Issue Operations

```
# Search issues
Use search_issues with:
  query: "repo:your-org/your-repo is:open label:bug"

# Create an issue
Use create_issue with:
  owner: "your-org"
  repo: "your-repo"
  title: "Bug: Something is broken"
  body: "Steps to reproduce..."
  labels: ["bug", "priority:high"]
```

## Search Query Syntax

GitHub search supports powerful query syntax:

```
# Repository search
language:python stars:>100 topic:data-science

# Code search
filename:config.py extension:py org:your-org

# Issue/PR search
repo:owner/repo is:open is:pr review:required
repo:owner/repo is:issue label:bug assignee:username
repo:owner/repo is:pr merged:>2024-01-01
```

## Environment Variables (Alternative)

Instead of hardcoding in mcp.json, set environment variable:

```bash
# .env or shell profile
export GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token_here
```

Then reference in mcp.json:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

## Troubleshooting

### Authentication Failed
- Verify your token is correct and not expired
- Check that the token has required scopes
- Regenerate token if needed

### Rate Limiting
- GitHub API has rate limits (5000 requests/hour for authenticated)
- Check rate limit status: `curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/rate_limit`
- Add delays between bulk operations

### Permission Denied
- Verify you have access to the repository
- Check if the repo is private and token has `repo` scope
- For org repos, ensure you have org membership

### NPX Issues
- Ensure Node.js and npm are installed
- Try clearing npm cache: `npm cache clean --force`
- Install package globally: `npm install -g @modelcontextprotocol/server-github`
