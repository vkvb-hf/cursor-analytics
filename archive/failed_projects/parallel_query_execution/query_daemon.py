#!/usr/bin/env python3
"""
Query Daemon - Persistent service that runs queries in background

This daemon runs continuously and processes query requests from files.
You start it once, and it keeps running. I can submit queries by writing to files.

Usage:
    # Start the daemon (run this once, it keeps running)
    python query_daemon.py start
    
    # Stop the daemon
    python query_daemon.py stop
    
    # Check status
    python query_daemon.py status
"""
import sys
import os
import json
import time
import signal
import atexit
from pathlib import Path
from datetime import datetime
from threading import Thread
import subprocess

# Add path
sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

# Daemon directories
DAEMON_DIR = Path('/tmp/databricks_query_daemon')
DAEMON_DIR.mkdir(exist_ok=True)
PID_FILE = DAEMON_DIR / 'daemon.pid'
REQUEST_DIR = DAEMON_DIR / 'requests'
RESULT_DIR = DAEMON_DIR / 'results'
STATUS_FILE = DAEMON_DIR / 'status.json'
REQUEST_DIR.mkdir(exist_ok=True)
RESULT_DIR.mkdir(exist_ok=True)

from parallel.agent_background_api import get_api


class QueryDaemon:
    """Daemon that processes query requests"""
    
    def __init__(self):
        self.running = False
        self.api = get_api()
        self.processor_thread = None
    
    def start(self):
        """Start the daemon"""
        if self.is_running():
            print("Daemon is already running!")
            return
        
        # Fork to background
        try:
            pid = os.fork()
            if pid > 0:
                # Parent - exit immediately
                print(f"Daemon started with PID {pid}")
                PID_FILE.write_text(str(pid))
                sys.exit(0)
        except OSError as e:
            print(f"Fork failed: {e}")
            sys.exit(1)
        
        # Child process continues
        os.setsid()
        os.umask(0)
        
        # Second fork
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            print(f"Second fork failed: {e}")
            sys.exit(1)
        
        # Daemon process
        self.running = True
        self.write_status({'status': 'running', 'started_at': datetime.now().isoformat()})
        
        # Register cleanup
        atexit.register(self.cleanup)
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
        
        # Start processor thread
        self.processor_thread = Thread(target=self.process_requests, daemon=False)
        self.processor_thread.start()
        
        # Keep running
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
    
    def process_requests(self):
        """Process query requests from files"""
        while self.running:
            # Check for new request files
            for request_file in REQUEST_DIR.glob('*.json'):
                try:
                    with open(request_file, 'r') as f:
                        request = json.load(f)
                    
                    query_id = request.get('query_id')
                    query = request.get('query')
                    metadata = request.get('metadata', {})
                    
                    # Submit query
                    self.api.submit_queries([query], [query_id], metadata=[metadata])
                    
                    # Move request to processing
                    request_file.unlink()
                    
                    print(f"[Daemon] Submitted query: {query_id}")
                    
                    # Monitor this query and write result when done
                    # Use daemon=False so thread continues after main thread
                    monitor_thread = Thread(target=self.monitor_query, args=(query_id,), daemon=False)
                    monitor_thread.start()
                    
                except Exception as e:
                    print(f"[Daemon] Error processing {request_file}: {e}")
                    request_file.unlink()
            
            # Update status
            status = self.api.get_status()
            self.write_status({
                'status': 'running',
                'queries': status,
                'last_check': datetime.now().isoformat()
            })
            
            time.sleep(0.5)  # Check every 500ms
    
    def monitor_query(self, query_id):
        """Monitor a query and write result when complete"""
        import time
        from parallel.query_tracker import QueryStatus
        
        max_wait = 300  # Wait up to 5 minutes
        waited = 0
        
        while self.running and waited < max_wait:
            try:
                query_info = self.api.get_tracker().get_query(query_id)
                
                if query_info is None:
                    time.sleep(0.5)
                    waited += 0.5
                    continue
            
            if query_info.status == QueryStatus.COMPLETED:
                # Write result to file
                result_file = RESULT_DIR / f"{query_id}.json"
                result_data = {
                    'query_id': query_id,
                    'status': 'completed',
                    'result_count': query_info.result_count,
                    'duration_seconds': query_info.duration_seconds,
                    'completed_at': query_info.end_time.isoformat() if query_info.end_time else None,
                    'result': [
                        dict(row) if hasattr(row, '_asdict') else 
                        {f'col_{i}': val for i, val in enumerate(row)} if isinstance(row, (list, tuple)) else
                        str(row)
                        for row in (query_info.result or [])
                    ] if query_info.result else []
                }
                
                with open(result_file, 'w') as f:
                    json.dump(result_data, f, indent=2, default=str)
                
                # Create notification for agent
                try:
                    from parallel.notify_agent import create_notification
                    create_notification(query_id, 'completed', f'Query completed with {query_info.result_count} rows')
                except:
                    pass
                
                print(f"[Daemon] Query {query_id} completed, result written")
                break
            
            elif query_info.status == QueryStatus.FAILED:
                # Write error to file
                result_file = RESULT_DIR / f"{query_id}.json"
                result_data = {
                    'query_id': query_id,
                    'status': 'failed',
                    'error': query_info.error,
                    'failed_at': query_info.end_time.isoformat() if query_info.end_time else None
                }
                
                with open(result_file, 'w') as f:
                    json.dump(result_data, f, indent=2)
                
                print(f"[Daemon] Query {query_id} failed: {query_info.error}")
                break
            
            time.sleep(1)  # Check every second
            waited += 1
        except Exception as e:
            print(f"[Daemon] Error monitoring {query_id}: {e}")
            import traceback
            traceback.print_exc()
            break
    
    def write_status(self, status):
        """Write status to file"""
        with open(STATUS_FILE, 'w') as f:
            json.dump(status, f, indent=2)
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        self.stop()
    
    def stop(self):
        """Stop the daemon"""
        self.running = False
        self.write_status({'status': 'stopped'})
        if PID_FILE.exists():
            PID_FILE.unlink()
        sys.exit(0)
    
    def cleanup(self):
        """Cleanup on exit"""
        if PID_FILE.exists():
            PID_FILE.unlink()
    
    def is_running(self):
        """Check if daemon is running"""
        if not PID_FILE.exists():
            return False
        
        try:
            pid = int(PID_FILE.read_text())
            os.kill(pid, 0)  # Check if process exists
            return True
        except (OSError, ValueError):
            PID_FILE.unlink()
            return False


def submit_query_to_daemon(query, query_id, metadata=None):
    """Submit a query to the daemon (non-blocking file write)"""
    request_file = REQUEST_DIR / f"{query_id}_{int(time.time())}.json"
    
    request = {
        'query_id': query_id,
        'query': query,
        'metadata': metadata or {},
        'submitted_at': datetime.now().isoformat()
    }
    
    with open(request_file, 'w') as f:
        json.dump(request, f)
    
    return query_id


def get_daemon_status():
    """Get daemon status"""
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            return json.load(f)
    return {'status': 'unknown'}


def main():
    daemon = QueryDaemon()
    
    if len(sys.argv) < 2:
        print("Usage: python query_daemon.py [start|stop|status|submit]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'start':
        daemon.start()
    elif command == 'stop':
        if daemon.is_running():
            pid = int(PID_FILE.read_text())
            os.kill(pid, signal.SIGTERM)
            print("Daemon stopped")
        else:
            print("Daemon is not running")
    elif command == 'status':
        if daemon.is_running():
            status = get_daemon_status()
            print(json.dumps(status, indent=2))
        else:
            print("Daemon is not running")
    elif command == 'submit':
        # For testing - submit a query
        query1 = "SELECT 1"
        submit_query_to_daemon(query1, "test_query")
        print("Query submitted to daemon")
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()

