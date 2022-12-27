from functools import wraps
from UTILS.auth import decode_auth_token
from flask import request, render_template, redirect

def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            pass
            #return A valid token is missing!, 401
        try:
            data = decode_auth_token(token)
            # query database lay thong tin user
        except: 
            pass
            # return Invalid token! 401
        return f(data, *args, **kwargs)
    return decorator