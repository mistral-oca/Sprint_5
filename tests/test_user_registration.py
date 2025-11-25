import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from generator import generate_unique_email, generate_password
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD

class TestRegistration:

    def test_registration(self, open_registration_form):
        driver = open_registration_form

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


    def test_registration_invalid_email(self, open_registration_form):
        driver = open_registration_form

        driver.find_element(*EMAIL_INPUT).send_keys("wrongemail")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(EMAIL_ERROR_TEXT)
        )
        assert error_message.text == "Ошибка"

        for field_name in ["email", "password", "submitPassword"]:
            container = driver.find_element(
                By.XPATH, FIELD_CONTAINER_TEMPLATE.format(field_name=field_name)
            )
            container_class = container.get_attribute("class")
            assert "input_inputError" in container_class


    def test_registration_existing_user(self, open_registration_form):
        driver = open_registration_form

        driver.find_element(*EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)

        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(EMAIL_ERROR_TEXT)
        )
        assert error_message.text == "Ошибка"

        for field_name in ["email", "password", "submitPassword"]:
            container = driver.find_element(
                By.XPATH, FIELD_CONTAINER_TEMPLATE.format(field_name=field_name)
            )
            container_class = container.get_attribute("class")
            assert "input_inputError" in container_class
