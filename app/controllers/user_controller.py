from flask import jsonify
from app.models.user_model import User


def get_users():
    users = User.read_users()

    user_columns = [
        "_id",
        "email",
        "birthdate",
        "children",
        "married",
        "account_balance",
    ]

    serialized_users = [dict(zip(user_columns, user)) for user in users]

    return jsonify(serialized_users)
