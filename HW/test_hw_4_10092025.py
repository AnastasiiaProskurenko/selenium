import math
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from typing_extensions import assert_type
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1 задание

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()


def test_text(driver):
    input_field = driver.find_element(By.CLASS_NAME, "form-control")
    input_field.send_keys("ITCH")
    submit_button = driver.find_element(By.ID, "updatingButton")
    submit_button.click()
    new_submit_button = driver.find_element(By.ID, "updatingButton")
    assert new_submit_button.text=="ITCH"


#  2 задание

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
#     yield driver
#     driver.quit()
#
# def test_image(driver):
#     WebDriverWait(driver, 20).until(
#         EC.text_to_be_present_in_element((By.CLASS_NAME, "lead"), "Done!")
#     )
#     image_list = driver.find_elements(By.TAG_NAME,"img")
#
#     image = image_list[3]
#     alt_value = image.get_attribute("alt")
#     assert alt_value == "award"