from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains, Keys
import time

from behave import *

from features.pages.HomePage import HomePage


@given(u'Landing page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.Page_title("Your Store")
    #page_title = "Your Store"
    #context.driver.title.__eq__(page_title)

@when(u'I search Valid Product in search box')
def step_impl(context):
    #context.home_page = HomePage(context.driver)
    context.home_page.send_keys("Honda")
    #context.driver.find_element(By.XPATH,"//*[@name='search']").send_keys("Apple")
    #print("Search box")




@when(u'Click on the search button')
def step_impl(context):
    context.home_page.click_search_button()

    #context.home_page.click_search_button()
    #context.driver.find_element(By.XPATH,"//*[@type='button']//i[@class='fa fa-search']").click()




@then(u'I should I see the Valid Result')
def step_impl(context):
    #context.home_page = HomePage(context.driver)
    context.home_page.valid_result()
    #scroll_down = context.driver.find_element(By.XPATH,"//a[contains(text(), 'Apple Cinema 30')]")

    #context.driver.execute_script("arguments[0].scrollIntoView(true)", scroll_down)
    #assert context.driver.find_element(By.XPATH,"//a[contains(text(), 'Apple Cinema 30')]").is_displayed()

@when(u'I search InValid Product in search box')
def step_impl(context):
    #context.home_page = HomePage(context.driver)
    context.home_page.invalid_result("BMW")
    #context.driver.find_element(By.XPATH,).send_keys("BMW")

@then(u'I should I see the InValid Result')
def step_impl(context):
    #context.home_page = HomePage(context.driver)
    context.home_page.search_results("There is no product that matches the search criteria.")
    #expected_result = "There is no product that matches the search criteria."
    #assert context.driver.find_element(By.XPATH,"//input[@value='Search']/following-sibling::p").text.__eq__(expected_result)



