import os
import math
import pandas as pd

from flask import Flask, render_template, request
from flask_sockets import Sockets
from src.api.user import user
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__,
            template_folder="public",
            static_folder="public",
            static_url_path="/")

app.register_blueprint(user)


if __name__ == "__main__":
    server = WSGIServer(
        ('127.0.0.1', 3000),
        app,
        handler_class=WebSocketHandler,
    )
    print("server start ...")
    server.serve_forever()