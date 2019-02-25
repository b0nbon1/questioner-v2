from werkzeug.security import generate_password_hash

user = ''' CREATE TABLE IF NOT EXISTS users (
                id serial PRIMARY KEY,
                firstname VARCHAR (30) NOT NULL,
                lastname VARCHAR (30) NOT NULL,
                othername VARCHAR (30) NOT NULL,
                username VARCHAR (30) NOT NULL,
                registered TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC'),
                email VARCHAR (30) UNIQUE NOT NULL,
                PhoneNumber VARCHAR NOT NULL,
                isAdmin BOOLEAN NOT NULL DEFAULT FALSE,
                password VARCHAR (200) NOT NULL
                
            );
            '''

password = generate_password_hash('admintest')
admin = """
        INSERT INTO users(firstname, lastname, othername, username, email, PhoneNumber, isAdmin, password) VALUES(
            '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'
        )""".format('new', 'ad', 'min', 'testx', 'admintestx@test.com', '80686995', True, password)

meetup = ''' CREATE TABLE IF NOT EXISTS meetups (
        id serial PRIMARY KEY,
        location  VARCHAR (50) NOT NULL,
        images  TEXT,
        topic   VARCHAR (50) NOT NULL,
        happeningOn VARCHAR(30) NOT NULL,
        tags VARCHAR(20),
        createdOn TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC')
        );
         '''

rsvp = ''' CREATE TABLE IF NOT EXISTS rsvps (
    id serial PRIMARY KEY,
    user_id integer REFERENCES users(id) ON DELETE CASCADE,
    meetup_id integer REFERENCES meetups(id) ON DELETE CASCADE,
    status VARCHAR (10) NOT NULL
    );
    '''

question = ''' CREATE TABLE IF NOT EXISTS questions(
                id serial PRIMARY KEY,
                user_id integer REFERENCES users(id) ON DELETE CASCADE,
                meeetup integer REFERENCES meetups(id) ON DELETE CASCADE,
                title VARCHAR (50) NOT NULL,
                body VARCHAR (500) NOT NULL
    );
'''

comment = '''CREATE TABLE IF NOT EXISTS comments(
            id serial PRIMARY KEY,
            user_id integer REFERENCES users(id) ON DELETE CASCADE,
            question_id integer REFERENCES questions(id) ON DELETE CASCADE,
            comment VARCHAR (30) NOT NULL
    );
'''
vote = '''CREATE TABLE IF NOT EXISTS votes(
            id serial PRIMARY KEY,
            user_id integer REFERENCES users(id) ON DELETE CASCADE,
            question_id integer REFERENCES questions(id) ON DELETE CASCADE,
            downvote integer,
            upvote integer
    );
    '''
queries = [user, meetup, rsvp, question, comment, vote, admin]

"""Destroying tables for the test database"""
table_users = ''' DROP TABLE IF EXISTS users CASCADE '''
table_meetups = ''' DROP TABLE IF EXISTS meetups CASCADE '''
table_rsvps = ''' DROP TABLE IF EXISTS rsvps CASCADE '''
table_questions = ''' DROP TABLE IF EXISTS questions CASCADE '''
table_comments = '''DROP TABLE IF EXISTS comments CASCADE'''
table_votes = '''DROP TABLE IF EXISTS votes CASCADE'''
tablequeries = [table_users, table_meetups, table_rsvps, table_questions, table_comments, table_votes]
