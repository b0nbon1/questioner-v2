import pytest
from flask import json


def test_create_questions(comments):
    response = comments.Create_comment()

    assert response.status_code == 201


def test_delete_comments(client, headers):
    response = client.delete('api/v1/questions/comments/1', headers=headers)
    assert response.status_code == 200


def test_edit_comments(client, headers):
    response = client.put('api/v1/questions/comments/1', headers=headers)
    assert response.status_code == 201
