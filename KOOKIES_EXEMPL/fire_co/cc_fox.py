import pickle
import selenium.webdriver

driver = selenium.webdriver.Firefox()
driver.get("https://shell.cloud.google.com/?show=ide%2Cterminal")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
