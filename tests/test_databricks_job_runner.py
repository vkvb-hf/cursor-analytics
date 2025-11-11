"""
Tests for databricks_job_runner.py
"""
import pytest
import sys
import os
from unittest.mock import Mock, MagicMock, patch, call

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
        mock_post.return_value = mock_response
        
        result = runner.create_notebook(
            notebook_path='/Workspace/test',
            content='# Test notebook',
            overwrite=True
        )
        
        assert result is True
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert '/api/2.0/workspace/import' in call_args[1]['url']
    
    @patch('core.databricks_job_runner.requests.post')
    def test_create_notebook_failure(self, mock_post, runner):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response
        
        result = runner.create_notebook(
            notebook_path='/Workspace/test',
            content='# Test notebook'
        )
        
        assert result is False
    
    @patch('core.databricks_job_runner.requests.post')
    @patch('core.databricks_job_runner.requests.get')
    def test_create_and_run_success(self, mock_get, mock_post, runner):
        # Mock job creation
        mock_job_response = MagicMock()
        mock_job_response.status_code = 200
        mock_job_response.json.return_value = {'job_id': 123}
        
        # Mock run submission
        mock_run_response = MagicMock()
        mock_run_response.status_code = 200
        mock_run_response.json.return_value = {'run_id': 456}
        
        mock_post.side_effect = [mock_job_response, mock_run_response]
        
        result = runner.create_and_run(
            notebook_path='/Workspace/test',
            notebook_content='# Test',
            job_name='test-job'
        )
        
        assert result is not None
        assert result['job_id'] == 123
        assert result['run_id'] == 456
    
    @patch('core.databricks_job_runner.requests.get')
    def test_get_job_status(self, mock_get, runner):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'state': {'life_cycle_state': 'RUNNING'},
            'run_id': 123
        }
        mock_get.return_value = mock_response
        
        status = runner.get_job_status(123)
        
        assert status is not None
        assert status['state']['life_cycle_state'] == 'RUNNING'
        mock_get.assert_called_once()


