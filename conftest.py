import os
from datetime import datetime

import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Browser, BrowserContext, Page
from api.clients.booking_client import BookingClient


load_dotenv()


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "")


@pytest.fixture(scope="session")
def credentials() -> dict[str, str]:
    return {
        "username": os.getenv("LOGIN", ""),
        "password": os.getenv("PASSWORD", ""),
    }


@pytest.fixture()
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context(
        record_video_dir="artifacts/videos",
        record_video_size={"width": 1280, "height": 720},
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    yield context

    context.close()


@pytest.fixture()
def page(context: BrowserContext, request) -> Page:
    page = context.new_page()

    yield page

    test_failed = request.node.rep_call.failed
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_name = request.node.name

    if test_failed:
        os.makedirs("artifacts/screenshots", exist_ok=True)
        os.makedirs("artifacts/traces", exist_ok=True)

        screenshot_path = f"artifacts/screenshots/{test_name}_{timestamp}.png"
        trace_path = f"artifacts/traces/{test_name}_{timestamp}.zip"

        screenshot = page.screenshot(
            path=screenshot_path,
            full_page=True,
        )

        allure.attach(
            screenshot,
            name=f"{test_name}_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

        context.tracing.stop(path=trace_path)

        allure.attach.file(
            trace_path,
            name=f"{test_name}_trace",
            attachment_type=allure.attachment_type.ZIP,
        )
    else:
        context.tracing.stop()

    page.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="session")
def booking_api_url() -> str:
    return os.getenv("BOOKING_API_URL", "")


@pytest.fixture()
def booking_client(booking_api_url) -> BookingClient:
    return BookingClient(booking_api_url) 