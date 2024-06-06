from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

class SbisHomePage(BasePage):
    CONTACTS_LINK = (By.LINK_TEXT, 'Контакты')
    BANNER_TENSOR = (By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')

    def  __init__(self, driver):
        super(). __init__(driver)  # Вызов конструктора родительского класса
        
    def go_to_contacts(self):
        self.click(self.CONTACTS_LINK)

    def click_tensor_banner(self):
        print("Waiting for the banner to be available...")
        attempts = 0
        while attempts < 3:  # Делаем 3 попытки
            try:
                banner_tensor = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(self.BANNER_TENSOR)
                )
                banner_tensor.click()
                print("Banner clicked successfully")
                return
            except StaleElementReferenceException as e:
                print("Stale element reference exception occurred. Trying again...")
                attempts += 1
                time.sleep(1)  # Немного подождем перед повторной попыткой
        raise Exception("Failed to click on the banner after multiple attempts")