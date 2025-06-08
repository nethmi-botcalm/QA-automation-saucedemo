import pytest
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage
from config import config

@pytest.mark.product
def test_product_display(browser):
    login = LoginPage(browser)
    products_page = ProductListingPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    products = products_page.get_all_product()
    #check product count is equal to 6
    assert len(products) == 6, f"Expected 6 products, found {len(products)}"


@pytest.mark.product
def test_product_name_and_price(browser):
    login = LoginPage(browser)
    products_page = ProductListingPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    # check product names and product price present
    names = products_page.get_product_name()
    prices = products_page.get_product_prices()

    assert all(name != "" for name in names), "Some product names are missing"
    assert all(price > 0 for price in prices), "Some product prices are invalid"


@pytest.mark.product
def test_product_image_visibility(browser):
    login = LoginPage(browser)
    products_page = ProductListingPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    # check all images are visible?
    images = products_page.get_product_image()
    for img in images:
        assert img.is_displayed(), "Product image not visible"


@pytest.mark.product
def test_sort_by_name_a_to_z(browser):
    login = LoginPage(browser)
    products_page = ProductListingPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username,config.password)

    # check Sorting by name (A-Z).
    products_page.sort_products("Name (A to Z)")

    names = products_page.get_product_name()
    assert names == sorted(names), "Products not sorted alphabetically A-Z"


@pytest.mark.product
def test_sort_by_name_z_to_a(browser):
    login = LoginPage(browser)
    products_page = ProductListingPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    #check sorting by name (Z-A).
    products_page.sort_products("Name (Z to A)")

    names = products_page.get_product_name()
    assert names == sorted(names, reverse = True), "Product not sorted alphabetically Z-A"


@pytest.mark.product
def test_sort_by_price_low_to_high(browser):
    login = LoginPage(browser)
    products_page = ProductListingPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username, config.password)

    # check Sorting by name (A-Z).
    products_page.sort_products("Price (low to high)")

    price = products_page.get_product_prices()
    assert price == sorted(price), "Products not sorted by price (low to high)"


@pytest.mark.product
def test_sort_by_price_high_to_low(browser):
    login = LoginPage(browser)
    products_page = ProductListingPage(browser)

    login.load(config.BASE_URL)
    login.login(config.username,config.password)

    # check Sorting by name (Z-A).
    products_page.sort_products("Price (high to low)")

    prices = products_page.get_product_prices()
    assert prices == sorted(prices, reverse = True), "Products not sorted by price (low to high)"

