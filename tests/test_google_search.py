from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_google_search_field_is_visible(driver):
    driver.get("https://www.google.pl")

    search_field = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "textarea[name='q'], input[name='q']")
        )
    )

    assert search_field.is_displayed()
