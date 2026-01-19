"""
Integration Tests for Core Modules

These tests verify the core modules work correctly with mocked Databricks services.
They test the full flow from function call to result.

Run with: pytest tests/test_core_integration.py -v
Skip integration tests: pytest tests/test_core_integration.py -v -m "not integration"
"""
import pytest
import sys
import os
import tempfile
from pathlib import Path
from unittest.mock import Mock, MagicMock, patch
from collections import namedtuple

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# =============================================================================
# WORKSPACE SYNC INTEGRATION TESTS
# =============================================================================

class TestWorkspaceSyncIntegration:
    """Integration tests for WorkspaceSync class"""
    
    @pytest.fixture
    def temp_local_dir(self):
        """Create temporary local directory"""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield Path(temp_dir).resolve()
    
    @pytest.mark.integration
    def test_upload_file_full_flow(self, temp_local_dir):
        """Test uploading a file to workspace"""
        # Create test file
        test_file = temp_local_dir / 'test_notebook.py'
        test_file.write_text('# Test notebook\nprint("Hello, Databricks!")')
        
        with patch('requests.post') as mock_post:
            mock_response = MagicMock()
            mock_response.raise_for_status = MagicMock()
            mock_response.status_code = 200
            mock_post.return_value = mock_response
            
            from core.workspace_sync import WorkspaceSync
            
            sync = WorkspaceSync(
                local_dir=str(temp_local_dir),
                workspace_dir='/Workspace/Users/test@example.com/notebooks',
                host='https://test.databricks.com',
                token='test-token'
            )
            
            # Use explicit workspace path to avoid relative path issues
            result = sync.upload_file(
                test_file, 
                workspace_path='/Workspace/Users/test@example.com/notebooks/test_notebook.py'
            )
            
            assert result['success'] is True
            assert 'workspace_path' in result
            assert result['size_kb'] > 0
    
    @pytest.mark.integration
    def test_download_file_full_flow(self, temp_local_dir):
        """Test downloading a file from workspace"""
        import base64
        
        content = '# Downloaded from Databricks\nprint("Success!")'
        content_b64 = base64.b64encode(content.encode()).decode()
        
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.raise_for_status = MagicMock()
            mock_response.json.return_value = {'content': content_b64}
            mock_get.return_value = mock_response
            
            from core.workspace_sync import WorkspaceSync
            
            sync = WorkspaceSync(
                local_dir=str(temp_local_dir),
                workspace_dir='/Workspace/Users/test@example.com/notebooks',
                host='https://test.databricks.com',
                token='test-token'
            )
            
            local_path = temp_local_dir / 'downloaded.py'
            result = sync.download_file(
                '/Workspace/Users/test@example.com/notebooks/test.py',
                local_path
            )
            
            assert result['success'] is True
            assert local_path.exists()
            assert 'Downloaded from Databricks' in local_path.read_text()
    
    @pytest.mark.integration
    def test_sync_to_workspace_dry_run(self, temp_local_dir):
        """Test dry run mode doesn't upload files"""
        (temp_local_dir / 'test.py').write_text('# Test')
        
        with patch('requests.post') as mock_post:
            from core.workspace_sync import WorkspaceSync
            
            sync = WorkspaceSync(
                local_dir=str(temp_local_dir),
                workspace_dir='/Workspace/test',
                host='https://test.databricks.com',
                token='test-token'
            )
            
            results = sync.sync_to_workspace(pattern='**/*.py', dry_run=True)
            
            # Should not make any API calls in dry run
            mock_post.assert_not_called()
            assert results['total'] == 1
            assert results['success'][0]['dry_run'] is True
    
    @pytest.mark.integration
    def test_list_workspace_files(self, temp_local_dir):
        """Test listing workspace files"""
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.raise_for_status = MagicMock()
            mock_response.json.return_value = {
                'objects': [
                    {'path': '/Workspace/test/notebook1', 'object_type': 'NOTEBOOK'},
                    {'path': '/Workspace/test/notebook2', 'object_type': 'NOTEBOOK'},
                    {'path': '/Workspace/test/file.txt', 'object_type': 'FILE'},
                ]
            }
            mock_get.return_value = mock_response
            
            from core.workspace_sync import WorkspaceSync
            
            sync = WorkspaceSync(
                local_dir=str(temp_local_dir),
                workspace_dir='/Workspace/test',
                host='https://test.databricks.com',
                token='test-token'
            )
            
            files = sync.list_workspace_files(recursive=False)
            
            assert len(files) == 3
            assert '/Workspace/test/notebook1' in files
    
    @pytest.mark.integration
    def test_upload_nonexistent_file(self, temp_local_dir):
        """Test upload handles nonexistent file"""
        from core.workspace_sync import WorkspaceSync
        
        sync = WorkspaceSync(
            local_dir=str(temp_local_dir),
            workspace_dir='/Workspace/test',
            host='https://test.databricks.com',
            token='test-token'
        )
        
        result = sync.upload_file(temp_local_dir / 'nonexistent.py')
        
        assert result['success'] is False
        assert 'not found' in result['error'].lower()
    
    @pytest.mark.integration
    def test_language_detection(self, temp_local_dir):
        """Test language detection from file extension"""
        from core.workspace_sync import WorkspaceSync
        
        sync = WorkspaceSync(
            local_dir=str(temp_local_dir),
            workspace_dir='/Workspace/test',
            host='https://test.databricks.com',
            token='test-token'
        )
        
        assert sync._get_language_from_extension(Path('test.py')) == 'PYTHON'
        assert sync._get_language_from_extension(Path('test.sql')) == 'SQL'
        assert sync._get_language_from_extension(Path('test.scala')) == 'SCALA'
        assert sync._get_language_from_extension(Path('test.r')) == 'R'
        assert sync._get_language_from_extension(Path('test.txt')) == 'PYTHON'  # Default


# =============================================================================
# QUERY UTIL INTEGRATION TESTS
# =============================================================================

class TestQueryUtilIntegration:
    """Integration tests for query_util module"""
    
    @pytest.mark.integration
    def test_print_table_formats_output(self):
        """Test print_table formats results correctly"""
        from core.query_util import print_table
        
        Row = namedtuple('Row', ['id', 'name'])
        rows = [Row(1, 'Alice'), Row(2, 'Bob')]
        columns = ['id', 'name']
        
        # Should not raise
        print_table(rows, columns)
    
    @pytest.mark.integration
    def test_print_table_with_limit(self):
        """Test print_table respects limit"""
        from core.query_util import print_table
        
        Row = namedtuple('Row', ['id', 'name'])
        rows = [Row(i, f'User{i}') for i in range(100)]
        columns = ['id', 'name']
        
        # Should not raise and should limit output
        print_table(rows, columns, limit=10)
    
    @pytest.mark.integration
    def test_format_value(self):
        """Test format_value handles different types"""
        from core.query_util import format_value
        from decimal import Decimal
        
        assert format_value(None) == 'NULL'
        assert format_value(True) == 'True'
        assert format_value(False) == 'False'
        assert format_value(1000) == '1,000'
        assert format_value(3.14159) == '3.14'
        assert format_value(Decimal('123.45')) == '123.45'
        assert format_value('hello') == 'hello'


# =============================================================================
# TABLE INSPECTOR INTEGRATION TESTS
# =============================================================================

class TestTableInspectorIntegration:
    """Integration tests for table_inspector module"""
    
    @pytest.mark.integration
    def test_get_table_schema(self):
        """Test getting table schema"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_conn = MagicMock()
            mock_cursor = MagicMock()
            
            # Mock DESCRIBE TABLE response
            mock_cursor.fetchall.return_value = [
                ('id', 'bigint', 'Primary key'),
                ('name', 'string', 'User name'),
                ('created_at', 'timestamp', 'Creation timestamp')
            ]
            
            mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
            mock_conn.cursor.return_value.__exit__.return_value = None
            mock_connect.return_value.__enter__.return_value = mock_conn
            mock_connect.return_value.__exit__.return_value = None
            
            from core.table_inspector import TableInspector
            
            inspector = TableInspector(
                server_hostname='test.databricks.com',
                http_path='/sql/test',
                token='test-token'
            )
            schema = inspector.get_table_schema('catalog.schema.users')
            
            assert len(schema) == 3
            assert schema[0]['column'] == 'id'
            assert schema[0]['data_type'] == 'bigint'
    
    @pytest.mark.integration
    def test_check_duplicates_by_column(self):
        """Test checking for duplicates"""
        with patch('databricks.sql.connect') as mock_connect:
            mock_conn = MagicMock()
            mock_cursor = MagicMock()
            
            # Mock duplicate check response
            mock_cursor.fetchall.return_value = [
                ('user@example.com', 5),
                ('admin@example.com', 3)
            ]
            
            mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
            mock_conn.cursor.return_value.__exit__.return_value = None
            mock_connect.return_value.__enter__.return_value = mock_conn
            mock_connect.return_value.__exit__.return_value = None
            
            from core.table_inspector import TableInspector
            
            inspector = TableInspector(
                server_hostname='test.databricks.com',
                http_path='/sql/test',
                token='test-token'
            )
            duplicates = inspector.check_duplicates_by_column('users', 'email')
            
            assert len(duplicates) == 2
            assert duplicates[0]['value'] == 'user@example.com'
            assert duplicates[0]['count'] == 5


# =============================================================================
# DATABRICKS JOB RUNNER INTEGRATION TESTS
# =============================================================================

class TestDatabricksJobRunnerIntegration:
    """Integration tests for databricks_job_runner module"""
    
    @pytest.mark.integration
    def test_create_notebook(self):
        """Test creating a notebook"""
        with patch('requests.post') as mock_post:
            mock_response = MagicMock()
            mock_response.raise_for_status = MagicMock()
            mock_post.return_value = mock_response
            
            from core.databricks_job_runner import DatabricksJobRunner
            
            runner = DatabricksJobRunner(
                host='https://test.databricks.com',
                token='test-token',
                cluster_id='test-cluster'
            )
            
            result = runner.create_notebook(
                '/Workspace/test/notebook',
                '# Test notebook\nprint("Hello")'
            )
            
            assert result is True
            mock_post.assert_called_once()
    
    @pytest.mark.integration
    def test_create_job(self):
        """Test creating a job"""
        with patch('requests.post') as mock_post:
            mock_response = MagicMock()
            mock_response.raise_for_status = MagicMock()
            mock_response.json.return_value = {'job_id': 123}
            mock_post.return_value = mock_response
            
            from core.databricks_job_runner import DatabricksJobRunner
            
            runner = DatabricksJobRunner(
                host='https://test.databricks.com',
                token='test-token',
                cluster_id='test-cluster'
            )
            
            job_id = runner.create_job(
                notebook_path='/Workspace/test/notebook',
                job_name='test-job'
            )
            
            assert job_id == 123
    
    @pytest.mark.integration
    def test_run_job(self):
        """Test running a job"""
        with patch('requests.post') as mock_post:
            mock_response = MagicMock()
            mock_response.raise_for_status = MagicMock()
            mock_response.json.return_value = {'run_id': 456}
            mock_post.return_value = mock_response
            
            from core.databricks_job_runner import DatabricksJobRunner
            
            runner = DatabricksJobRunner(
                host='https://test.databricks.com',
                token='test-token',
                cluster_id='test-cluster'
            )
            
            run_id = runner.run_job(123)
            
            assert run_id == 456
    
    @pytest.mark.integration
    def test_get_run_status(self):
        """Test getting run status"""
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.raise_for_status = MagicMock()
            mock_response.json.return_value = {
                'state': {
                    'life_cycle_state': 'TERMINATED',
                    'result_state': 'SUCCESS'
                }
            }
            mock_get.return_value = mock_response
            
            from core.databricks_job_runner import DatabricksJobRunner
            
            runner = DatabricksJobRunner(
                host='https://test.databricks.com',
                token='test-token',
                cluster_id='test-cluster'
            )
            
            status = runner.get_run_status(456)
            
            assert status['state']['life_cycle_state'] == 'TERMINATED'
            assert status['state']['result_state'] == 'SUCCESS'
    
    @pytest.mark.integration
    def test_monitor_job_success(self):
        """Test monitoring a job to completion"""
        with patch('requests.get') as mock_get, \
             patch('time.sleep'):  # Skip actual sleeping
            
            # Simulate job completing
            mock_response = MagicMock()
            mock_response.raise_for_status = MagicMock()
            mock_response.json.return_value = {
                'state': {
                    'life_cycle_state': 'TERMINATED',
                    'result_state': 'SUCCESS'
                },
                'tasks': []
            }
            mock_get.return_value = mock_response
            
            from core.databricks_job_runner import DatabricksJobRunner
            
            runner = DatabricksJobRunner(
                host='https://test.databricks.com',
                token='test-token',
                cluster_id='test-cluster'
            )
            
            result = runner.monitor_job(456, poll_interval=0, max_wait=10)
            
            assert result['state'] == 'TERMINATED'
            assert result['result_state'] == 'SUCCESS'
