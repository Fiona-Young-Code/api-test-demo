import requests
from config.config import BASE_URL,LOGIN_PATH
from utils.logger import get_logger

logger = get_logger()
def login(username, password, headers=None):
    url =BASE_URL + LOGIN_PATH 
    payload = {
        "username": username,
        "password": password
    }
    logger.info(f"Request URL: {url}")
    logger.info(f"Request Payload: {payload}")
    return requests.post(url, json=payload)
