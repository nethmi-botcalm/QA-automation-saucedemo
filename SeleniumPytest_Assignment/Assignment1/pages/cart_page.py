from locators.cart_locator import CartLocator


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*CartLocator.cart_item))

    def click_cart_icon(self):
        self.driver.find_element(*CartLocator.cart_icon).click()

    def get_cart_item_names(self):
        return [item.text for item in self.driver.find_elements(*CartLocator.product_name)]

    def get_cart_item_prices(self):
        return [item.text for item in self.driver.find_elements(*CartLocator.item_price)]

    def navigate_to_inventory(self):
        self.driver.find_element(*CartLocator.continue_shopping_btn).click()

    def navigate_to_checkout(self):
        self.driver.find_element(*CartLocator.Checkout_btn).click()

    def remove_first_item(self):
        self.driver.find_elements(*CartLocator.remove_btn)[0].click()

    def is_item_removed(self, expected_count):
        return self.get_cart_item_count() == expected_count
