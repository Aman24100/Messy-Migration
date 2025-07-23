from flask import Blueprint, request, jsonify
from services.user_service import login_user

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["POST"])
def _login():
    try:
        uid = login_user(request.get_json())
        return jsonify({"status":"success","user_id":uid}), 200
    except ValueError as e:
        return jsonify({"status":"failed","error":str(e)}), 401
