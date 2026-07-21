"""
Login -> logout regression test, rewritten with Page Object Model.

Compared to the original flat script, this version:
- has no hardcoded time.sleep() - every wait is explicit and condition-based
- has no duplicate find_element calls
- separates "what the page looks like" (page objects) from
  "what the test verifies" (this file)
- relies on the `driver` fixture for setup/teardown, so a failed
  assertion still closes the browser cleanly
"""

from pages.login_page import LoginPage, URL as LOGIN_URL
from pages.secure_page import SecurePage

USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


def test_login_logout(driver):
    login_page = LoginPage(driver).load()
    login_page.login(USERNAME, PASSWORD)

    secure_page = SecurePage(driver)
    secure_page.logout()

    # Wait for the redirect back to the login page instead of sleeping blindly
    login_page.wait_for_url(LOGIN_URL)

    assert "Login Page" in driver.page_source
