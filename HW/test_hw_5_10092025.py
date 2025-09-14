import math
from itertools import count
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
from selenium.webdriver.common.action_chains import ActionChains

# 1 задание

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
#     yield driver
#     driver.quit()
#
# def test_iframe(driver):
#     box= driver.find_element(By.TAG_NAME, "iframe")
#     driver.switch_to.frame(box)
#     text_bloc = driver.find_element(By.XPATH, "//*[@id='content']/p[2]")
#     t="semper posuere integer et senectus justo curabitur."
#     assert t in text_bloc.text
#     assert text_bloc.is_displayed()
#     driver.switch_to.default_content()




# 2 задание

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    yield driver
    driver.quit()

def test_image(driver):
    button_agree = driver.find_element(By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")
    button_agree.click()
    box = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(box)
    draggable = driver.find_element(By.XPATH, "//*[@id='gallery']/li[1]")
    box_util = driver.find_element(By.CSS_SELECTOR, ".ui-widget-content.ui-state-default.ui-droppable")
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, box_util).perform()
    number = driver.find_elements(By.XPATH, "//*[@id='gallery']/li")
    num_ut = driver.find_elements(By.XPATH, "//*[@id='trash']/ul/li")
    num = [l for l in number if l.is_displayed()]
    n_ut = [l for l in num_ut if l.is_displayed()]
    assert len(num)==3
    assert len(n_ut)==1






