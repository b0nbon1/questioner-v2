import os
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify, make_response
from config import app_config
from databases.db_connect import init_db, create_tables, destroy_tables


def create_app(config_name):
    '''initialize the app and configures it'''
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config['JWT_SECRET_KEY'] = 'yjfhrtht'
    jwt = JWTManager(app)
    init_db(config_name)
    destroy_tables()
    create_tables()

    from .api.v2.views.auth import auth
    app.register_blueprint(auth)

    from .api.v2.views.meetup import meetup
    app.register_blueprint(meetup)

    # factory set app

    @app.route('/')
    def hello():
        return make_response(jsonify({"message": "hello, world!"})), 200

    '''error handlers for main page'''
    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({'error': 'Url not found. Check your url and try again', 'status': 404}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({'error': 'Method not allowed', 'status': 405}), 405

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad request. Check the syntax', 'status': 400}), 400

    return app
