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


def save_html(doc, fp: str):
    with open(fp, "w") as f:
        f.write(str(doc))


def get_google_searched_html(event_query: str, headless=True) -> str:
    driver = get_chrome_driver(headless)
    url = 'https://www.google.com/'
    driver.get(url)
    search_bar = driver.find_element_by_tag_name('input')
    search_bar.send_keys(event_query)
    search_bar.send_keys(Keys.ENTER)

    html = driver.page_source
    driver.close()

    return html


def get_doc(html: Union[str, HtmlElement]) -> pq:
    if isinstance(html, HtmlElement):
        html = etree.tostring(html, pretty_print=True)

    soup = BeautifulSoup(html, 'html.parser')
    pretty_html = soup.prettify(formatter='html5')
    # print(pretty_html)

    return pq(pretty_html)


def get_search_result(event_query: str, headless=True) -> list:
    gs_html = get_google_searched_html(event_query, headless)
    doc = get_doc(gs_html)

    search_res_div = doc('div.yuRUbf')

    search_result = list()
    for i, el in enumerate(search_res_div):
        el = get_doc(el)
        title = el('h3').text().strip()
        link = el('a').attr('href')
        search_result.append((title, link))

    return search_result


def get_search_result_by_bs4(event_query: str, headless=True) -> list:
    gs_html = get_google_searched_html(event_query, headless)
    soup = BeautifulSoup(gs_html, 'html.parser')

    search_res_div = soup.select('div.yuRUbf')

    search_result = list()
    for i, el in enumerate(search_res_div):
        el: Tag
        title = el.select_one('h3').text.strip()
        link = el.select_one('a').get('href')
        search_result.append((title, link))

    return search_result


# def search_event(event_query: str, headless=True):
#     search_result = get_search_result(event_query, headless)
#
#     for title, link in search_result:
#         print(title, link)
