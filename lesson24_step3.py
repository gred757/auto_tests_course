from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/wait1.html'



try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get(link)

    # time.sleep(5)
    button = browser.find_element(By.ID, 'verify')
    button.click()

    message = browser.find_element(By.ID, 'verify_message')

    assert('successful' in message.text)
finally:
    time.sleep(15)
    browser.quit()

