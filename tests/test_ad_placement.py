import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from helpers import get_next_ad_number, wait_for_last_ad_card
from data import *


class TestCreateAd:

    def test_create_ad_authorized(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(*LOGIN_REG_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_NAME_TEXT))

        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PROFILE_BUTTON)
        )
        driver.execute_script("arguments[0].click();", profile_button)

        ad_number = get_next_ad_number(driver)
        AD_TITLE = f"Тестовое объявление {ad_number}"

        create_ad_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CREATE_AD_BUTTON)
        )
        driver.execute_script("arguments[0].click();", create_ad_button)

        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(NAME_INPUT)
        )
        name_input.send_keys(AD_TITLE)

        description_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(DESCRIPTION_INPUT)
        )
        driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
            description_input, AD_DESCRIPTION
        )

        price_input = driver.find_element(*PRICE_INPUT)
        price_input.send_keys(AD_PRICE)

        category_input = driver.find_element(*CATEGORY_INPUT)
        driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
            category_input, AD_CATEGORY
        )

        city_input = driver.find_element(*CITY_INPUT)
        driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
            city_input, AD_CITY
        )

        condition_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, CONDITION_LABEL_TEMPLATE.format(AD_CONDITION))
            )
        )
        driver.execute_script("arguments[0].click();", condition_label)

        publish_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PUBLISH_BUTTON)
        )
        driver.execute_script("arguments[0].click();", publish_button)

        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PROFILE_BUTTON)
        )
        driver.execute_script("arguments[0].click();", profile_button)

        last_ad = wait_for_last_ad_card(driver, AD_TITLE, timeout=20)
        assert last_ad is not None, f"Не удалось найти объявление с названием '{AD_TITLE}'"


    def test_create_ad_unauthorized(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(*PLACE_AD_BUTTON).click()

        modal_title = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MODAL_TITLE)
        )

        assert modal_title.is_displayed(), "Модальное окно не появилось"
