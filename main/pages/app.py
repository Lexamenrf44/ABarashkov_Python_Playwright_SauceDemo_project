from playwright.sync_api import expect, Page

from main.support.data import Data

data = Data()

class App:
    def __init__(self, page: Page):
        self.page = page
        self.app_username = '[data-test="username"]'
        self.app_password = '[data-test="password"]'
        self.app_login_button = '[data-test="login-button"]'
        self.app_logo = '.header_label'

    def login_ui(self, username=data.user_test_login, password=data.user_test_password, success=True):
        self.page.fill(self.app_username, username)
        self.page.fill(self.app_password, password)
        self.page.click(self.app_login_button)
        if success:
            expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        else:
            expect(self.page).to_have_url("https://www.saucedemo.com/")
