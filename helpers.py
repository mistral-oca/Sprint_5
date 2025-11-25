from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

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
    try:
        return WebDriverWait(driver, timeout).until(
            lambda d: next(
                (ad for ad in d.find_elements(By.XPATH, "//div[contains(@class,'card')]//h2")
                 if ad_title in ad.text),
                None
            )
        )
    except TimeoutException:
        return None
