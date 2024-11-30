import time
from telnetlib import EC

from behave import given, when, then
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import random

from generic_methods.reusable_methode import step_capture_screenshot
from pageObjects.RMPage import RMPage


random_3_digit_number = random.randint(100, 999)
ran_num = str(random_3_digit_number)
dummy_KYC_Users = 'QA Automation Client' + ran_num
def step_Other_National(context):

    objRMPage = RMPage(context.driver)
    objRMPage.LoginAccountOpening()
    step_capture_screenshot(context)
    time.sleep(3)
   # time.sleep(3)
    context.driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/form/div[1]/div").click()
    time.sleep(3)
    dropdown_element = (context.driver.find_element(By.XPATH,
    "/html/body/main/div/div/div/div/div/div/form/div[1]/div/select/option[5]")).click()
    #/html/body/main/div/div/div/div/div/div/form/div[1]/div/select/option[4]
    #//*[@id="ddlApplicantType"]/option[5]
    time.sleep(3)
    context.driver.find_element(By.ID, "txtIdentificationNumber").send_keys("51234" + ran_num)
    context.driver.find_element(By.ID, "btnVerifyNin").click()
    time.sleep(5)
    step_capture_screenshot(context)
    context.driver.find_element(By.ID, "btnProceedForGccAndOthers").click()
    context.driver.find_element(By.ID, "Inputs_TitleId").click()
    # Engr
    context.driver.find_element(By.XPATH,
                        "/html/body/main/main/div/div/div/form/div[1]/div[1]/div[1]/div/div/select/option[4]").click()
    # Full Name as in Passport
    context.driver.find_element(By.ID, "FullNameArabic").send_keys("اختبار البيانات")
    # Full Name as in Passport (English)
    context.driver.find_element(By.ID, "FullNameEnglish").send_keys("QQ Testing ABC")

    actions = ActionChains(context.driver)
    time.sleep(2)
    # Date of birth
    # Example of executing JavaScript to remove 'disabled' attribute from an element
    context.driver.find_element(By.ID, "datePickerDOB").click()
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]").click()
    time.sleep(2)
    # 5 Place of birth
    context.driver.find_element(By.ID, "Inputs_PlaceOfBirth").send_keys("Karachi")
    # datePickerExpiryDate
    context.driver.find_element(By.ID, "datePickerExpiryDate").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='30'])[1]").click()
    # datePickerIssueDate
    context.driver.find_element(By.ID, "datePickerIssueDate").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]").click()
    context.driver.find_element(By.ID, "Inputs_IdentificationNumberIssuePlace").send_keys("karachi")

    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(5)
    context.driver.execute_script("window.scrollBy(0, 500);")  # Scroll down by 500 pixels

    context.driver.find_element(By.ID, "select2-countriesListNationality-container").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//input[@role='textbox'])[2]").send_keys("United")
    context.driver.find_element(By.XPATH, "(//span[normalize-space()='United Kingdom'])[1]").click()
    step_capture_screenshot(context)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(5)

    context.driver.find_element(By.XPATH, "(//span[normalize-space()='No'])[1]").click()
    context.driver.find_element(By.ID, "select2-KSAResidentStatusForNonSaudiCountriesList-container").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//input[@role='textbox'])[2]").send_keys("United")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//span[normalize-space()='United Arab Emirates'])[1]").click()

    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(5)

    select = Select(context.driver.find_element(By.ID, "Inputs_MaritalStatusId"))
    select.select_by_value("28")
    context.driver.find_element(By.ID, "PIA14Depen_Txt").send_keys("100")

    context.driver.find_element(By.XPATH,  "(//label[normalize-space()='Postgraduate'])[1]").click()
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()
    time.sleep(7)

    #   2. Contact Information
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//label[normalize-space()='English'])[1]").click()
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalAddress").send_keys("Address")
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalCity").send_keys("Karachi")
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalPostalCode").send_keys("1234")
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalProvince").send_keys("Sindh")

    context.driver.find_element(By.ID, "select2-nonKSACountry-container").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//input[@role='textbox'])[1]").send_keys("United")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//span[normalize-space()='United Arab Emirates'])[1]").click()
    step_capture_screenshot(context)
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()
    time.sleep(7)
    step_Account_Opening_With_GCC(context)
    #step_KYC_GCC_National(context)

def step_GCC_National(context):

    objRMPage = RMPage(context.driver)
    objRMPage.LoginAccountOpening()
    step_capture_screenshot(context)
    time.sleep(3)
    context.driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/form/div[1]/div").click()
    time.sleep(3)
    dropdown_element = (context.driver.find_element(By.XPATH,
                                                    "/html/body/main/div/div/div/div/div/div/form/div[1]/div/select/option[4]")).click()
    # /html/body/main/div/div/div/div/div/div/form/div[1]/div/select/option[4]
    # //*[@id="ddlApplicantType"]/option[5]
    time.sleep(3)
    context.driver.find_element(By.ID, "txtIdentificationNumber").send_keys("51234" + ran_num)
    step_capture_screenshot(context)
    context.driver.find_element(By.ID, "btnVerifyNin").click()
    time.sleep(5)
    context.driver.find_element(By.ID, "btnProceedForGccAndOthers").click()
    context.driver.find_element(By.ID, "Inputs_TitleId").click()
    # Engr
    context.driver.find_element(By.XPATH,
                                "/html/body/main/main/div/div/div/form/div[1]/div[1]/div[1]/div/div/select/option[4]").click()
    context.driver.find_element(By.ID, "FullNameArabic").send_keys("اختبار البيانات")
    context.driver.find_element(By.ID, "FullNameEnglish").send_keys("QQ Testing ABC")

    actions = ActionChains(context.driver)

    # actions.send_keys(Keys.)
    # actions.send_keys(Keys.ENTER)
    # actions.perform()
    time.sleep(2)

    # Example of executing JavaScript to remove 'disabled' attribute from an element
    # Date of birth*
    context.driver.find_element(By.ID, "datePickerDOB").click()
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]").click()
    time.sleep(2)
    context.driver.find_element(By.ID, "Inputs_PlaceOfBirth").send_keys("Karachi")
    # Expiry date
    context.driver.find_element(By.ID, "datePickerExpiryDate").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='30'])[1]").click()
    # datePickerIssueDate
    context.driver.find_element(By.ID, "datePickerIssueDate").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]").click()
    context.driver.find_element(By.ID, "Inputs_IdentificationNumberIssuePlace").send_keys("karachi")

    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(5)
    context.driver.execute_script("window.scrollBy(0, 500);")  # Scroll down by 500 pixels

    context.driver.find_element(By.ID, "select2-countriesListNationality-container").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//input[@role='textbox'])[2]").send_keys("Bahrain")
    context.driver.find_element(By.XPATH, "(//ul[@id='select2-countriesListNationality-results'])[1]").click()

    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(5)

    context.driver.find_element(By.XPATH, "(//span[normalize-space()='No'])[1]").click()
    context.driver.find_element(By.ID, "select2-KSAResidentStatusForNonSaudiCountriesList-container").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//input[@role='textbox'])[2]").send_keys("United")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//span[normalize-space()='United Arab Emirates'])[1]").click()

    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(5)

    select = Select(context.driver.find_element(By.ID, "Inputs_MaritalStatusId"))
    select.select_by_value("28")
    context.driver.find_element(By.ID, "PIA14Depen_Txt").send_keys("100")

    context.driver.find_element(By.XPATH, "(//label[normalize-space()='Postgraduate'])[1]").click()
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()
    time.sleep(7)

    #   2. Contact Information
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//label[normalize-space()='English'])[1]").click()
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalAddress").send_keys("Address")
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalCity").send_keys("Karachi")
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalPostalCode").send_keys("1234")
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalProvince").send_keys("Sindh")

    context.driver.find_element(By.ID, "select2-nonKSACountry-container").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//input[@role='textbox'])[1]").send_keys("United")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//span[normalize-space()='United Arab Emirates'])[1]").click()

    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()
    step_capture_screenshot(context)
    time.sleep(7)

    step_Account_Opening_With_GCC(context)

def step_KSA_National(context):

    objRMPage = RMPage(context.driver)
    objRMPage.LoginAccountOpening()
    step_capture_screenshot(context)
    time.sleep(3)
    #time.sleep(3)
    context.driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/form/div[1]/div").click()
    time.sleep(3)
    dropdown_element = (context.driver.find_element(By.XPATH,
                                                        "/html/body/main/div/div/div/div/div/div/form/div[1]/div/select/option[2]")).click()
    # /html/body/main/div/div/div/div/div/div/form/div[1]/div/select/option[4]
    # //*[@id="ddlApplicantType"]/option[5]
    context.driver.find_element(By.ID, "txtIdentificationNumber").send_keys("12345" + ran_num)
    step_capture_screenshot(context)
    context.driver.find_element(By.ID, "btnVerifyNin").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@id='btnProceedForNationalsAndResidents']").click()
    context.driver.find_element(By.XPATH, "//button[@id='btnSendVerificationRequest']").click()
    time.sleep(7)
    proceed_Button = context.driver.find_element(By.XPATH, "(//button[normalize-space()='Proceed'])[1]")
    print(proceed_Button)
    #TryAgain_Button = context.driver.find_element(By.XPATH, "//button[@id='btnTryAgain']")

    if proceed_Button.is_displayed():
        time.sleep(4)
        print("proceed_Button")
        context.driver.find_element(By.XPATH, "(//button[normalize-space()='Proceed'])[1]").click()
    else:
        time.sleep(8)
        print("proceed_ButtonNot")
        context.driver.find_element(By.XPATH, "//button[@id='btnTryAgain']").click()
        time.sleep(8)
        context.driver.find_element(By.XPATH, "//button[@id='btnSendVerificationRequest']").click()
        time.sleep(7)
        context.driver.find_element(By.XPATH, "(//button[normalize-space()='Proceed'])[1]").click()

    context.driver.find_element(By.ID, "Inputs_TitleId").click()
    # Engr
    context.driver.find_element(By.XPATH,
                                "/html/body/main/main/div/div/div/form/div[1]/div[1]/div[1]/div/div/select/option[4]").click()
    #  Do you have another nationality?*
    context.driver.find_element(By.XPATH, "(//span[normalize-space()='No'])[1]").click()
    # Level of education
    context.driver.find_element(By.XPATH, "(//label[normalize-space()='Postgraduate'])[1]").click()
    time.sleep(7)
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()
    # Preferred language for correspondence*
    context.driver.find_element(By.XPATH, "(//label[normalize-space()='English'])[1]").click()
    time.sleep(4)
    step_capture_screenshot(context)
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()
    time.sleep(4)

    step_Account_Opening_With_KSA(context)

def step_KSA_Resident(context):

    objRMPage = RMPage(context.driver)
    objRMPage.LoginAccountOpening()
    step_capture_screenshot(context)
    time.sleep(3)

    context.driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/form/div[1]/div").click()
    time.sleep(3)
    dropdown_element = (context.driver.find_element(By.XPATH,
                                                        "/html/body/main/div/div/div/div/div/div/form/div[1]/div/select/option[3]")).click()
    # /html/body/main/div/div/div/div/div/div/form/div[1]/div/select/option[4]
    # //*[@id="ddlApplicantType"]/option[5]
    context.driver.find_element(By.ID, "txtIdentificationNumber").send_keys("23456" + ran_num)
    step_capture_screenshot(context)
    context.driver.find_element(By.ID, "btnVerifyNin").click()
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@id='btnProceedForNationalsAndResidents']").click()
    context.driver.find_element(By.XPATH, "//button[@id='btnSendVerificationRequest']").click()
    time.sleep(7)
    proceed_Button = context.driver.find_element(By.XPATH, "(//button[normalize-space()='Proceed'])[1]")
    print(proceed_Button)
    # TryAgain_Button = context.driver.find_element(By.XPATH, "//button[@id='btnTryAgain']")
    if proceed_Button.is_displayed():
        time.sleep(8)
        print("proceed_Button")
        context.driver.find_element(By.XPATH, "(//button[normalize-space()='Proceed'])[1]").click()
        step_capture_screenshot(context)
    else:
        time.sleep(8)
        print("proceed_ButtonNot")
        context.driver.find_element(By.XPATH, "//button[@id='btnTryAgain']").click()
        time.sleep(8)
        context.driver.find_element(By.XPATH, "//button[@id='btnSendVerificationRequest']").click()
        step_capture_screenshot(context)
        time.sleep(7)
        context.driver.find_element(By.XPATH, "(//button[normalize-space()='Proceed'])[1]").click()
    # Title
    context.driver.find_element(By.ID, "Inputs_TitleId").click()
    # Engr
    context.driver.find_element(By.XPATH,
                                "/html/body/main/main/div/div/div/form/div[1]/div[1]/div[1]/div/div/select/option[4]").click()
    #  Do you have another nationality?*
    context.driver.find_element(By.XPATH, "(//span[normalize-space()='No'])[1]").click()
    # No. of dependants
    context.driver.find_element(By.ID, "PIA14Depen_Txt").send_keys("100")
    # Level of education
    context.driver.find_element(By.XPATH, "(//label[normalize-space()='Postgraduate'])[1]").click()
    time.sleep(7)
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()
    step_capture_screenshot(context)
    #   2. Contact Information
    time.sleep(3)
    context.driver.find_element(By.XPATH, "(//label[normalize-space()='English'])[1]").click()
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalAddress").send_keys("Address")
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalCity").send_keys("Karachi")
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalPostalCode").send_keys("1234")
    context.driver.find_element(By.ID, "Inputs_NonKsaNationalProvince").send_keys("Sindh")

    context.driver.find_element(By.ID, "select2-nonKSACountry-container").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//input[@role='textbox'])[1]").send_keys("United")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "(//span[normalize-space()='United Arab Emirates'])[1]").click()
    step_capture_screenshot(context)
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()
    time.sleep(7)

    step_Account_Opening_With_KSA(context)

def step_Account_Opening_With_KSA(context):

    #   3. Professional Information

    # Employment status
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline mb-4'])[3]").click()
    step_capture_screenshot(context)
    # Save and next
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()

    time.sleep(5)

    #   4. Client Classification

    # Are you a qualified investor? Yes
    context.driver.find_element(By.XPATH, "//label[@for='radQualifiedInvestor']").click()
    # Please select from the following criteria:
    context.driver.find_element(By.XPATH, "(//label[@for='chkQualifiedInvestorCriteria_808'])[1]").click()
    context.driver.find_element(By.XPATH, "//label[@for='chkQualifiedInvestorCriteria_809']").click()
    context.driver.find_element(By.XPATH, "//label[@for='chkQualifiedInvestorCriteria_810']").click()

    # What is your approximate annual income (in SAR)?
    select = Select(context.driver.find_element(By.XPATH, "(//select[@id='AnnualIncomeId'])[1]"))
    select.select_by_value("55")
    # What is your approximate net worth  excluding residence (in SAR)?
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='Inputs_NetWorthId']"))
    select.select_by_value("55")
    step_capture_screenshot(context)
    # Source of investment funds?
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Income from own business']").click()
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Existing investment portfolio']").click()
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Gift or inheritance from a third party']").click()

    # Will you be the beneficial owner of this account?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[4]").click()
    # Please provide the name of the beneficial owner
    context.driver.find_element(By.XPATH, "(//input[@id='Inputs_NameOfTheBeneficialOwner'])[1]").send_keys("Address")

    actions = ActionChains(context.driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(5)

    # Financial Experience

    # How would you evaluate your investment knowledge and experience?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[7]").click()

    # Have you worked in the financial sector in the past five years?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[8]").click()

    # Do you have any other practical experience related to the financial sector?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[10]").click()

    # Do you have a degree or professional certification in finance or investment?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[13]").click()
    step_capture_screenshot(context)
    # Expected number of transactions?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[16]").click()

    # Please estimate the total value of those transactions (in SAR).
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='Inputs_PleaseEstimateTheTotalVolumeOfThoseTransactionsId']"))
    select.select_by_value("965")

    # How have you made (the majority of)these investments?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[17]").click()

    # Number of years of investment in securities
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='Inputs_ForHowManyYearsHaveYouInvestedFinancialSecuritiesId']"))
    select.select_by_value("88")
    step_capture_screenshot(context)
    # What types of investments have you made in the past?
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Public equity']").click()
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Private equity']").click()
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Real estate']").click()

    # Have you conducted any margin transactions in the past five years?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[20]").click()

    # Risk Profile Questionnaire

    # medium     low ,   high

    step_Risk_Type(context, "high")
    step_capture_screenshot(context)
    #  Other Information

    # Are you a member of the Board of Directors, an audit committee member, or a senior executive at a publicly listed company?
    context.driver.find_element(By.XPATH, "//body[1]/main[1]/main[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[25]/div[1]/div[1]/div[1]/div[2]").click()

    # Are you related to a member of the Board of Directors, an audit committee member, or a senior executive at a publicly listed company?
    context.driver.find_element(By.XPATH,
                                "//body[1]/main[1]/main[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[26]/div[1]/div[1]/div[1]/div[2]").click()

    # Are you entrusted with a prominent position?
    context.driver.find_element(By.XPATH,
                                "//body[1]/main[1]/main[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[27]/div[1]/div[1]/div[1]/div[2]").click()

    # Do you have a relationship (by blood or marriage up to the second degree) or association with a person entrusted with a prominent public function in the Kingdom or a foreign country, senior management positions, or a position in an international organization?
    context.driver.find_element(By.XPATH,
                                "//body[1]/main[1]/main[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[28]/div[1]/div[1]/div[1]/div[2]").click()
    # Is there any other financial information that you would like to disclose?
    context.driver.find_element(By.XPATH,
                                "(//input[@id='Inputs_IsThereAnyOtherFinancialInformationThatYouWouldLikeToDisclose'])[1]").send_keys("Address")

    step_capture_screenshot(context)
    # Save and next
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()

    #   Investment Portfolio

    # 5. Investment Information

    # Do you have an existing portfolio?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[1]").click()

    # What is the value of your existing portfolio (in SAR)?
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='Inputs_ExistingPortfolioId']"))
    select.select_by_value("56")

    # How long have you held these investments?
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='Inputs_HowLongHaveYouHeldTheseInvestmentId']"))
    select.select_by_value("521")

    # What is the breakdown of your existing investment portfolio?
    context.driver.find_element(By.XPATH, "(//input[@id='ExistingInvestmentPortfolio0'])[1]").send_keys( "100")

    # Have you invested in financial securities outside Saudi Arabia?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[4]").click()

    # What is your debt to investment ratio?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[9]").click()
    step_capture_screenshot(context)
    # Target Portfolio

    # What are your general investment objectives?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[10]").click()

    # The period during which the client expects to cash out the invested money?
    select = Select(context.driver.find_element(By.XPATH, "(//select[@id='Inputs_WhatIsYourExpectedTimeHorizonForRedeemingYourInvestment'])[1]"))
    select.select_by_value("524")

    # What is your preferred investment currency?
    context.driver.find_element(By.XPATH, "(//div[@class='form__checkbox form-check-inline'])[1]").click()

    # Do you have any restrictions on the markets in which to invest?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[18]").click()

    # Do you have any restrictions on the type of securities in which to invest?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[20]").click()

    medium_radio = context.driver.find_element(By.XPATH, "(//input[@id='radRiskAppetite_787'])[1]")
    low_radio = context.driver.find_element(By.XPATH, "//input[@id='radRiskAppetite_788']")
    high_radio = context.driver.find_element(By.XPATH, "(//input[@id='radRiskAppetite_786'])[1]")
    
    # Check which radio button is selected
    if medium_radio.is_selected():
        # What is the breakdown of your ideal investment portfolio?
        context.driver.find_element(By.XPATH, "//input[@id='TargetInvestmentPortfolio_medium0']").send_keys("100")
        step_capture_screenshot(context)
        print("It is medium")
    elif low_radio.is_selected():
        # What is the breakdown of your ideal investment portfolio?
        context.driver.find_element(By.XPATH, "//input[@id='TargetInvestmentPortfolio_low0']").send_keys("100")
        step_capture_screenshot(context)
        print("It is low")
    elif high_radio.is_selected():
        # What is the breakdown of your ideal investment portfolio?
        context.driver.find_element(By.XPATH, "//input[@id='TargetInvestmentPortfolio_high0']").send_keys("100")
        step_capture_screenshot(context)
        print("It is high")
    else:
        # What is the breakdown of your ideal investment portfolio?
        print("Nothing")

    # Save and next
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()

    # What type of bank account would you like to add?
    # Bank name
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='BACI_F1_BANK_ddl']"))
    select.select_by_value("856")

    # Beneficiary name
    context.driver.find_element(By.XPATH, "//input[@id='BACI_F3_BeneficiaryName_Txt']").send_keys("Auto Bank")

    # IBAN
    context.driver.find_element(By.XPATH, "//input[@id='BACI_F4_IBAN_Txt']").send_keys("SA6576785769857854")
    step_capture_screenshot(context)
    # Add
    context.driver.find_element(By.XPATH, "//button[@id='btnAddKsaBank']").click()

    # Custodian Information
    # Do you have a custodian?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[8]").click()
    step_capture_screenshot(context)
    # Save and next
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()

    #   7. Tax Declaration

    # Are you a US citizen or resident?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[2]").click()
    time.sleep(2)
    # Do you have an immigrant visa or permanent residency  in a country other than Saudi Arabia?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[4]").click()
    time.sleep(2)
    # Are you a tax resident of any country or countries outside of Saudi Arabia? By selecting ‘No’.
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[18]").click()
    time.sleep(2)
    step_capture_screenshot(context)
    # Save and next
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()
    time.sleep(2)
    # Locate the modal element
    modal = context.driver.find_element(By.XPATH, "//section[@id='modalTermsAndConditions']//div[@class='modal__content']")  # Replace with the actual ID of your modal
    # Scroll down within the modal using JavaScript
    context.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    step_capture_screenshot(context)
    # Accept
    context.driver.find_element(By.XPATH, "//button[@id='btnSubmitTaxDeclarationConsent']").click()
    #   Document Vault
    #   KSA     GCC
    step_documentType(context, "KSA")
    step_capture_screenshot(context)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(5)
    # Save and next
    context.driver.find_element(By.XPATH, "(//button[normalize-space()='Save and Proceed'])[1]").click()
    # Submit Application
    context.driver.find_element(By.XPATH, "//input[@id='btnSubmitApplication']").click()
    # Locate the modal element
    modal = context.driver.find_element(By.XPATH, "//div[@id='myModal']")  # Replace with the actual ID of your modal

    # Scroll down within the modal using JavaScript
    context.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

    # Accept
    context.driver.find_element(By.XPATH, "//button[@id='btnSubmitTaxDeclarationConsent']").click()
    time.sleep(80)
    step_capture_screenshot(context)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//img[@class='logoutimg']").click()

def step_Account_Opening_With_GCC(context):

    #   3. Professional Information

    # Employment status
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline mb-4'])[3]").click()
    step_capture_screenshot(context)
    # Save and next
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()

    time.sleep(5)

    #   4. Client Classification

    # Are you a qualified investor? Yes
    context.driver.find_element(By.XPATH, "//label[@for='radQualifiedInvestor']").click()
    # Please select from the following criteria:
    context.driver.find_element(By.XPATH, "(//label[@for='chkQualifiedInvestorCriteria_808'])[1]").click()
    context.driver.find_element(By.XPATH, "//label[@for='chkQualifiedInvestorCriteria_809']").click()
    context.driver.find_element(By.XPATH, "//label[@for='chkQualifiedInvestorCriteria_810']").click()

    # What is your approximate annual income (in SAR)?
    select = Select(context.driver.find_element(By.XPATH, "(//select[@id='AnnualIncomeId'])[1]"))
    select.select_by_value("55")
    # What is your approximate net worth  excluding residence (in SAR)?
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='Inputs_NetWorthId']"))
    select.select_by_value("55")
    step_capture_screenshot(context)
    # Source of investment funds?
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Income from own business']").click()
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Existing investment portfolio']").click()
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Gift or inheritance from a third party']").click()

    # Will you be the beneficial owner of this account?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[4]").click()
    # Please provide the name of the beneficial owner
    context.driver.find_element(By.XPATH, "(//input[@id='Inputs_NameOfTheBeneficialOwner'])[1]").send_keys("Address")

    actions = ActionChains(context.driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(5)

    # Financial Experience

    # How would you evaluate your investment knowledge and experience?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[7]").click()

    # Have you worked in the financial sector in the past five years?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[8]").click()

    # Do you have any other practical experience related to the financial sector?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[10]").click()

    # Do you have a degree or professional certification in finance or investment?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[13]").click()
    step_capture_screenshot(context)
    # Expected number of transactions?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[16]").click()

    # Please estimate the total value of those transactions (in SAR).
    select = Select(context.driver.find_element(By.XPATH,
                                                "//select[@id='Inputs_PleaseEstimateTheTotalVolumeOfThoseTransactionsId']"))
    select.select_by_value("965")

    # How have you made (the majority of)these investments?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[17]").click()

    # Number of years of investment in securities
    select = Select(context.driver.find_element(By.XPATH,
                                                "//select[@id='Inputs_ForHowManyYearsHaveYouInvestedFinancialSecuritiesId']"))
    select.select_by_value("88")
    step_capture_screenshot(context)
    # What types of investments have you made in the past?
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Public equity']").click()
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Private equity']").click()
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Real estate']").click()

    # Have you conducted any margin transactions in the past five years?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[20]").click()

    # Risk Profile Questionnaire

    # medium     low ,   high

    step_Risk_Type(context, "medium")
    step_capture_screenshot(context)
    #  Other Information

    # Are you a member of the Board of Directors, an audit committee member, or a senior executive at a publicly listed company?
    context.driver.find_element(By.XPATH,
                                "//body[1]/main[1]/main[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[25]/div[1]/div[1]/div[1]/div[2]").click()

    # Are you related to a member of the Board of Directors, an audit committee member, or a senior executive at a publicly listed company?
    context.driver.find_element(By.XPATH,
                                "//body[1]/main[1]/main[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[26]/div[1]/div[1]/div[1]/div[2]").click()

    # Are you entrusted with a prominent position?
    context.driver.find_element(By.XPATH,
                                "//body[1]/main[1]/main[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[27]/div[1]/div[1]/div[1]/div[2]").click()

    # Do you have a relationship (by blood or marriage up to the second degree) or association with a person entrusted with a prominent public function in the Kingdom or a foreign country, senior management positions, or a position in an international organization?
    context.driver.find_element(By.XPATH,
                                "//body[1]/main[1]/main[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[28]/div[1]/div[1]/div[1]/div[2]").click()
    # Is there any other financial information that you would like to disclose?
    context.driver.find_element(By.XPATH,
                                "(//input[@id='Inputs_IsThereAnyOtherFinancialInformationThatYouWouldLikeToDisclose'])[1]").send_keys(
        "Address")

    step_capture_screenshot(context)
    # Save and next
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()

    #   Investment Portfolio

    # 5. Investment Information

    # Do you have an existing portfolio?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[1]").click()

    # What is the value of your existing portfolio (in SAR)?
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='Inputs_ExistingPortfolioId']"))
    select.select_by_value("56")

    # How long have you held these investments?
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='Inputs_HowLongHaveYouHeldTheseInvestmentId']"))
    select.select_by_value("521")

    # What is the breakdown of your existing investment portfolio?
    context.driver.find_element(By.XPATH, "(//input[@id='ExistingInvestmentPortfolio0'])[1]").send_keys("100")

    # Have you invested in financial securities outside Saudi Arabia?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[4]").click()

    # What is your debt to investment ratio?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[9]").click()
    step_capture_screenshot(context)
    # Target Portfolio

    # What are your general investment objectives?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[10]").click()

    # The period during which the client expects to cash out the invested money?
    select = Select(context.driver.find_element(By.XPATH,
                                                "(//select[@id='Inputs_WhatIsYourExpectedTimeHorizonForRedeemingYourInvestment'])[1]"))
    select.select_by_value("524")

    # What is your preferred investment currency?
    context.driver.find_element(By.XPATH, "(//div[@class='form__checkbox form-check-inline'])[1]").click()

    # Do you have any restrictions on the markets in which to invest?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[18]").click()

    # Do you have any restrictions on the type of securities in which to invest?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[20]").click()

    medium_radio = context.driver.find_element(By.XPATH, "(//input[@id='radRiskAppetite_787'])[1]")
    low_radio = context.driver.find_element(By.XPATH, "//input[@id='radRiskAppetite_788']")
    high_radio = context.driver.find_element(By.XPATH, "(//input[@id='radRiskAppetite_786'])[1]")

    # Check which radio button is selected
    if medium_radio.is_selected():
        # What is the breakdown of your ideal investment portfolio?
        context.driver.find_element(By.XPATH, "//input[@id='TargetInvestmentPortfolio_medium0']").send_keys("100")
        step_capture_screenshot(context)
        print("It is medium")
    elif low_radio.is_selected():
        # What is the breakdown of your ideal investment portfolio?
        context.driver.find_element(By.XPATH, "//input[@id='TargetInvestmentPortfolio_low0']").send_keys("100")
        step_capture_screenshot(context)
        print("It is low")
    elif high_radio.is_selected():
        # What is the breakdown of your ideal investment portfolio?
        context.driver.find_element(By.XPATH, "//input[@id='TargetInvestmentPortfolio_high0']").send_keys("100")
        step_capture_screenshot(context)
        print("It is high")
    else:
        # What is the breakdown of your ideal investment portfolio?
        print("Nothing")

    # Save and next
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()

    # What type of bank account would you like to add?
    # Bank name
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='BACI_F1_BANK_ddl']"))
    select.select_by_value("856")

    # Beneficiary name
    context.driver.find_element(By.XPATH, "//input[@id='BACI_F3_BeneficiaryName_Txt']").send_keys("Auto Bank")

    # IBAN
    context.driver.find_element(By.XPATH, "//input[@id='BACI_F4_IBAN_Txt']").send_keys("SA6576785769857854")
    step_capture_screenshot(context)
    # Add
    context.driver.find_element(By.XPATH, "//button[@id='btnAddKsaBank']").click()

    # Custodian Information
    # Do you have a custodian?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[8]").click()
    step_capture_screenshot(context)
    # Save and next
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()

    #   7. Tax Declaration

    # Are you a US citizen or resident?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[2]").click()
    time.sleep(2)
    # Do you have an immigrant visa or permanent residency  in a country other than Saudi Arabia?
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[4]").click()
    time.sleep(2)
    # Are you a tax resident of any country or countries outside of Saudi Arabia? By selecting ‘No’.
    context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[18]").click()
    time.sleep(2)
    step_capture_screenshot(context)
    # Save and next
    context.driver.find_element(By.XPATH, "(//input[@id='btnNext'])[1]").click()
    time.sleep(2)
    # Locate the modal element
    modal = context.driver.find_element(By.XPATH,
                                        "//section[@id='modalTermsAndConditions']//div[@class='modal__content']")  # Replace with the actual ID of your modal
    # Scroll down within the modal using JavaScript
    context.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    step_capture_screenshot(context)
    # Accept
    context.driver.find_element(By.XPATH, "//button[@id='btnSubmitTaxDeclarationConsent']").click()
    #   Document Vault
    #   KSA     GCC
    step_documentType(context, "GCC")
    step_capture_screenshot(context)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(5)
    # Save and next
    context.driver.find_element(By.XPATH, "(//button[normalize-space()='Save and Proceed'])[1]").click()
    # Submit Application
    context.driver.find_element(By.XPATH, "//input[@id='btnSubmitApplication']").click()
    # Locate the modal element
    modal = context.driver.find_element(By.XPATH, "//div[@id='myModal']")  # Replace with the actual ID of your modal

    # Scroll down within the modal using JavaScript
    context.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

    # Accept
    context.driver.find_element(By.XPATH, "//button[@id='btnSubmitTaxDeclarationConsent']").click()
    time.sleep(80)
    step_capture_screenshot(context)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//img[@class='logoutimg']").click()


def step_Risk_Type(context, risk_type):

        if risk_type == "low":

            # What is the extent of your knowledge / experience in the investment products and stock markets field?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[21]").click()
            # What is your main objective from investing in securities?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[24]").click()
            #How long do you intend / want to keep your funds invested in the securities?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[27]").click()
            # Which of the investment options below would you prefer to follow in order to invest an amount of ten thousand riyals for more than a year?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[30]").click()
            # What is the percentage of the total assets that you wish to invest in the securities?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[33]").click()
            # What is the highest annual loss that you have suffered in your investment?
            context.driver.find_element(By.XPATH, "//body[1]/main[1]/main[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[22]/div[1]/div[1]/div[1]/div[1]").click()
            # What was your reaction when the loss mentioned in the previous question had occurred?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[39]").click()

            print("Risk type is low.")
        elif risk_type == "medium":

            # What is the extent of your knowledge / experience in the investment products and stock markets field?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[22]").click()
            # What is your main objective from investing in securities?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[25]").click()
            # How long do you intend / want to keep your funds invested in the securities?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[28]").click()
            # Which of the investment options below would you prefer to follow in order to invest an amount of ten thousand riyals for more than a year?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[31]").click()
            # What is the percentage of the total assets that you wish to invest in the securities?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[34]").click()
            # What is the highest annual loss that you have suffered in your investment?
            context.driver.find_element(By.XPATH,"(//div[@class='form__radio form-check-inline'])[37]").click()
            # What was your reaction when the loss mentioned in the previous question had occurred?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[40]").click()

            print("Risk type is medium.")
        elif risk_type == "high":

            # What is the extent of your knowledge / experience in the investment products and stock markets field?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[23]").click()
            # What is your main objective from investing in securities?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[26]").click()
            # How long do you intend / want to keep your funds invested in the securities?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[29]").click()
            # Which of the investment options below would you prefer to follow in order to invest an amount of ten thousand riyals for more than a year?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[32]").click()
            # What is the percentage of the total assets that you wish to invest in the securities?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[35]").click()
            # What is the highest annual loss that you have suffered in your investment?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[38]").click()
            # What was your reaction when the loss mentioned in the previous question had occurred?
            context.driver.find_element(By.XPATH, "(//div[@class='form__radio form-check-inline'])[41]").click()

            print("Risk type is high.")

        else:
            print("Risk type is Nothing.")
def step_documentType(context, documentType):

    # Copy of Passport
    if documentType == "GCC":
        context.driver.find_element(By.XPATH, "(//input[@id='file1'])[1]").send_keys(
        r"C:\Users\Administrator\Desktop\Automation\Doc1.pdf")
        time.sleep(2)
        # Identification Letter for Non-Saudi
        context.driver.find_element(By.XPATH, "(//input[@id='file2'])[1]").send_keys(
        r"C:\Users\Administrator\Desktop\2024-08-21_20h45_31.png")
        time.sleep(2)
        # Signature specimen
        context.driver.find_element(By.XPATH, "(//input[@id='file3'])[1]").send_keys(
        r"C:\Users\Administrator\Desktop\Automation\Doc1.pdf")
        time.sleep(3)
    elif documentType == "KSA":
        context.driver.find_element(By.XPATH, "//input[@id='file3']").send_keys(
            r"C:\Users\Administrator\Desktop\Automation\Doc1.pdf")
        time.sleep(2)
    else:
        print("Document type is Nothing.")

def step_KYC_GCC_National(context):

    context.driver.switch_to.window(context.driver.window_handles[1])
    time.sleep(5)
    try:
        time.sleep(15)
        context.driver.find_element(By.XPATH, "//a[normalize-space()='Back to Inbox']").click()
    finally:

        time.sleep(4)
        context.driver.find_element(By.XPATH, "//td[normalize-space()='Welcome to SEDCO Capital']").click()
        time.sleep(2)
        # Execute JavaScript to open a new tab
        # Scroll down the page by pixel
        iframe = context.driver.find_element(By.XPATH, "(//iframe[@id='html_msg_body'])[1]")
        context.driver.switch_to.frame(iframe)
        print(iframe)
        # time.sleep(7)
        actions = ActionChains(context.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        #actions.send_keys(Keys.ENTER)
        #actions.perform()
        context.driver.find_element(By.XPATH, "(//a[normalize-space()='Setup Account Credentials'])[1]").send_keys(Keys.ARROW_DOWN)
        context.driver.find_element(By.XPATH, "(//a[normalize-space()='Setup Account Credentials'])[1]").click()
        time.sleep(7)
        context.driver.switch_to.window(context.driver.window_handles[1])
        time.sleep(8)
        context.driver.find_element(By.XPATH, "//a[normalize-space()='Back to Inbox']").click()
        time.sleep(8)
        context.driver.find_element(By.XPATH,
         "(//td[@class='ng-binding'][normalize-space()='Authentication Code (OTP)'])[1]").click()
        time.sleep(8)
        iframe = context.driver.find_element(By.XPATH, "//iframe[@id='html_msg_body']")
        time.sleep(8)
        context.driver.switch_to.frame(iframe)
        print(iframe)
        OTP = context.driver.find_element(By.XPATH,
         "/html/body/table/tbody/tr/td/center/table/tbody/tr/td/table[3]/tbody/tr/th[2]/table/tbody/tr/th/p[2]/span")
        Verify = OTP.text
        print(Verify)
        context.driver.switch_to.window(context.driver.window_handles[2])
        time.sleep(4)
        context.driver.find_element(By.XPATH, "(//input[@id='txtVerificationCode'])[1]").send_keys(Verify)
        context.driver.find_element(By.XPATH, "//button[@id='btnConfirmCode']").click()
        time.sleep(4)
        context.driver.find_element(By.XPATH, "//input[@id='txtEmail']").send_keys(dummy_KYC_Users)
        context.driver.find_element(By.XPATH, "//input[@id='txtConfirmEmail']").send_keys("Abc@123456")
        context.driver.find_element(By.XPATH, "//button[@id='btnSubmit']").click()
        time.sleep(8)

        context.driver.find_element(By.XPATH, "//button[normalize-space()='Back to home']").click()
        time.sleep(8)

        context.driver.find_element(By.XPATH, "//a[normalize-space()='KYC Update']").click()
        context.driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys(dummy_KYC_Users)
        context.driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("Abc@123456")
        context.driver.find_element(By.XPATH, "//button[@id='btnSubmit']").click()
        #context.driver.switch_to.window(context.driver.window_handles[1])

        context.driver.find_element(By.XPATH, "//input[@id='txtVerificationCode']").send_keys("2244")
        context.driver.find_element(By.XPATH, "//button[@id='btnConfirmCode']").click()

        # Create an ActionChains instance
        actions = ActionChains(context.driver)
        # Send the END key to scroll to the bottom of the page
        actions.send_keys(Keys.END).perform()

        time.sleep(6)
        context.driver.find_element(By.ID, "btnSubmit").click()
        time.sleep(60)

