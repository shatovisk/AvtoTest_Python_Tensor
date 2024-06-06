import pytest
from pages.sbis_home_page import SbisHomePage
from pages.contacts_page import ContactsPage

def test_change_region(driver):
    # Переходим на главную страницу СБИС
    sbis_home_page = SbisHomePage(driver)
    sbis_home_page.navigate_to("https://sbis.ru/")
    
    # Переходим в раздел Контакты
    sbis_home_page.go_to_contacts()
    
    contacts_page = ContactsPage(driver)

    # Проверяем текущий регион и наличие списка партнеров
    region = contacts_page.get_current_region()
    assert "Нижний Новгород" in region
    print("Region is correct")
    partners = contacts_page.get_partners_list()
    partners_texts = [partner.text for partner in partners]
    assert len(partners) > 0
    print("List of partners is exist")

    # Меняем регион на Камчатский край
    contacts_page.change_region("Камчатский край")

    # Проверяем, что регион изменился, список партнеров обновился
    new_region = contacts_page.get_current_region()
    assert "Петропавловск-Камчатский" in new_region
    print("Region is changed")

    new_partners = contacts_page.get_partners_list()
    new_partners_texts = [partner.text for partner in new_partners]
    print(f"New partners: {new_partners_texts}")
    assert len(new_partners) > 0
    print("Partners in new region is exist")
    assert new_partners_texts != partners_texts, "Expected different list of partners after region change"
    print("Partners in new region is changed")

    # Проверяем URL и title на наличие информации о новом регионе
    assert "kamchatskij-kraj" in driver.current_url.lower()
    assert "Камчатский край" in driver.title
    print("URL and title is changed")