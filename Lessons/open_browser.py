from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver_path = "C:/Users/prosk/Desktop/chromedriver-win64/chromedriver.exe"
# Создание сервиса для драйвера
service = Service(driver_path)
# Инициализация драйвера с использованием сервиса
driver = webdriver.Chrome(service=service)

# Открытие сайта
driver.get("https://itcareerhub.de/ru")

# Задержка перед закрытием браузера
sleep(5)