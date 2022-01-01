# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 1/1/22
"""
import imaplib
import smtplib
import email
from tqdm import tqdm
import configparser
from email.header import decode_header

# account credentials
config = configparser.ConfigParser()
config.read('settings.ini')

username = config['MailSender']['Mail']
password = config['MailSender']['Password']

if __name__ == '__main__':
    with imaplib.IMAP4_SSL('imap.gmail.com') as imap:
        imap.login(username, password)
        imap.select('INBOX')
        status, messages = imap.search(None, 'ALL')
        messages = messages[0].split(b' ')

        for mail in tqdm(messages):
            _, msg = imap.fetch(mail, '(RFC822)')

            # # you can delete the for loop for performance if you have a long list of emails
            # # because it is only for printing the SUBJECT of target email to delete
            # for response in msg:
            #     if isinstance(response, tuple):
            #         msg = email.message_from_bytes(response[1])
            #         # decode the email subject
            #         subject = decode_header(msg['Subject'])[0][0]
            #         if isinstance(subject, bytes):
            #             # if it's a bytes type, decode to str
            #             subject = subject.decode()
            #         print(f"Deleting : {subject}")

            # mark the mail as deleted
            imap.store(mail, "+FLAGS", "\\Deleted")

        '''
        permanently remove mails that are marked as deleted 
        from the selected mailbox (in this case, INBOX)
        '''
        imap.expunge()
