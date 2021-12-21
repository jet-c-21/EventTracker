# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
from .chrome_driver import get_chrome_driver
from pyquery import PyQuery as pq

from lxml.html import HtmlElement
import time


def search_event(event_query: str, headless=True):
    driver = get_chrome_driver(headless)
    url = f"https://www.google.com/search?q={event_query}"
    driver.get(url)

    html = driver.page_source
    doc = pq(html)
    search_div = doc.find('#search > div > div')
    # print(type(search_div))

    # for el in doc.find('a'):
    #     el = pq(el)
    #     print(el.attr('href'))

    for el in search_div.children('div'):
        el = pq(el)
        el = el.find('div > div:first-child > div > div > div > div:first-child')
        title = el.find('h3').text()
        link = el.find('a').attr('href')
        print(title, link)

        # break

    time.sleep(300)
