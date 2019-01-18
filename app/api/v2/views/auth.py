from flask import Flask, abort, jsonify, make_response, request, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_access_token
from app.api.v2.models.users_models import User
from ..utils.validators import validators


auth = Blueprint('auth2', __name__, url_prefix='/api/v2/auth')


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    try:  
        username = data['username']
        firstname = data['firstname']
        lastname = data['lastname']
        othername = data['othername']
        PhoneNumber = data['PhoneNumber']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
    except:
        return make_response(jsonify({"error": "Please provide a json data",
                                      "status": 400}), 400)

    '''validations'''
    fields = [username, firstname, lastname, othername,
              PhoneNumber, email, password, confirm_password]
    for fields in fields:
        if not fields:
            return make_response(jsonify({"error": "all fields required"}), 400)

    validator = validators(username, email, password)
    check_username = validator.validate_username()
    username_exist = validator.username_exists()
    email_exist = validator.email_exists()
    check_email = validator.valid_email()
    check_password = validator.validate_password()

    if username_exist is True:
        return make_response(jsonify({"error": "username exists",
                                      "status": 409}), 409)

    if email_exist is True:
        return make_response(jsonify({"error": "email exists",
                                      "status": 409}), 409)

    if check_username is False:
        return make_response(jsonify({"error": "invalid username"}), 400)

    if check_email is False:
        return make_response(jsonify({"error": "invalid email",
                                      "status": 400}), 400)

    if not check_password:
        return make_response(jsonify({"error": "invalid password"})), 400

    if password == confirm_password:
        '''Add user to the data structure'''
        password = generate_password_hash(password)
        new_user = User(firstname, lastname, othername,
                        PhoneNumber, username, email, password)
        new_user.register_user()
        reg_user = User.get_user(username)
        public_id = reg_user[1]
        access_token = create_access_token(identity=public_id)
        return make_response(jsonify({"message": "user successfull registered!",
                                      "token": access_token,
                                      "status": 201})), 201
    else:
        return make_response(
            jsonify({"error": "Passwords don't match"})), 400
