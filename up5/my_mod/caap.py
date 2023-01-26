
import names , random , requests , io, os
from pydub import AudioSegment
import speech_recognition as sr



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
    # print("Transcription: " + audio_output)
    os.system("rm test1.wav")
    return audio_output



def cppatcha_res(browser):

    # iframes = browser.find_elements_by_xpath("//iframe")
    iframes =browser.find_elements(by=By.XPATH, value="//iframe")
    # iframes=browser.find_elements_by_tag_name("iframe")
    # print(str(len(iframes)))
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
            # print("end for")
    #######
    except Exception as a:
        print(str(a))
    print("END oF capatcha")