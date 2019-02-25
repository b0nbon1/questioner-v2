from flask import Flask, abort, jsonify, make_response, request
from datetime import datetime
from databases.db_connect import init_db
import psycopg2
from psycopg2.extras import RealDictCursor


class Comment(object):
    def __init__(self, user, body):
        self.user = user
        self.body = body

    def create_comment():
        new_comment = {
            "user": self.user,
            "body": self.body
        }
        try:
            query = """INSERT INTO questions(user, body)
                    VALUES (%(user)s, %(body)s) """
            con = init_db()
            cur = con.cursor()
            cur.execute(query, new_comment)
            con.commit()
            return new_question
        except(Exception, psycopg2.DatabaseError) as error:
            return {'error': '{}'.format(error)}, 400
        