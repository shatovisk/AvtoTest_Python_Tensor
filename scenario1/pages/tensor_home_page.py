from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
import time
from selenium.webdriver.common.action_chains import ActionChains


class TensorHomePage(BasePage):
    BLOCK_SILA_V_LYUDAKH = (By.XPATH, '//*[contains(text(), "Сила в людях")]')
    LINK_PODROBNEE = (By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-content .tensor_ru-link')
    CHRONOLOGY_PHOTOS = (By.CSS_SELECTOR, 'div.tensor_ru-About__block3 .s-Grid-container')
    
    def  __init__(self, driver):
        super(). __init__(driver)  # Вызов конструктора родительского класса

    def check_sila_v_lyudah(self):
        return self.find_element(self.BLOCK_SILA_V_LYUDAKH)

    def click_podrobnee(self):
        print("Waiting for the 'podrobnee' button to be clickable...")
        attempts = 0
        while attempts < 3:  # Делаем 3 попытки
            try:
                podrobnee_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.LINK_PODROBNEE)
                )
                # Прокрутка элемента в видимую область
                self.driver.execute_script("arguments[0].scrollIntoView(true);", podrobnee_button)
                
                # # Клик с использованием JavaScript
                self.driver.execute_script("arguments[0].click();", podrobnee_button)

                print("'Podrobnee' button clicked successfully")
                return
            except StaleElementReferenceException as e:
                print("Stale element reference exception occurred. Trying again...")
                attempts += 1
                time.sleep(1)
            except ElementClickInterceptedException as e:
                print("Element click intercepted. Trying again...")
                attempts += 1
                time.sleep(1)
        raise Exception("Failed to click on the 'podrobnee' button after multiple attempts")

    def get_chronology_photos(self):
        return self.find_elements(self.CHRONOLOGY_PHOTOS)