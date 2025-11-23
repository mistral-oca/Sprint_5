import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestCreateAd:  

    def test_create_ad_unauthorized(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(*PLACE_AD_BUTTON).click()

        modal_title = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MODAL_TITLE)
        )

        assert modal_title.is_displayed(), "Модальное окно не появилось"
