# demo_auto_python

# Playwright Pytest Automation Demo

Demo UI automation framework built with Python, Playwright and Pytest.

The project demonstrates a production-like approach to UI test automation: Page Object Model, environment-based configuration, CI pipeline, screenshots on failure and Allure-compatible test results.

## Tech Stack

- Python 3.12
- Playwright
- Pytest
- Pytest-BDD
- Allure Pytest
- GitHub Actions
- Page Object Model
- dotenv configuration

## Project Structure

```text
.
├── pages/
│   ├── base_page.py
│   └── login_page.py
├── tests/
│   └── test_demo_login.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
└── README.md