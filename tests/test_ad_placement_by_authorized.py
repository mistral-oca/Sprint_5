import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

EXISTING_USER_EMAIL = "ponomarevamaria_28@gmail.com"
EXISTING_USER_PASSWORD = "1"

AD_DESCRIPTION = "Состояние отличное"
AD_PRICE = "15000"
AD_CATEGORY = "Технологии"
AD_CITY = "Москва"
AD_CONDITION = "Б/У"


def get_next_ad_number(driver):
    all_ads = driver.find_elements(By.XPATH, "//div[contains(@class,'adCard')]//h2")
    numbers = []
    for ad in all_ads:
        title = ad.text
        if title.startswith("Тестовое объявление"):
            parts = title.split()
            if parts[-1].isdigit():
                numbers.append(int(parts[-1]))
    return max(numbers, default=0) + 1


def wait_for_last_ad_card(driver, ad_title, timeout=20):
    end_time = time.time() + timeout
    while time.time() < end_time:
        ads = driver.find_elements(By.XPATH, "//div[contains(@class,'card')]//h2")
        for ad in ads:
            if ad_title in ad.text:
                return ad
        time.sleep(1)
    return None


class TestCreateAd:  

    def test_create_ad_authorized(self, driver):  # <-- перенесли внутрь класса
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(*LOGIN_REG_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_AVATAR))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_NAME_TEXT))

        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button:has(svg.svgSmall)"))
        )
        driver.execute_script("arguments[0].click();", profile_button)

        ad_number = get_next_ad_number(driver)
        AD_TITLE = f"Тестовое объявление {ad_number}"

        create_ad_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Разместить объявление']"))
        )
        driver.execute_script("arguments[0].click();", create_ad_button)

        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        name_input.send_keys(AD_TITLE)

        description_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "description"))
        )
        driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
            description_input, AD_DESCRIPTION
        )

        price_input = driver.find_element(By.NAME, "price")
        price_input.send_keys(AD_PRICE)

        category_input = driver.find_element(By.NAME, "category")
        driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
            category_input, AD_CATEGORY
        )

        city_input = driver.find_element(By.NAME, "city")
        driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
            city_input, AD_CITY
        )

        condition_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//label[contains(., '{AD_CONDITION}')]"))
        )
        driver.execute_script("arguments[0].click();", condition_label)

        publish_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Опубликовать']"))
        )
        driver.execute_script("arguments[0].click();", publish_button)

        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button:has(svg.svgSmall)"))
        )
        driver.execute_script("arguments[0].click();", profile_button)

        last_ad = wait_for_last_ad_card(driver, AD_TITLE, timeout=20)
        assert last_ad is not None, f"Не удалось найти объявление с названием '{AD_TITLE}'"
