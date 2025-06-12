from locators.Checkout_locator import checkoutLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import TimeoutException, NoAlertPresentException


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_customer_information(self, first_name="", last_name="", postal_code=""):
        try:
            self.wait.until(
                EC.visibility_of_element_located(checkoutLocators.first_name)
            )
        except TimeoutException:
            raise Exception("Checkout form did not load properly")


        self.driver.find_element(*checkoutLocators.first_name).clear()
        self.driver.find_element(*checkoutLocators.second_name).clear()
        self.driver.find_element(*checkoutLocators.postal_code).clear()

        self.driver.find_element(*checkoutLocators.first_name).send_keys(first_name)
        self.driver.find_element(*checkoutLocators.second_name).send_keys(last_name)
        self.driver.find_element(*checkoutLocators.postal_code).send_keys(postal_code)


    def click_continue(self):
        self.driver.find_element(*checkoutLocators.continue_btn).click()

    def handle_alert_if_present(self, timeout: object = 3) -> object:
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()  # or alert.dismiss() if you want
            print("Alert detected and accepted.")
        except TimeoutException:
            # No alert appeared within timeout
            pass
        except NoAlertPresentException:
            # No alert present
            pass
        
    def wait_for_error_message(self, timeout=5):
        self.handle_alert_if_present(timeout=2)
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*checkoutLocators.error_msg).text.strip() != ""
        )

    def get_error_message(self):
        try:
            element = self.driver.find_element(*checkoutLocators.error_msg)
            return element.text.strip()
        except Exception:
            return ""

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

