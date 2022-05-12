import time
from EnumsPackage.Beauty import Beauty
from EnumsPackage.Emolyne import Emolyne
from Pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class BeautyTab(BasePage):
     
    def __init__(self, driver):
        super().__init__(driver)

    '''Adding Emolynes in the cart'''
    def addEmolyneItemsInCart(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        element = self.driver.find_element_by_link_text("Beauty")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        beautyProd = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Beauty.Beauty_Name_Emolyne.value))
        beautyProd.click()
        for items in Emolyne:
            try:
                beautyItems = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % str(items.value))
                beautyItems.click()
            except:
                pass
            '''Adding in the cart'''
            try:
                self.driver.find_element_by_xpath(
                    "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            except Exception:
                pass
                print(items.value," : ", "Beauty items not available")
            '''Taking us back again on the Emlyne page'''
            element = self.driver.find_element_by_link_text("Beauty")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            beautyProd = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Beauty.Beauty_Name_Emolyne.value))
            beautyProd.click()