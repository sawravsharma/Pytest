import sys, os

import pytest
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Locators.Locators import Locators
from Pages.BasePage import BasePage
from EnumsPackage.Clothing import Clothing
from selenium.webdriver.common.action_chains import ActionChains
from EnumsPackage.TshirtsAndSweatShirts import TshirtsAndSweatShirts, TshirtsAndSweatShirtsAddedInCart

class AddToCartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_add_to_cart_page_header(self):
            return self.get_element_text(Locators.CART_PAGE_HEADER)

    @pytest.mark.xfail
    @pytest.mark.expectingFailure
    def is_items_exist_in_cart(self):
        self.if_alert()
        element = self.driver.find_element_by_link_text("Clothing")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        Tees = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Clothing.CLOTHING_Name_TShirt.value))
        Tees.click()
        for cloth in TshirtsAndSweatShirts:
            cloth = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % str(cloth.value))
            cloth.click()
            self.driver.find_element_by_xpath(
                "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            element = self.driver.find_element_by_link_text("Clothing")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            Tees = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Clothing.CLOTHING_Name_TShirt.value))
            Tees.click()
        self.driver.find_element_by_xpath("//*[text()='Cart']").click()
        for getValue in TshirtsAndSweatShirtsAddedInCart:
            searchProductPresence  = self.driver.find_element_by_xpath(
                     "//a[contains(text(),'%s')]" % str(getValue.value))
        print(searchProductPresence.text)
        assert searchProductPresence.text == getValue.value

    def do_click_checkout_button(self):
        self.do_click(Locators.CHECKOUT_BUTTON)

