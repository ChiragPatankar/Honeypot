import json
from datetime import datetime

def log_event(website, event):
    log_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "website": website,
        "event": event
    }
    log_file = f"logs/{website}_logs.json"
    try:
        with open(log_file, "a") as file:
            file.write(json.dumps(log_data) + "\n")
    except Exception as e:
        print(f"Error logging event: {e}")
