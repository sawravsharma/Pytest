from pyrsistent import b
from selenium.webdriver.common.by import By

class Locators:
    
    '''Loginpage'''
    LOGIN_PAGE_TITLE = (By.XPATH, "//h2[text()='Login to my account']")
    CLICK_ON_MY_ACCOUNT = (By.XPATH, "(//a[@href = '/account/login'])[2]")
    EMAIL = (By.XPATH, "//*[@id='login-customer[email]']")
    PASSWORD = (By.XPATH, "(//input[@name='customer[password]'])[1]")
    LOGIN_BUTTON = (By.XPATH, "//*[text()='Login']")
    LOGGED_IN_USER = (By.XPATH, "//div[@class='header__action-item header__action-item--account']/span[text()='Hello Saurav']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Incorrect email')]")
    NEW_CUSTOMER_LINK = (By.XPATH, "//*[contains(text(),'Create your account')]")
    CUSTOMER_PAGE_TITLE = (By.XPATH, "//h2[contains(text(),'Create my account')]")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Recover password')]")
    RECOVER_PAGE_TITLE = (By.XPATH, "//a[contains(text(),'Recover password')]")
    CLOTHING_TAB = (By.XPATH, "//li[@class='nav-bar__item']/a[text()='Clothing']")

    '''Homepage'''
    HOME_PAGE_TITLE = (By.XPATH, "//*[text()='Swag Labs']")
    PRODUCT_SORT_CONTAINER = (By.XPATH, "//*[@class='product_sort_container']")
    CART_ICON = (By.XPATH, "//span[@class='hidden-pocket hidden-lap']")
    COMMON_XPATH_SORT_CONTAINER = (By.XPATH, "//*[@class='product_sort_container']//option)[%s]")
    HEADER = (By.XPATH, "//span[text()='Products']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')])[%s]")
    BURGER_MENU_BUTTON = (By.XPATH, "//button[text()='Open Menu']")
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='popover__linklist']/a[text()='Logout']")

    '''Cart page'''
    CART_PAGE_HEADER = (By.XPATH, "//span[text()='Your Cart']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Checkout']")