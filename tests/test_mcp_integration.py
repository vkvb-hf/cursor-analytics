"""
Integration Tests for MCP Servers

These tests verify the MCP servers work correctly with mocked external services.
They test the full flow from tool invocation to response.

Run with: pytest tests/test_mcp_integration.py -v
Skip integration tests: pytest tests/test_mcp_integration.py -v -m "not integration"
"""
import pytest
import sys
import os
import json
import tempfile
import importlib.util
from pathlib import Path
from unittest.mock import Mock, MagicMock, patch, AsyncMock

# Get paths to MCP servers
MCP_DATABRICKS_PATH = Path(__file__).parent.parent / 'mcp' / 'databricks'
MCP_SHEETS_PATH = Path(__file__).parent.parent / 'mcp' / 'google_sheets'


def load_module_from_path(module_name: str, file_path: Path):
    """Load a module from a specific file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    return module, spec


# =============================================================================
# DATABRICKS MCP INTEGRATION TESTS
# =============================================================================

class TestDatabricksMCPIntegration:
    """Integration tests for Databricks MCP server"""
    
    @pytest.fixture
    def mock_databricks_env(self):
        """Set up mock environment for Databricks"""
        env_vars = {
            'DATABRICKS_HOST': 'https://test.cloud.databricks.com',
            'DATABRICKS_TOKEN': 'test-token-12345',
            'DATABRICKS_HTTP_PATH': '/sql/1.0/warehouses/test',
            'DATABRICKS_SERVER_HOSTNAME': 'test.cloud.databricks.com',
            'CLUSTER_ID': 'test-cluster-123'
        }
        with patch.dict(os.environ, env_vars, clear=False):
            yield env_vars
    
    @pytest.mark.integration
    def test_databricks_mcp_server_structure(self):
        """Test Databricks MCP server has correct structure"""
        server_path = MCP_DATABRICKS_PATH / 'server.py'
        assert server_path.exists()
        
        content = server_path.read_text()
        
        # Verify key components exist
        assert 'class ConnectionPool' in content
        assert 'class DatabricksClient' in content
        assert 'execute_sql' in content
        assert 'create_notebook' in content
        assert 'run_notebook' in content
    
    @pytest.mark.integration
    def test_databricks_client_methods(self, mock_databricks_env):
        """Test DatabricksClient has all required methods"""
        server_path = MCP_DATABRICKS_PATH / 'server.py'
        content = server_path.read_text()
        
        required_methods = [
            'def create_notebook',
            'def create_job',
            'def run_job',
            'def get_run_status',
            'def upload_file',
            'def download_file',
        ]
        
        for method in required_methods:
            assert method in content, f"Missing method: {method}"
    
    @pytest.mark.integration
    def test_connection_pool_structure(self, mock_databricks_env):
        """Test ConnectionPool has correct structure"""
        server_path = MCP_DATABRICKS_PATH / 'server.py'
        content = server_path.read_text()
        
        assert 'def get_connection' in content
        assert 'def execute_query' in content
        assert 'def close' in content
    
    @pytest.mark.integration
    def test_all_tools_defined(self, mock_databricks_env):
        """Test all expected tools are defined"""
        server_path = MCP_DATABRICKS_PATH / 'server.py'
        content = server_path.read_text()
        
        expected_tools = [
            'execute_sql',
            'run_sql_file',
            'create_notebook',
            'run_notebook',
            'get_job_status',
            'sync_to_workspace',
            'sync_from_workspace'
        ]
        
        for tool in expected_tools:
            assert f'name="{tool}"' in content, f"Missing tool: {tool}"


# =============================================================================
# GOOGLE SHEETS MCP INTEGRATION TESTS
# =============================================================================

class TestGoogleSheetsMCPIntegration:
    """Integration tests for Google Sheets MCP server"""
    
    @pytest.fixture
    def mock_sheets_env(self):
        """Set up mock environment for Google Sheets"""
        with patch.dict(os.environ, {
            'GOOGLE_SERVICE_ACCOUNT_FILE': '/fake/service-account.json'
        }):
            # Clear cached module
            for mod_name in list(sys.modules.keys()):
                if 'server' in mod_name:
                    del sys.modules[mod_name]
            yield
    
    @pytest.mark.integration
    def test_read_sheet_full_flow(self, mock_sheets_env):
        """Test full read_sheet flow with mocked Google API"""
        with patch('google.oauth2.service_account.Credentials.from_service_account_file') as mock_creds, \
             patch('googleapiclient.discovery.build') as mock_build:
            
            # Setup mocks
            mock_creds.return_value = MagicMock()
            
            mock_service = MagicMock()
            mock_sheet = MagicMock()
            mock_values = MagicMock()
            
            # Simulate a real spreadsheet response
            mock_values.get.return_value.execute.return_value = {
                'values': [
                    ['Employee ID', 'Name', 'Department', 'Salary'],
                    ['E001', 'Alice Smith', 'Engineering', '120000'],
                    ['E002', 'Bob Johnson', 'Marketing', '95000'],
                    ['E003', 'Carol Williams', 'Engineering', '115000'],
                ]
            }
            mock_sheet.values.return_value = mock_values
            mock_service.spreadsheets.return_value = mock_sheet
            mock_build.return_value = mock_service
            
            # Import the module
            sys.path.insert(0, str(MCP_SHEETS_PATH))
            import server
            importlib.reload(server)
            
            result = server.read_sheet('1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms', 'Sheet1')
            
            assert result['success'] is True
            assert result['row_count'] == 3
            assert result['headers'] == ['Employee ID', 'Name', 'Department', 'Salary']
            assert result['data'][0]['Name'] == 'Alice Smith'
            assert result['data'][1]['Department'] == 'Marketing'
    
    @pytest.mark.integration
    def test_get_sheet_info_full_flow(self, mock_sheets_env):
        """Test full get_sheet_info flow"""
        with patch('google.oauth2.service_account.Credentials.from_service_account_file') as mock_creds, \
             patch('googleapiclient.discovery.build') as mock_build:
            
            mock_creds.return_value = MagicMock()
            
            mock_service = MagicMock()
            mock_sheet = MagicMock()
            
            mock_sheet.get.return_value.execute.return_value = {
                'properties': {'title': 'Employee Database'},
                'sheets': [
                    {
                        'properties': {
                            'title': 'Employees',
                            'sheetId': 0,
                            'index': 0,
                            'gridProperties': {'rowCount': 1000, 'columnCount': 26}
                        }
                    },
                    {
                        'properties': {
                            'title': 'Departments',
                            'sheetId': 1,
                            'index': 1,
                            'gridProperties': {'rowCount': 100, 'columnCount': 10}
                        }
                    }
                ]
            }
            mock_service.spreadsheets.return_value = mock_sheet
            mock_build.return_value = mock_service
            
            sys.path.insert(0, str(MCP_SHEETS_PATH))
            import server
            importlib.reload(server)
            
            result = server.get_sheet_info('test-spreadsheet-id')
            
            assert result['success'] is True
            assert result['spreadsheet_title'] == 'Employee Database'
            assert len(result['sheets']) == 2
            assert result['sheets'][0]['title'] == 'Employees'
            assert result['sheets'][1]['title'] == 'Departments'
    
    @pytest.mark.integration
    def test_read_multiple_ranges_full_flow(self, mock_sheets_env):
        """Test reading multiple ranges in one call"""
        with patch('google.oauth2.service_account.Credentials.from_service_account_file') as mock_creds, \
             patch('googleapiclient.discovery.build') as mock_build:
            
            mock_creds.return_value = MagicMock()
            
            mock_service = MagicMock()
            mock_sheet = MagicMock()
            mock_values = MagicMock()
            
            mock_values.batchGet.return_value.execute.return_value = {
                'valueRanges': [
                    {'range': 'Sheet1!A1:B3', 'values': [['A1', 'B1'], ['A2', 'B2'], ['A3', 'B3']]},
                    {'range': 'Sheet1!D1:E2', 'values': [['D1', 'E1'], ['D2', 'E2']]}
                ]
            }
            mock_sheet.values.return_value = mock_values
            mock_service.spreadsheets.return_value = mock_sheet
            mock_build.return_value = mock_service
            
            sys.path.insert(0, str(MCP_SHEETS_PATH))
            import server
            importlib.reload(server)
            
            result = server.read_multiple_ranges(
                'test-id',
                ['Sheet1!A1:B3', 'Sheet1!D1:E2']
            )
            
            assert result['success'] is True
            assert 'Sheet1!A1:B3' in result['ranges']
            assert 'Sheet1!D1:E2' in result['ranges']
    
    @pytest.mark.integration
    def test_read_sheet_empty_data(self, mock_sheets_env):
        """Test read_sheet handles empty sheet"""
        with patch('google.oauth2.service_account.Credentials.from_service_account_file') as mock_creds, \
             patch('googleapiclient.discovery.build') as mock_build:
            
            mock_creds.return_value = MagicMock()
            
            mock_service = MagicMock()
            mock_sheet = MagicMock()
            mock_values = MagicMock()
            
            mock_values.get.return_value.execute.return_value = {'values': []}
            mock_sheet.values.return_value = mock_values
            mock_service.spreadsheets.return_value = mock_sheet
            mock_build.return_value = mock_service
            
            sys.path.insert(0, str(MCP_SHEETS_PATH))
            import server
            importlib.reload(server)
            
            result = server.read_sheet('test-id', 'Sheet1')
            
            assert result['success'] is True
            assert result['data'] == []
    
    @pytest.mark.integration
    def test_read_sheet_with_sparse_data(self, mock_sheets_env):
        """Test read_sheet handles rows with missing columns"""
        with patch('google.oauth2.service_account.Credentials.from_service_account_file') as mock_creds, \
             patch('googleapiclient.discovery.build') as mock_build:
            
            mock_creds.return_value = MagicMock()
            
            mock_service = MagicMock()
            mock_sheet = MagicMock()
            mock_values = MagicMock()
            
            # Row 2 is missing the last column
            mock_values.get.return_value.execute.return_value = {
                'values': [
                    ['Name', 'Age', 'City'],
                    ['Alice', '30'],  # Missing City
                    ['Bob', '25', 'NYC']
                ]
            }
            mock_sheet.values.return_value = mock_values
            mock_service.spreadsheets.return_value = mock_sheet
            mock_build.return_value = mock_service
            
            sys.path.insert(0, str(MCP_SHEETS_PATH))
            import server
            importlib.reload(server)
            
            result = server.read_sheet('test-id', 'Sheet1')
            
            assert result['success'] is True
            assert result['data'][0]['City'] == ''  # Should be padded
            assert result['data'][1]['City'] == 'NYC'
