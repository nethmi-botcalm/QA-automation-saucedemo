from selenium.webdriver.common.by import By

class CartLocator:
    cart_icon = (By.CLASS_NAME , "shopping_cart_link")
    remove_btn = (By.ID, "remove-sauce-labs-backpack")
    Checkout = (By.ID, "checkout")
    continue_shopping = (By.ID, "continue-shopping")
    product_name = (By.CLASS_NAME, "inventory_item_name")