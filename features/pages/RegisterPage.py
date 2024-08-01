import time

from selenium.webdriver.common.by import By


class register_Page:
    def __init__(self,driver):
        self.driver=driver

        self.my_Account_Xpath = "//a[@title = 'My Account']"
        self.register_Xpath = "//a[text()='Register']"
        self.firstname_Xpath = "//input[@name='firstname']"
        self.lastname_Xpath =  "//input[@name='lastname']"
        self.email_Xpath = "//input[@name='email']"
        self.telephone_Xpath = "//input[@name='telephone']"
        self.password_Xpath = "//input[@name='password']"
        self.confirm_Xpath = "//input[@name='confirm']"
        self.agree_Xpath = "//input[@name='agree']"
        self.continue_Xpath = "//input[@type='submit']"
        self.error_message_Xpath = "//div[text()='First Name must be between 1 and 32 characters!']"


    def landing_page(self):
        self.driver.find_element(By.XPATH,self.my_Account_Xpath).click()
        self.driver.find_element(By.XPATH,self.register_Xpath).click()

    def register_details(self,firstname,lastname,email,telephone,password,confirm):
        self.driver.find_element(By.XPATH,self.firstname_Xpath).send_keys(firstname)
        self.driver.find_element(By.XPATH,self.lastname_Xpath).send_keys(lastname)
        self.driver.find_element(By.XPATH,self.email_Xpath).send_keys(email)
        self.driver.find_element(By.XPATH,self.telephone_Xpath).send_keys(telephone)
        self.driver.find_element(By.XPATH,self.password_Xpath).send_keys(password)
        self.driver.find_element(By.XPATH,self.confirm_Xpath).send_keys(confirm)
        self.driver.find_element(By.XPATH,self.agree_Xpath).click()

    def click_Continue(self):
        self.driver.find_element(By.XPATH,self.continue_Xpath).click()

    def error_message(self,err_msg):
         assert self.driver.find_element(By.XPATH,self.error_message_Xpath).text.__eq__(err_msg)

time.sleep(10)

