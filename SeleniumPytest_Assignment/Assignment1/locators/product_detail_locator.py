from selenium.webdriver.common.by import By

class ProductDetailLocator:
    product_title = (By.CLASS_NAME, "inventory_item_name")
    product_desc = (By.CLASS_NAME, "inventory_item_desc")
    product_price = (By.CLASS_NAME, "inventory_item_price")
    back_to_product = (By.ID, "back-to-products")
