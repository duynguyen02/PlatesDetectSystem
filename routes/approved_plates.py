from routes.jwt_auth import token_required
from app_utils.status_code import *
from flask import Blueprint, request, jsonify
from service import get_all_approved_plates, add_approved_plate

plate_bp = Blueprint('approved_plates', __name__)


@plate_bp.route('/', methods=['GET'])
@token_required
def get_approved_plates(username):
    return jsonify(
        {
            "status": OK,
            "message": "Yêu Cầu Dữ Liệu Thành Công!",
            "data": get_all_approved_plates()
        }
    ), OK


@plate_bp.route('/', methods=['POST'])
@token_required
def add_approved_plates(username):

    request_data = request.get_json()

    add_approved_plate(
        request_data['plate']
    )

    return jsonify(
        {
            "status": CREATE,
            "message": "Thêm Biển Số Thành Công!"
        }
    ), CREATE

