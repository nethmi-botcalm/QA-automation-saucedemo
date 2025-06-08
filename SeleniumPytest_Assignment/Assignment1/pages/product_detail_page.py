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

    def click_back_to_product(self):
        self.driver.find_element(*ProductDetailLocator.back_to_product).click()