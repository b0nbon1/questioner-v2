from flask import Flask, jsonify, json
from datetime import datetime
from databases.db_connect import init_db
import psycopg2
from psycopg2.extras import RealDictCursor


class Meetup(object):

    def __init__(self, *args):
        self.location = args[0]
        self.images = args[1]
        self.topic = args[2]
        self.happeningOn = args[3]
        self.tags = args[4]

    def create_meetup(self):
        new_meetup = {
            'location': self.location,
            'createdOn': datetime.now(),
            'images': self.images,
            'topic': self.topic,
            'happeningOn': self.happeningOn,
            "tags": self.tags,
        }
        
        try:
            query = """INSERT INTO meetups(location, createdOn, images, topic, happeningOn, tags) 
                    VALUES (%(location)s, %(createdOn)s, %(images)s, %(topic)s, %(happeningOn)s, %(tags)s) """
            con = init_db()
            cur = con.cursor()
            cur.execute(query, new_meetup)
            con.commit()
            return new_meetup
        except(Exception, psycopg2.DatabaseError) as error:
            return {'error': '{}'.format(error)}, 401

    @staticmethod
    def delete_meetup(meetup_id):
        try:
            conn = init_db()
            cursor = conn.cursor()
            # delete single record now
            sql_delete_query = """Delete from meetups where id = %s"""
            cursor.execute(sql_delete_query, (meetup_id, ))
            conn.commit()
            count = cursor.rowcount
            if count == 0:
                return jsonify({"error": "no such available meetup right now",
                                      "status": 404}), 404
            return jsonify({"data": count,
                            "message": "meetup deleted successfully "}),200
        except (Exception, psycopg2.Error) as error:
            return jsonify({'error': '{}'.format(error)}), 401

    @staticmethod
    def get_meetup():
        try:
            conn = init_db()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("select * from meetups", ())
            meetup = cur.fetchall()
            cur.close()
            conn.close()

            return meetup
        except(Exception, psycopg2.DatabaseError) as error:
            return {'error': '{}'.format(error)}, 401

    @staticmethod
    def new_rsvp(status, meetup_id, user_id):
        rsvp = {
            "user_id": user_id,
            "meetup_id": meetup_id,
            "status": status
            }

        try:
            query = """INSERT INTO rsvps (user_id, meetup_id, status)
                    VALUES (%(user_id)s, %(meetup_id)s, %(status)s) """
            con = init_db()
            cur = con.cursor()
            cur.execute(query, rsvp)
            con.commit()
            return jsonify({"message": "rsvp successfully created"}), 201
        except(Exception, psycopg2.DatabaseError) as error:
            return jsonify({'error': '{}'.format(error)}), 400
