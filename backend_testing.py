import requests
import sys
from utils.mysql_connection import establish_connection
import random

postEndPoint = "http://127.0.0.1:5000/users/1"
names = ["Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "Grace", "Harry", "Ivy", "Jack"]
userName = random.choice(names)
data = {
    "user_name": userName
}

postResponse = requests.post(postEndPoint, json=data)
if postResponse.status_code != 200:
    print("Test Failed! POST request didn't return status_code 200")
    sys.exit()
print("Post test OK! POST request returned status_code 200")

data = postResponse.json()
addedUserId = data['id']
getEndPoint = "http://127.0.0.1:5000/users/" + str(addedUserId)
getResponse = requests.get(getEndPoint)
if getResponse.status_code != 200:
    print("Test Failed! GET request didn't return status_code 200")
    sys.exit()

data = getResponse.json()
if userName == data['user_name']:
    print("GET test OK. Successfully added user " + userName)
else:
    print("Test Failed! Sent " + userName + " and received " + data['user_name'])

connection = establish_connection()
try:
    with connection.cursor() as cursor:
        query = "SELECT * FROM users WHERE id = %s AND user_name = %s"
        cursor.execute(query, (addedUserId, data['user_name']))
        result = cursor.fetchone()
        if result:
            print("DB test OK! User " + data['user_name'] + " found in the DB at id " + str(addedUserId))
            sys.exit()
        print("DB test failed! User " + data['user_name'] + " not found in the DB")
finally:
    connection.close()
