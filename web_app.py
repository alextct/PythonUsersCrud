from flask import Flask, request
from app.models.user import User

app = Flask(__name__)


# supported methods
@app.route('/get_user_data/<user_id>', methods=['GET'])
def get_user_name(user_id):
    if request.method == 'GET':
        response = User.get_by_id(user_id)
        if response:
            return "<H1 id='user'>" + response.user_name + "</H1>"
        return "<H1 id='error'> no such user: " + user_id + "</H1>"
    else:
        return "<H1 id='error'> method not allowed " + request.method + "</H1>"


app.run(host='127.0.0.1', debug=True, port=5001)