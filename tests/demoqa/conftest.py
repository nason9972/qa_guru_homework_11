import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selene import browser

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.utils import attach

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()

    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # Настраиваем глобальный browser
    browser.config.driver = driver
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://demoqa.com"

    yield

    # Сохраняем session_id перед аттачами
    session_id = driver.session_id

    # Аттачи - передаем DRIVER
    try:
        attach.add_screenshot(driver)
        print("✅ Скриншот добавлен")
    except Exception as e:
        print(f"❌ Ошибка скриншота: {e}")

    try:
        attach.add_logs(driver)
        print("✅ Логи добавлены")
    except Exception as e:
        print(f"❌ Ошибка логов: {e}")

    try:
        attach.add_html(driver)
        print("✅ HTML добавлен")
    except Exception as e:
        print(f"❌ Ошибка HTML: {e}")

    try:
        attach.add_video(driver)
        print("✅ Видео добавлено")
    except Exception as e:
        print(f"❌ Ошибка видео: {e}")

    # Закрываем
    driver.quit()

    # Сообщение о видео
    if session_id:
        print(f"\n🎬 Видео доступно по ссылке: https://selenoid.autotests.cloud/video/{session_id}.mp4")