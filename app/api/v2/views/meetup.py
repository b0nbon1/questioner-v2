from flask import Flask, jsonify, make_response, request, Blueprint
from ..models.model_meetups import Meetup
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.validators import validators


meetup = Blueprint('meetup', __name__, url_prefix='/api/v2/meetup')


# create a meetup
@meetup.route('/', methods=['POST'])
@jwt_required
def create():
    userid = get_jwt_identity()
    if userid != 1:
        return make_response(jsonify({
            "error": "Cannot perform this operation",
            "status": 401}), 401)
    try:
        data = request.get_json()
        location = data['location']
        images = data['images']
        topic = data['topic']
        happeningOn = data['happeningOn']
        tags = data['tags']
    

        fields = [location, topic, happeningOn]
        for field in fields:
            if not field.strip():
                return make_response(jsonify({"error": "all fields required"}), 400)
    except:
        return make_response(jsonify({"error": "Please provide a json data",
                                      "status": 400}), 400)
    new_meetup = Meetup(location, images, topic, happeningOn, tags)
    add_meetup = new_meetup.create_meetup()

    return make_response(jsonify({"data": add_meetup,
                                    "message": "meetup successful created!",
                                    "status": 201})), 201

@meetup.route('/upcoming', methods=['GET'])
@jwt_required
def get_upcoming():
    meetups = Meetup.get_meetup()
    upcoming_meetups = meetups[::-1]
    if not upcoming_meetups:
        return make_response(jsonify({"message": "no available meetups right now",
                                      "status": 404})), 404
    return make_response(jsonify({"status": 200},
                                 {"data": upcoming_meetups})), 200


# get specific meetup
@meetup.route('/<int:meetup_id>', methods=['GET'])
@jwt_required
def get_meetup(meetup_id):
    meetups = Meetup.get_meetup()
    meetup = [
            meetup for meetup in meetups if meetup['id'] == meetup_id]
    if len(meetup) == 0:
        return make_response(jsonify({"error": "no such available meetup right now",
                                      "status": 404})), 404
    return make_response(jsonify({"status": 200},
                                 {"data": meetup})), 200


@meetup.route('/<int:meetup_id>', methods=['DELETE'])
@jwt_required
def delete_question(meetup_id):

    return Meetup.delete_meetup(meetup_id)


@meetup.route('/<int:meetup_id>/rsvps', methods=['POST'])
@jwt_required
def create_rsvp(meetup_id):
    userid = get_jwt_identity()
    meetups = Meetup.get_meetup()
    meetup = [
            meetup for meetup in meetups if meetup['id'] == meetup_id]
    if len(meetup) == 0:
        return make_response(jsonify(
            {
                "status": 404,
                "error": "error can't find meetup data"
            })), 404
    data = request.get_json()
    status = data['status']
    status = status.lower()
    if status == 'yes' or status == 'maybe' or status == 'no':

        return Meetup.new_rsvp(status, meetup_id, userid)

    else:
        return make_response(jsonify(
            {
                "status": 406,
                "error": "there is no such status"
            })), 406