from flask import Blueprint

from app.controllers.product_controller import get_products

bp = Blueprint("products", __name__, url_prefix="/api")

# def product_route(app: Flask):
#     @app.get("/products")
#     def retrieve():
#         return get_products()

bp.get("/products")(get_products)