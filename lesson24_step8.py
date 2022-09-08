from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math



def calc(_x):
    return str(math.log(abs(12*math.sin(int(x)))))



link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, 'book')

    buy = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    if buy:
        button.click()
    
    # x = browser.find_element(By.ID, 'input_value').text
    x = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.ID, 'input_value'))
    ).text

    print(x)
    
    if x:
        res = calc(x)

        el_answer = browser.find_element(By.ID, 'answer')
        el_answer.send_keys(res)

        el_btn_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        el_btn_submit.click()
    else:
        print("X is empty!!")
finally:
    time.sleep(15)
    browser.quit()
    