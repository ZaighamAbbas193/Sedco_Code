import os
import random
import time
import logging

import allure
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from generic_methods.helping_methods import methods


import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

"""""""""
from elements.registration_elements import *


def login(context):
    # KSA National registration
    context.driver.find_element(By.CSS_SELECTOR, button_getstarted_css).click()
    context.driver.find_element(By.CSS_SELECTOR, icon_individualinvestor_css).click()
    # context.driver.find_element(By.ID, phone_element_id).click()
    random_3_digit_number = random.randint(100, 999)
    ran_num = str(random_3_digit_number)
    time.sleep(2)
    context.driver.find_element(By.ID, phone_element_id).clear()
    context.driver.find_element(By.ID, phone_element_id).send_keys("56 856 6" + ran_num)

    context.driver.find_element(By.ID, txt_email_id).clear()
    dummy_email = 'testin' + ran_num + '@yopmail.com'
    context.driver.find_element(By.ID, txt_email_id).send_keys(dummy_email)
    context.driver.find_element(By.ID, txt_confirm_email_id).clear()
    context.driver.find_element(By.ID, txt_confirm_email_id).send_keys(dummy_email)
    context.driver.find_element(By.CSS_SELECTOR, checkbox_understand_css).click()
    context.driver.find_element(By.ID, btn_submit_id).click()
    context.driver.find_element(By.ID, txt_verification_code_id).send_keys("1234")
    context.driver.find_element(By.ID, btn_confirm_code_id).click()
    context.driver.find_element(By.ID, ddl_applicant_type_id).click()

"""""""""

def step_capture_screenshot(context):
    # Capture screenshot and save it in the "screenshots" directory
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    random_3_digit_number = random.randint(100, 999)
    ran_num = str(random_3_digit_number)
    screenshot_name="screenshot"+ran_num+".png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)

    context.driver.save_screenshot(screenshot_path)

    # Attach the screenshot to the Allure report
    with allure.step('Attach Screenshot'):
        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG, name=screenshot_name)

    # # Optionally, you can embed the screenshot in the HTML report
    # context.embed_image(screenshot_path, "screenshot.png")

