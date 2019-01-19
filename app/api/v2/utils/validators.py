import re
import psycopg2
from flask import jsonify
from databases.db_connect import init_db


class validators():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def valid_email(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return False

    def validate_password(self):
        if len(self.password) >= 6 and len(self.password) <= 16:
            return True

    def validate_username(self):
        if not len(self.username) >= 3:
            return False

    def username_exists(self):
        try:
            conn = init_db()
            cur = con.cursor()
            cur.execute("select * from users where username = %s", ([self.username]))
            username = cur.fetchone()
            cur.close()
            conn.close()
            if username:
                return True

        except(Exception, psycopg2.DatabaseError) as error:
            return jsonify({'error': '{}'.format(error)}), 401

    def email_exists(self):
        try:
            conn = init_db()
            cur = conn.cursor()
            cur.execute("select * from users where email = %s", ([self.email]))
            email = cur.fetchone()
            cur.close()
            conn.close()
            if email:
                return True
        except(Exception, psycopg2.DatabaseError) as error:
            return jsonify({'error': '{}'.format(error)}), 401

    
