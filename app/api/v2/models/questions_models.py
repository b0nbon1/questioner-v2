from flask import Flask, abort, jsonify, make_response, request
from datetime import datetime
import psycopg2


class Questions():
    def __init__(self, user, meetup, title, body):
        self.user = user
        self.meetup = meetup
        self.title = title
        self.body = body

    def create_question(self):
        new_question = {
            "user": self.user,
            "meetup": self.meetup,
            "title": self.title,
            "body": self.body,
        }
        try:
            query = """INSERT INTO questions(user, meetup, title, body)
                    VALUES (%(user)s, %(meetup)s, %(title)s, %(body)s) """
            con = init_db()
            cur = con.cursor()
            cur.execute(query, new_question)
            con.commit()
            return new_question
        except(Exception, psycopg2.DatabaseError) as error:
            return {'error': '{}'.format(error)}, 400

    @staticmethod
    def get_question():
        try:
            conn = init_db()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("select * from questions", ())
            questions = cur.fetchall()
            cur.close()
            conn.close()

            return questions
        except(Exception, psycopg2.DatabaseError) as error:
            return {'error': '{}'.format(error)}, 401

    @classmethod
    def add_vote(cls, question_id, user):
        try:
            conn = init_db()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("select * from votes", ())
            votes = cur.fetchall()
            cur.close()
            conn.close()
        except(Exception, psycopg2.DatabaseError) as error:
            return {'error': '{}'.format(error)}, 401

        if len(votes) == 0:
            cls.vote(user, question_id)
        else:
            vote_question = [v for v in votes if v['question_id'] == question_id]
            if len(v) == 0:
               
                return votes

    @staticmethod
    def vote(user, question_id):
        new_vote = {
                "user": user,
                "question_id": question_id,
                "upvotes": 0,
                "downvotes": 0
            }

        try:
            query = """INSERT INTO votes(user, question_id, upvotes, downvotes)
                    VALUES (%(user)s, %(question_id)s, %(upvotes)s, %(downvotes)s) """
            con = init_db()
            cur = con.cursor()
            cur.execute(query, new_vote)
            con.commit()
            return new_question
        except(Exception, psycopg2.DatabaseError) as error:
            return {'error': '{}'.format(error)}, 400
