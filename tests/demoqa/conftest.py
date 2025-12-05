import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from tests.demoqa.utils import attach


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    options.set_capability('goog:loggingPrefs', {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL'
    })

    # Также добавляем эти опции
    options.add_argument('--enable-logging')
    options.add_argument('--v=1')
    options.add_argument('--log-level=0')
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()