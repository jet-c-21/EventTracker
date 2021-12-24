# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) ' \
             'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'

PROD_FLAG = os.environ.get('ET_PRODUCTION')
DRIVER_REMOTE_URL = 'http://selenium:4444/wd/hub'


def get_chrome_opt(headless=True) -> webdriver.ChromeOptions:
    opt = webdriver.ChromeOptions()
    opt.add_argument('no-sandbox')
    opt.add_argument('disable-dev-shm-usage')
    opt.add_argument('disable-setuid-sandbox')

    if headless:
        opt.add_argument('headless')

    return opt


def get_chrome_driver(headless=True) -> webdriver:
    opt = get_chrome_opt(headless)

    if PROD_FLAG:
        driver = webdriver.Remote(DRIVER_REMOTE_URL, options=opt)
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    return driver


def check_webdriver_remote_link(link=DRIVER_REMOTE_URL) -> bool:
    try:
        requests.get(link)
        msg = f"[VITAL] - Web Driver Remote link is initialized."
        print(msg)
        return True

    except Exception as e:
        msg = f"[INFO] - Web Driver Remote isn't initialized yet: {e}"
        print(msg)
        return False
