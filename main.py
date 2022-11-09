# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://100.11.185.178/doc/page/playback.asp")

title = driver.title

driver.implicitly_wait(30)

# Login Page
user_text_box = driver.find_element(by=By.ID, value="username")
user_text_box.send_keys("admin")

pass_text_box = driver.find_element(by=By.ID, value="password")
pass_text_box.send_keys("a1234567")

submit = driver.find_element(By.CSS_SELECTOR, "button")
driver.execute_script("arguments[0].click()", submit)

# Configuration Page

#system_button = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[2]/div[2]/div")
#system_button.click()