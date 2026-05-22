from playwright.sync_api import Page

from pages.login_page import LoginPage


def test_successful_login(
    page: Page,
    base_url,
    credentials,
):
    login_page = LoginPage(page)

    login_page.open(base_url)
    login_page.login(
        username=credentials["username"],
        password=credentials["password"],
    )
    login_page.check_successful_login()


def test_login_with_invalid_password(
    page: Page,
    base_url,
    credentials,
):
    login_page = LoginPage(page)

    login_page.open(base_url)
    login_page.login(
        username=credentials["username"],
        password="wrong_password",
    )
    login_page.check_login_error(
        "Username and password do not match any user in this service"
    )