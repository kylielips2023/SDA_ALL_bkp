import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import names , random

from selenium.webdriver.common.keys import Keys
urls=['@blue-vovo.nl.eu.org','@red-vovo.nl.eu.org','@green-vovo.nl.eu.org']
def gen_na():
    f_na=names.get_first_name(gender='male')
    y = random.randrange(104, 1999)
    random_url=random.choice(urls)
    dogo=f_na+str(y)
    hh_y=f_na+str(y)+random_url
    print(dogo)
    return hh_y ,dogo
# rnd_email=["@red-vovo.nl.eu.org","@green-vovo.nl.eu.org","@blue-vovo.nl.eu.org"]

# def genrate_new_name():
#     print()
#     email_add
#     return email_add
def open_session():

    options = webdriver.ChromeOptions()
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')
    browser = uc.Chrome(options=options,)
    return browser



def start_i(browser):
    email_reg,namee=gen_na()
    print(namee,email_reg)
    try:
        browser.get('https://www.skillshare.com/')
        preform_one=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/section[1]/div[2]/div[3]/div[2]/div/div/div/div/form/div/div[3]/div/div/input')))
        print("email field found")
        browser.execute_script("arguments[0].scrollIntoView();", preform_one)
        preform_one.click()
        preform_one.send_keys(email_reg,Keys.TAB)
        preform_tow=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/section[1]/div[2]/div[3]/div[2]/div/div/div/div/form/div/div[4]/div/div/input')))
        # //*[@id="page-wrapper"]/section[1]/div[2]/div[3]/div[2]/div/div/div/div/form/div/div[4]/div/div/input
        preform_tow.send_keys("baba123A*")
        # //*[@id="page-wrapper"]/section[1]/div[2]/div[3]/div[2]/div/div/div/div/form/div/div[6]/button/span
        preform_tow=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/section[1]/div[2]/div[3]/div[2]/div/div/div/div/form/div/div[6]/button/span')))
        preform_one.click()
        input("visite")
    except Exception as e:
        print("lol error "+str(e))




if __name__ == '__main__':
    email = "tow62@blue-vovo.nl.eu.org"
    password = "baba123A*"
    browser = open_session()
    start_i(browser)


    


    # m 
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