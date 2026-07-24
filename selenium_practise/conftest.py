import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Pytest fixture that provides a Chrome WebDriver instance.

    The driver is created before the test and quit after the test.
    """
    drv = webdriver.Chrome()
    yield drv
    drv.quit()
