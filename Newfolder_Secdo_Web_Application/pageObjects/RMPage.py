import random
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

import random
random_3_digit_number = random.randint(100, 999)
ran_num = str(random_3_digit_number)
dummy_email = 'qqdtsqaengineer' + ran_num + '@mailinator.com'

class RMPage:
    def __init__(self, driver):
        self.driver = driver

    def Account_Opening_Link(context):
        context.driver.find_element(By.XPATH, "/html/body/header/div[2]/div/nav/div[1]/ul/li[9]/a").click()

    def Create_Invitation(context):
        context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/a").click()
    def Inputs_IsEmail(context):
        context.driver.find_element(By.ID, "Inputs_IsEmail").click()

    def Inputs_Emailfield(context):
        context.driver.find_element(By.ID, "Inputs_Email").send_keys(dummy_email)
    def Create_Link_Button(context):
        context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/form/div/div[1]/div/div[6]/div/div/input").click()

    def search_Inputfield(context):
        context.driver.find_element(By.ID, "inbox_field").clear()
        context.driver.find_element(By.ID, "inbox_field").send_keys(dummy_email)
        context.driver.find_element(By.ID, "inbox_field").send_keys(Keys.ENTER)
        time.sleep(2)

    def LoginAccountOpening(context):
        context.driver.find_element(By.ID, "phone").send_keys("512345"+ran_num)
        context.driver.find_element(By.ID, "txtEmail").send_keys(dummy_email)
        context.driver.find_element(By.ID, "txtConfirmEmail").send_keys(dummy_email)
        context.driver.find_element(By.ID, "btnSubmit").click()
        time.sleep(4)
        # OTP
        context.driver.find_element(By.ID, "digit-1").send_keys("2")
        context.driver.find_element(By.ID, "digit-2").send_keys("2")
        context.driver.find_element(By.ID, "digit-3").send_keys("4")
        context.driver.find_element(By.ID, "digit-4").send_keys("4")
        context.driver.find_element(By.ID, "btnConfirmCode").click()
        time.sleep(2)

    def logout_RM(context):
        context.driver.find_element(By.XPATH, "//a[normalize-space()='Log Out']").click()



