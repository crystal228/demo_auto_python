from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    PRODUCTS_TITLE = '.title'

    def login(self, username: str, password: str):
        self.wait_and_fill(self.USERNAME_INPUT, username)
        self.wait_and_fill(self.PASSWORD_INPUT, password)
        self.wait_and_click(self.LOGIN_BUTTON)

    def check_successful_login(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

        expect(
            self.get_locator(self.PRODUCTS_TITLE)
        ).to_have_text("Products")