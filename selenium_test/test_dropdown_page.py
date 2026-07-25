from pages.dropdown_page import DropdownPage


def test_selected_option(driver):
    dropdown_option = DropdownPage(driver)
    dropdown_option.load()
    dropdown_option.select_option("Option 1")
    assert dropdown_option.selected_option() == "Option 1"
    dropdown_option.select_option("Option 2")
    assert dropdown_option.selected_option() == "Option 2"
