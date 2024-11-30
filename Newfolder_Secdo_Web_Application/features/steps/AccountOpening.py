import time

from allure_commons._allure import feature
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from features.steps.Sedco_ApplicationsType import step_GCC_National, step_KSA_National, \
    step_KSA_Resident, step_Account_Opening_With_GCC, step_Account_Opening_With_KSA
from features.steps.Sedco_ApplicationsType import step_Other_National
from features.steps.Sedco_Approvals import step_BD_Admin_Approval, step_Compliance_Manager, step_Compliance_Officer, \
    step_Compliance_Manager_FinalApproval
from features.steps.login_step import Open_SedcoApplication, Enter_Credentials
from generic_methods.reusable_methode import step_capture_screenshot
from pageObjects.RMPage import RMPage

@when(u'Open Client portal with valid Credentials, fill the all forms and submit the application')
def step_impl(context):
    try:
        time.sleep(3)
        """""""""
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
        time.sleep(5)
        
        
        # Switch to the newly opened tab
        context.driver.switch_to.window(context.driver.window_handles[2])
        # Navigate to another webpage in the new tab
        # context.driver.get("http://10.10.0.50:8502/client/AccountOpeningAuth/ChooseAccountType")
        time.sleep(6)
        context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/a").click()
        time.sleep(3)
        context.driver.find_element(By.XPATH, "/html/body/section/div/footer/div/div[2]/button[1]").click()
        time.sleep(3)
        
        """""""""

        #objRMPage = RMPage(context.driver)
        #objRMPage.LoginAccountOpening()
        #step_capture_screenshot(context)

        step_GCC_National(context)
        # step_Other_National(context)
        # step_KSA_National(context)
        # step_KSA_Resident(context)

        #step_Account_Opening_With_KSA(context)
        #step_Account_Opening_With_GCC(context)
        #step_capture_screenshot(context)

    finally:
        # Close the browser
        # context.driver.quit()
        time.sleep(2)