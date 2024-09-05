from AffiliateUITest.Helpers.BasicHelper import BasicHelper
from selenium.webdriver.common.by import By
import logging


class LandingPage(BasicHelper):
    signin_button = (By.XPATH, '//span[text()="Sign In"]')
    register_button = (By.XPATH, '//span[text()="Register"]')

    def go_to_login_page(self):
        self.find_and_click(self.signin_button)
        logging.info("Go to Login page!")

    def go_to_register_page(self):
        self.find_and_click(self.register_button)
        logging.info("Go to Registration page!")
