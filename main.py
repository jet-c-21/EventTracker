# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
import os
import sys
from time import sleep
from search.google_search import get_search_result, check_webdriver_remote_link
from ult import MailHelper, get_client_data, get_matched_event_data, get_curr_time_str


def service_all_clients():
    mail_tool = MailHelper(CONFIG_PATH)
    client_data = get_client_data(CLIENTS_DIR)

    for cld in client_data:
        client_mail = cld['mail']
        client_evt = cld['event']
        client_evt = client_evt.strip()

        search_result = get_search_result(client_evt)
        matched_event_data = get_matched_event_data(client_evt, search_result)

        if matched_event_data:
            notif_mail = mail_tool.gen_notification_mail(client_mail, client_evt, matched_event_data)
            mail_tool.send_mail(notif_mail)

        log_mail = mail_tool.gen_log_mail(client_mail, client_evt, search_result, matched_event_data)
        mail_tool.send_mail(log_mail)


if __name__ == '__main__':
    CONFIG_PATH = 'settings.ini'
    CLIENTS_DIR = 'clients'

    msg = f"Start Task at: {get_curr_time_str()}"
    print(msg)

    print(f"ET_PRODUCTION = {os.environ.get('ET_PRODUCTION')}")
    if os.environ.get('ET_PRODUCTION'):
        while not check_webdriver_remote_link():
            sleep(0.5)

        service_all_clients()

    else:
        service_all_clients()

    msg = 'Task Finish!\n\n'
    print(msg)

    # sys.exit('Close Task.')
