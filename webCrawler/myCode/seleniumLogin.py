import time
import traceback

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import munch

def startChrome():

    options = ChromeOptions()
    # options.add_argument('--kiosk')
    # options.add_argument('--headless')
    # options.add_argument("window-size=1920,1080")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    browser = Chrome(chrome_options=options)
    # browser.maximize_window()

    # 進入登入畫面
    browser.get('https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2F')

    with open(r'C:\Users\Student\Desktop\shopee.password.txt') as f:
        password = f.read()

    try:
        element_username = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="loginKey"]'))
        )
        element_username.send_keys('erinus')

        element_password = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
        )
        element_password.send_keys(f'{password}\n')

        time.sleep(3)

        while True:
            element_verify = None
            elements = browser.find_elements_by_tag_name('div')
            for element in elements:
                if element.get_attribute('innerText') == '使用連結驗證':
                    element_verify = element
                    break
            if element_verify is not None:
                element_verify.click()
                break
            time.sleep(1)
    except:
        e = traceback.format_exc()
        print(e)
        return

    # browser.get_screenshot_as_file('shopee.png')

    time.sleep(3)

    cookies = munch.munchify(browser.get_cookies())
    for cookie in cookies:
        print(f'{cookie.name}: {cookie.value}')

    time.sleep(60)

    browser.quit()

if __name__ == '__main__':
    startChrome()