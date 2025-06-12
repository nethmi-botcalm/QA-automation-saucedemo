from selenium.webdriver.common.by import By

class checkoutLocators:
    first_name = (By.ID, "first-name")
    second_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    error_msg = (By.CLASS_NAME, "error-message-container")

    summary_product = (By.CLASS_NAME, "cart_item")
    product_name = (By.CLASS_NAME, "inventory_item_name")
    product_desc = (By.CLASS_NAME, "inventory_item_desc")
    product_price = (By.CLASS_NAME, "inventory_item_price")
    product_quantity = (By.CLASS_NAME, "cart_quantity")

    item_total = (By.CLASS_NAME, "summary_subtotal_label")
    tax = (By.CLASS_NAME, "summary_tax_label")
    total = (By.CLASS_NAME, "summary_total_label")
    finish_button = (By.ID, "finish")

    complete_title = (By.CLASS_NAME, "complete-header")
    complete_text = (By.CLASS_NAME, "complete-text")