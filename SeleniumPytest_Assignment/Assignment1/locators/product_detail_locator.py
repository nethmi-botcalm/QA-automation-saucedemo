from selenium.webdriver.common.by import By

class ProductDetailLocator:
    product_title = (By.CLASS_NAME, "inventory_details_name")
    product_image = (By.CLASS_NAME, "inventory_details_img")
    product_desc = (By.CLASS_NAME, "inventory_details_desc")
    product_price = (By.CLASS_NAME, "inventory_details_price")
    add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
    back_to_product = (By.CLASS_NAME, "btn_inventory")
    cart_count = (By.CLASS_NAME, "shopping_cart_badge")
