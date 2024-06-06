from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisHomePage:
    CONTACTS_LINK = (By.CSS_SELECTOR, "a[href='/contacts']")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def go_to_contacts(self):
        contacts_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTACTS_LINK)
        )
        contacts_link.click()