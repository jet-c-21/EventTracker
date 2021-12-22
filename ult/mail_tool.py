# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/22/21
"""
import pathlib
import smtplib
from email.message import EmailMessage
import configparser
from .general import get_curr_time_str


class MailHelper:
    def __init__(self, cfg_path: str):
        self.cfg_path = cfg_path
        self.config = configparser.ConfigParser()
        self.config.read(self.cfg_path)

        self.sender_name = self.config['MailSender']['Name']
        self.sender_mail = self.config['MailSender']['Mail']
        self.sender_pwd = self.config['MailSender']['Password']

        self.log_mail = self.config['Log']['Mail']
        self.dev_author_link = 'https://github.com/jet-c-21'

    def __repr__(self):
        s = f"MailHelper ({self.sender_name} - {self.sender_mail})"
        return s

    def send_mail(self, mail: EmailMessage):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.sender_mail, self.sender_pwd)
            smtp.send_message(mail)

            msg = f"Mail : {mail.get('Subject')}\nhas sent.\n"
            print(msg)

    def gen_log_mail(self, client_mail: str, client_evt: str,
                     search_result: list, matched_event_data: list) -> EmailMessage:
        email_msg = EmailMessage()

        curr_time_str = get_curr_time_str()
        subject = f"(Log) {curr_time_str}, MEC: {len(matched_event_data)} / SRC: {len(search_result)}, " \
                  f"📝: <{client_evt}> 😃: <{client_mail}>"
        email_msg['Subject'] = subject

        email_msg['From'] = self.sender_name
        email_msg['To'] = self.log_mail

        #  >>> content >>>
        content = f"<h1>Matched Event Count: {len(matched_event_data)}</h1><br><br>"
        for evt_title, evt_link in matched_event_data:
            line = f"<h3>{evt_title}</h3><p>{evt_link}</p><br>"
            content += line

        content += f"<h1>Search Result Count: {len(search_result)}</h1><br><br>"
        for evt_title, evt_link in search_result:
            line = f"<h3>{evt_title}</h3><p>{evt_link}</p><br>"
            content += line

        email_msg.set_content(content, subtype='html')

        #  <<< content <<<

        return email_msg

    def _add_end_greet_str(self, content: str) -> str:
        content += f"<h3>By Jet C. Bot</h3>" \
                   f"<h3>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href=\"{self.dev_author_link}\">開發作者</a></h3>"

        return content

    @staticmethod
    def _add_med_str_ol_ver(client_evt: str, matched_event_data: list, content=''):
        content += f"<h1>小弟弟我呢 這邊幫您找到了 {len(matched_event_data)} 則關於 \"{client_evt}\" 的新消息:</h1><br>"
        content += '<ol>'
        for i, (evt_title, evt_link) in enumerate(matched_event_data, start=1):
            line = f"<li><h3><a href=\"{evt_link}\">{evt_title}</a></h3></li>"
            content += line

        content += '</ol>'
        content += '<br>'

        return content

    @staticmethod
    def _add_med_str(client_evt: str, matched_event_data: list, content=''):
        content += f"<h1>小弟弟我呢 這邊幫您找到了 {len(matched_event_data)} 則關於 📝{client_evt}📝 的新消息:</h1><br>"
        for i, (evt_title, evt_link) in enumerate(matched_event_data, start=1):
            line = f"<h3>{i}. <a style=\"overflow: visible;\" href=\"{evt_link}\">{evt_title}</a></h3>"
            # line = f"<h3>{i}. {evt_title} <a style=\"overflow: visible;\" href=\"{evt_link}\">Click Me!</a></h3>"
            content += line

        content += '<br>'

        return content

    def gen_notification_mail(self, client_mail: str, client_evt: str, matched_event_data: list) -> EmailMessage:
        email_msg = EmailMessage()

        # subject = f"🔔 您關心的 ──  ✨{client_evt}✨  貌似有新消息了🔥 快來看看吧！"
        subject = f"🔔 您關心的 -  ✨{client_evt}✨  貌似有新消息了🔥 快來看看吧！"
        email_msg['Subject'] = subject

        email_msg['From'] = self.sender_name
        email_msg['To'] = client_mail

        #  >>> content >>>
        content = ''
        content = self._add_med_str(client_evt, matched_event_data, content)
        content = self._add_end_greet_str(content)
        email_msg.set_content(content, subtype='html')
        #  <<< content <<<

        return email_msg
