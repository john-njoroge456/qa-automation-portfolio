"""
Shared pytest fixtures for the Selenium suite.

The `driver` fixture replaces manual try/finally blocks in every test:
pytest guarantees the code after `yield` runs after each test finishes,
whether it passed or failed - so the browser always closes cleanly.
"""

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    yield drv          # test runs here
    drv.quit()          # guaranteed cleanup, pass or fail
