# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) ' \
             'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'


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
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    return driver
