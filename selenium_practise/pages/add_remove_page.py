from selenium.webdriver.common.by import By
from pages.base_page import BasePage


URL = "https://the-internet.herokuapp.com/add_remove_elements/"


class AddRemoveElement(BasePage):
    """Page object for the Add/Remove Elements page.

    Provides methods to load the page, add an element, and delete an element.
    """
    ADD_ELEMENT = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[class='added-manually']")

    def load(self):
        """Load the Add/Remove Elements page and return this page object."""
        self.driver.get(URL)
        return self

    def add_element(self):
        """Wait for and click the Add Element button."""
        self.wait_for_clickable(self.ADD_ELEMENT).click()

    def delete_element(self):
        """Wait for and click the Delete button."""
        self.wait_for_clickable(self.DELETE_BUTTON).click()
