from AffiliateUITest.Helpers.BasicHelper import BasicHelper
from selenium.webdriver.common.by import By
import logging


class SignIn(BasicHelper):
    username = (By.ID, 'userName')
    password = (By.ID, 'password')
    signin_button = (By.ID, 'signIn')

    def login_system(self, username, password):
        self.find_and_send_keys(self.username, username)
        self.find_and_send_keys(self.password, password)
        logging.info("Sign in button is active:")
        self.find_and_click(self.signin_button)
