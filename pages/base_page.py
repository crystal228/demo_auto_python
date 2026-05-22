from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def wait_and_click(self, locator: str):
        self.page.locator(locator).wait_for(state="visible")
        self.page.locator(locator).click()

    def wait_and_fill(self, locator: str, text: str):
        self.page.locator(locator).wait_for(state="visible")
        self.page.locator(locator).fill(text)

    def get_locator(self, locator: str):
        return self.page.locator(locator)