import pytest
from flask import json


def test_create_meetup(meetups):
    response = meetups.Create_meetup()

    assert response.status_code == 201


def test_get_all_meetups(meetups, client, headers):
    assert client.get('/api/v1/meetup/upcoming',
                      headers=headers).status_code == 200


def test_get_specific_meetup(meetups, client, headers):
    assert client.get('/api/v1/meetup/1', headers=headers).status_code == 200


def test_get_specific_meetup_not_found(meetups, client, headers):
    assert client.get('/api/v1/meetup/2', headers=headers).status_code == 404


@pytest.mark.parametrize(('url', 'status', 'status_code'), (
    ('/api/v1/meetup/2/rsvps', 'yes', 404),
    ('/api/v1/meetup/1/rsvps', 'kgggiyt', 406),
    ('/api/v1/meetup/1/rsvps', 'yes', 201),
    ('/api/v1/meetup/1/rsvps', 'maybe', 201),
    ('/api/v1/meetup/1/rsvps', 'no', 201),
))
def test_create_rsvp(meetups, url, status, status_code):
    response = meetups.rsvp(url, status)
    assert response.status_code == status_code


def test_delete_meetup(client, headers):
    assert client.delete('/api/v1/meetup/1',
                         headers=headers).status_code == 200


def test_delete_meetup_not_found(client, headers):
    assert client.delete('/api/v1/meetup/1',
                         headers=headers).status_code == 404
