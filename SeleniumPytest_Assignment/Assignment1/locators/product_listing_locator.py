from selenium.webdriver.common.by import By

class ProductListingLocators:
    product_items = (By.CLASS_NAME, "inventory_item")
    product_names = (By.CLASS_NAME, "inventory_item_name ")
    product_price = (By.CLASS_NAME, "inventory_item_price")
    product_image = (By.CLASS_NAME, "inventory_item_img")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
