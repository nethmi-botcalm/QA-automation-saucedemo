from locators.Checkout_locator import checkoutLocators

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_customer_information(self, first_name="", last_name="", postal_code=""):
        self.driver.find_element(*checkoutLocators.first_name).clear()
        self.driver.find_element(*checkoutLocators.second_name).clear()
        self.driver.find_element(*checkoutLocators.postal_code).clear()
        self.driver.find_element(*checkoutLocators.first_name).send_keys(first_name)
        self.driver.find_element(*checkoutLocators.second_name).send_keys(last_name)
        self.driver.find_element(*checkoutLocators.postal_code).send_keys(postal_code)


    def click_continue(self):
        self.driver.find_element(*checkoutLocators.continue_btn).click()

    def get_error_message(self):
        return self.driver.find_element(*checkoutLocators.error_msg).text

    def get_item_name(self):
        return self.driver.find_element(*checkoutLocators.product_name).text

    def get_item_desc(self):
        return self.driver.find_element(*checkoutLocators.product_desc).text

    def get_item_price(self):
        return self.driver.find_element(*checkoutLocators.product_price).text

    def get_item_quantity(self):
        return self.driver.find_element(*checkoutLocators.product_quantity).text

    def get_item_total(self):
        return self.driver.find_element(*checkoutLocators.item_total).text

    def get_item_tax(self):
        return self.driver.find_element(*checkoutLocators.tax).text

    def get_total(self):
        return self.driver.find_element(*checkoutLocators.total).text

    def click_finish(self):
        self.driver.find_element(*checkoutLocators.finish_button).click()

    def get_complete_header(self):
        return self.driver.find_element(*checkoutLocators.complete_title).text

    def get_complete_text(self):
        return self.driver.find_element(*checkoutLocators.complete_text).text

