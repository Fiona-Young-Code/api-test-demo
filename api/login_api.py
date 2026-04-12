import requests
from config.config import BASE_URL,LOGIN_PATH

def login(username, password, headers=None):
    url =BASE_URL + LOGIN_PATH 
    payload = {
        "username": username,
        "password": password
    }
    return requests.post(url, json=payload)
