from flask import Flask, abort, jsonify
from databases.db_connect import init_db
import psycopg2
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import uuid


class User(object):

    def __init__(self, *args):
        self.firstname = args[0]
        self.lastname = args[1]
        self.othername = args[2]
        self.PhoneNumber = args[3]
        self.username = args[4]
        self.email = args[5]
        self.password = args[6]
        self.db = init_db()

    def register_user(self):
        new_user = {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'othername': self.othername,
            'PhoneNumber': self.PhoneNumber,
            'isAdmin': False,
            "username": self.username,
            'registered': datetime.now(),
            "email": self.email,
            "password": self.password
        }
        try:
            query = """INSERT INTO USERS(firstname, lastname, othername, PhoneNumber, isAdmin, registered, username, email, password) 
                    VALUES (%(firstname)s, %(lastname)s, %(othername)s, %(PhoneNumber)s, %(isAdmin)s,%(registered)s, %(username)s, %(email)s,%(password)s) """
            cur = self.db.cursor()
            cur.execute(query, new_user)
            self.db.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
            return {"message": "Not able to insert in users table"}, 400

    @staticmethod
    def get_user(username):
        try:
            conn = init_db()
            cur = conn.cursor()
            cur.execute("select * from users where username = %s", ([username]))
            user = cur.fetchone()
            cur.close()
            conn.close()
            if user:
                return user
        except(Exception, psycopg2.DatabaseError) as error:
            return {'error': '{}'.format(error)}, 401
