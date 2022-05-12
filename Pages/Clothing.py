import time
from EnumsPackage.Clothing import Clothing
from selenium.webdriver.common.action_chains import ActionChains
from EnumsPackage.TshirtsAndSweatShirts import TshirtsAndSweatShirts
from Pages.BasePage import BasePage

class ClothingTab(BasePage):
     
    def __init__(self, driver):
        super().__init__(driver)
        
    def clickTshirtsAndSweatShirtsTab(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        element = self.driver.find_element_by_link_text("Clothing")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        Tees = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Clothing.CLOTHING_Name_TShirt.value))
        Tees.click()
        for cloth in TshirtsAndSweatShirts:
            try:
                clothes = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % str(cloth.value))
                clothes.click()
            except:
                pass
            time.sleep(3)
            '''Adding clothes in the cart '''
            try:
                self.driver.find_element_by_xpath(
                    "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            except:
                pass
                print(cloth.value," : ", "Following product not available")

            '''Taking us back again on the Tshirt and SwearShirts tab'''
            element = self.driver.find_element_by_link_text("Clothing")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            Tees = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Clothing.CLOTHING_Name_TShirt.value))
            Tees.click()