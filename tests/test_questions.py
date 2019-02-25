import pytest
from flask import json


def test_create_question(questions):
    response = questions.Create_question()

    assert response.status_code == 201


def test_voteup(questions):
    questions.Create_question()
    response = questions.vote('/api/v2/questions/upvote/1')

    assert response.status_code == 200


def test_voteup(questions):
    response = questions.vote('/api/v2/question/upvote/1')

    assert response.status_code == 200


def test_votedown(questions):
    questions.Create_question()
    response = questions.vote('/api/v2/questions/downvote/2')

    assert response.status_code == 200


def test_fail_votedown(questions):
    questions.Create_question()
    response = questions.vote('/api/v2/questions/downvote/5')

    assert response.status_code == 404


def test_fail_voteup(questions):
    questions.Create_question()
    response = questions.vote('/api/v2/questions/upvote/5')

    assert response.status_code == 404
