import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function")
def config_browser():
    browser.config.base_url = "https://demoqa.com"
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.add_argument("--headless=new")
    browser.config.driver_options.add_argument("--window-size=1920,1080")
    browser.config.timeout = 8
    yield
    browser.quit()
