import pytest
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.Checkout_page import CheckoutPage
from config import config

@pytest.mark.order
def test_checkout_form_validation_and_completion(browser):
    login = LoginPage(browser)
    listing = ProductListingPage(browser)
    detail = ProductDetailPage(browser)
    cart = CartPage(browser)
    checkout = CheckoutPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)


    product_name = listing.get_product_name()[0]
    listing.click_on_product_by_name(product_name)


    detail.click_add_to_cart()
    assert detail.get_add_to_cart_button_text() == "Remove", "Add to cart failed"


    cart.click_cart_icon()

    assert cart.get_cart_product_name() == product_name, "Product not in cart"
    assert cart.get_cart_count() == "1", "Cart count mismatch"

    cart.navigate_to_checkout()


    checkout.enter_customer_information("", "", "")
    checkout.click_continue()
    assert "Error" in checkout.get_error_message()

    checkout.enter_customer_information("nethmi", "", "80400")
    checkout.click_continue()
    assert "Error" in checkout.get_error_message()

    checkout.enter_customer_information("nethmi","rashmika","80400")
    checkout.click_continue()

    assert checkout.get_item_name() == product_name
    assert checkout.get_item_quantity() == "1"
    assert "$9.99" in checkout.get_item_price()
    assert "$9.99" in checkout.get_item_total()
    assert "$0.80" in checkout.get_item_tax()
    assert "$10.79" in checkout.get_total()

    checkout.click_finish()
    assert checkout.get_complete_header() == "Thank you for your order!"
    assert "Your order has been dispatched" in checkout.get_complete_text()




