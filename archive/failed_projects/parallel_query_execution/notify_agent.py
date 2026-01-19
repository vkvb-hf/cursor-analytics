#!/usr/bin/env python3
"""
Notify Agent - Trigger agent/chat when queries complete

This creates a notification file that can trigger the agent to check results.
"""
import json
import time
from pathlib import Path
from datetime import datetime

NOTIFICATION_DIR = Path('/tmp/databricks_query_notifications')
NOTIFICATION_DIR.mkdir(exist_ok=True)

def create_notification(query_id, status, message=None):
    """Create a notification file for the agent"""
    notification_file = NOTIFICATION_DIR / f"{query_id}_{int(time.time())}.json"
    
    notification = {
        'query_id': query_id,
        'status': status,  # 'completed', 'failed', etc.
        'message': message,
        'timestamp': datetime.now().isoformat()
    }
    
    with open(notification_file, 'w') as f:
        json.dump(notification, f, indent=2)
    
    return str(notification_file)

def check_notifications():
    """Check for pending notifications"""
    notifications = []
    for notif_file in NOTIFICATION_DIR.glob('*.json'):
        with open(notif_file, 'r') as f:
            notifications.append(json.load(f))
        notif_file.unlink()  # Remove after reading
    return notifications

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        query_id = sys.argv[1]
        status = sys.argv[2] if len(sys.argv) > 2 else 'completed'
        create_notification(query_id, status)
        print(f"Notification created for {query_id}: {status}")
    else:
        # Check for notifications
        notifs = check_notifications()
        if notifs:
            print(json.dumps(notifs, indent=2))
        else:
            print("No notifications")

