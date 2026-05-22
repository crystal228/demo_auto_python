import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open page: {url}")
    def open(self, url: str) -> None:
        self.page.goto(url)

    @allure.step("Click element: {locator}")
    def wait_and_click(self, locator: str) -> None:
        self.page.locator(locator).wait_for(state="visible")
        self.page.locator(locator).click()

    @allure.step("Fill element: {locator}")
    def wait_and_fill(self, locator: str, text: str) -> None:
        self.page.locator(locator).wait_for(state="visible")
        self.page.locator(locator).fill(text)