# We are using Flask, FLask-SQLAlchemy, mysqlclient, and flask-marshmallow
from flask import flask

backend = flask(__name__)
@backend.route('/', methods = ['GET'])
def get_articles():
    return jsonify({'hello':'world'})


if __name__ == "__main__":
    backend.run(debug=True)