import requests

def test_login_success():
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

def test_login_failed_without_password():
    url = "https://reqres.in/api/login"
    payload = {
        "email": "eve.holt@reqres.in"
    }

    response = requests.post(url, json=payload)

    # 状态码校验
    assert response.status_code == 400

    res = response.json()

    # 业务校验
    assert "error" in res
