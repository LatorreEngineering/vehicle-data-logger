import datetime

def timestamp():
    """Returns the current UTC timestamp as a string."""
    return datetime.datetime.utcnow().isoformat()
