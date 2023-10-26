from functools import wraps
from flask import request, jsonify
from module import jwt_service
from app_utils.status_code import *


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({
                "status": UNAUTHORIZED,
                "message": "Không có token được cung cấp!"
            }), UNAUTHORIZED

        token = token.split('Bearer ')[1]
        username = jwt_service.verify_access_token(token)

        if not username:
            return jsonify({
                "status": UNAUTHORIZED,
                "message": "Access token không hợp lệ. Vui lòng đăng nhập lại."
            }), UNAUTHORIZED

        kwargs['username'] = username
        return f(*args, **kwargs)

    return decorated
