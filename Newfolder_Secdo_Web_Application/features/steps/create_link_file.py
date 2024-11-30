import time

from allure_commons._allure import feature
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from features.steps.Sedco_ApplicationsType import step_GCC_National, step_KSA_National, \
    step_KSA_Resident
from features.steps.Sedco_ApplicationsType import step_Other_National
from features.steps.Sedco_Approvals import step_BD_Admin_Approval, step_Compliance_Manager
from features.steps.login_step import Open_SedcoApplication, Enter_Credentials
from generic_methods.reusable_methode import step_capture_screenshot
from pageObjects.RMPage import RMPage

#from pageObjects.RMPage import RMPage

"""""""""
@when(u'RM Login with valid Credentials')
def step_impl(context):
    Open_SedcoApplication(context)
    Enter_Credentials(context)
@when(u'Click on the Create Invitation Link')
def step_implCreate_Invitation(context):
    # Click on the Account Opening Invitation
    context.driver.find_element(By.XPATH, "/html/body/header/div[2]/div/nav/div[1]/ul/li[9]/a").click()
    time.sleep(3)
    objRMPage = RMPage(context.driver)
    objRMPage.Create_Invitation()
    time.sleep(3)
@when(u'Enter Email Address')
def step_impl(context):
    objRMPage = RMPage(context.driver)
    objRMPage.Inputs_IsEmail()
    objRMPage.Inputs_Emailfield()
    step_capture_screenshot(context)
@then(u'Click on the Create Link')
def step_impl(context):
    objRMPage = RMPage(context.driver)
    objRMPage.Create_Link_Button()
    # logout_RM
    objRMPage.logout_RM()

@then(u'Open Invitation Link on Email')
def step_impl(context):
    # Execute JavaScript to open a new tab
    #time.sleep(3)
    try:
        context.driver.execute_script("window.open('');")
        time.sleep(3)
        # Switch to the newly opened tab
        context.driver.switch_to.window(context.driver.window_handles[1])
        # Navigate to another webpage in the new tab
        context.driver.get(
            "https://www.mailinator.com/v4/public/inboxes.jsp?to=qqdtsqaengineer002")
        time.sleep(4)
        objRMPage = RMPage(context.driver)
        objRMPage.search_Inputfield()
        step_capture_screenshot(context)
        time.sleep(2)
        # Switch back to the original tab (if necessary)
        #context.driver.switch_to.window(context.driver.window_handles[0])
    finally:
        # Close the browser
        #context.driver.quit()
        time.sleep(3)

@then(u'Click on the Setup Account Link')
def step_impl(context):

    try:
        time.sleep(3)
        context.driver.find_element(By.XPATH, "//td[normalize-space()='SEDCO Capital - Account Opening Invitation']").click()
        # //td[normalize-space()='SEDCO CIS']
        # //td[normalize-space()='SEDCO CIS Vault']
        time.sleep(8)
        # Execute JavaScript to open a new tab
        # Scroll down the page by pixel
        iframe = context.driver.find_element(By.CSS_SELECTOR, "#html_msg_body")
        context.driver.switch_to.frame(iframe)
        print(iframe)
        #time.sleep(7)
        actions = ActionChains(context.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        #time.sleep(4)
        #context.driver.execute_script("window.open('');")
        context.driver.find_element(By.XPATH, "(//a[normalize-space()='Setup Account'])[1]").click()
        time.sleep(5)

       
        # Switch to the newly opened tab
        context.driver.switch_to.window(context.driver.window_handles[2])
        # Navigate to another webpage in the new tab
        #context.driver.get("http://10.10.0.50:8502/client/AccountOpeningAuth/ChooseAccountType")
        time.sleep(6)
        context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/a").click()
        time.sleep(3)
        context.driver.find_element(By.XPATH, "/html/body/section/div/footer/div/div[2]/button[1]").click()
        time.sleep(3) 
        objRMPage = RMPage(context.driver)
        objRMPage.LoginAccountOpening()
        step_capture_screenshot(context)
        #step_GCC_National(context)
        #step_Other_National(context)
        #step_KSA_National(context)
        step_KSA_Resident(context)
        step_capture_screenshot(context)
        step_Account_Opening(context)
        step_capture_screenshot(context)
        step_BD_Admin_Approval(context)
        step_Compliance_Manager(context)

    finally:
        # Close the browser
        #context.driver.quit()
        time.sleep(2)
        """""""""

@when(u'RM Login with valid Credentials and Create Invitation Link')
def step_Create_Invitation(context):
    Open_SedcoApplication(context)
    Enter_Credentials(context)
    # Click on the Account Opening Invitation
    context.driver.find_element(By.XPATH, "/html/body/header/div[2]/div/nav/div[1]/ul/li[9]/a").click()
    time.sleep(3)
    objRMPage = RMPage(context.driver)
    objRMPage.Create_Invitation()
    objRMPage.Inputs_IsEmail()
    objRMPage.Inputs_Emailfield()
    step_capture_screenshot(context)
    objRMPage.Create_Link_Button()
    # logout_RM
    objRMPage.logout_RM()

@then(u'Open Invitation Link on Email')
def step_Open_Invitation_Link(context):
    # Execute JavaScript to open a new tab
    #time.sleep(3)
    try:
        context.driver.execute_script("window.open('');")
        time.sleep(3)
        # Switch to the newly opened tab
        context.driver.switch_to.window(context.driver.window_handles[1])
        # Navigate to another webpage in the new tab
        context.driver.get(
            "https://www.mailinator.com/v4/public/inboxes.jsp?to=qqdtsqaengineer002")
        time.sleep(4)
        objRMPage = RMPage(context.driver)
        objRMPage.search_Inputfield()
        step_capture_screenshot(context)
        time.sleep(2)
        # Switch back to the original tab (if necessary)
        #context.driver.switch_to.window(context.driver.window_handles[0])
    finally:
        # Close the browser
        #context.driver.quit()
        time.sleep(3)

    try:
            time.sleep(3)
            context.driver.find_element(By.XPATH,
                                        "//td[normalize-space()='SEDCO Capital - Account Opening Invitation']").click()
            # //td[normalize-space()='SEDCO CIS']
            # //td[normalize-space()='SEDCO CIS Vault']
            time.sleep(8)
            # Execute JavaScript to open a new tab
            # Scroll down the page by pixel
            iframe = context.driver.find_element(By.CSS_SELECTOR, "#html_msg_body")
            context.driver.switch_to.frame(iframe)
            print(iframe)
            # time.sleep(7)
            actions = ActionChains(context.driver)
            actions.send_keys(Keys.ARROW_DOWN)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            # time.sleep(4)
            # context.driver.execute_script("window.open('');")
            context.driver.find_element(By.XPATH, "(//a[normalize-space()='Setup Account'])[1]").click()
            time.sleep(2)
            #context.driver.find_element(By.XPATH, "//a[normalize-space()='Back to Inbox']").click()
            #time.sleep(3)
    finally:
            # Close the browser
            # context.driver.quit()
            time.sleep(3)

            # Switch to the newly opened tab
            context.driver.switch_to.window(context.driver.window_handles[2])
            # Navigate to another webpage in the new tab
            # context.driver.get("http://10.10.0.50:8502/client/AccountOpeningAuth/ChooseAccountType")
            time.sleep(6)
            context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/a").click()
            time.sleep(2)
            context.driver.find_element(By.XPATH, "/html/body/section/div/footer/div/div[2]/button[1]").click()
            time.sleep(2)