from AffiliateUITest.Helpers.BasicHelper import BasicHelper
from selenium.webdriver.common.by import By
import logging


class HomePage(BasicHelper):
    login_icon = (By.XPATH, '//div[@class="user-avatar-c size-default color-default shape-circle bc-icon-user clickable"]')

    def is_login_icon_visible(self):
        try:
            self.find_elem_ui(self.login_icon)
            logging.info("Login icon is visible.")
            return True
        except Exception as e:
            logging.error(f"Login icon not visible: {e}")
            return False
