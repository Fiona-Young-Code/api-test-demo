# import requests
#
# def test_login_success():
#     url = "https://reqres.in/api/login"
#
#     payload = {
#         "email": "eve.holt@reqres.in",
#         "password": "cityslicka"
#     }
#
#     response = requests.post(url, json=payload)
#
#     # 状态码校验
#     assert response.status_code == 200
#
#     res = response.json()
#
#     # 业务校验
#     assert "token" in res
#
# def test_login_failed_without_password():
#     url = "https://reqres.in/api/login"
#     payload = {
#         "email": "eve.holt@reqres.in"
#     }
#
#     response = requests.post(url, json=payload)
#
#     # 状态码校验
#     assert response.status_code == 400
#
#     res = response.json()
#
#     # 业务校验
#     assert "error" in res
import requests


def test_login_success():
    url = "https://httpbin.org/post"

    payload = {
        "username": "testuser",
        "password": "123456"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

    res = response.json()
    assert res["json"]["username"] == "testuser"


def test_login_failed_without_password():
    url = "https://httpbin.org/post"

    payload = {
        "email": "testuser"
    }

    response = requests.post(url, json=payload)

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200
