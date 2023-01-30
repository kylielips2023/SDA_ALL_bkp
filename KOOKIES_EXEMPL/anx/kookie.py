

import pickle ,time
import json

print('module Kookie')

def dump_coockies(browser,profil_pickle):
    cookies = browser.get_cookies()
    # print('ok')
    pickle.dump(cookies, open("prf_kok/"+profil_pickle, "wb"))
    print("DUmp dump_coockies")




def load_cookies(browser,profil_pickle):
    # browser=chrome_session()
    path_prof="prf_kok/"+profil_pickle
    print("Loading Profile : [ "+path_prof+" ]")
    browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    cookies = pickle.load(open(path_prof, "rb"))
    cookies_list = list(json.dumps(cookies))
    # print(cookies)
    for cookie in cookies:
        # print(cookie['domain'])
        cookie['domain'] = ".google.com"
        
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            # print(str(e))
            pass
        # print(cookie['domain'])
        cookie['domain'] = "shell.cloud.google.com"
        
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            # print(str(e))
            pass

    url_1="https://shell.cloud.google.com"
    # url_1="https://mail.google.com/mail/u/0/#inbox"
    browser.get(url_1)


    # time.sleep(120)
    # input("gfg")
    browser.get('https://shell.cloud.google.com')
    # time.sleep(120)