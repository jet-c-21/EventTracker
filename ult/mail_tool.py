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


class MailTool:
    def __init__(self, cfg_path: str):
        self.cfg_path = cfg_path
        self.config = configparser.ConfigParser()
        self.config.read(self.cfg_path)

    def _make_log_mail(self, search_result):


        email_msg = EmailMessage()


    def send_log_mail(self, search_result:list):

