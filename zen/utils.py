# -*- coding: utf-8 -*-

import requests

from zen.settings import MASHAPE_API_KEY, MASHAPE_API_URL


__all__ = (
    'yodaize',
)


HEADERS = {
    'X-Mashape-Authorization': MASHAPE_API_KEY,
}


def yodaize(message):
    data = {
        'sentence': message,
    }
    message = requests.get(MASHAPE_API_URL, params=data, headers=HEADERS)
    return message.content
