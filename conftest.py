import os
from datetime import datetime

import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page


load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("LOGIN"),
        "password": os.getenv("PASSWORD"),
    }


@pytest.fixture()
def page(context, request) -> Page:
    page = context.new_page()

    yield page

    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = request.node.name

        os.makedirs("artifacts/screenshots", exist_ok=True)

        screenshot_path = f"artifacts/screenshots/{test_name}_{timestamp}.png"

        screenshot = page.screenshot(
            path=screenshot_path,
            full_page=True,
        )

        allure.attach(
            screenshot,
            name=f"{test_name}_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

    page.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)