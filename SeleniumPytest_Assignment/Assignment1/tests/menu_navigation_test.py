import pytest
from pages.login_page import LoginPage
from pages.menu_section import menu_section
from config import config

@pytest.mark.menu
def test_menu_navigation(browser):
    login = LoginPage(browser)
    menu = menu_section(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    menu.open_menu()
    assert menu.is_menu_display()
    menu.close_menu()


@pytest.mark.menu
def test_navigation_to_all_item(browser):
    login = LoginPage(browser)
    menu = menu_section(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    menu.open_menu()
    menu.click_all_item()
    assert "inventory" in browser.current_url


@pytest.mark.menu
def test_navigation_to_about(browser):
    login = LoginPage(browser)
    menu = menu_section(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    menu.open_menu()
    menu.click_about()
    assert "saucelabs.com" in browser.current_url


@pytest.mark.menu
def test_navigation_to_logout(browser):
    login = LoginPage(browser)
    menu = menu_section(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    menu.open_menu()
    menu.click_logout()
    assert "https://www.saucedemo.com/" in browser.current_url


@pytest.mark.menu
def test_reset_app_state(browser):
    login = LoginPage(browser)
    menu = menu_section(browser)

    login.load(config.BASE_URL)
    login.login(config.username,config.password)

    menu.open_menu()
    menu.click_reset_app_state()
    assert "inventory" in browser.current_url