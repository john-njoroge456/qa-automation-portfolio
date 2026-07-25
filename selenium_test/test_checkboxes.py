from pages.checkboxes import CheckBoxes


def test_toggle_checkbox_is_checked(driver):
    """Verify toggling a checkbox updates its checked state."""
    checkbox_object = CheckBoxes(driver)
    checkbox_object.load()
    assert not checkbox_object.is_checked(0)
    assert checkbox_object.is_checked(1)
    checkbox_object.toggle_checkbox(0)
    assert checkbox_object.is_checked(0)
