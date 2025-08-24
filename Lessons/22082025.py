from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#
# # Настройка ChromeDriver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# # Открытие сайта
# driver.get("https://itcareerhub.de/ru")
#
# driver.get("https://www.berlin.de")
# driver.save_screenshot("./berlin_screenshot.png")
#
# sleep(3)

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# Настройка драйвера для Firefox с использованием WebDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Открытие сайта
driver.get("https://itcareerhub.de/ru")

driver.get("https://www.berlin.de")
driver.save_screenshot("./berlin_screenshot.png")

sleep(3)
driver.quit()