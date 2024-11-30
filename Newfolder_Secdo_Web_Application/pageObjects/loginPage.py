
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(context, driver):
        context.driver = driver
    def setUserName(context, username):
        context.driver.find_element(By.ID, "username").send_keys(username)

    def setPassword(context, password):
        context.driver.find_element(By.ID, "password").send_keys(password)

    def clickLogin(context):
        context.driver.find_element(By.ID, "btnSubmit").click()

