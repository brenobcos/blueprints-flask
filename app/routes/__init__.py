from flask import Flask, Blueprint

from .user_route import bp as bp_users
from .product_route import bp as bp_products

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_users)
    bp_api.register_blueprint(bp_products)

    app.register_blueprint(bp_api)
