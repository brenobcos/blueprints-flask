from flask import Flask
from .product_route import product_route
from .user_route import user_route

from .user_route import bp as bp_users


def init_app(app: Flask):
    product_route(app)
    user_route(app)

    app.register_blueprint(bp_users)  

    # 20min
