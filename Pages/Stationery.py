
import sys
from selenium.webdriver.common.action_chains import ActionChains
from EnumsPackage.EnamelPin import EnamelPin
from EnumsPackage.Stationery import Stationery
from Pages.BasePage import BasePage


class StationeryTab(BasePage):
     
    def __init__(self, driver):
        super().__init__(driver)

    '''this function is for adding Enamel pin in cart'''
    def addProductsOfEnamelPinBadgesinCart(self):
        element = self.driver.find_element_by_link_text("Stationery")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        Enamel = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Stationery.Stationery_Name_EnamelPinBadges.value))
        Enamel.click()
        for pins in EnamelPin:
            enamelPins = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % str(pins.value))
            if(enamelPins.is_displayed()):
                enamelPins.click()
            else:
                raise Exception("Element not found")

            '''this block of code is for adding Enamel Pins in the cart'''
            element = self.driver.find_elements_by_xpath(
                     "//div[@class='product-form__payment-container']//button[text()='Add to cart']")
            if not element:
                pass
                print(pins.value," : ","Element sold out")
            else: 
                self.driver.find_element_by_xpath(
                     "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()

            # try:
            #     enamelPinAddedInCart=self.driver.find_element_by_xpath(
            #         "//div[@class='product-form__payment-container']//button[text()='Add to cart']")
            #     enamelPinAddedInCart.click()
            # except:
            #     pass
            #     print(enamelPinAddedInCart,"Product sold out")

            '''this will again take us back to the Enamel Pins page'''
            element = self.driver.find_element_by_link_text("Stationery")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            Enamel = self.driver.find_element_by_xpath(
                    "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Stationery.Stationery_Name_EnamelPinBadges.value))
            Enamel.click()