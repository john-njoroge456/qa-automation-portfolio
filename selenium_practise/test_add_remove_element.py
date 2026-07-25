from pages.add_remove_page import AddRemoveElement
from selenium.webdriver.common.by import By


def test_add_element(driver):
    """Verify that adding an element displays the delete button."""
    button_click = AddRemoveElement(driver)
    button_click.load()
    button_click.add_element()
    assert driver.find_elements(*AddRemoveElement.DELETE_BUTTON)

    # assert driver.find_elements(
    #     By.CSS_SELECTOR, "button[class='added-manually']")


def test_delete_element(driver):
    """Verify that deleting an element removes the delete button."""
    button_click = AddRemoveElement(driver)
    button_click.load()
    button_click.add_element()

    button_click.delete_element()

    assert driver.find_elements(*AddRemoveElement.DELETE_BUTTON) == []
