import json


def format_event_log(timestamp, user_id, session_id, action):
    log = {
        'version': '0.1',
        'timestamp': timestamp,
        'user_id': user_id,
        'session_id': session_id,
        'action': action
    }
    return json.dumps(log)
