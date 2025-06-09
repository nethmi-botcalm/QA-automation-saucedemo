from selenium.webdriver.common.by import By

class CartLocator:
    cart_item = (By.CLASS_NAME, "cart_item")
    remove_btn = (By.ID, "remove-sauce-labs-backpack")
    Checkout_btn = (By.ID, "checkout")
    continue_shopping_btn = (By.ID, "continue-shopping")
    product_name = (By.CLASS_NAME, "inventory_item_name")
    product_price = (By.CLASS_NAME, "inventory_item_price")