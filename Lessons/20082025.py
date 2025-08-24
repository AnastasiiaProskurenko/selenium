
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Настройка ChromeDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.set_window_size(640, 460)
driver.fullscreen_window()
driver.maximize_window()
# Открытие сайта
driver.get("https://itcareerhub.de/ru")
driver.get("https://www.berlin.de")

driver.back()
driver.forward()
# Задержка перед закрытием браузера
sleep(3)