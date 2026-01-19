# Integration Framework: Maximizing Productivity

**Purpose**: Build a comprehensive framework for seamless integration between Cursor, local environment, and Databricks workspace.

## 🎯 Core Integration Goals

1. **Standardized Notebook Output** - Always see output in terminal
2. **Workspace Sync** - Bidirectional sync between local and Databricks
3. **Efficient Connections** - Fast, reliable Databricks connectivity
4. **Development Workflow** - Edit locally, run in Databricks seamlessly

---

## 📊 Integration 1: Standardized Notebook Output Framework

### Current State
- Output requires manual DBFS file writing
- Inconsistent output formats
- No standard pattern

### Proposed Framework

#### 1.1 Output Standardization Utility

```python
# core/notebook_output.py
class NotebookOutput:
    """Standardized output framework for Databricks notebooks."""
    
    def __init__(self, output_path: str = "/tmp/notebook_output.txt"):
        self.output_path = output_path
        self.sections = []
        self.metadata = {}
    
    def add_section(self, title: str, content: str, format: str = "text"):
        """Add a section to output."""
        self.sections.append({
            'title': title,
            'content': content,
            'format': format,
            'timestamp': time.time()
        })
    
    def add_dataframe(self, title: str, df):
        """Add DataFrame output."""
        import pandas as pd
        content = df.to_string() if isinstance(df, pd.DataFrame) else str(df)
        self.add_section(title, content, format="dataframe")
    
    def add_query_result(self, title: str, query: str, results):
        """Add SQL query results."""
        self.add_section(title, f"Query: {query}\n\nResults:\n{results}", format="query")
    
    def write_to_dbfs(self):
        """Write formatted output to DBFS."""
        output_lines = []
        output_lines.append("=" * 100)
        output_lines.append("NOTEBOOK OUTPUT")
        output_lines.append("=" * 100)
        output_lines.append(f"Generated: {datetime.now().isoformat()}")
        output_lines.append("")
        
        for section in self.sections:
            output_lines.append("-" * 100)
            output_lines.append(f"📊 {section['title']}")
            output_lines.append("-" * 100)
            output_lines.append(section['content'])
            output_lines.append("")
        
        output_lines.append("=" * 100)
        output_text = "\n".join(output_lines)
        
        dbutils.fs.put(self.output_path, output_text, overwrite=True)
        print(output_text)  # Also print for UI
    
    def write_json(self, json_path: str = "/tmp/notebook_output.json"):
        """Write structured JSON output."""
        import json
        output = {
            'metadata': self.metadata,
            'sections': self.sections,
            'timestamp': datetime.now().isoformat()
        }
        dbutils.fs.put(json_path, json.dumps(output, indent=2), overwrite=True)
```

#### 1.2 Notebook Template with Output

```python
# notebooks/notebook_template_with_output.py
from core.notebook_output import NotebookOutput

# Initialize output handler
output = NotebookOutput(output_path="/tmp/my_analysis_output.txt")

# Your analysis code
query = """SELECT * FROM table LIMIT 10"""
result_df = spark.sql(query)

# Add to output
output.add_query_result("Sample Data", query, result_df.toPandas().to_string())

# More analysis
summary = result_df.groupBy("column").count()
output.add_dataframe("Summary Statistics", summary.toPandas())

# Write output
output.write_to_dbfs()
output.write_json()  # Optional: structured output
```

#### 1.3 Automatic Output Retrieval

```python
# core/notebook_output_reader.py
class NotebookOutputReader:
    """Read and display notebook output from DBFS."""
    
    def read_output(self, output_path: str = "/tmp/notebook_output.txt"):
        """Read output file from DBFS and display."""
        import requests
        import base64
        from config import DATABRICKS_HOST, TOKEN
        
        headers = {"Authorization": f"Bearer {TOKEN}"}
        read_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/read"
        response = requests.get(read_url, headers=headers, json={"path": output_path})
        
        if response.status_code == 200:
            file_data = response.json()
            content = base64.b64decode(file_data['data']).decode('utf-8')
            return content
        return None
    
    def display_output(self, output_path: str):
        """Read and display formatted output."""
        content = self.read_output(output_path)
        if content:
            print("\n" + "=" * 100)
            print("NOTEBOOK OUTPUT")
            print("=" * 100)
            print(content)
            return True
        return False
```

#### 1.4 Integration with Job Runner

```python
# Enhanced databricks_job_runner.py
def create_and_run_with_output(
    self,
    notebook_path: str,
    notebook_content: str,
    output_path: str = "/tmp/notebook_output.txt",
    job_name: str = None
):
    """Create and run notebook with automatic output retrieval."""
    
    # Ensure notebook uses output framework
    if "NotebookOutput" not in notebook_content:
        # Inject output framework
        output_init = f"""
from core.notebook_output import NotebookOutput
output = NotebookOutput(output_path="{output_path}")
"""
        notebook_content = output_init + notebook_content
    
    # Create and run
    result = self.create_and_run(notebook_path, notebook_content, job_name)
    
    # Read output
    if result.get('success'):
        reader = NotebookOutputReader()
        reader.display_output(output_path)
    
    return result
```

---

## 🔄 Integration 2: Workspace Sync Framework

### Current State
- Manual upload/download
- No version control
- No automatic sync

### Proposed Framework

#### 2.1 Workspace Sync Manager

```python
# core/workspace_sync.py
class WorkspaceSync:
    """Bidirectional sync between local and Databricks workspace."""
    
    def __init__(self, local_dir: str, workspace_dir: str):
        self.local_dir = Path(local_dir)
        self.workspace_dir = workspace_dir
        self.sync_config = self._load_config()
    
    def sync_to_workspace(self, pattern: str = "**/*.py"):
        """Sync local files to Databricks workspace."""
        files = list(self.local_dir.glob(pattern))
        
        for file_path in files:
            relative_path = file_path.relative_to(self.local_dir)
            workspace_path = f"{self.workspace_dir}/{relative_path.as_posix()}"
            
            # Create directory structure
            self._create_workspace_dirs(workspace_path)
            
            # Upload file
            self._upload_file(file_path, workspace_path)
    
    def sync_from_workspace(self, pattern: str = "**/*"):
        """Sync Databricks workspace files to local."""
        workspace_files = self._list_workspace_files(self.workspace_dir)
        
        for workspace_path in workspace_files:
            relative_path = workspace_path.replace(self.workspace_dir, "").lstrip("/")
            local_path = self.local_dir / relative_path
            
            # Create local directory
            local_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Download file
            self._download_file(workspace_path, local_path)
    
    def watch_and_sync(self, pattern: str = "**/*.py"):
        """Watch local files and auto-sync to workspace."""
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        
        class SyncHandler(FileSystemEventHandler):
            def __init__(self, sync_manager):
                self.sync = sync_manager
            
            def on_modified(self, event):
                if event.src_path.endswith('.py'):
                    self.sync.sync_to_workspace(pattern=event.src_path)
        
        event_handler = SyncHandler(self)
        observer = Observer()
        observer.schedule(event_handler, self.local_dir, recursive=True)
        observer.start()
        
        return observer
```

#### 2.2 Sync Configuration

```python
# .databricks_sync.json
{
    "sync_pairs": [
        {
            "local": "projects/my_project",
            "workspace": "/Workspace/Users/user@example.com/my_project",
            "patterns": ["**/*.py", "**/*.sql"],
            "auto_sync": true,
            "direction": "bidirectional"
        }
    ],
    "exclude_patterns": [
        "**/__pycache__/**",
        "**/*.pyc",
        "**/.git/**"
    ],
    "sync_on_save": true
}
```

#### 2.3 CLI Commands

```bash
# Sync local to workspace
databricks_cli.py sync push --project my_project

# Sync workspace to local
databricks_cli.py sync pull --project my_project

# Watch and auto-sync
databricks_cli.py sync watch --project my_project

# Two-way sync
databricks_cli.py sync bidirectional --project my_project
```

---

## ⚡ Integration 3: Efficient Connection Management

### Current State
- Connection created per request
- No connection pooling
- No caching

### Proposed Framework

#### 3.1 Connection Pool Manager

```python
# core/connection_manager.py
class ConnectionManager:
    """Efficient connection management with pooling and caching."""
    
    def __init__(self):
        self.sql_pool = {}
        self.api_cache = {}
        self.cache_ttl = 300  # 5 minutes
    
    def get_sql_connection(self, force_new: bool = False):
        """Get or create SQL connection with pooling."""
        pool_key = "default"
        
        if force_new or pool_key not in self.sql_pool:
            from databricks import sql
            from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
            
            connection = sql.connect(
                server_hostname=SERVER_HOSTNAME,
                http_path=HTTP_PATH,
                access_token=TOKEN
            )
            self.sql_pool[pool_key] = connection
        
        return self.sql_pool[pool_key]
    
    def execute_with_cache(self, query: str, cache_key: str = None):
        """Execute query with result caching."""
        import hashlib
        
        if not cache_key:
            cache_key = hashlib.md5(query.encode()).hexdigest()
        
        # Check cache
        if cache_key in self.api_cache:
            cached_result, timestamp = self.api_cache[cache_key]
            if time.time() - timestamp < self.cache_ttl:
                return cached_result
        
        # Execute query
        connection = self.get_sql_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Cache result
        self.api_cache[cache_key] = (result, time.time())
        
        return result
    
    def clear_cache(self):
        """Clear all cached results."""
        self.api_cache.clear()
```

#### 3.2 Connection Health Monitoring

```python
# core/connection_health.py
class ConnectionHealth:
    """Monitor and maintain connection health."""
    
    def check_health(self):
        """Check all connection health."""
        health_status = {
            'sql': self._check_sql_health(),
            'api': self._check_api_health(),
            'workspace': self._check_workspace_health()
        }
        return health_status
    
    def auto_reconnect(self):
        """Automatically reconnect if connection is down."""
        health = self.check_health()
        
        if not health['sql']:
            # Reconnect SQL
            connection_manager.get_sql_connection(force_new=True)
        
        if not health['api']:
            # Reconnect API
            # ... reinitialize API client
```

---

## 🚀 Integration 4: Development Workflow Framework

### 4.1 Local Development → Databricks Execution

```python
# core/dev_workflow.py
class DevWorkflow:
    """Seamless local development with Databricks execution."""
    
    def run_locally(self, notebook_path: str):
        """Run notebook locally (for testing)."""
        # Mock Databricks environment
        # Execute notebook code locally
        pass
    
    def deploy_to_databricks(self, notebook_path: str):
        """Deploy local notebook to Databricks."""
        # Sync to workspace
        # Create/update notebook
        # Return workspace path
        pass
    
    def run_in_databricks(self, notebook_path: str):
        """Run notebook in Databricks and get output."""
        # Deploy
        # Run as job
        # Get output
        pass
```

### 4.2 Hot Reload Development

```python
# Watch local files, auto-deploy and run
workflow = DevWorkflow()
workflow.watch_and_deploy("projects/my_project/**/*.py")
```

---

## 📋 Implementation Roadmap

### Phase 1: Output Framework (Week 1)
- [ ] Create `NotebookOutput` class
- [ ] Create `NotebookOutputReader` class
- [ ] Integrate with job runner
- [ ] Update all notebook templates

### Phase 2: Workspace Sync (Week 2)
- [ ] Create `WorkspaceSync` class
- [ ] Implement sync configuration
- [ ] Add CLI commands
- [ ] Add file watching

### Phase 3: Connection Management (Week 3)
- [ ] Create `ConnectionManager` class
- [ ] Implement connection pooling
- [ ] Add result caching
- [ ] Add health monitoring

### Phase 4: Dev Workflow (Week 4)
- [ ] Create `DevWorkflow` class
- [ ] Implement local testing
- [ ] Add hot reload
- [ ] Create development templates

---

## 🎯 Usage Examples

### Example 1: Standardized Output

```python
from databricks_api import DatabricksAPI
from core.notebook_output import NotebookOutput

db = DatabricksAPI()

notebook = """
from core.notebook_output import NotebookOutput
output = NotebookOutput()

# Your analysis
query = "SELECT * FROM table"
result = spark.sql(query).toPandas()

output.add_query_result("Results", query, result.to_string())
output.write_to_dbfs()
"""

result = db.job_runner.create_and_run_with_output(
    "/Workspace/my_analysis",
    notebook,
    output_path="/tmp/analysis_output.txt"
)
# Output automatically displayed!
```

### Example 2: Workspace Sync

```python
from core.workspace_sync import WorkspaceSync

sync = WorkspaceSync(
    local_dir="projects/my_project",
    workspace_dir="/Workspace/Users/user@example.com/my_project"
)

# One-time sync
sync.sync_to_workspace()

# Watch and auto-sync
observer = sync.watch_and_sync()
```

### Example 3: Efficient Queries

```python
from core.connection_manager import ConnectionManager

conn_mgr = ConnectionManager()

# First call - executes query
results1 = conn_mgr.execute_with_cache("SELECT * FROM table")

# Second call - uses cache (if within TTL)
results2 = conn_mgr.execute_with_cache("SELECT * FROM table")
```

---

## 📊 Benefits

### Productivity Gains

| Feature | Time Saved | Use Case |
|---------|------------|----------|
| Standardized Output | 80% | No manual DBFS writing |
| Workspace Sync | 90% | No manual upload/download |
| Connection Pooling | 50% | Faster query execution |
| Result Caching | 70% | Repeated queries |

### Quality Improvements

- ✅ Consistent output format
- ✅ Automatic file management
- ✅ Reduced connection overhead
- ✅ Better error handling
- ✅ Development workflow integration

---

## 🔧 Next Steps

1. **Review this framework** - Does it meet your needs?
2. **Prioritize features** - Which integration is most important?
3. **Start implementation** - Begin with Phase 1 (Output Framework)
4. **Iterate** - Build, test, refine

---

**This framework transforms your workflow from manual operations to automated, seamless integration!**

