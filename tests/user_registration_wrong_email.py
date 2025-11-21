import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_registration_invalid_email(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*LOGIN_REG_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

    driver.find_element(*EMAIL_INPUT).send_keys("wrongemail")
    
    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(EMAIL_ERROR_TEXT)
    )
    assert error_message.text == "Ошибка"

    for field_name in ["email", "password", "submitPassword"]:
        container = driver.find_element(By.XPATH, f"//input[@name='{field_name}']/parent::*")
        container_class = container.get_attribute("class")
        assert "input_inputError" in container_class, \
            f"Ожидался класс ошибки для поля '{field_name}', но получен: {container_class}"
