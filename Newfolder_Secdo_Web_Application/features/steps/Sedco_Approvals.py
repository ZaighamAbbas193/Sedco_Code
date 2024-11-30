import random
import time
from multiprocessing import context
from allure_commons._allure import feature
from behave import given, when, then
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.steps.Sedco_ApplicationsType import step_KYC_GCC_National
from generic_methods.reusable_methode import step_capture_screenshot
from pageObjects.RMPage import dummy_email

@when(u'BD Admin login into the Admin  portal with valid Credentials and Approved the application')
def step_BD_Admin_Approval(context):

    context.driver.switch_to.window(context.driver.window_handles[0])
    time.sleep(4)
    context.driver.find_element(By.ID, "username").send_keys("sedco-bd-admin")
    context.driver.find_element(By.ID, "password").send_keys("Abc@123456")
    context.driver.find_element(By.ID, "btnSubmit").click()
    time.sleep(2)
    # OTP
    context.driver.find_element(By.ID, "digit-1").send_keys("2")
    context.driver.find_element(By.ID, "digit-2").send_keys("2")
    context.driver.find_element(By.ID, "digit-3").send_keys("4")
    context.driver.find_element(By.ID, "digit-4").send_keys("4")
    # btnConfirmCode
    context.driver.find_element(By.XPATH, "//input[@value='Confirm Code']").click()
    time.sleep(2)

    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(dummy_email)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'View')])[1]").click()
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Approvals'])[1]").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//textarea[@id='Remarks']").send_keys("Automation QA Remarks")
    context.driver.find_element(By.XPATH, "(//input[@id='ApproveBtn'])[1]").click()
    time.sleep(2)
    step_capture_screenshot(context)
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Log Out'])[1]").click()
    time.sleep(2)

@when(u'Compliance Manager login into the Admin  portal with valid Credentials and Send the application for Screening')
def step_Compliance_Manager(context):
    # Compliance Manager
    context.driver.find_element(By.ID, "username").send_keys("sedco-compliance-manager")
    context.driver.find_element(By.ID, "password").send_keys("Abc@123456")
    context.driver.find_element(By.ID, "btnSubmit").click()
    time.sleep(2)
    # OTP
    context.driver.find_element(By.ID, "digit-1").send_keys("2")
    context.driver.find_element(By.ID, "digit-2").send_keys("2")
    context.driver.find_element(By.ID, "digit-3").send_keys("4")
    context.driver.find_element(By.ID, "digit-4").send_keys("4")
    # btnConfirmCode
    context.driver.find_element(By.XPATH, "//input[@value='Confirm Code']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(dummy_email)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'View')])[1]").click()
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Approvals'])[1]").click()
    context.driver.find_element(By.XPATH, "//textarea[@id='Remarks']").send_keys("Automation QA Remarks")
    time.sleep(2)
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='ComplianceOfficersId']"))
    select.select_by_value("152")
    #context.driver.find_element(By.XPATH, "(//input[@id='ApproveBtn'])[1]").click()
    context.driver.find_element(By.XPATH, "//input[@id='AssignComplianceOfficer']").click()
    step_capture_screenshot(context)
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Log Out'])[1]").click()
    time.sleep(2)

@when(u'Compliance Officer login into the Admin  portal with valid Credentials and Set Risk type and Send Back application to the Compliance Manager')
def step_Compliance_Officer(context):
    # Compliance Manager
    context.driver.find_element(By.ID, "username").send_keys("sedco-compliance-officer")
    context.driver.find_element(By.ID, "password").send_keys("Abc@123456")
    context.driver.find_element(By.ID, "btnSubmit").click()
    time.sleep(2)
    # OTP
    context.driver.find_element(By.ID, "digit-1").send_keys("2")
    context.driver.find_element(By.ID, "digit-2").send_keys("2")
    context.driver.find_element(By.ID, "digit-3").send_keys("4")
    context.driver.find_element(By.ID, "digit-4").send_keys("4")
    # btnConfirmCode
    context.driver.find_element(By.XPATH, "//input[@value='Confirm Code']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(dummy_email)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'View')])[1]").click()
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Approvals'])[1]").click()
    context.driver.find_element(By.XPATH, "//textarea[@id='Remarks']").send_keys("Automation QA Remarks")
    time.sleep(2)
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='ScreeningResultId']"))
    select.select_by_value("1229")
    context.driver.find_element(By.XPATH, "//input[@id='ScreeningDocument']").send_keys(r"C:\Users\Administrator\Desktop\Automation\Doc1.pdf")
    time.sleep(4)
    context.driver.find_element(By.XPATH, "//input[@id='SendBackBtnComplianceManagerBYCO']").click()
    step_capture_screenshot(context)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Log Out'])[1]").click()
    time.sleep(6)

@when(u'Compliance Manager login into the Admin  portal with valid Credentials and Approve the application')
def step_Compliance_Manager_FinalApproval(context):
    # Compliance Manager
    context.driver.find_element(By.ID, "username").send_keys("sedco-compliance-manager")
    context.driver.find_element(By.ID, "password").send_keys("Abc@123456")
    context.driver.find_element(By.ID, "btnSubmit").click()
    time.sleep(2)
    # OTP
    context.driver.find_element(By.ID, "digit-1").send_keys("2")
    context.driver.find_element(By.ID, "digit-2").send_keys("2")
    context.driver.find_element(By.ID, "digit-3").send_keys("4")
    context.driver.find_element(By.ID, "digit-4").send_keys("4")
    # btnConfirmCode
    context.driver.find_element(By.XPATH, "//input[@value='Confirm Code']").click()
    time.sleep(6)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/a[3]").click()
    #
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(dummy_email)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'View')])[1]").click()
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Approvals'])[1]").click()
    context.driver.find_element(By.XPATH, "//textarea[@id='Remarks']").send_keys("Automation QA Remarks")
    time.sleep(2)
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='RiskTypeDropdown']"))
    select.select_by_value("869")
    context.driver.find_element(By.XPATH, "//input[@id='ApproveBtnComplianceManager']").click()
    step_capture_screenshot(context)
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Log Out'])[1]").click()
    time.sleep(3)

@when(u'CEO login into the Admin  portal with valid Credentials and Approve the application')
def step_Ceo_Approval(context):
    # Compliance Manager
    context.driver.find_element(By.ID, "username").send_keys("sedco-ceo")
    context.driver.find_element(By.ID, "password").send_keys("Abc@123456")
    context.driver.find_element(By.ID, "btnSubmit").click()
    time.sleep(2)
    # OTP
    context.driver.find_element(By.ID, "digit-1").send_keys("2")
    context.driver.find_element(By.ID, "digit-2").send_keys("2")
    context.driver.find_element(By.ID, "digit-3").send_keys("4")
    context.driver.find_element(By.ID, "digit-4").send_keys("4")
    # btnConfirmCode
    context.driver.find_element(By.XPATH, "//input[@value='Confirm Code']").click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(dummy_email)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'View')])[1]").click()
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Approvals'])[1]").click()
    context.driver.find_element(By.XPATH, "//textarea[@id='Remarks']").send_keys("Automation QA Remarks")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@id='ApproveBtnBYCEO']").click()
    step_capture_screenshot(context)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Log Out'])[1]").click()
    time.sleep(3)

@when(u'BD-Head login into the Admin  portal with valid Credentials and Approve the application')
def step_BD_Head_Approval(context):

    # BD Head
    context.driver.find_element(By.ID, "username").send_keys("sedco-bd-head")
    context.driver.find_element(By.ID, "password").send_keys("Abc@123456")
    context.driver.find_element(By.ID, "btnSubmit").click()
    time.sleep(2)
    # OTP
    context.driver.find_element(By.ID, "digit-1").send_keys("2")
    context.driver.find_element(By.ID, "digit-2").send_keys("2")
    context.driver.find_element(By.ID, "digit-3").send_keys("4")
    context.driver.find_element(By.ID, "digit-4").send_keys("4")
    # btnConfirmCode
    context.driver.find_element(By.XPATH, "//input[@value='Confirm Code']").click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(dummy_email)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@id='Filters_EmailAddress']").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, "(//a[contains(text(),'View')])[1]").click()
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Approvals'])[1]").click()
    context.driver.find_element(By.XPATH, "//textarea[@id='Remarks']").send_keys("Automation QA Remarks")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@id='ApproveBtnBYBdHead']").click()
    step_capture_screenshot(context)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='Log Out'])[1]").click()
    time.sleep(3)



