# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
from search.google_search import get_search_result, get_search_result_by_bs4, search_event
from ult import get_matched_event_data
from ult import MailTool

def service_all_clients():
    pass


if __name__ == '__main__':
    q = '111年 上半年 替代役'
    cfg_path = 'settings.ini'

    mail_tool = MailTool(cfg_path)

    print(mail_tool.config['Log']['SavedAddress'])

    # search_result = get_search_result(q)

    # m_evt_data = get_matched_event_data(q, search_result)

    # print(m_evt_data)

    # search_event_bs4(q, headless=False)
