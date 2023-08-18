import requests
import sys
from app.utils.mysql_connection import establish_connection
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import random

# BACKEND TEST
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
        else:
            print("DB test failed! User " + data['user_name'] + " not found in the DB")
finally:
    connection.close()


# FRONT END TESTING
driver = webdriver.Chrome(service=Service("/home/alex/work/learn/PythonDevopsLessons/chromedriver"))
driver.implicitly_wait(1)
getEndpoint = "http://127.0.0.1:5001/get_user_data/" + str(addedUserId)
driver.get(getEndpoint)

try:
    element = driver.find_element(By.ID, "user")
    expectedUserName = element.text
    if expectedUserName == userName:
        print("Selenium Test OK, User found: " + element.text)
    else:
        print("Test Failed! User expected: " + expectedUserName + " and found " + userName)

except NoSuchElementException:
    try:
        element = driver.find_element(By.ID, "error")
        print("Test OK, Frontend message: " + element.text)

    except NoSuchElementException:
        print("Test Failed, nor user or error id found")
