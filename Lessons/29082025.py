import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Инициализация WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Максимизация окна
    driver.implicitly_wait(10)
    driver.maximize_window()
    # Передача драйвера в тест
    yield driver
    # Закрытие браузера
    driver.quit()

def test_open_cats_page(driver):
    # Открытие сайта
    driver.get("https://suninjuly.github.io/cats.html")
    page_header = driver.find_element(By.CSS_SELECTOR, "[class='jumbotron-heading']")
    assert page_header.text == "Dog memes"
#Check that name of the second cat card is "Serious Cat"
def test_name_of_second_cat_card(driver):
    # Открытие сайта
    driver.get("https://suninjuly.github.io/cats.html")
    page_header = driver.find_element(By.CSS_SELECTOR, "p.card-text.second")
    assert page_header.text == "Serious cat"

def test_name_of_second_cat(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    second_cat = driver.find_element(By.XPATH, "//p[contains(@class, 'second')]")

    # Проверяем текст
    assert second_cat.text == "Serious cat"

def test_name_of_second_cats(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    min_cat = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(5) small")

    # Проверяем текст
    assert min_cat.text == "9 mins"

def test_name_of_second_cata(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    second_cat = driver.find_element(By.XPATH, "(//div[@class='col-sm-4'])[5]//small")

    # Проверяем текст
    assert second_cat.text == "9 mins"

   # / html / body / header / div / div / a / strong

def test_name_of_second_caty(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    second_cat = driver.find_element(By.CSS_SELECTOR, ".navbar-brand")

    # Проверяем текст
    assert second_cat.text == "Cats album"

def test_name_of_second_cato(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    min_cat = driver.find_element(By.CSS_SELECTOR, "svg")

    # Проверяем текст
    assert min_cat.is_displayed()==True

def test_name_of_second_cate(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    min_cat = driver.find_element(By.XPATH, "(//div[@class='col-sm-4'])[4]//button[2]")

    # Проверяем текст
    assert min_cat.is_displayed()==True

def test_name_of_second(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    min_cat = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(4) button:nth-child(2)")

    # Проверяем текст
    assert min_cat.is_displayed()==True

def test_cat_cards_quantity(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    cat_cards = driver.find_elements(By.CLASS_NAME, "col-sm-4")
    assert len(cat_cards) == 6

def test_cat_cards_quant(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    cat_cards = driver.find_elements(By.TAG_NAME, "img")
    assert len(cat_cards) == 6