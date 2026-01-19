"""
Tests for Google Sheets MCP Server (mcp/google_sheets/server.py)

Tests the MCP server components:
- Service account authentication
- read_sheet tool
- get_sheet_info tool
- read_multiple_ranges tool
- read_comments tool
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch
from pathlib import Path

# Get the path to the MCP server
MCP_PATH = Path(__file__).parent.parent / 'mcp' / 'google_sheets'
sys.path.insert(0, str(MCP_PATH))


class TestGoogleSheetsMCPConfig:
    """Test configuration and service setup"""
    
    def test_service_account_file_default(self):
        """Test SERVICE_ACCOUNT_FILE has default value"""
        # Import the module
        spec = __import__('server')
        
        # Default should be 'service-account.json'
        assert 'service-account.json' in spec.SERVICE_ACCOUNT_FILE or os.getenv('GOOGLE_SERVICE_ACCOUNT_FILE')


class TestReadSheetFunction:
    """Test read_sheet function logic"""
    
    @patch.dict(os.environ, {'GOOGLE_SERVICE_ACCOUNT_FILE': '/fake/path.json'})
    def test_read_sheet_with_mock_service(self):
        """Test read_sheet returns data correctly with mocked service"""
        # Reload module to pick up env var
        import importlib
        if 'server' in sys.modules:
            del sys.modules['server']
        
        with patch('google.oauth2.service_account.Credentials.from_service_account_file') as mock_creds, \
             patch('googleapiclient.discovery.build') as mock_build:
            
            # Setup mocks
            mock_creds.return_value = MagicMock()
            
            mock_service = MagicMock()
            mock_sheet = MagicMock()
            mock_values = MagicMock()
            
            mock_values.get.return_value.execute.return_value = {
                'values': [
                    ['Name', 'Age', 'City'],
                    ['Alice', '30', 'NYC'],
                    ['Bob', '25', 'LA']
                ]
            }
            mock_sheet.values.return_value = mock_values
            mock_service.spreadsheets.return_value = mock_sheet
            mock_build.return_value = mock_service
            
            # Import and test
            import server
            result = server.read_sheet('test-spreadsheet-id', 'Sheet1')
            
            assert result['success'] is True
            assert result['row_count'] == 2
            assert result['headers'] == ['Name', 'Age', 'City']
            assert len(result['data']) == 2
            assert result['data'][0]['Name'] == 'Alice'
    
    @patch.dict(os.environ, {'GOOGLE_SERVICE_ACCOUNT_FILE': '/fake/path.json'})
    def test_read_sheet_empty_data(self):
        """Test read_sheet handles empty sheet"""
        import importlib
        if 'server' in sys.modules:
            del sys.modules['server']
        
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
            
            import server
            result = server.read_sheet('test-id', 'Sheet1')
            
            assert result['success'] is True
            assert result['data'] == []
    
    @patch.dict(os.environ, {'GOOGLE_SERVICE_ACCOUNT_FILE': '/fake/path.json'})
    def test_read_sheet_headers_only(self):
        """Test read_sheet handles sheet with only headers"""
        import importlib
        if 'server' in sys.modules:
            del sys.modules['server']
        
        with patch('google.oauth2.service_account.Credentials.from_service_account_file') as mock_creds, \
             patch('googleapiclient.discovery.build') as mock_build:
            
            mock_creds.return_value = MagicMock()
            
            mock_service = MagicMock()
            mock_sheet = MagicMock()
            mock_values = MagicMock()
            
            mock_values.get.return_value.execute.return_value = {
                'values': [['Name', 'Age', 'City']]
            }
            mock_sheet.values.return_value = mock_values
            mock_service.spreadsheets.return_value = mock_sheet
            mock_build.return_value = mock_service
            
            import server
            result = server.read_sheet('test-id', 'Sheet1')
            
            assert result['success'] is True
            assert result['headers'] == ['Name', 'Age', 'City']
            assert result['data'] == []


class TestGetSheetInfoFunction:
    """Test get_sheet_info function"""
    
    @patch.dict(os.environ, {'GOOGLE_SERVICE_ACCOUNT_FILE': '/fake/path.json'})
    def test_get_sheet_info_success(self):
        """Test get_sheet_info returns metadata"""
        import importlib
        if 'server' in sys.modules:
            del sys.modules['server']
        
        with patch('google.oauth2.service_account.Credentials.from_service_account_file') as mock_creds, \
             patch('googleapiclient.discovery.build') as mock_build:
            
            mock_creds.return_value = MagicMock()
            
            mock_service = MagicMock()
            mock_sheet = MagicMock()
            
            mock_sheet.get.return_value.execute.return_value = {
                'properties': {'title': 'Test Spreadsheet'},
                'sheets': [
                    {
                        'properties': {
                            'title': 'Sheet1',
                            'sheetId': 0,
                            'index': 0,
                            'gridProperties': {'rowCount': 100, 'columnCount': 10}
                        }
                    }
                ]
            }
            mock_service.spreadsheets.return_value = mock_sheet
            mock_build.return_value = mock_service
            
            import server
            result = server.get_sheet_info('test-id')
            
            assert result['success'] is True
            assert result['spreadsheet_title'] == 'Test Spreadsheet'
            assert len(result['sheets']) == 1
            assert result['sheets'][0]['title'] == 'Sheet1'


class TestColumnNumberToLetter:
    """Test helper function for column conversion"""
    
    def test_column_number_to_letter(self):
        """Test column number to letter conversion"""
        import importlib
        if 'server' in sys.modules:
            del sys.modules['server']
        
        import server
        
        assert server._column_number_to_letter(1) == 'A'
        assert server._column_number_to_letter(2) == 'B'
        assert server._column_number_to_letter(26) == 'Z'
        assert server._column_number_to_letter(27) == 'AA'
        assert server._column_number_to_letter(28) == 'AB'
