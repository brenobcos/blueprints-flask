from flask import Blueprint

from app.controllers.order_controller import get_orders, get_orders_by

bp = Blueprint("orders", __name__, url_prefix="/orders")

bp.get("")(get_orders)
bp.get("/<order_id>")(get_orders_by)
