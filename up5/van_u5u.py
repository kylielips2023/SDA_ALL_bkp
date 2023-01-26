
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
# from my_mod import m_vpn_van
# from my_mod import m_vpn_van
from my_mod import m_vpn
from my_mod import cnf_bvb
from my_mod import drive_md_chrom
from my_mod import caap

# rnd_link=["57q24h07g9ol","vconr1lk7kts","q0femtpjjr3e","co9ftvadm472"]

mon_url=cnf_bvb.rnd_url_4evr

kol=[]
error_log=[]
cardi_number=[]


def my_log_error(error_string):
    print("ADDING ERROR : |E| "+error_string)
    error_log.append(error_string)
    print(error_string)




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
        free_download_click(driver)

    except Exception as e :
        # print(str(e))
        print("passsed")


def click_down(browser):
    print("click_down")
    try:
        browser.switch_to.window(browser.window_handles[0])
        browser.switch_to.default_content()
        bo_free_down=bxp_id(browser,5, 'downloadbtn')
        # countdown countdown
        # countdown_free_down=bxp_id(driver,15, 'countdown')
        bo_free_down.click()
        browser.switch_to.window(browser.window_handles[0])
    except Exception as e:
        print(str(e))
    try:
        time.sleep(5)
        bo2_free_down=bxp_id(browser,15, 'download-btn')
        # countdown countdown
        # countdown_free_down=bxp_id(driver,15, 'countdown')
        bo2_free_down.click()
        browser.switch_to.window(browser.window_handles[0])
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
        browser.switch_to.frame(2)
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

def check_countdown(browser):
    print("check_countdown..... ", end='')
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
        print("still "+waat2)
        time.sleep(int(waat2)+2)
    except Exception as e :
        print("Countdown Not Found")
        # print(str(e))


def check_free_download_click(browser):
    # print("free_download_click")
    print("CHECK !!! free_download_click ..... ", end='')
    try:
        # free_download_click
        # 
        bo_free_down=bxp(browser,3, '/html/body/section/div/div/div[2]/form/input[7]')
        bo_free_down.click()
        browser.switch_to.window(browser.window_handles[0])
        print('clicked aagain ')
        # input('lol')
    except Exception as e :
        # print(str(e))
        print('Not Found')


def free_download_click(browser):
    # print("free_download_click")
    print("free_download_click ..... ", end='')
    try:
        # free_download_click
        # 
        bo_free_down=bxp(browser,15, '/html/body/section/div/div/div[2]/form/input[7]')
        bo_free_down.click()
        browser.switch_to.window(browser.window_handles[0])
        # print('lol')
        # input('lol')
    except Exception as e :
        print(str(e))

    # chec_1(browser)
    check_free_download_click(browser)
    check_countdown(browser)
    # input('lol')

    
        # downloadbtn

    # go_cap(driver)
    go_cap(browser)





#--------------------------------------------
def open_url_and_vist(browser):
    try:
        browser.get(mon_url)
        # input('lol')
        # /html/body/section/div/div/div[2]/form/input[7]
        free_download_click(driver)
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
        m_vpn.fnc_vpn ()
        # input("lol")
        visible_v=cnf_bvb.visible_v
        width ,height=cnf_bvb.resolution_func()
        sz=height+","+width
        display = Display(visible=visible_v, size=(width,height)).start()
        driver=drive_md_chrom.build_driver(sz)
        driver.maximize_window()
        open_url_and_vist(driver)
        time.sleep(2)
        display.stop()
        driver.close()
        driver.quit()

        # start_session()
    except Exception as a:
        print("error in main"+str(a))
    # os.system("pkill chrome")
    driver.quit()
    os.system("rm -rf /tmp/*")

# try:

# except Exception as e :
#     print(str(e))