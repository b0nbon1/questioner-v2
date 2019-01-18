# questioner-v2

[![Coverage Status](https://coveralls.io/repos/github/b0nbon1/questioner-v2/badge.svg?branch=develop)](https://coveralls.io/github/b0nbon1/questioner-v2?branch=develop)  [![Build Status](https://travis-ci.org/b0nbon1/questioner-v2.svg?branch=develop)](https://travis-ci.org/b0nbon1/questioner-v2)

this is crowd platform where meetups are created questions are asked


# API-endpoints


## The following are API endpoints enabling one to: 
* Create a meetup record.
* Create a question record.
* Get a specific meetup record.
* Get all meetup records.
* Upvote or downvote a question.
* Rsvp for a meetup.
## Here is a list of the functioning endpoints

| EndPoint                | Functionality        | Routes            |
| :---                    |     :---:            | :---              |
| POST /meetup            | admin post a meetup       | /api/v1/meetup    |
| GET /meetups/< meetup_id >   | Get a specific meetup by meetup id| /api/v1/meetups/< meetup_id > |
| GET /meetups/upcoming            | Get upcoming meetups        | /api/v1/orders    |
| POST /Questions            | Post questions          | /api/v1/meetups/upcoming |
| PATCH /questions/< question_id>/upvote             | Vote for question          | /api/v1/questions/< question_id>/upvote  |
| PATCH /questions/< question_id>/downvote   | Vote for question     | /api/v1/questions/< question_id>/downvote  |
| POST /meetups/< meetup_id >/rsvp             | post meetups rasvp          | /api/v1/meetups/< meetup_id >/rsvp|
| POST /auth/signup            | post a registers new user      | /api/v2/auth/signup    |
| POST /auth/login            | post a logs in a user      | /api/v2/auth/login    |
| POST /< question_id >/comments            | post comments     | /api/v2/< question_id >/comments    |

  
## QUICK START

* clone the repo
* install virtualenv by `virtualenv venv`
* activate env by `. venv/bin/activate`
* `pip3 install -r requirements.txt`
* run the app

## how to run tests

* use `pytest -v` to run the tests

# Written by: Bonvic Bundi
#### Copyright © Andela 2019 
