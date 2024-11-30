import random
import time
from multiprocessing import context

from allure_commons._allure import feature
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from features.steps.Sedco_ApplicationsType import step_GCC_National, step_KSA_National, \
    step_KSA_Resident
from features.steps.Sedco_ApplicationsType import step_Other_National
from features.steps.Sedco_Approvals import step_BD_Admin_Approval, step_Compliance_Manager, \
    step_Compliance_Manager_FinalApproval, step_Compliance_Officer, step_Ceo_Approval, step_BD_Head_Approval
from features.steps.create_link_file import step_Create_Invitation, step_Open_Invitation_Link
from features.steps.login_step import Open_SedcoApplication, Enter_Credentials
from generic_methods.reusable_methode import step_capture_screenshot
from pageObjects.RMPage import RMPage


"""""
@when(u'RM Login with valid Credentials and Create Invitation Link1')

def step_Create_Invitation1(context):
    step_Create_Invitation(context)
@when(u'Open Invitation Link on Email1')
def step_Open_Invitation_Link1(context):
    step_Open_Invitation_Link(context)
@when(u'Open Client portal with valid Credentials, fill the all forms and submit the application1')
def step_SubmitAccountOpeningApplication(context):
    try:
        #time.sleep(3)
        # step_GCC_National(context)
        # step_Other_National(context)
        # step_KSA_National(context)
        step_KSA_Resident(context)

    finally:
        # Close the browser
        # context.driver.quit()
        time.sleep(2)
    """""


@when(u'RM Login with valid Credentials and Create Invitation Link1')
def step_Create_Invitation1(context):
            # Loop to repeat the sequence multiple times
            for i in range(1, 4):  # Repeat 3 times
                # print(f"Iteration {i}: Creating invitation link")
                step_Create_Invitation(context)
                step_Open_Invitation_Link(context)

                if i == 1:
                    step_Other_National(context)
                    #step_KSA_Resident(context)
                elif i == 2:
                    #step_KSA_National(context)
                    step_GCC_National(context)
                elif i == 3:
                    step_KSA_National(context)
                else:
                    step_KSA_Resident(context)

                step_BD_Admin_Approval(context)
                step_Compliance_Manager(context)
                step_Compliance_Officer(context)
                step_Compliance_Manager_FinalApproval(context)
                step_Ceo_Approval(context)
                step_BD_Head_Approval(context)

                #print(f"Iteration {i + 1}: Creating invitation link")

"""""

def step_Open_Invitation_Link1(context):
            # Loop to repeat the sequence multiple times
            for i in range(3):  # Repeat 3 times
                print(f"Iteration {i + 1}: Opening invitation link")
                step_Open_Invitation_Link(context)

@when(u'Open Client portal with valid Credentials, fill the all forms and submit the application1')
def step_SubmitAccountOpeningApplication(context):
            try:
                # Loop to repeat the process multiple times
                for i in range(3):  # Repeat 3 times
                    print(f"Iteration {i + 1}: Submitting the application")

                    # Ensure to reinitialize or reset the state if necessary before each iteration
                    # This can include logging in again or navigating to the right page

                    # Assuming step_KSA_Resident fills out the form and submits it
                    step_KSA_Resident(context)

                    # Optional: Add a sleep time between iterations if necessary
                    time.sleep(2)

                    # Optionally handle any post-submission verification or cleanup

            finally:
                # Optionally close the browser after all iterations
                if context.driver:
                    context.driver.quit()

"""""