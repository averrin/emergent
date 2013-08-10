from .settings import MASHAPE_API_KEY, MASHAPE_API_URL
import requests

headers = {
    'X-Mashape-Authorization': MASHAPE_API_KEY,
}

def yodaize(message):
    data = {
        'sentence': message,
    }
    message = requests.get(MASHAPE_API_URL, params=data, headers=headers)
    return message.content
