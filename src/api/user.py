from flask import Blueprint, request
from src.db.user import *

user = Blueprint("user", __name__)


@user.route("/api/user/register", methods=["POST"])
def register():
    print(request.json)  # dict
    body = request.json
    arg_list = list(body.values())
    res = user_register(arg_list)
    return {
        "result": False if res[0] == 'UR0' else True,
        "u_id": res[0],
        "remark": res[1],
    }



@user.route("/api/user/login", methods=["POST"])
def login():
    body = request.json
    arg_list = list(body.values())
    print(arg_list)
    res = user_login(arg_list)
    return {
        "result": res[0],
        "u_id": res[1],
        "u_type": res[2],
    }
