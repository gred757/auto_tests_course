from concurrent.futures import BrokenExecutor

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get('http://suninjuly.github.io/wait2.html')

    button = WebDriverWait(browser, 5).until(
        ES.element_to_be_clickable((By.ID, 'verify'))
    )

    # button = browser.find_element(By.ID, 'verify')
    button.click()
    message = browser.find_element(By.ID, 'verify_message')

    assert 'successful' in message.text
finally:
    time.sleep(15)
    browser.quit()


