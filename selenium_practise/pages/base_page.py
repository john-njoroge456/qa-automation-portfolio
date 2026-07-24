from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 5


class BasePage:
    """Base page class for Selenium page objects."""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait until an element is present in the DOM and return it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait until an element is clickable and return it. """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url(self, url, timeout=DEFAULT_TIMEOUT):
        """ wait for brwoser to navigate to given url"""
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )
