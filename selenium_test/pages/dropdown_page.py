from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

URL = "https://the-internet.herokuapp.com/dropdown"


class DropdownPage(BasePage):
    DROPDOWN = (By.ID, "dropdown")

    def load(self):
        self.driver.get(URL)
        return self

    def select_option(self, option_text):
        dropdown_option = self.driver.find_element(*self.DROPDOWN)
        select = Select(dropdown_option)
        select.select_by_visible_text(option_text)

    def selected_option(self):
        dropdown_option = self.driver.find_element(*self.DROPDOWN)
        select = Select(dropdown_option)
        return select.first_selected_option.text
