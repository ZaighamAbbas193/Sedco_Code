import configparser
import time
from lib2to3.fixes.fix_input import context

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from generic_methods.reusable_methode import step_capture_screenshot
from pageObjects.loginPage import LoginPage

#@when(u'I enter URL')
def Open_SedcoApplication(context):
    context.driver.get("https://kyc.sedcocapital.com/admin")  # Replace with your login page URL

    #  http://10.10.0.50:8502/admin
    #  https://kyc.sedcocapital.com/admin

    time.sleep(2)
#@when(u'I enter my username and password')
def Enter_Credentials(context):

    login_page = LoginPage(context.driver)
    login_page.setUserName("Sedco-rm")
    login_page.setPassword("Abc@123456")
    step_capture_screenshot(context)
    login_page.clickLogin()
    time.sleep(2)
    # OTP
    context.driver.find_element(By.ID, "digit-1").send_keys("2")
    context.driver.find_element(By.ID, "digit-2").send_keys("2")
    context.driver.find_element(By.ID, "digit-3").send_keys("4")
    context.driver.find_element(By.ID, "digit-4").send_keys("4")
    step_capture_screenshot(context)
    # btnConfirmCode
    context.driver.find_element(By.XPATH, "//input[@value='Confirm Code']").click()
    assert True

