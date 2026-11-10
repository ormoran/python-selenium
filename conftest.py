import os

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    if os.getenv("SELENIUM_HEADLESS", "").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")

    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1280, 900)
    yield browser
    browser.quit()
