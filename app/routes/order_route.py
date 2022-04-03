from flask import Blueprint

from app.controllers.order_controller import get_orders

bp = Blueprint("orders", __name__, url_prefix="/orders")

bp.get('')(get_orders)