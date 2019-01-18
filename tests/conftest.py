import pytest
import os
import json
from app import create_app
from flask_jwt_extended import create_access_token
from databases.db_connect import destroy_tables


@pytest.fixture(scope="module")
def app():
    ''' initialize test module to testing mode '''
    # os.environ["FLASK_ENV"] = "testing"
    app = create_app("testing")
    app.testing= True
    print("db connected")
    yield app
    destroy_tables()
    print("\ndb closed")


class Setup_auth():
    # setups the tests
    def __init__(self, client):
        self._client = client

    def login(self, username='pytest3', password='testpytest'):
        return self._client.post(
            '/api/v2/auth/login',
            data=json.dumps({'username': username, 'password': password}),
            content_type='application/json'
        )

    def register(self, firstname='test1',
                 lastname='test2',
                 othername='test3',
                 PhoneNumber='254712345678',
                 email='test1@test.com',
                 username='pytest3',
                 password='testpytest',
                 confirm_password='testpytest'):
        return self._client.post(
            '/api/v2/auth/register',
            data=json.dumps({'firstname': firstname,
                             'lastname': lastname,
                             'othername': othername,
                             'PhoneNumber': PhoneNumber,
                             'email': email,
                             'username': username,
                             'password': password,
                             'confirm_password': confirm_password}),
            content_type='application/json'
        )

    def update_user(self):
        return self._client.put('/api/v2/auth/update/1')


# creates a fixture for class auth
@pytest.fixture
def auth(client):
    return Setup_auth(client)


# creates client fixture for app.test_client
@pytest.fixture
def client(app):
    return app.test_client()


# creates a jwt header for test authentications
@pytest.fixture
def headers(app, auth):
    auth.register()
    auth.update_user()
    response = auth.login()
    token = json.loads(response.get_data(as_text=True))['access_token']
    headers = {'Authorization': 'Bearer {}'.format(token)}

    return headers


class Setup_meetup():
    # setups the tests
    def __init__(self, client, headers):
        self._client = client
        self._headers = headers

    def Create_meetup(self, topic='Flask', location='Nairobi',
                      happeningOn='1st Feb',
                      images=['https://www.cs.ucdavis.edu/wp-content/uploads/2014/02/cover.jpg',
                              'https://www.gsd.harvard.edu/wp-content/uploads/2017/08/Lib-Lab.jpg'],
                      tags=['python', 'flask']):
        return self._client.post(
            '/api/v2/meetup/',
            data=json.dumps({'topic': topic,
                             'location': location,
                             'happeningOn': happeningOn,
                             'images': images,
                             'tags': tags}),
            content_type='application/json', headers=self._headers
        )

    def rsvp(self, url, status):
        return self._client.post(
            url,
            data=json.dumps({
                'status': status
            }),
            content_type='application/json', headers=self._headers
        )


# creates fixture meetup
@pytest.fixture
def meetups(client, headers):
    return Setup_meetup(client, headers)


class Setup_question():
    # setups the tests
    def __init__(self, client, headers):
        self._client = client
        self._headers = headers

    def Create_question(self, user=2,
                        meetup=1,
                        title='flask',
                        body='There available by injected humour, or randomised words which don\'t look even slightly believable?'
                        ):
        return self._client.post(
            '/api/v2/question/',
            data=json.dumps({'user': user,
                             'meetup': meetup,
                             'title': title,
                             'body': body,
                             }),
            content_type='application/json', headers=self._headers
        )

    def vote(self, url):
        return self._client.patch(
            url,
            content_type='application/json', headers=self._headers
        )


# creates a fixture for class questions
@pytest.fixture
def questions(client, headers):
    return Setup_question(client, headers)
