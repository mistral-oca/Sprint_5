import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

EXISTING_USER_EMAIL = "ponomarevamaria_27@gmail.com"
EXISTING_USER_PASSWORD = "Darling157"

def test_login_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*LOGIN_REG_BUTTON).click()

    driver.find_element(*EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)

    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_NAME_TEXT))

    assert driver.find_element(*USER_NAME_TEXT).is_displayed()
    assert driver.find_element(*USER_AVATAR).is_displayed()
