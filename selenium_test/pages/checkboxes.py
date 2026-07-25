from pages.base_page import BasePage
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/checkboxes"


class CheckBoxes(BasePage):
    """Page object for the checkboxes page."""

    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def load(self):
        """Load the checkboxes page and return this page object."""
        self.driver.get(URL)
        return self

    def toggle_checkbox(self, index):
        """Toggle the checkbox at the given zero-based index."""
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        checkboxes[index].click()

    def is_checked(self, index):
        """Return True if the checkbox at the given zero-based index is selected."""
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        return checkboxes[index].is_selected()
