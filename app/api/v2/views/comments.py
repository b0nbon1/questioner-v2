from flask import Flask, jsonify, make_response, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.comments_model import Comment
from ..models.users_models import User

comment = Blueprint('comments', __name__, url_prefix='/api/v2/comments')

@comment.route('/', methods=['POST'])
@jwt_required
def ask_question():
    user = get_jwt_identity()
    data = request.get_json()
    try:
        body = data["body"]
    except:
        return jsonify({"error": "enter json data"}, 400)

    comments = Questions(user, body)
    add_comment = comments.create_comment()
    return make_response(jsonify({"data": add_comment,
                                    "message": "question successful created!",
                                    "status": 201})), 201


