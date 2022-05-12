import sys
import time
from selenium.webdriver.common.action_chains import ActionChains
from EnumsPackage.Homeware import Homeware
from EnumsPackage.FoodDrinks import FoodAndDrinks
from Pages.BasePage import BasePage


class HomewareTab(BasePage):
     
    def __init__(self, driver):
        super().__init__(driver)

    '''Adding food and drinks in the cart'''
    def addFoodAndDrinksInCart(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        element = self.driver.find_element_by_link_text("Homeware")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        foods = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Homeware.Homeware_Name_Food_Drink.value))
        foods.click()
        for food in FoodAndDrinks:
            foodAndDrinks = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % str(food.value))
            foodAndDrinks.click()
            time.sleep(3)
            '''Adding items in cart'''
            try:
                self.driver.find_element_by_xpath(
                    "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            except:
                pass
                print(food.value," :","Sold out")
            '''Taking us back again on the Homeware page'''
            element = self.driver.find_element_by_link_text("Homeware")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            foods = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Homeware.Homeware_Name_Food_Drink.value))
            foods.click()