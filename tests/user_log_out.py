import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from locators import *

EXISTING_USER_EMAIL = "ponomarevamaria_27@gmail.com"
EXISTING_USER_PASSWORD = "Darling157"

def is_element_visible(driver, locator):
    
    try:
        element = driver.find_element(*locator)
        return element.is_displayed()
    except NoSuchElementException:
        return False

def test_logout_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    driver.find_element(*LOGIN_REG_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_NAME_TEXT))

    assert driver.find_element(*USER_NAME_TEXT).is_displayed()
    assert driver.find_element(*USER_AVATAR).is_displayed()

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

    login_button = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LOGIN_REG_BUTTON)
    )
    assert login_button.is_displayed()
