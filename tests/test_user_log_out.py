import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestLogoutUser:   

    def test_logout_user(self, login_user):
        driver = login_user  
        
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

        login_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_REG_BUTTON)
        )
        assert login_button.is_displayed()
