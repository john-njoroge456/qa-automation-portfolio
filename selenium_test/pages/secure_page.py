"""
SecurePage represents the page a user lands on after a successful login
(the-internet.herokuapp.com/secure). Its only job here is logging out.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class SecurePage(BasePage):
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".button.secondary.radius")

    def logout(self):
        """Wait for the logout button to be clickable, then click it."""
        self.wait_for_clickable(self.LOGOUT_BUTTON).click()
