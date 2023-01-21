
from pathlib import Path
import pickle
import undetected_chromedriver as uc
import time ,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import os, datetime,sys
import calendar


from my_mod import chrom_v1 
from my_mod import bin00
from my_mod import m_vpn_van
# from my_mod import m_vpn_van
from my_mod import cnf_bvb
from my_mod import drive_md_chrom
from my_mod import caap

# rnd_link=["57q24h07g9ol","vconr1lk7kts","q0femtpjjr3e","co9ftvadm472"]

mon_url=cnf_bvb.rnd_url_4evr

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

def bxp(driver,wt ,path):
    SUCCESS_MSG_BUTTON=WebDriverWait(driver, wt).until(EC.presence_of_element_located((By.XPATH, path)))
    return SUCCESS_MSG_BUTTON

def bxp_id(driver,wt ,path):
    SUCCESS_MSG_BUTTON=WebDriverWait(driver, wt).until(EC.presence_of_element_located((By.ID, path)))
    return SUCCESS_MSG_BUTTON

def chec_1(driver):
    try:
        driver.switch_to.window(driver.window_handles[0])
        bo_free_down=bxp(driver,5, '/html/body/div[3]/main/section/div/div/div/div[1]/div/form/span[2]/input')
        try_close_coockies(driver)

    except Exception as e :
        # print(str(e))
        print("passsed")


def click_down(browser):
    print("click_down")
    try:
        browser.switch_to.window(browser.window_handles[0])
        browser.switch_to.default_content()
        bo_free_down=bxp_id(browser,15, 'downloadbtn')
        # countdown countdown
        # countdown_free_down=bxp_id(driver,15, 'countdown')
        bo_free_down.click()
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(5)
        bo2_free_down=bxp_id(browser,15, 'downLoadLinkButton')
        # countdown countdown
        # countdown_free_down=bxp_id(driver,15, 'countdown')
        bo2_free_down.click()


    except Exception as e:
        print(str(e))




def click_audi(browser):
    browser.switch_to.window(browser.window_handles[0])
    iframes =browser.find_elements(by=By.XPATH, value="//iframe")
    try:
        for index , iframe in enumerate(iframes):
            yhio=iframe.get_attribute('title')
            print(str(index)+" -- "+iframe.get_attribute('title'))
            if "expires" in yhio :
                browser.switch_to.frame(int(index))
                time.sleep(2)

                try:
                    singup_green_button=WebDriverWait(browser, 13).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-audio-button"]')))
                    singup_green_button.click()
                    time.sleep(2)
                    try:
                        print("get the source")
                        eto_firstName=WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, 'audio-source')))
                        download_link = eto_firstName.get_attribute('src')
                        # print(download_link)
                        audio_output= caap.audio_fonction(download_link)
                        text_cap=WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID,'audio-response')))
                        text_cap.send_keys(audio_output)
                        time.sleep(2)
                        text_cap.send_keys(Keys.ENTER)
                        print("wwwwwwwwwwwww")
                        time.sleep(2)
                        # donne_ok=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'//span[@aria-checked="true"]')))
                        print("ZZZZZZZZZZZZZZZZZZ")
                        luky_che(browser)
                        # 
                    except Exception as error:
                        print("error audio 222222 "+str(error))
                except Exception as error:
                    print(str(error))
                break
            browser.switch_to.default_content()
            print("wwwwwwwwwwwww")
            time.sleep(2)


    except Exception as error:
        print(str(error))
    click_down(browser)
    time.sleep(2)


def luky_che(browser):
    print("Lucky Start")
    browser.switch_to.default_content()
    time.sleep(2)
    try:
        browser.switch_to.frame(0)
        capa_button=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@aria-checked="true"]')))
        time.sleep(1)
        print("Lucky Succed")
        click_down(browser)

        
    except Exception as e:
        # print(str(e))
        print("No Luck")
    browser.switch_to.default_content()




def go_frame_audio(browser,index):
    print("Start fram audio")
    try:
        cap_button=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]')))
        cap_button.click()
        time.sleep(1)
        print("click recaptcha adio")
        browser.switch_to.window(browser.window_handles[0])  
        # if check_exists_by_xpath('//span[@aria-checked="true"]'): 
        # print(index)
        # browser.switch_to.frame(int(index))
        # browser.switch_to.default_content()
        # time.sleep(2)
        # browser.switch_to.frame(int(index)+3)
    except Exception as e:
        print(str(e))
        pass
    luky_che(browser)






    browser.switch_to.default_content()
    time.sleep(2)
    click_audi(browser)





def go_cap(browser):
    print("Start Caap.........")
    browser.switch_to.window(browser.window_handles[0])
    iframes =browser.find_elements(by=By.XPATH, value="//iframe")
    # input("wwwwwww")

    # iframes = browser.find_elements_by_xpath("//iframe")
    # iframes=browser.find_elements_by_tag_name("iframe")
    # print(str(len(iframes)))
    print('READY TO KILL bCAOTCHA singup')
    #######
    try:
        for index , iframe in enumerate(iframes):
            yhio=iframe.get_attribute('title')
            print(str(index)+" -- "+iframe.get_attribute('title'))
            if "reCAPTCHA" in yhio :

                try:
                    browser.switch_to.frame(int(index))
                    go_frame_audio(browser,index)
                    time.sleep(2)
                except Exception as e :
                    print("not foooond"+str(e))
                    pass

                print("end if")
                browser.switch_to.default_content()
                time.sleep(2)
                break
            # print("end for")
    #######
    except Exception as a:
        print(str(a))
    print("END oF capatcha")


# def go_cap(driver):
#     print("Start Caap.........")
#     try:


#     except Exception as e :
#         print("passsed")


# downLoadLinkButton



def try_close_coockies(browser):
    print("try_close_coockies")
    try:
        
        # try_close_coockies
        # 
        bo_free_down=bxp(browser,15, '/html/body/div[3]/main/section/div/div/div/div[1]/div/form/span[2]/input')
        bo_free_down.click()
        browser.switch_to.window(browser.window_handles[0])


    except Exception as e :
        print(str(e))

    chec_1(browser)

    try:
        browser.switch_to.window(browser.window_handles[0])
        bo_free_down=bxp_id(driver,15, 'downloadbtn')
        # countdown countdown
        countdown_free_down=bxp_id(driver,15, 'countdown')

        # countdown_free_down=bxp(driver,15, '//*[@id="commonId"]/center/div[2]')
        browser.execute_script("arguments[0].scrollIntoView();", countdown_free_down)
        waat=countdown_free_down.text
        waat1=waat.replace("Wait ", "")
        waat2=waat1.replace(" seconds", "")


        print("downloadbtn "+waat2)
        time.sleep(int(waat2)+2)

    except Exception as e :
        print(str(e))
        # downloadbtn

    go_cap(driver)
    # go_cap(browser)





#--------------------------------------------
def visit_play(browser):
    try:
        browser.get(mon_url)
        try_close_coockies(driver)
        print("vist ok delete_all_cookies")
        browser.delete_all_cookies()
        cnf_bvb.clean_up()


    except Exception as e :
        print(str(e))






if __name__ == '__main__':

    try:
        # ccchec()
        print("new")
        cnf_bvb.clean_up()
        # bin00.add_to_last_bin()
        m_vpn_van.fnc_vpn ()
        visible_v=cnf_bvb.visible_v
        width ,height=cnf_bvb.resolution_func()
        sz=height+","+width
        display = Display(visible=visible_v, size=(width,height)).start()
        driver=drive_md_chrom.build_driver(sz)
        driver.maximize_window()
        visit_play(driver)
        time.sleep(2)
        display.stop()

        # start_session()
    except Exception as a:
        print("error in main"+str(a))
    # os.system("pkill chrome")

# try:

# except Exception as e :
#     print(str(e))