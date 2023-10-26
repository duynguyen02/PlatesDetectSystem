from flask import Blueprint, request, jsonify

from routes.jwt_auth import token_required
from app_utils import *
from service import get_user_by_id, update_user
from module import jwt_service
from sercurity import verify, encrypt

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()

    user = get_user_by_id(request_data['username'])
    if user:
        if (verify(
                request_data['password'],
                user[0].get('password')
        )):
            token = jwt_service.create_token(request_data['username'])

            return jsonify({
                "status": OK,
                "message": "Đăng Nhập Thành Công!",
                "data": token.__dict__
            })

    return jsonify({
        "status": UNAUTHORIZED,
        "message": "Tên đăng nhập hoặc mật khẩu không đúng!"
    }), UNAUTHORIZED


@auth_bp.route('/change_password', methods=['POST'])
@token_required
def change_password(username):

    request_data = request.get_json()

    update_user(
        username,
        encrypt(request_data['password'])
    )

    return jsonify(
        {
            "status": OK,
            "message": "Đổi Mật Khẩu Thành Công!"
        }
    ), OK
