import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Disable Chrome's password manager
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
