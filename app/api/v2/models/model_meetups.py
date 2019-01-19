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
