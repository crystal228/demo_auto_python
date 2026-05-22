from pytest_bdd import given, scenario, then, when
from playwright.sync_api import Page

from pages.login_page import LoginPage


@scenario("../features/login.feature", "Successful login with valid credentials")
def test_successful_login_bdd():
    pass


@given("user opens login page")
def open_login_page(page: Page, base_url):
    login_page = LoginPage(page)
    login_page.open(base_url)


@when("user logs in with valid credentials")
def login_with_valid_credentials(page: Page, credentials):
    login_page = LoginPage(page)
    login_page.login(
        username=credentials["username"],
        password=credentials["password"],
    )


@then("user should see products page")
def check_products_page(page: Page):
    login_page = LoginPage(page)
    login_page.check_successful_login()