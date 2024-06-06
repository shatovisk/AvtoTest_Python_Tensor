from pages.sbis_home_page import SbisHomePage
from pages.tensor_home_page import TensorHomePage

def test_scenario(driver):
    print(type(driver))  # Это поможет увидеть, что передается в driver
    sbis_home_page = SbisHomePage(driver)
    sbis_home_page.navigate_to('https://sbis.ru/')
    sbis_home_page.go_to_contacts()
    sbis_home_page.click_tensor_banner()

    tensor_home_page = TensorHomePage(driver)
    tensor_home_page.navigate_to('https://tensor.ru/')
    assert tensor_home_page.check_sila_v_lyudah() is not None
    print("Verified 'Sila v lyudah' is present")
    
    tensor_home_page.click_podrobnee()
    assert driver.current_url == 'https://tensor.ru/about'

    photos = tensor_home_page.get_chronology_photos()
    assert len(photos) > 0, "No photos found in chronology section"
    first_photo_size = photos[0].size
    width = first_photo_size['width']
    height = first_photo_size['height']
    
    for photo in photos:
        assert photo.size['width'] == width
        assert photo.size['height'] == height