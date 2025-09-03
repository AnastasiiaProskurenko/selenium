import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
   # driver.implicitly_wait(20)
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()

def test_for_logo_img(driver):
    logo_img = driver.find_element(By.CSS_SELECTOR, '[alt="IT Career Hub"]')
    assert logo_img.is_displayed()

def test_for_link_prog(driver):
    link_prog = driver.find_element(By.CSS_SELECTOR, '.tn-elem.tn-elem__12064537861754487411327')
    assert link_prog.is_displayed()

def test_for_typs_of_pay(driver):
    typs_of_pay = driver.find_element(By.CSS_SELECTOR, '.tn-elem__12064537861754487411320')
    assert typs_of_pay.is_displayed()

def test_for_news(driver):
    news = driver.find_element(By.CSS_SELECTOR, '.tn-elem__12064537861754487411331')
    assert news.is_displayed()

def test_for_about_us(driver):
    about_us = driver.find_element(By.CSS_SELECTOR, '.tn-elem__12064537861754487411334')
    assert about_us.is_displayed()

def test_for_reviews(driver):
    reviews = driver.find_element(By.CSS_SELECTOR, '.tn-elem__12064537861754487411336')
    assert reviews.is_displayed()

def test_for_language_button(driver):
    language_button_ru = driver.find_element(By.CSS_SELECTOR, '.tn-elem__12064537861710152827519')
    assert language_button_ru.is_displayed()
    language_button_de = driver.find_element(By.CSS_SELECTOR, '.tn-elem__12064537861710153064158')
    assert language_button_de.is_displayed()

def test_for_call(driver):
    button_call = driver.find_element(By.CSS_SELECTOR,'.tn-elem__12064537861710153310161')
    button_call.click()

def test_for_right_antwort(driver):
    button_call = driver.find_element(By.CSS_SELECTOR, '.tn-elem__12064537861710153310161')
    button_call.click()
    wait = WebDriverWait(driver, 15)
    antwort = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.tn-elem__7679561671711363912027   [field="tn_text_1711363912027"]')))
    assert antwort.text.strip() == "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"


