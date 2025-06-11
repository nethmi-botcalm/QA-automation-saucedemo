from selenium.webdriver.common.by import By

class CartLocator:
    cart_item = (By.CLASS_NAME, "cart_item")
    item_name = (By.CLASS_NAME, "inventory_item_name")
    item_desc = (By.CLASS_NAME, "inventory_item_desc")
    item_price = (By.CLASS_NAME, "inventory_item_price")
    remove_btn = (By.XPATH, "//button[text()='Remove']")
    Checkout_btn = (By.ID, "checkout")
    continue_shopping_btn = (By.ID, "continue-shopping")
    product_name = (By.CLASS_NAME, "inventory_item_name")
    cart_icon = (By.XPATH, "//*[@id='shopping_cart_container']/a")
