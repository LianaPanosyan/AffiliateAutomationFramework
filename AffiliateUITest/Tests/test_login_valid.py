from AffiliateUITest.Pages.LandingPage import LandingPage
from AffiliateUITest.Pages.SignIn import SignIn
from AffiliateUITest.Pages.HomePage import HomePage
import test_data
import logging


def test_login_valid(driver, config):
    try:
        landing_page = LandingPage(driver)
        login_page = SignIn(driver)
        home_page = HomePage(driver)
        landing_page.open_url(config.baseUrl)
        landing_page.go_to_login_page()

        logging.info(f"Attempting to login with username: {test_data.validUsername} and password: {test_data.validPassword}")
        login_page.login_system(test_data.validUsername, test_data.validPassword)

        logging.info("Checking if login icon is visible")
        assert home_page.is_login_icon_visible(), "Login icon not visible. Invalid login failed."

        logging.info("Test case completed successfully!")
    except Exception as e:
        logging.error(f"Test case failed due to: {e}")
        raise  # Re-raise the exception to ensure pytest catches it
