import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function", autouse=True)
def browser():

    """Fixture to provide Playwright browser instance."""

    with sync_playwright() as playwright:
        browser_instance = playwright.chromium.launch(headless=False)

        yield browser_instance

        browser_instance.close()


@pytest.fixture(scope="function", autouse=True)
def page(browser):

    """Fixture to provide a new Playwright page and base URL."""

    context = browser.new_context()
    page = context.new_page()

    # Yield the page and base_url as a tuple
    yield page

    context.close()

@pytest.fixture(scope="session", autouse=True)
def base_url():
    return "https://www.saucedemo.com/" # Define the base URL inside the fixture