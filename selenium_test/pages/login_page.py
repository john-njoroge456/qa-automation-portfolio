"""
LoginPage represents the-internet.herokuapp.com/login.

It knows two things, and only two things:
1. Where its elements live (locators)
2. What actions can be performed on it (methods)

Tests never touch By.ID / By.CSS_SELECTOR directly - they call these
methods instead. If the site's HTML changes, only this file needs updating,
not every test that logs in.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage

URL = "https://the-internet.herokuapp.com/login"


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def load(self):
        self.driver.get(URL)
        return self

    def login(self, username, password):
        """Fill the login form and submit it."""
        self.wait_for_element(self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
