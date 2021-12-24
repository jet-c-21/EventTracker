# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/24/21
"""
import sys
import pathlib
from time import sleep
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROJECT_DIR = str(pathlib.Path(__file__).parent.parent)  # EventTracker
sys.path.append(PROJECT_DIR)

from search.google_search.chrome_driver import PROD_FLAG, check_webdriver_remote_link, get_chrome_driver


def take_screenshot_for_page(url: str):
    driver = get_chrome_driver()
    if driver:
        msg = f"[VITAL] - Get Web Driver Successfully!"
        print(msg)

    google_url = 'https://www.google.com/'
    driver.get(google_url)
    print(driver)

    driver.get(url)
    sleep(1)

    shot_save_path = f"{PROJECT_DIR}/test_temp/screenshot.png"
    driver.save_screenshot(shot_save_path)

    driver.close()


if __name__ == '__main__':
    url = 'http://www.bangweb.com.tw/life.php?act=view&id=530'
    # url = 'https://www.instagram.com/aohsuehfu/'

    if PROD_FLAG:
        while not check_webdriver_remote_link():
            sleep(0.5)

        take_screenshot_for_page(url)

    else:
        take_screenshot_for_page(url)
