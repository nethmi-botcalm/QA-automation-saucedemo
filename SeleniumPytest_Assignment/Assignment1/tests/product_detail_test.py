import pytest
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage
from pages.product_detail_page import ProductDetailPage
from config import config

@pytest.mark.ProductDetail
def test_product_detail_content(browser):
    login = LoginPage(browser)
    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    listing = ProductListingPage(browser)
    first_name = listing.get_product_name()[0]
    listing.click_on_product_by_name(first_name)

    detail = ProductDetailPage(browser)
    assert detail.is_correct_product_loaded(first_name), "Product detail title does not match"


@pytest.mark.ProductDetail
def test_product_image_redirection(browser):
    login = LoginPage(browser)
    listing = ProductListingPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    first_name = listing.get_product_name()[0]
    listing.click_on_product_image_by_index(0)

    detail = ProductDetailPage(browser)
    assert detail.is_correct_product_loaded(first_name), "Image click did not redirect to correct product page"



@pytest.mark.ProductDetail
def test_back_to_productListing(browser):
    login = LoginPage(browser)
    listing = ProductListingPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    product_name = listing.get_product_name()[0]
    listing.click_on_product_by_name(product_name)

    detail = ProductDetailPage(browser)
    detail.click_back_to_product()
    assert "inventory" in browser.current_url, "Did not navigated to the product listing page"


@pytest.mark.ProductDetail
def test_add_remove_from_cart_on_detail_page(browser):
    login = LoginPage(browser)
    listing = ProductListingPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    product_name = listing.get_product_name()[0]
    listing.click_on_product_by_name(product_name)

    detail = ProductDetailPage(browser)

    detail.click_add_to_cart()
    assert detail.get_add_to_cart_button_text() == "Remove", "Button text did not change to 'Remove'"
    assert detail.get_cart_count() == "1", "Cart count did not increase to 1"

    detail.click_add_to_cart()
    assert detail.get_add_to_cart_button_text() == "Add to cart", "Button text did not revert to 'Add to cart'"
    assert detail.get_cart_count() == "0", "Cart count did not decrease to 0"

