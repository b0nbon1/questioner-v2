import psycopg2
import os
from .createtables import queries, tablequeries


def init_db(config_name=None):
    try:
        """Creates Database development Connection"""
        if config_name == "development":
        # url = app_config[config_name].DATABASE_URL
            url = os.getenv('DATABASE_URL')
            conn = psycopg2.connect(url)
            print('databases connected')
            conn.autocommit = True
            return conn
        else:
            """Creates Database testing Connection"""
            url = os.getenv('DATABASE_URL_TEST')
            conn = psycopg2.connect(url)
            # print('testing databases connected')
            conn.autocommit = True
            return conn
    except (Exception, psycopg2.Error) as error:
        print("Not able to connect to the database", error)


# def connect_to_db():
#     """making a connection to the db"""
#     try:
#         conn = psycopg2.connect(db_url)
#         print('databases connected')
#         return conn

#     except (Exception, psycopg2.Error) as error:
#         print("Not unable to connect to the database", error)


def create_tables():
    """creating tables for the database"""
    try:
        conn = init_db()
        cursor = conn.cursor()
        for query in queries:
            cursor.execute(query)
        conn.commit()
        print("successful created")
    except (Exception, psycopg2.Error) as error:
        print("Not able to create tables", error)


def destroy_tables():
    """Destroying tables for the test database"""
    try:
        conn = init_db()
        cursor = conn.cursor()
        for table in tablequeries:
            cursor.execute(table)
        conn.commit()
        print("successful destroyed")
    except (Exception, psycopg2.Error) as error:
        print("Not able to destroy tables", error)
