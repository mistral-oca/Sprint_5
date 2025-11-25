import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    driver.find_element(*LOGIN_REG_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_NAME_TEXT))

    return driver

@pytest.fixture
def open_registration_form(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    driver.find_element(*LOGIN_REG_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
    return driver