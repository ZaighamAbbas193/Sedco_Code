import math
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
def before_all(context):

    # Set up a WebDriver instance (in this example, Chrome)
    #context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    pass

def after_all(context):
    # Clean up resources, e.g., close the WebDriver instance
    #context.driver.quit()
    pass

def before_scenario(context, scenario):
    # Any setup that needs to be done before each scenario
    pass

def after_scenario(context, scenario):
    # This hook runs after each scenario
    # Add any cleanup code here if needed
    # Any cleanup that needs to be done after each scenario
    pass

def before_feature(context, feature):
    # This hook runs before each feature
    pass

def after_feature(context, feature):
    # This hook runs after each feature

    pass

