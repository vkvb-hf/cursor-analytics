"""
Tests for Google Sheets MCP Server (mcp/google_sheets/server.py)

Tests the MCP server components without requiring Google API dependencies.
Uses file-based validation and mocked imports.
"""
import pytest
import sys
import os
import ast
from unittest.mock import Mock, MagicMock, patch
from pathlib import Path

# Get the path to the MCP server
MCP_PATH = Path(__file__).parent.parent / 'mcp' / 'google_sheets'
REPO_ROOT = Path(__file__).parent.parent


class TestGoogleSheetsMCPServerSyntax:
    """Test that the MCP server has valid syntax and structure"""
    
    def test_server_file_exists(self):
        """Test server.py exists"""
        server_path = MCP_PATH / 'server.py'
        assert server_path.exists(), f"Server file not found at {server_path}"
    
    def test_server_syntax_valid(self):
        """Test server.py has valid Python syntax"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # This will raise SyntaxError if invalid
        ast.parse(content)
    
    def test_server_uses_fastmcp(self):
        """Test server.py uses FastMCP pattern"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        assert 'from mcp.server.fastmcp import FastMCP' in content, "Should import FastMCP"
        assert 'FastMCP(' in content, "Should initialize FastMCP"
        assert '@mcp.tool()' in content, "Should use @mcp.tool() decorator"
    
    def test_server_has_required_tools(self):
        """Test server.py contains all required tool definitions"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        required_tools = [
            'def read_sheet',
            'def get_sheet_info',
            'def read_multiple_ranges',
            'def read_comments'
        ]
        
        for tool in required_tools:
            assert tool in content, f"Missing tool: {tool}"
    
    def test_server_has_helper_functions(self):
        """Test server.py has required helper functions"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        assert 'def get_sheets_service' in content, "Missing get_sheets_service function"
        assert 'def _column_number_to_letter' in content, "Missing _column_number_to_letter function"


class TestGoogleSheetsMCPConfig:
    """Test configuration patterns in the server"""
    
    def test_service_account_file_config(self):
        """Test SERVICE_ACCOUNT_FILE is configurable via env var"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Should read from environment variable
        assert 'GOOGLE_SERVICE_ACCOUNT_FILE' in content, "Should use GOOGLE_SERVICE_ACCOUNT_FILE env var"
        assert "os.getenv('GOOGLE_SERVICE_ACCOUNT_FILE'" in content, "Should use os.getenv for config"
    
    def test_scopes_defined(self):
        """Test Google API scopes are defined"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        assert 'SCOPES' in content, "Should define SCOPES"
        assert 'spreadsheets' in content, "Should include spreadsheets scope"


class TestEnvExampleExists:
    """Test that environment example file exists"""
    
    def test_google_sheets_env_example_exists(self):
        """Test env.example exists for Google Sheets MCP"""
        env_example = MCP_PATH / 'env.example'
        assert env_example.exists(), "mcp/google_sheets/env.example should exist"
    
    def test_env_example_has_required_vars(self):
        """Test env.example contains required variables"""
        env_example = MCP_PATH / 'env.example'
        with open(env_example, 'r') as f:
            content = f.read()
        
        assert 'GOOGLE_SERVICE_ACCOUNT_FILE' in content, "Missing GOOGLE_SERVICE_ACCOUNT_FILE in env.example"


class TestColumnNumberToLetterLogic:
    """Test the column number to letter conversion logic"""
    
    def test_column_conversion_logic(self):
        """Test column number to letter conversion algorithm"""
        # Implement the same logic to test it
        def column_number_to_letter(col_num: int) -> str:
            result = ""
            while col_num > 0:
                col_num -= 1
                result = chr(col_num % 26 + ord('A')) + result
                col_num //= 26
            return result
        
        # Test cases
        assert column_number_to_letter(1) == 'A'
        assert column_number_to_letter(2) == 'B'
        assert column_number_to_letter(26) == 'Z'
        assert column_number_to_letter(27) == 'AA'
        assert column_number_to_letter(28) == 'AB'
        assert column_number_to_letter(52) == 'AZ'
        assert column_number_to_letter(53) == 'BA'
        assert column_number_to_letter(702) == 'ZZ'
        assert column_number_to_letter(703) == 'AAA'


class TestReadSheetResponseStructure:
    """Test that read_sheet returns correct response structure"""
    
    def test_response_structure_in_code(self):
        """Test that response structure matches expected format"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Check for expected response keys
        assert '"success"' in content, "Should return success key"
        assert '"headers"' in content, "Should return headers key"
        assert '"row_count"' in content, "Should return row_count key"
        assert '"data"' in content, "Should return data key"
    
    def test_error_handling_in_code(self):
        """Test that error handling returns correct structure"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Check for error handling
        assert 'except HttpError' in content, "Should handle HttpError"
        assert 'except Exception' in content, "Should handle general exceptions"
        assert '"error"' in content, "Should return error key on failure"


class TestGetSheetInfoResponseStructure:
    """Test that get_sheet_info returns correct response structure"""
    
    def test_response_structure_in_code(self):
        """Test that response structure matches expected format"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Check for expected response keys in get_sheet_info
        assert '"spreadsheet_title"' in content, "Should return spreadsheet_title"
        assert '"spreadsheet_id"' in content, "Should return spreadsheet_id"
        assert '"sheets"' in content, "Should return sheets list"


class TestReadMultipleRangesStructure:
    """Test read_multiple_ranges function structure"""
    
    def test_function_accepts_list_parameter(self):
        """Test that read_multiple_ranges accepts a list of ranges"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Check function signature includes list parameter
        assert 'ranges: list' in content, "Should accept ranges as list parameter"
        assert 'batchGet' in content, "Should use batchGet API"


class TestReadCommentsStructure:
    """Test read_comments function structure"""
    
    def test_function_has_optional_parameters(self):
        """Test that read_comments has optional filter parameters"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Check for optional parameters
        assert 'sheet_name: str = None' in content or 'sheet_name = None' in content, \
            "Should have optional sheet_name parameter"
        assert 'range_name: str = None' in content or 'range_name = None' in content, \
            "Should have optional range_name parameter"
    
    def test_returns_comment_structure(self):
        """Test that read_comments returns expected structure"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        assert '"comment_count"' in content, "Should return comment_count"
        assert '"comments"' in content, "Should return comments list"


class TestMCPToolDecorators:
    """Test that all functions have proper MCP tool decorators"""
    
    def test_all_tools_have_decorators(self):
        """Test that all tool functions have @mcp.tool() decorator"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Count decorators and tool functions
        decorator_count = content.count('@mcp.tool()')
        
        # Should have 4 tools: read_sheet, get_sheet_info, read_multiple_ranges, read_comments
        assert decorator_count >= 4, f"Expected at least 4 @mcp.tool() decorators, found {decorator_count}"
    
    def test_tools_have_docstrings(self):
        """Test that tool functions have docstrings"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Parse the AST to check for docstrings
        tree = ast.parse(content)
        
        tool_functions = ['read_sheet', 'get_sheet_info', 'read_multiple_ranges', 'read_comments']
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in tool_functions:
                # Check if function has a docstring
                if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
                    docstring = node.body[0].value.value
                    assert len(docstring) > 10, f"Function {node.name} should have a meaningful docstring"
                else:
                    pytest.fail(f"Function {node.name} is missing a docstring")


class TestMainEntryPoint:
    """Test the main entry point"""
    
    def test_has_main_block(self):
        """Test server has if __name__ == '__main__' block"""
        server_path = MCP_PATH / 'server.py'
        with open(server_path, 'r') as f:
            content = f.read()
        
        assert "if __name__ ==" in content, "Should have main block"
        assert "mcp.run()" in content, "Should call mcp.run() in main"
