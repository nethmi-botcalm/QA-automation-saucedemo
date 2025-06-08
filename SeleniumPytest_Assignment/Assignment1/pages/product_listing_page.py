
from locators.product_listing_locator import ProductListingLocators
from selenium.webdriver.support.ui import Select

class ProductListingPage:

    def __init__(self, driver):
        self.driver = driver

    def get_all_product(self):
        return self.driver.find_elements(*ProductListingLocators.product_items)

    def get_product_name(self):
        return [el.text for el in self.driver.find_elements(*ProductListingLocators.product_names)]

    def get_product_prices(self):
        return [float(el.text.replace('$', '')) for el in self.driver.find_elements(*ProductListingLocators.product_price)]

    def get_product_image(self):
        return self.driver.find_elements(*ProductListingLocators.product_image)

    def sort_products(self, visible_text):
        select = Select(self.driver.find_element(*ProductListingLocators.sort_dropdown))
        select.select_by_visible_text(visible_text)

    def click_on_product_by_name(self,product_name):
        for el in self.driver.find_elements(*ProductListingLocators.product_names):
            if el.text == product_name:
                el.click()
                return
            raise Exception(f"Product named '{product_name}' not found")

    def click_on_product_image_by_index(self, index = 0):
        image = self.driver.find_elements(*ProductListingLocators.product_image)
        if index >= len(image):
            raise IndexError("Product Image index out of range")
        image[index].click()




