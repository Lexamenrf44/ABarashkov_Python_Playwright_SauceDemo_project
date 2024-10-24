from main.pages.app import App
from main.support.data import Data

def test_e2e(page, base_url):

    # Set up the application
    app = App(page)

    # Navigate to the base URL
    page.goto(base_url)

    # Perform login
    app.login_ui(Data.user_test_login, Data.user_test_password)