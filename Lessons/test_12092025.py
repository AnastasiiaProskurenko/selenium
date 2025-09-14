import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
   # driver.implicitly_wait(20)
    driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
    yield driver
    driver.quit()

def test_drag_and_drop(driver):
    draggable = driver.find_element(By.ID, "draggable")
    droppable = driver.find_element(By.ID, "droppable")
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable).perform()
    # sleep(2)
    # ##CHeck that text "Dropped!" is displayed
    # dr = driver.find_element((By.LINK_TEXT, "Dropped!"))
    # assert dr.is_displayed()

    dropped = driver.find_element(By.ID, "droppable")
    assert dropped.text == "Dropped!"

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#    # driver.implicitly_wait(20)
#     driver.get("http://suninjuly.github.io/file_input.html")
#     yield driver
#     driver.quit()

# def test_alert_text(driver):
#     input_fields = driver.find_elements(By.CLASS_NAME, "form-control")
#     for field in input_fields:
#         field.send_keys("Hello")
#         sleep(2)
#         file_path = os.path.abspath("test_file.txt")
#         with open(file_path, "w") as f:
#             f.write("Hello, this is a test file.")
#         wait = WebDriverWait(driver, 20)
#         alert = wait.until(EC.alert_is_present())
#         assert "Congrats, you've passed the task!" in alert.text

# def test_upoad_file_form(driver):
#     first_name = driver.find_element(By.NAME, "firstname")
#     first_name.send_keys("Hans")
#
#     last_name = driver.find_element(By.NAME, "lastname")
#     last_name.send_keys("Schmidt")
#
#     email = driver.find_element(By.NAME, "email")
#     email.send_keys("afsgdfasd@gmail.com")
#     file_path = os.path.abspath("test_file.txt")
#     with open(file_path, "w") as f:
#         f.write("Hello, this is a test file.")
#     file_input = driver.find_element(By.ID, "file")
#     file_input.send_keys(file_path)
#     sleep(0)
#
#     wait = WebDriverWait(driver, 50)
#     alert = wait.until(EC.alert_is_present())
#     assert "Congrats, you've passed the task!" in alert.text

