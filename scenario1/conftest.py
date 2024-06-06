import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    print("Launching driver...")  # Для отладки
    service=Service(executable_path='E:\Работа\Тестировщик\Тензор\my_project\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    print("Driver launched successfully")  # Убедитесь, что драйвер инициализирован
    yield driver
    print("Quitting driver...")  # Для отладки
    driver.quit()