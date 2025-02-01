# api/index.py

from sol import app  # Import your Flask app from sol.py
from vercel_wsgi import handle_request

def handler(event, context):
    """
    This function is the entry point for Vercel.
    It adapts the Flask WSGI app to Vercel's serverless interface.
    """
    return handle_request(app, event, context)
