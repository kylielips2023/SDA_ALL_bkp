

import undetected_chromedriver as uc
import time


def chrome_session():

    options = uc.ChromeOptions()
    options.arguments.extend(["--no-sandbox", "--disable-setuid-sandbox","--disable-web-security"])
    browser = uc.Chrome(options)
    return browser