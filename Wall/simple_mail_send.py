# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
import datetime
import imghdr
import smtplib
from email.message import EmailMessage
from pprint import pprint as pp


class MailTool:
    ADDRESS = 'jet.bot.service@gmail.com'
    PASSWORD = 'Edward261'

    def __init__(self, receiver_email):
        self.receiver_email = receiver_email

    def send_notification(self):
        mail = self.make_mail(self.receiver_email)
        # print(mail, type(mail))
        # pp(dir(mail))

        MailTool.send(mail)

    def make_mail(self, receiver) -> EmailMessage:
        content = 'This is Event Tracker!'

        msg = EmailMessage()
        msg['Subject'] = 'Event Tracker simple mail send test'
        msg['From'] = 'Jet Bot'  # gmail sender display name
        msg['To'] = receiver
        msg['X-Priority'] = '5'
        msg.set_content(content)

        return msg

    @staticmethod
    def send(mail):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(MailTool.ADDRESS, MailTool.PASSWORD)
            smtp.send_message(mail)


if __name__ == '__main__':
    rc = 'edward871130@gmail.com'

    mt = MailTool(rc)
    mt.send_notification()
