import sys

from flask import Flask, request
from app.models.user import User
import os
import signal

app = Flask(__name__)


# supported methods
@app.route('/stop_server')
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)

@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        response = User.get_by_id(user_id)
        if response:
            return {'status': 'ok', 'user_name': response.user_name}, 200
        return {"status": "error", "reason": "no such id - " + user_id}, 500

    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        user = User(id=None, user_name=user_name)
        response = user.save()
        if response:
            return {'status': 'ok', 'user_added': response.user_name, 'id':response.id}, 200
        return {"status": "error", "reason": "user " + user_name + " cannot be saved in the database"}, 500

    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        id = user_id
        user = User(id=id, user_name=user_name)
        response = user.save()
        if response:
            return {'status': 'ok', 'user_updated': response.user_name}, 200
        return {"status": "error", "reason": "user " + id + " does not exists in the database to be updated"}, 500

    elif request.method == "DELETE":
        id = user_id
        user = User(id=id)
        response = user.delete()
        if response:
            return {'status': 'ok', 'user_deleted': response.user_name}, 200
        else:
            return {"status": "error", "reason": "user " + id + " does not exist in the database to be deleted"}, 500


app.run(host='127.0.0.1', debug=True, port=5000)
