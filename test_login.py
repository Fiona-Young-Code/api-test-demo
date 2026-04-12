import pytest
from api.login_api import login
from utils.data_loader import load_login_test_data

login_test_data = load_login_test_data()

@pytest.mark.parametrize("case", login_test_data, ids=[case["title"] for case in login_test_data])
def test_login_success(case, common_headers):
    response = login(case["username"], case["password"], common_headers)

    assert response.status_code == 200

    res = response.json()
    assert "json" in res
    assert res["json"]["username"] == case["username"]
    assert res["json"]["password"] == case["password"]
