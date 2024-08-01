import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from ConfigReader import configur

def before_scenario(context,driver):
    browser_name = configur.config_reader("basic info","browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


    context.driver.get(configur.config_reader("basic info","url"))
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    print()
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),name="failed_screenshots",attachment_type=AttachmentType.PNG)

