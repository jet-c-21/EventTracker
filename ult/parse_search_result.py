# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/22/21
"""


def get_event_str_token(event_query: str) -> list:
    return event_query.split(' ')


def is_matched_link(evt_q_tokens: list, evt_title: str) -> bool:
    for t in evt_q_tokens:
        if t not in evt_title:
            return False
    return True


def get_matched_event_data(event_query: str, event_result: list) -> list:
    result = list()
    evt_q_tokens = get_event_str_token(event_query)
    for evt_title, evt_link in event_result:
        if is_matched_link(evt_q_tokens, evt_title):
            result.append((evt_title, evt_link))

    return result
