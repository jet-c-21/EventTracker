# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
from .chrome_driver import get_chrome_driver
from pyquery import PyQuery as pq
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from bs4.element import Tag

from lxml.html import HtmlElement
from time import sleep
from pprint import pp
from typing import Union
from lxml import etree


def soup_to_html(doc, fp: str):
    with open(fp, "w") as f:
        f.write(str(doc))


def get_doc(html: Union[str, HtmlElement]) -> pq:
    if isinstance(html, HtmlElement):
        html = etree.tostring(html, pretty_print=True)

    soup = BeautifulSoup(html, 'html.parser')
    pretty_html = soup.prettify(formatter='html5')
    # print(pretty_html)

    return pq(pretty_html)


def search_event(event_query: str, headless=True):
    driver = get_chrome_driver(headless)
    url = 'https://www.google.com/'
    driver.get(url)
    search_bar = driver.find_element_by_tag_name('input')
    search_bar.send_keys(event_query)
    search_bar.send_keys(Keys.ENTER)

    # url = f"https://www.google.com/search?q={event_query}"
    # driver.get(url)

    html = driver.page_source
    # print(type(html))
    doc = get_doc(html)

    search_res_div = doc('#rso > div')
    # soup_to_html(search_res_div, 'HTML_Wall/temp1.html')

    for i, el in enumerate(search_res_div):
        el = get_doc(el)
        el = el('div.yuRUbf')
        if el.size() == 0:
            continue

        title = el('h3').text()
        link = el('a').attr('href')
        print(title, link)
        # print(f"el.size() = {el.size()}")
        # for res_idx in range(el.size()):
        #     el = el.eq(res_idx)
        #     print(type(el), el.size())

        # break

    # soup_to_html(el, f"HTML_Wall/el_{i}.html")

    # for el in doc.find('a'):
    #     el = pq(el)
    #     print(el.attr('href'))

    # for el in search_div.children('div'):
    #     el = pq(el)
    #     el = el.find('div > div:first-child > div > div > div > div:first-child')
    #     title = el.find('h3').text()
    #     link = el.find('a').attr('href')
    #     print(title, link)
    #
    #     # break
    #
    sleep(600)


def search_event_bs4(event_query: str, headless=True):
    driver = get_chrome_driver(headless)
    url = 'https://www.google.com/'
    driver.get(url)
    search_bar = driver.find_element_by_tag_name('input')
    search_bar.send_keys(event_query)
    search_bar.send_keys(Keys.ENTER)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    search_res_div = soup.select('#rso > div')
    # print(type(search_res_div))
    for item in search_res_div:
        item: Tag
        el = item.select('div.yuRUbf')


        print(len(el), el)


        # break

    sleep(600)
