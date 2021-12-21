# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


# from googlesearch.googlesearch import GoogleSearch


def soup_to_html(soup: BeautifulSoup, fp: str):
    with open(fp, "w") as f:
        f.write(str(soup))


if __name__ == '__main__':
    q = '111年 上半年替代役'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://www.google.com/search?q=111年上半年替代役'
    driver.get(url)
    time.sleep(50)
    driver.close()
