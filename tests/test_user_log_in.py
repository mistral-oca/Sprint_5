import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from urls import BASE_URL


class TestLoginUser:   

    def test_login_user(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*LOGIN_REG_BUTTON).click()

        driver.find_element(*EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)

        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_NAME_TEXT))

        assert driver.find_element(*USER_NAME_TEXT).is_displayed()
        assert driver.find_element(*USER_AVATAR).is_displayed()
