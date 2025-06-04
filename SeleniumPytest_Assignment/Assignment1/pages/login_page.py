import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocators

#for encapsulation all logics and locators related to the login page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver


    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*LoginLocators.USERNAME_INPUT).send_keys(username)
        time.sleep(5)
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        time.sleep(5)
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def get_error_message(self):
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(LoginLocators.ERROR_MESSAGE)
            )
            return error_element.text.strip()
        except Exception as e:
            print(f"Error element not found: {e}")
            return ""


