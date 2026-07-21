"""
BasePage holds behavior shared by every page object:
- a reference to the driver
- a reusable explicit-wait helper

Every page-specific class (LoginPage, SecurePage, ...) inherits from this,
so we only write the waiting logic once instead of repeating it everywhere.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait until an element is present in the DOM, then return it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait until an element is present AND clickable, then return it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url(self, url, timeout=DEFAULT_TIMEOUT):
        """Wait until the browser navigates to the given URL."""
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))
