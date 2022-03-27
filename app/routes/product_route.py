from flask import Blueprint

from app.controllers.product_controller import get_products

bp = Blueprint("products", __name__, url_prefix="/products")

bp.get("")(get_products)