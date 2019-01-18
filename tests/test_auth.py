import pytest
import json


def test_login(client, auth):
    auth.register()
    response = auth.login()

    assert response.status_code == 200


@pytest.mark.parametrize(('username', 'password', 'status_code'), (
    ('not', 'test', 404),
    ('pytest3', 'guess', 401),
    ('pytest3', 'testpytest', 200)
))
def test_login_validate_input(auth, username, password, status_code):
    auth.register()
    response = auth.login(username, password)
    assert response.status_code == status_code


@pytest.mark.parametrize(("username", "email", "password", "confirm_password", "error"), [
    ("test5", "test@test123.com", "test1pytest",
     "test1pytest", b"user successfull registered!"),
    ("te", "testguuk@test.com", "testpytest", "testpytest", b"invalid username"),
    ("test2", "test", "testpytest", "testpytest", b"invalid email"),
    ("test3", "test@test.com", "test", "test", b"invalid password"),
    ("test4", "test1@test.com", "testpytest", "testpytest", b"email exists"),
    ("test4", "test@test.com", "testpytest", "test", b"Passwords don't match")
])
def test_register_validate_input(auth, username, email, password, confirm_password, error):
    auth.register()
    response = auth.register(firstname='test1', lastname='test2', othername='test3',
                             PhoneNumber='873462', username=username, email=email,
                             password=password, confirm_password=confirm_password)

    assert error in response.data


def test_empty_fiels(auth):
    response = auth.register(firstname='', lastname='', othername='',
                             PhoneNumber='', username='', email='',
                             password='', confirm_password='')

    assert b'all fields required' in response.data
