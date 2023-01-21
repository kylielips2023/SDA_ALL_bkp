import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    email = "tow62@blue-vovo.nl.eu.org"
    password = "baba123A*"

    options = webdriver.ChromeOptions()
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')
    browser = uc.Chrome(options=options,)
    browser.get('https://www.skillshare.com/')
    # m 
    preform_one=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="site-content"]/div[3]/div[2]/div[2]/div[5]/div/button')))
    preform_one.click()
    input("")
    # browser.find_element(By.ID, 'identifierId').send_keys(email)

    # browser.find_element(
    #     By.CSS_SELECTOR, '#identifierNext > div > button > span').click()

    # password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"

    # WebDriverWait(browser, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))

    # browser.find_element(
    #     By.CSS_SELECTOR, password_selector).send_keys(password)

    # browser.find_element(
    #     By.CSS_SELECTOR, '#passwordNext > div > button > span').click()

    # time.sleep(5)

    cookies = browser.get_cookies()

    pickle.dump(cookies, open("skill_cookies.pkl", "wb"))
    input("")