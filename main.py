# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
from search.google_search import search_event

if __name__ == '__main__':
    q = '111年上半年替代役'

    search_event(q, headless=False)
