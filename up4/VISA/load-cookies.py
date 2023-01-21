import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def chrome_session():

    options = uc.ChromeOptions()
    options.arguments.extend(["--no-sandbox", "--disable-setuid-sandbox","--disable-web-security"])
    browser = uc.Chrome(options)
    return browser


if __name__ == '__main__':
    browser=chrome_session()
    browser.get('https://www.skillshare.com')
    cookies = pickle.load(open("skill_cookies.pkl", "rb"))
    for cookie in cookies:
        cookie['domain'] = ".skillshare.com"
        
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            # print(str(e))
            pass

    browser.get('https://www.skillshare.com/')

    # time.sleep(120)
    input("gfg")
    browser.get('https://amiunique.org/')
    time.sleep(120)