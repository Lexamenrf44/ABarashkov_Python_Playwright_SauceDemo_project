from playwright.sync_api import Playwright, sync_playwright, expect
from main.config import Settings
from main.pages.app import App

settings = Settings()


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto(settings.base_url)
    page.fill(App.username, 'standard_user')
    page.fill('input[data-test="password"]', 'secret_sauce')
    page.click('input[data-test="login-button"]')
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
