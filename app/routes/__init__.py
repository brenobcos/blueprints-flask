from flask import Flask

from .user_route import bp as bp_users
from .product_route import bp as bp_products


def init_app(app: Flask):
    # product_route(app)
    # user_route(app)

    app.register_blueprint(bp_users)
    app.register_blueprint(bp_products)
