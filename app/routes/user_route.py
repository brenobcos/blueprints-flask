from flask import Flask, Blueprint

bp = Blueprint("users", __name__, url_prefix="/api")


def user_route(app: Flask):
    # @app.get("/users")
    # def retrieve():
    #     return {"msg": "rota busca de usuários"}

        @bp.get("/users")
        def retrieve():
            return {"msg": "rota busca de usuários"}
