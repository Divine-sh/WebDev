from flask import Blueprint, request
from src.db.user import *

user = Blueprint("user", __name__)


@user.route("/api/user/register", methods=["POST"])
def register():

    return {
        "success":
            True if user_signin(request.form["username"],
                                request.form["password"], 2) else False
    }


@user.route("/api/user/login", methods=["POST"])
def login():
    print(request.json)  # dict
    body = request.json
    arg_list = []
    arg_list.append(body['u_name'])
    arg_list.append(body['u_pwd'])
    res = user_login(arg_list)
    if not res:
        return {
            "result": False,
            "u_id": None,
            "u_type": None,
        }
    else:
        return {
            "result": True,
            "u_id": res[0],
            "u_type": res[1],
        }