from playwright.sync_api import Playwright, sync_playwright
from main.pages.app import App

app = App()


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    app.login_ui(page)
    page.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
