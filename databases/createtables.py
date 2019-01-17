users_table = ''' CREATE TABLE IF NOT EXISTS users (
                id serial PRIMARY KEY,
                public_id VARCHAR (100),
                firstname VARCHAR (30) NOT NULL,
                lastname VARCHAR (30) NOT NULL,
                othername VARCHAR (30) NOT NULL,
                username VARCHAR (30) UNIQUE NOT NULL,
                registered DATE NOT NULL,
                email VARCHAR (30) UNIQUE NOT NULL,
                PhoneNumber VARCHAR NOT NULL,
                isAdmin BOOLEAN NOT NULL DEFAULT FALSE,
                password VARCHAR (200) NOT NULL
                
            );
            '''

queries = [users_table]

"""Destroying tables for the test database"""
table_users = ''' DROP TABLE IF EXISTS users CASCADE '''
tablequeries = [table_users]
