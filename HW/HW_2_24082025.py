from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.fullscreen_window()

try:
    driver.get("https://itcareerhub.de/ru")
    # ждем до 10 секунд загрузки, далее ищем тег <а> , с атрибутом "tn-atom",
    # который мы увидели на сайте, и текстом "Способы оплаты"
    payment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="tn-atom" and contains(text(), "Способы оплаты")]'))
    )
    payment_button.click()
    # из-за плохого инета, даю время на загрузку, перед скриншотом( иначе получаю белый экран)
    sleep(3)
    # Делаем скриншот этой секции
    name_screen="itcareerhub.png"
    driver.save_screenshot(f"./{name_screen}")

    print(f"Сохранен скриншот {name_screen}")

finally:
    driver.quit()