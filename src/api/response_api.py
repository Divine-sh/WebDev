from flask import Blueprint, request
from src.db.response import *

rsp = Blueprint("rsp", __name__)


@rsp.route("/api/user/request/response_info", methods=["GET"])
def requestRspInfo():
    arg = request.args.get("req_id")
    print(arg)
    res = user_request_response_info(arg)
    keys = [
        "rsp_id",
        "req_id",
        "rsp_uid",
        "rsp_idct",
        "rsp_time",
        "rsp_status",
    ]
    return {
        "result": False if not res[0] else True,
        "info_arr": None if not res[0] else dict(zip(range(len(res[1])), [dict(zip(keys, i)) for i in res[1]])),
    }


@rsp.route("/api/user/request/opt_response", methods=["POST"])
def requestOptResponse():
