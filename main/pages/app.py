from playwright.sync_api import expect
from main.config import Settings
from main.data import Data

settings = Settings()
data = Data()


class App:
    # Methods
    def login_ui(self, page, username=data.user_test_login, password=data.user_test_password, success=True):
        page.goto(settings.base_url)
        page.fill(self.app_username, username)
        page.fill(self.app_password, password)
        page.click(self.app_login_button)
        if success:
            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        else:
            expect(page).to_have_url("https://www.saucedemo.com/")

    # Common locators
    app_username = '[data-test="username"]'
    app_password = '[data-test="password"]'
    app_login_button = '[data-test="login-button"]'
    app_logo = '.header_label'
