from AffiliateUITest.Pages.LandingPage import LandingPage
from AffiliateUITest.Pages.SignIn import SignIn
from AffiliateUITest.Pages.HomePage import HomePage
import test_data
import logging


def test_login_invalid(driver, config):
    landing_page = LandingPage(driver)
    login_page = SignIn(driver)
    home_page = HomePage(driver)
    landing_page.open_url(config.baseUrl)
    landing_page.go_to_login_page()
    logging.info(f"Attempting to login with username: {test_data.invalidUsername} and password: {test_data.invalidPassword}")
    login_page.login_system(test_data.invalidUsername, test_data.invalidPassword)
    try:
        assert home_page.is_login_icon_visible(), "Login icon not visible. Invalid login failed."
        logging.info("Login icon visibility check passed. Test case completed successfully!")
    except AssertionError as e:
        logging.error(f"AssertionError: {e}")
        logging.error("Test case failed due to login icon not being visible")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise
