from flask import Flask, request
from app.models.user import User

app = Flask(__name__)


# supported methods
@app.route('/data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        response =  User.get_by_id(user_id)
        if response:
            return response
        return {"message": "User not found in DB"}

    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        user = User(None, user_name)
        response = User.save()
        return response

        # return {'user id': user_id, 'user name': user_name}


# todo elif for put and delete


app.run(host='127.0.0.1', debug=True, port=5000)
