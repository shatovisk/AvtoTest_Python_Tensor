from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class ContactsPage:
    REGION_SELECTOR = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text")
    REGION_NAME = (By.ID, "city-id-2")
    PARTNERS_LIST = (By.NAME, "itemsContainer")
    SUGGEST_ITEM = (By.XPATH, '//*[contains(text(), "Камчатский край")]')

    def __init__(self, driver):
        self.driver = driver

    def get_current_region(self):
        attempts = 0
        while attempts < 3:
            try:
                region_name = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.REGION_NAME)
                )
                return region_name.text
            except StaleElementReferenceException:
                attempts += 1
                print(f"Attempt {attempts}: StaleElementReferenceException encountered. Retrying...")

        raise Exception("Failed to get current region after multiple attempts")

    def get_partners_list(self):
        return self.driver.find_elements(*self.PARTNERS_LIST)

    def change_region(self, region_name):
        region_selector = self.driver.find_element(*self.REGION_SELECTOR)
        region_selector.click()


        suggest_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUGGEST_ITEM)
        )
        suggest_item.click()

        # Добавим дополнительное ожидание после клика
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.SUGGEST_ITEM)
        )

        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(self.REGION_SELECTOR, region_name)
            )
            print("Element found")
        except TimeoutException:
            print("TimeoutException: Region name not updated in time")
            raise