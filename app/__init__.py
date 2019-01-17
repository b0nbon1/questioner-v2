import os
from flask import Flask, jsonify, make_response
from config import app_config


def create_app(config_name):
    # initialize the app and configures it
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # factory set app

    @app.route('/')
    def hello():
        return make_response(jsonify({"message": "hello, world!"})), 200
    return app
