from werkzeug.security import generate_password_hash

users_table = ''' CREATE TABLE IF NOT EXISTS users (
                id serial PRIMARY KEY,
                firstname VARCHAR (30) NOT NULL,
                lastname VARCHAR (30) NOT NULL,
                othername VARCHAR (30) NOT NULL,
                username VARCHAR (30) NOT NULL,
                registered TIMESTAMP,
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
        createdOn TIMESTAMP
        );
         '''

rsvps = ''' CREATE TABLE IF NOT EXISTS rsvps (
    id serial PRIMARY KEY,
    user_id integer REFERENCES users(id),
    meetup_id integer REFERENCES meetups(id),
    status VARCHAR (10) NOT NULL
    );
    '''

queries = [users_table, admin, meetup, rsvps]

"""Destroying tables for the test database"""
table_users = ''' DROP TABLE IF EXISTS users CASCADE '''
table_meetups = ''' DROP TABLE IF EXISTS meetups CASCADE '''
table_rsvps = ''' DROP TABLE IF EXISTS rsvps CASCADE '''
tablequeries = [table_users, table_meetups, table_rsvps]
