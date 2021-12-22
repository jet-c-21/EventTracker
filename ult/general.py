# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/22/21
"""
import json
import datetime
import pytz
import os


def read_json(fp: str) -> dict:
    return json.load(open(fp, 'r', encoding='utf-8'))


def get_curr_time(tz='Asia/Taipei') -> datetime.datetime:
    time_zone = pytz.timezone(tz)
    return time_zone.localize(datetime.datetime.now())


def get_curr_time_str(tz='Asia/Taipei', fmt='%Y-%m-%d %H:%M:%S') -> str:
    now = get_curr_time(tz)
    return now.strftime(fmt)


def get_client_data(clients_dir_path: str) -> list:
    result = list()
    for fn in os.listdir(clients_dir_path):
        fp = f"{clients_dir_path}/{fn}"
        result.append(read_json(fp))

    return result
