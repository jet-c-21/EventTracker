# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
import requests
from bs4 import BeautifulSoup


# from googlesearch.googlesearch import GoogleSearch



def soup_to_html(soup: BeautifulSoup, fp: str):
    with open(fp, "w") as f:
        f.write(str(soup))


if __name__ == '__main__':
    q = '111年 上半年替代役'



    # response = GoogleSearch().search("something")
    # for result in response.results:
    #     print("Title: " + result.title)
    #     print("Content: " + result.getText())

    # url = 'https://www.google.com/search?q=111年上半年替代役'
    # url = 'https://monthtkt.pma.gov.tw/park/'
    # res = requests.get(url)
    # soup = BeautifulSoup(res.text, 'html.parser')
    # soup_to_html(soup, 'html_files/1.html')
