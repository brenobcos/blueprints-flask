from flask import Blueprint

from app.controllers.user_controller import get_users

bp = Blueprint("users", __name__, url_prefix="/api")


# def user_route(app: Flask):
#     # @app.get("/users")
#     # def retrieve():
#     #     return {"msg": "rota busca de usuários"}
#     ...

# @bp.get("/users")
# def retrieve():
#     return get_users()

bp.get("/users")(get_users)


