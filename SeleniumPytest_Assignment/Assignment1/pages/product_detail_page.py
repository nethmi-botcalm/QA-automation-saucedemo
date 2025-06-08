from locators.product_detail_locator import ProductDetailLocator

class ProductDetailPage:

    def __init__(self,driver):
        self.driver = driver

    def get_product_title(self):
        return self.driver.find_element(*ProductDetailLocator.product_title).text

    def get_product_description(self):
        return self.driver.find_element(*ProductDetailLocator.product_desc).text

    def get_product_price(self):
        return self.driver.find_element(*ProductDetailLocator.product_price).text

    def get_product_image(self):
        return self.driver.find_element(*ProductDetailLocator.product_image).get_attribute("src")

    def is_correct_product_loaded(self, expected_title):
        actual_title = self.get_product_title()
        return expected_title == actual_title

    def click_back_to_product(self):
        self.driver.find_element(*ProductDetailLocator.back_to_product).click()

    def click_add_to_cart(self):
        self.driver.find_element(*ProductDetailLocator.add_to_cart_button).click()

    def get_cart_count(self):
        elements = self.driver.find_elements(*ProductDetailLocator.cart_count)
        return elements[0].text if elements else "0"

    def get_add_to_cart_button_text(self):
        return self.driver.find_element(*ProductDetailLocator.add_to_cart_button).text

