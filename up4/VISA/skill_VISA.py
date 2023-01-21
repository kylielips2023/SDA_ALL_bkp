import pickle
import undetected_chromedriver as uc
import time
import chrom_v1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import bin00

kol=["4790565102491063","10","24","110"]

def generate_bin():
    print("generate bin")




def bin_operation():
    print("------------------------------------------------------------------")
    print(" _GET THE LAST BIN ",end='',flush=True)
    arry_card_all_info=[]
    the_last_bin=bin00.read_the_last_bin()
    # time.sleep(1)
    print(" _LAST BIN : [  "+the_last_bin+"  ]")
    arry_card_bin_info=bin00.generate_card_from_bin(the_last_bin)
    # arry_card_all_info.extend((card_num,card_date,card_ccv))
    # print(card_num,card_date,card_ccv)
    # print(arry_card_bin_info)
    return arry_card_bin_info


def switch_to_iframe_1(browser,kol):
    browser.switch_to.default_content()
    time.sleep(2)
    browser.switch_to.frame(1)
    # time.sleep(5)
    try:
        singup_green_button=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'Field-numberInput')))
        singup_green_button.send_keys(kol[0],Keys.TAB,kol[1],Keys.TAB,kol[2])
        print("FILLING ALL ")
        # input("")
    except Exception as e:
        print(str(e))
        pass





def switch_to_iframe(browser,kol):
    browser.switch_to.default_content()
    time.sleep(2)
    browser.switch_to.frame(0)
    # time.sleep(5)
    try:
        singup_green_button=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'Field-numberInput')))
        singup_green_button.send_keys(kol[0],Keys.TAB,kol[1],Keys.TAB,kol[2])
        print("FILLING ALL ")
        # input("")
    except Exception as e:
        switch_to_iframe_1(browser,kol)
        print(str(e))
        






def go_fill(browser):
    arry_card_bin_info=bin_operation()
    kol=arry_card_bin_info
    switch_to_iframe(browser,kol)


    # input("")
        # browser.switch_to.default_content()
        # time.sleep(2)
        # browser.switch_to.frame(1)
        # singup_green_button=WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, 'Field-numberInput')))
        # singup_green_button.send_keys(kol[0],Keys.TAB,kol[1],Keys.TAB,kol[2])
        # print("FILLING ALL ")
    browser.switch_to.default_content()
    try:
        singup_green_button=WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-checkout"]/div/div[1]/form/div[2]/div[2]/div[2]/div[2]/div/button')))
        print("Start Subscribing")
        singup_green_button.click()


    except Exception as e:
        print(str(e))


    try:
        singup_green_button=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-checkout"]/div/div[1]/form/div[1]/div/div[2]/div[1]/div/div[1]/div/p')))
        print("ilad : "+singup_green_button.text)
        bin00.add_to_last_bin()
        browser.get("https://www.skillshare.com/en/membership/checkout")
        # input("gggg")
        go_fill(browser)
    except Exception as e:
        print(str(e))



def check_pay(browser):

    iframes = browser.find_elements_by_xpath("//iframe")
    browser.switch_to.default_content()
    go_fill(browser)




def runn_ing(browser):
    print("llll")
    try:

        preform_one=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, 'checkout-variant-1')))
        print("llll")
        preform_one.click()
        preform_one.send_keys(Keys.TAB*10,Keys.SPACE)
        print("coockie accepted")
    except Exception as e:
        print("hhhhhhhhhh"+str(e))

def start_session():
    browser=chrom_v1.chrome_session()
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
    print("runn_ing")
    runn_ing(browser)
    check_pay(browser)
    # input("gfg")


if __name__ == '__main__':

    try:
        start_session()
    except:
        print("erroç________")


# 
# bin_operation()