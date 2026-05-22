# Playwright Pytest Automation Framework

Production-like UI and API automation demo framework built with Python, Playwright, Requests and Pytest.

The project demonstrates a scalable approach to test automation using Page Object Model, reusable fixtures, CI integration, Allure reporting, API client abstraction and automatic artifact collection on test failure.

---

# Tech Stack

* Python 3.12
* Playwright
* Pytest
* Pytest-BDD
* Requests
* Allure Pytest
* GitHub Actions
* Page Object Model
* dotenv configuration

---

# Features

* UI automation with Playwright
* API testing with Requests
* Page Object Model architecture
* Reusable API client layer
* Reusable BasePage methods
* Environment-based configuration
* Pytest fixtures and hooks
* Screenshots on failure
* Playwright trace collection
* Video recording
* Allure-compatible results
* GitHub Actions CI pipeline
* BDD support with pytest-bdd

---

# Project Structure

```text
.
├── api/
│   ├── __init__.py
│   └── clients/
│       ├── __init__.py
│       └── booking_client.py
│
├── artifacts/
│   ├── screenshots/
│   ├── traces/
│   └── videos/
│
├── features/
│   └── login.feature
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_api_booking.py
│   ├── test_demo_login.py
│   └── test_login_bdd.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
└── README.md
```

---

# Local Setup

## Clone repository

```bash
git clone <repository_url>
cd <repository_name>
```

---

## Create virtual environment

```bash
python -m venv .venv
```

---

## Activate virtual environment

### Windows PowerShell

```bash
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Playwright browser

```bash
playwright install chromium
```

---

# Environment Configuration

Create `.env` file in project root:

```env
BASE_URL=https://www.saucedemo.com/
LOGIN=standard_user
PASSWORD=secret_sauce
BOOKING_API_URL=https://restful-booker.herokuapp.com
```

---

# Running Tests

## Run all tests

```bash
pytest
```

---

## Run UI tests only

```bash
pytest tests/test_demo_login.py tests/test_login_bdd.py
```

---

## Run API tests only

```bash
pytest tests/test_api_booking.py
```

---

## Run tests with browser UI

```bash
pytest --headed
```

---

## Run tests with Allure results

```bash
pytest --alluredir=allure-results
```

---

# UI Tests

UI tests are based on Playwright and Page Object Model.

Implemented UI scenarios:

* successful login
* negative login with invalid password
* BDD login scenario with pytest-bdd

Example Page Object:

```python
class LoginPage(BasePage):
    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    PRODUCTS_TITLE = ".title"
    ERROR_MESSAGE = '[data-test="error"]'
```

---

# API Tests

API tests use a separate client layer based on `requests`.

The current API scenario uses Restful Booker public API.

Implemented API scenario:

* create booking via API
* validate response status code
* validate response body fields
* verify that `bookingid` is returned

Example API client:

```python
class BookingClient:
    def __init__(self, api_url: str):
        self.api_url = api_url.rstrip("/")

    def create_booking(self, payload: dict):
        return requests.post(
            f"{self.api_url}/booking",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
```

---

# UI and API Coverage

The framework contains both UI and API test layers:

* UI tests use Playwright and Page Object Model.
* API tests use Requests and a reusable API client.
* Both layers share the same Pytest infrastructure, fixtures, reporting and CI pipeline.

This structure can be extended for end-to-end scenarios where test data is created via API and validated through UI.

---

# BDD Example

Example feature file:

```gherkin
Feature: Login

  Scenario: Successful login with valid credentials
    Given user opens login page
    When user logs in with valid credentials
    Then user should see products page
```

---

# Test Artifacts

Framework automatically collects debugging artifacts on test failure.

Generated artifacts:

* screenshots
* Playwright traces
* videos
* Allure attachments

Artifacts location:

```text
artifacts/
├── screenshots/
├── traces/
└── videos/
```

---

# Playwright Trace Viewer

To open saved trace locally:

```bash
playwright show-trace artifacts/traces/<trace-file>.zip
```

---

# Allure Reporting

Generate Allure results:

```bash
pytest --alluredir=allure-results
```

Serve local Allure report:

```bash
allure serve allure-results
```

Screenshots and traces are automatically attached to failed tests.

---

# CI Pipeline

GitHub Actions workflow automatically runs tests on:

* push to `main`
* pull request to `main`
* manual workflow dispatch

Pipeline steps:

* install dependencies
* install Playwright browsers
* execute Pytest suite
* generate Allure results
* upload artifacts

Required CI environment variables:

```yaml
BASE_URL: https://www.saucedemo.com/
LOGIN: standard_user
PASSWORD: secret_sauce
BOOKING_API_URL: https://restful-booker.herokuapp.com
```

Uploaded artifacts:

* screenshots
* Playwright traces
* videos
* Allure results

---

# Architecture Highlights

* Separation of concerns using Page Object Model
* Reusable BasePage methods
* Reusable API client abstraction
* Centralized environment configuration
* Reusable Pytest fixtures
* Failure diagnostics automation
* CI-ready project structure
* Scalable automation framework approach

---

# Future Improvements

* Parallel execution
* Docker support
* API schema validation
* Retry strategy for flaky tests
* Advanced reporting
* Multi-browser execution
* Test data factories
* Full UI + API end-to-end flow
