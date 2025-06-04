import pytest
from pages.login_page import LoginPage
from config import config

@pytest.mark.login
def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load(config.BASE_URL)
    login_page.login(config.username, config.password)
    assert "inventory" in browser.current_url

@pytest.mark.login
def test_invalid_username(browser):
    login_page = LoginPage(browser)
    login_page.load(config.BASE_URL)
    login_page.login("invalid_user", config.password)
    assert "Epic sadface" in login_page.get_error_message()

@pytest.mark.login
def test_invalid_password(browser):
    login_page = LoginPage(browser)
    login_page.load(config.BASE_URL)
    login_page.login(config.username, "invalid_password")
    assert "Epic sadface" in login_page.get_error_message()

@pytest.mark.login
def test_blank_username(browser):
    login_page = LoginPage(browser)
    login_page.load(config.BASE_URL)
    login_page.login("", config.password)
    assert "Username is required" in login_page.get_error_message()

@pytest.mark.login
def test_blank_password(browser):
    login_page = LoginPage(browser)
    login_page.load(config.BASE_URL)
    login_page.login(config.username, "")
    assert "Password is required" in login_page.get_error_message()

@pytest.mark.login
def test_blank_username_and_password(browser):
    login_page = LoginPage(browser)
    login_page.load(config.BASE_URL)
    login_page.login("", "")
    assert "Epic sadface" in login_page.get_error_message()