
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)
title = "Your Stoe"
driver.get_screenshot_as_png()
assert driver.title.__eq__(title)

print(driver.title)
scroll_down = driver.find_element(By.XPATH, "//h5[contains(text(), 'Information')]")

driver.execute_script("arguments[0].scrollIntoView(true)", scroll_down)
time.sleep(5)







