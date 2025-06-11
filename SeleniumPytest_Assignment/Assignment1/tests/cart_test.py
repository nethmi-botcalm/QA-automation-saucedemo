import pytest
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from config import config

@pytest.mark.cart
def test_cart_add_remove_flow(browser):
    login = LoginPage(browser)
    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    listing = ProductListingPage(browser)
    first_product_name = listing.get_product_name()[0]
    listing.click_on_product_by_name(first_product_name)

    detail = ProductDetailPage(browser)
    assert detail.is_correct_product_loaded(first_product_name)

    detail.click_add_to_cart()

    cart = CartPage(browser)
    cart.click_cart_icon()

    initial_count = cart.get_cart_item_count()
    cart.remove_first_item()

    assert cart.is_item_removed(initial_count - 1), "item was not removed from the count"

@pytest.mark.cart
def test_continue_shopping_redirection(browser):
    login = LoginPage(browser)
    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    cart = CartPage(browser)
    cart.click_cart_icon()
    cart.navigate_to_inventory()

    assert "inventory" in browser.current_url, "did not navigate back to the product listing page"

@pytest.mark.cart
def test_checkout_button_redirection(browser):
    login = LoginPage(browser)
    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    cart = CartPage(browser)
    cart.click_cart_icon()
    cart.navigate_to_checkout()

    assert "checkout-step-one" in browser.current_url, "Did not navigate to checkout step one page"