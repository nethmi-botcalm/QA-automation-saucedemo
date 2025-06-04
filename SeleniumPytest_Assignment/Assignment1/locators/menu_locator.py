from selenium.webdriver.common.by import By

class MenuLocator:
    Menu_button = (By.ID, "react-burger-menu-btn")
    Menu_close_button = (By.ID, "react-burger-cross-btn")
    All_item_text = (By.ID, "inventory_sidebar_link")
    About_text = (By.ID, "about-sidebar-link")
    Logout_text = (By.ID, "logout_sidebar_link")
    Reset_text = (By.ID, "reset_sidebar_link")
    Slidebar_menu = (By.CLASS_NAME, "bm-item-list")