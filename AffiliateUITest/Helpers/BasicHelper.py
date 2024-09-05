from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasicHelper:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        logging.info(f"Open url {url}")

    def find_elem_ui(self, loc, sec=10):
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.visibility_of_element_located(loc)
            )
            return elem
        except Exception as e:
            logging.error(f"Failed to find element using locator {loc}: {e}")
            raise

    def find_and_send_keys(self, loc, keys_to_send, sec=10):
        elem = self.find_elem_ui(loc, sec)
        elem.clear()
        elem.send_keys(keys_to_send)

    def find_and_click(self, loc, sec=10):
        elem = self.find_elem_ui(loc, sec)
        elem.click()

    def find_elements(self, loc, sec=10):
        elements = WebDriverWait(self.driver, sec).until(
            EC.visibility_of_any_elements_located(loc))
        return elements

    def find_elem_dom(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(
            EC.presence_of_element_located(loc))
        return elem

    def scroll_to_element(self, element):
        try:
            self.driver.execute_script('arguments[0].scrollIntoView();', element)
        except Exception as ER:
            logging.error(f"Failed to scroll to element: {ER}")
            raise

    def wait_for_element_to_be_clickable(self, loc, sec=10):
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.element_to_be_clickable(loc)
                )
            return elem
        except Exception as e:
            logging.error(f"Element not clickable using locator {loc}: {e}")
        raise
