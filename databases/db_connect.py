import psycopg2
import os
from createtables import queries, tablequeries
db_url = os.getenv('DATABASE_URL')


def connect_to_db():
    """making a connection to the db"""
    try:
        conn = psycopg2.connect(db_url)
        print('databases connected')
        return conn

    except (Exception, psycopg2.Error) as error:
        print("Not unable to connect to the database", error)


def create_tables():
    """creating tables for the database"""
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        for query in queries:
            cursor.execute(query)
        conn.commit()
        print("successful created")
    except (Exception, psycopg2.Error) as error:
        print("Not unable to create tables", error)

def destroy_tables():
    """Destroying tables for the test database"""
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        for table in tablequeries:
            cursor.execute(table)
        conn.commit()
        print("successful destroyed")
    except (Exception, psycopg2.Error) as error:
        print("Not unable to destroy tables", error)
