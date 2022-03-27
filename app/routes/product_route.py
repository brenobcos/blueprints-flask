from flask import Flask

def product_route(app: Flask):
    @app.get("/products")
    def retrieve():
        return {"msg": "rota busca de produtos"}