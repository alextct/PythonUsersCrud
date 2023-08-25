from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service("/home/alex/work/learn/PythonDevopsLessons/chromedriver-linux64/chromedriver"))
driver = webdriver.Chrome(service=Service("./chromedriver"))
driver.implicitly_wait(1)
driver.get('http://127.0.0.1:5001/get_user_data/1')

try:
    element = driver.find_element(By.ID, "user")
    print("Test OK, User found: " + element.text)

except NoSuchElementException:
    try:
        element = driver.find_element(By.ID, "error")
        print("Test OK, Frontend message: " + element.text)

    except NoSuchElementException:
        print("Test Failed, nor user or error id found")