import requests

def test_login():
    url = "https://reqres.in/api/login"

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url, json=payload)

    # 状态码校验
    assert response.status_code == 200

    res = response.json()

    # 业务校验
    assert "token" in res
