from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(_x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    el_btn_troll = browser.find_element(By.CSS_SELECTOR, '.trollface')
    el_btn_troll.click()

    cur_win = browser.window_handles[0]
    new_win = browser.window_handles[1]

    browser.switch_to.window(new_win)

    x = browser.find_element(By.ID, 'input_value').text
    res = calc(x)

    el_answer = browser.find_element(By.ID, 'answer')
    el_answer.send_keys(res)

    el_btn_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    el_btn_submit.click()

finally:
    time.sleep(15)
    browser.quit()
