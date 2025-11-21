import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from generator import generate_unique_email, generate_password

def test_registration(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*LOGIN_REG_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

    email = generate_unique_email()
    password = generate_password()

    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(password)

    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_NAME_TEXT))

    assert driver.find_element(*USER_NAME_TEXT).is_displayed()
    assert driver.find_element(*USER_AVATAR).is_displayed()
