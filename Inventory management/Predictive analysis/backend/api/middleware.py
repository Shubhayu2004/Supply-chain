from functools import wraps
from flask import jsonify

def handle_errors(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e),
                'error_type': e.__class__.__name__
            }), 400
    return wrapper