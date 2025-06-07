from locators.menu_locator import MenuLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class menu_section:

    def __init__(self, driver):
        self.driver = driver

    def open_menu(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(MenuLocator.Menu_button)).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MenuLocator.Sidebar_menu))
        # self.driver.find_element(*MenuLocator.Menu_button).click()


    def close_menu(self):
        self.driver.find_element(*MenuLocator.Menu_close_button).click()

    def is_menu_display(self):
        return WebDriverWait(self.driver, 5 ).until(EC.visibility_of_element_located(MenuLocator.Sidebar_menu))

    def click_all_item(self):
        self.driver.find_element(*MenuLocator.All_item_text).click()

    def click_about(self):
        self.driver.find_element(*MenuLocator.About_text).click()


    def click_logout(self):
        self.driver.find_element(*MenuLocator.Logout_text).click()

    def click_reset_app_state(self):
        self.driver.find_element(*MenuLocator.Reset_text).click()

