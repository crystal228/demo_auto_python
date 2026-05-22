import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    PRODUCTS_TITLE = ".title"
    ERROR_MESSAGE = '[data-test="error"]'

    @allure.step("Login with username: {username}")
    def login(self, username: str, password: str) -> None:
        self.wait_and_fill(self.USERNAME_INPUT, username)
        self.wait_and_fill(self.PASSWORD_INPUT, password)
        self.wait_and_click(self.LOGIN_BUTTON)

    @allure.step("Check successful login")
    def check_successful_login(self) -> None:
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(self.page.locator(self.PRODUCTS_TITLE)).to_have_text("Products")

    @allure.step("Check login error message")
    def check_login_error(self, expected_text: str) -> None:
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(expected_text)