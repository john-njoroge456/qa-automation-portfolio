from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


PAGE_URL = "https://the-internet.herokuapp.com/add_remove_elements/"
TIME_OUT = 10
ADD_ELEMENT = (By.CSS_SELECTOR, "button[onclick='addElement()']")
DELETE_BUTTON = (By.CSS_SELECTOR, "button[class='added-manually']")
driver = webdriver.Chrome()
driver.get(PAGE_URL)
assert driver.find_element(*ADD_ELEMENT)
print("Test 1 Passed")
time.sleep(2)
add_element_button = WebDriverWait(driver, timeout=TIME_OUT).until(
    EC.element_to_be_clickable(ADD_ELEMENT)

)
time.sleep(5)
add_element_button.click()

assert driver.find_element(*DELETE_BUTTON)
print("Test 2 passed, New Element added")

time.sleep(5)
remove_element = WebDriverWait(driver, timeout=TIME_OUT).until(
    EC.element_to_be_clickable(DELETE_BUTTON)
)
remove_element.click()
assert not driver.find_elements(*DELETE_BUTTON)
print("Test 3 passed , Element deleted")
time.sleep(5)
assert "Add/Remove Elements" in driver.page_source
print("Test 4 passed")
driver.quit()
