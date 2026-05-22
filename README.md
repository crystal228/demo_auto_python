# Playwright Pytest Automation Framework

Production-like UI automation demo framework built with Python, Playwright and Pytest.

The project demonstrates a scalable approach to UI test automation using Page Object Model, reusable fixtures, CI integration, Allure reporting and automatic artifact collection on test failure.

---

# Tech Stack

* Python 3.12
* Playwright
* Pytest
* Pytest-BDD
* Allure Pytest
* GitHub Actions
* Page Object Model
* dotenv configuration

---

# Features

* UI automation with Playwright
* Page Object Model architecture
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
```

---

# Running Tests

## Run all tests

```bash
pytest
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
* execute pytest suite
* generate Allure results
* upload artifacts

Uploaded artifacts:

* screenshots
* Playwright traces
* videos
* Allure results

---

# Architecture Highlights

* Separation of concerns using Page Object Model
* Reusable BasePage methods
* Centralized environment configuration
* Reusable pytest fixtures
* Failure diagnostics automation
* CI-ready project structure
* Scalable automation framework approach

---

# Example Stack Used

* Python
* Playwright
* Pytest
* Pytest-BDD
* GitHub Actions
* Allure
* SQL
* Bash
* dotenv

---

# Future Improvements

* Parallel execution
* Docker support
* API testing layer
* Retry strategy for flaky tests
* Advanced reporting
* Multi-browser execution
* Test data factories
