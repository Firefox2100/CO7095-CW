from flask import *
import mysql.connector
from datetime import datetime
from uuid import uuid4

import flask_functions

mydb = mysql.connector.connect(
  host="localhost",
  user="patrick",
  password="Wangyunze001021!",
  database="co7095"
)

app = Flask(__name__)


@app.route('/events/<usertoken>/<date>', methods=["GET"])
def get_events(usertoken, date):
    try:
        result = flask_functions.get_event(usertoken, date)
        if type(result) == str:
            return result, 403
        return jsonify(result), 200

    except Exception as e:
        return f"An Error Occured: {e}", 400


@app.route('/add/<usertoken>', methods=['POST'])
def add_event(usertoken):
    try:
        data = request.get_json()

        result = flask_functions.add_event(usertoken, data)
        if type(result) == str:
            return result, 403

        return 'Success', 200

    except Exception as e:
        return f"An Error Occurred: {e}", 400


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()

        result = flask_functions.register(data)
        if result == "User already exist":
            return result, 403

        return result, 200

    except Exception as e:
        return f"An Error Occurred: {e}", 400


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        result = flask_functions.login(data)
        if result == "User doesn't exist" or result == "Password error":
            return result, 403

        return result, 200

    except Exception as e:
        return f"An Error Occurred: {e}", 400


if __name__ == '__main__':
    app.run(debug=True)
