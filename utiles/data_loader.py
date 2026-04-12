import json


def load_login_test_data():
    with open("data/login_data.json", "r", encoding="utf-8") as f:
        return json.load(f)
