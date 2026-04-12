# api-test-demo
A simple API automation testing project using Python, requests, and pytest.
## Tech Stack
- requests 基本用法
- pytest 运行机制
- 参数化
- 分层
- 导入包
- 返回体断言
- 配置拆分
- fixture
- 报告
## Project Structure
```text
api_test_demo/
├── api/
│   ├── __init__.py
│   └── login_api.py
├── config/
│   ├── __init__.py
│   └── config.py
├── data/
│   ├── login_data.json
├── utils/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── logger.py
│── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_login.py
```
