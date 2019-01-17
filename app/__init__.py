import os
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify, make_response
from config import app_config
from databases.db_connect import init_db, create_tables, destroy_tables


def create_app(config_name):
    # initialize the app and configures it
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config['JWT_SECRET_KEY'] = 'yjfhrtht'
    jwt = JWTManager(app)
    init_db(config_name=config_name)
    destroy_tables()
    create_tables()

    from .api.v2.views.auth import auth
    app.register_blueprint(auth)

    # factory set app

    @app.route('/')
    def hello():
        return make_response(jsonify({"message": "hello, world!"})), 200
    return app
