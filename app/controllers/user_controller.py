from http import HTTPStatus
from flask import jsonify, request
from app.models.user_model import User
from psycopg2.errors import UniqueViolation


def get_users():
    users = User.select_all()

    # serialized_users = [User.serialize(user) for user in users]

    # return jsonify(serialized_users)
    return jsonify(users)


def get_user_by_id():
    return {"msg": "get_user_by_id"}


def add_user():
    data = request.get_json()

    user = User(**data)

    try:
        # inserted_user = user.create_user()
        inserted_user = user.insert_into()
    except UniqueViolation:
        return {'error': 'email already in use'}, HTTPStatus.UNPROCESSABLE_ENTITY

    serialized_user = User.serialize(inserted_user)

    return serialized_user, HTTPStatus.CREATED

def update_user(user_id:str):
    data = request.get_json()

    update_user = User.update_user(user_id, data)

    if not update_user:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND

    serialized_user = User.serialize(update_user)

    return serialized_user, HTTPStatus.OK
