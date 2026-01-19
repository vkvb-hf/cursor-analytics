"""
Tests for databricks_job_runner.py
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.databricks_job_runner import DatabricksJobRunner


class TestDatabricksJobRunner:
    """Tests for DatabricksJobRunner class"""
    
    @pytest.fixture
    def runner(self):
        return DatabricksJobRunner(
            host='https://test.databricks.com',
            token='test-token',
            cluster_id='test-cluster'
        )
    
    def test_init(self, runner):
        assert runner.host == 'https://test.databricks.com'
        assert runner.token == 'test-token'
        assert runner.cluster_id == 'test-cluster'
        assert 'Authorization' in runner.headers
    
    @patch('core.databricks_job_runner.requests.post')
    def test_create_notebook_success(self, mock_post, runner):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response
        
        result = runner.create_notebook(
            notebook_path='/Workspace/test',
            content='# Test notebook',
            overwrite=True
        )
        
        assert result is True
        mock_post.assert_called_once()
        # Check the URL is in the call
        call_args = mock_post.call_args
        assert 'workspace/import' in str(call_args)
    
    @patch('core.databricks_job_runner.requests.post')
    def test_create_notebook_failure(self, mock_post, runner):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("API Error")
        mock_post.return_value = mock_response
        
        result = runner.create_notebook(
            notebook_path='/Workspace/test',
            content='# Test notebook'
        )
        
        assert result is False
    
    @patch('core.databricks_job_runner.requests.post')
    def test_create_job(self, mock_post, runner):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {'job_id': 123}
        mock_post.return_value = mock_response
        
        job_id = runner.create_job(
            notebook_path='/Workspace/test',
            job_name='test-job'
        )
        
        assert job_id == 123
    
    @patch('core.databricks_job_runner.requests.get')
    def test_get_run_status(self, mock_get, runner):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {
            'state': {'life_cycle_state': 'RUNNING'},
            'run_id': 123
        }
        mock_get.return_value = mock_response
        
        status = runner.get_run_status(123)
        
        assert status is not None
        assert status['state']['life_cycle_state'] == 'RUNNING'
        mock_get.assert_called_once()
    
    @patch('core.databricks_job_runner.requests.post')
    def test_run_job(self, mock_post, runner):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {'run_id': 456}
        mock_post.return_value = mock_response
        
        run_id = runner.run_job(123)
        
        assert run_id == 456
