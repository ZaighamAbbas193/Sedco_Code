import time

from allure_commons._allure import feature
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from features.steps.Sedco_ApplicationsType import step_GCC_National, step_KSA_National, \
    step_KSA_Resident, step_Account_Opening_With_GCC, step_Account_Opening_With_KSA, step_KYC_GCC_National
from features.steps.Sedco_ApplicationsType import step_Other_National
from features.steps.Sedco_Approvals import step_BD_Admin_Approval, step_Compliance_Manager, step_Compliance_Officer, \
    step_Compliance_Manager_FinalApproval, step_Ceo_Approval, step_BD_Head_Approval
from features.steps.login_step import Open_SedcoApplication, Enter_Credentials
from generic_methods.reusable_methode import step_capture_screenshot
from pageObjects.RMPage import RMPage


@when(u'Setup Account Credentials and Login into the Client Portal and Update require data, Submit the KYC update Application')
def step_impl(context):
    try:
        time.sleep(3)

        step_KYC_GCC_National(context)
        step_capture_screenshot(context)


    finally:
        # Close the browser
        # context.driver.quit()
        time.sleep(2)

@when(u'Approve KYC update Application from all back off users')
def step_impl(context):
    try:
        time.sleep(3)

        step_BD_Admin_Approval(context)
        step_Compliance_Manager(context)
        step_Compliance_Officer(context)
        step_Compliance_Manager_FinalApproval(context)
        step_Ceo_Approval(context)
        step_BD_Head_Approval(context)

    finally:
        # Close the browser
        # context.driver.quit()
        time.sleep(2)
