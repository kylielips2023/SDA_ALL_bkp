import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import names , random , requests , io, os
from pydub import AudioSegment
import speech_recognition as sr

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

def cokie_get(browser):
    cookies = browser.get_cookies()
    cookies_name="skill_cookies.pkl"

    pickle.dump(cookies, open(cookies_name, "wb"))
    print("coockies saved !!")


def open_session():

    options = webdriver.ChromeOptions()
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')
    browser = uc.Chrome(options=options)
    return browser

def check_brot(browser):
    print("ee")
    get_url = browser.current_url
    print("The current url is:"+str(get_url))
    if 'checkout' in get_url:
        cokie_get(browser)


def audio_fonction(download_link):
    #data = open('1.mp3', 'rb').read()
    # print("ok download_link")
    request = requests.get(download_link)
    # print("ok request download_link")
    audio_file = io.BytesIO(request.content)
    sound = AudioSegment.from_mp3(audio_file)
    dst = "test1.wav"
    sound.export(dst, format="wav")
    r = sr.Recognizer()
    with sr.WavFile("test1.wav") as source:
        audio = r.record(source)
    
    audio_output=r.recognize_google(audio)
    print("Transcription: " + audio_output)
    os.system("rm test1.wav")
    return audio_output



def go_frame_audio(browser,index):
    try:
        # print(index)
        time.sleep(1)
        singup_green_button=WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-audio-button"]')))
        singup_green_button.click()
        print("click recaptcha adio")
        try:
            print("get the source")
            eto_firstName=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'audio-source')))
            download_link = eto_firstName.get_attribute('src')
            print(download_link)
            audio_output= audio_fonction(download_link)
            text_cap=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID,'audio-response')))
            text_cap.send_keys(audio_output)
            time.sleep(2)
            text_cap.send_keys(Keys.ENTER)
            time.sleep(2)
            # 
        except Exception as error:
            print("error audio 222222 "+str(error))


    except Exception as e:
        # print(str(e))
        pass
    browser.switch_to.default_content()



def cppatcha_res(browser):

    # iframes = browser.find_elements_by_xpath("//iframe")
    # iframes =browser.find_elements(by=By.XPATH, value="//iframe")
    iframes=browser.find_elements_by_tag_name("iframe")
    print(str(len(iframes)))
    print('READY TO KILL bCAOTCHA singup')
    #######
    try:
        for index , iframe in enumerate(iframes):
            yhio=iframe.get_attribute('title')
            # print(str(index)+" -- "+iframe.get_attribute('title'))
            if "challenge" in yhio :

                try:
                    browser.switch_to.frame(int(index))
                    go_frame_audio(browser,index)
                    time.sleep(3)
                except:
                    print("not foooond")
                    pass

                print("end if")
                browser.switch_to.default_content()
                time.sleep(1)
                break
            print("end for")
    #######   
    except Exception as a:
        print(str(a))








def start_i(browser):
    email_reg,namee=gen_na()
    print(namee,email_reg)
    try:
        browser.get('https://www.skillshare.com/')
        try:
            preform_coockies=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/section[1]/div[2]/div[3]/div[2]/div/div/div/div/form/div/div[3]/div/div/input')))
            # browser.execute_script("arguments[0].scrollIntoView();", preform_coockies)
            print("fo")
            # preform_coockies.click()
            browser.execute_script("arguments[0].scrollIntoView();", preform_coockies)
            preform_coockies.send_keys(Keys.TAB*10,Keys.SPACE)
            # input("")
            print("okk filll")
            time.sleep(3)
        except Exception as aa:
            print("close error"+str(aa))
        preform_one=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/section[1]/div[2]/div[3]/div[2]/div/div/div/div/form/div/div[3]/div/div/input')))
        print("email field found")
        browser.execute_script("arguments[0].scrollIntoView();", preform_one)
        preform_one.click()
        preform_one.send_keys(email_reg,Keys.TAB)
        preform_tow=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/section[1]/div[2]/div[3]/div[2]/div/div/div/div/form/div/div[4]/div/div/input')))
        preform_tow.send_keys("baba123A*",Keys.RETURN)
        time.sleep(2)
        # preform_tow=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/section[1]/div[2]/div[3]/div[2]/div/div/div/div/form/div/div[6]/button/span')))
        # preform_one.click()
        print("check capatcha")
        cppatcha_res(browser)
        

    except Exception as e:
        print("lol error ")#+str(e))
    check_brot(browser)




if __name__ == '__main__':
    email = "tow62@blue-vovo.nl.eu.org"
    password = "baba123A*"
    browser = open_session()
    start_i(browser)


