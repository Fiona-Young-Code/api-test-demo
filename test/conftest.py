import pytest

@pytest.fixture
def common_headers():
    return {
        "Content-Type": "application/json"
    }
