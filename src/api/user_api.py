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


@user.route("/api/user/info", methods=["GET"])
def userPerInfo():
    arg = request.args.get("u_id")
    # print(request.args)
    print(arg)
    res = user_info(arg)
    return {
        "result": res[0],
        "u_name": res[1],
        "u_type": res[2],
        "r_name": res[3],
        "c_type": res[4],
        "c_num": res[5],
        "p_num": res[6],
        "u_level": res[7],
        "u_idct": res[8],
        "r_city": res[9],
        "r_cmty": res[10],
        "r_time": res[11],
        "m_time": res[12],
    }


@user.route("/api/user/modify", methods=["POST"])
def userPerInfoModify():
    body = request.json
    arg_list = list(body.values())
    print(arg_list)
    return {
        'result': True if user_info_modify(arg_list) else False
    }