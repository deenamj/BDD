import time

from selenium.webdriver.common.by import By
from selenium import webdriver


class HomePage:
    def __init__(self,driver):
        self.driver = driver


        self.scroll_down_Xpath = "//a[contains(text(), 'Apple Cinema 30')]"
        self.valid_result_Xpath = "//a[contains(text(), 'Apple Cinema 30')]"
        self.invalid_Xapth = "//*[@name='search']"
        self.search_results_Xpath = "//input[@value='Search']/following-sibling::p"
        self.search_box_Xpath = "//*[@name='search']"
        self.click_on_searchbox_Xpath = "//*[@type='button']//i[@class='fa fa-search']"

    def Page_title(self,page_title):
        assert self.driver.title.__eq__(page_title)
        time.sleep(3)
    def send_keys(self,text):
        self.driver.find_element(By.XPATH,self.search_box_Xpath).send_keys(text)
        time.sleep(3)

    def click_search_button(self):
        self.driver.find_element(By.XPATH,self.click_on_searchbox_Xpath).click()
        time.sleep(3)

    def valid_result(self):
        scroll_down = self.driver.find_element(By.XPATH,self.scroll_down_Xpath)

        self.driver.execute_script("arguments[0].scrollIntoView(true)", scroll_down)
        assert self.driver.find_element(By.XPATH,self.valid_result_Xpath).is_displayed()
        time.sleep(3)

    def invalid_result(self,invalid_text):
        self.driver.find_element(By.XPATH,self.invalid_Xapth).send_keys(invalid_text)
        time.sleep(3)

    def search_results(self,expected_result):

        assert self.driver.find_element(By.XPATH,self.search_results_Xpath).text.__eq__(expected_result)
        time.sleep(3)

