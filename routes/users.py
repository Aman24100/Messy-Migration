from flask import Blueprint, request, jsonify
from services.user_service import (
    list_users, get_user, create_user,
    modify_user, remove_user, search_by_name
)

bp = Blueprint("users", __name__)

@bp.route("/users", methods=["GET"])
def _list():
    return jsonify(list_users()), 200

@bp.route("/user/<int:uid>", methods=["GET"])
def _get(uid):
    try:
        return jsonify(get_user(uid)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@bp.route("/users", methods=["POST"])
def _create():
    try:
        return jsonify(create_user(request.get_json())), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/user/<int:uid>", methods=["PUT"])
def _update(uid):
    try:
        return jsonify(modify_user(uid, request.get_json())), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/user/<int:uid>", methods=["DELETE"])
def _delete(uid):
    try:
        remove_user(uid)
        return "", 204
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@bp.route("/search", methods=["GET"])
def _search():
    try:
        return jsonify(search_by_name(request.args.get("name",""))), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
