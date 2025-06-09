from locators.cart_locator import CartLocator

class CartPage:
    def __int__(self, driver):
        self.driver = driver

    def get_cart_element(self):
        self.driver.find_elements(*CartLocator.cart_item)

    def get_cart_item_name(self):
        return [item.text for item in self.driver.find_elements(*CartLocator.product_name)]

    def get_cart_item_price(self):
        return [item.text for item in self.driver.find_elements(*CartLocator.product_price)]

    def navigate_to_inventory(self):
        self.driver.find_element(*CartLocator.continue_shopping_btn).click()

    def navigate_to_checkout(self):
        self.driver.find_element(*CartLocator.Checkout_btn).click()

    def remover_from_cart(self):
        self.driver.find_elements(*CartLocator.remove_btn)[0].click()



