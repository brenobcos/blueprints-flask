from flask import Blueprint

from app.controllers.user_controller import get_users, get_user_by_id, add_user, update_user

bp = Blueprint("users", __name__, url_prefix="/users")

bp.get("")(get_users)
bp.post("")(add_user)
bp.get("/<user_id>")(get_user_by_id)
bp.patch("/<user_id>")(update_user)



