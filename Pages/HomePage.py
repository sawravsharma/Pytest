
# import os,sys
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')

from ast import Assert
import time
import string
import random
from selenium import webdriver
from EnumsPackage.EnamelPin import EnamelPin
from EnumsPackage.FoodDrinks import FoodAndDrinks
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from EnumsPackage.Clothing import Clothing
from selenium.webdriver.common.action_chains import ActionChains
from EnumsPackage.Beauty import Beauty
from EnumsPackage.DisplayPerPage import DisplayPerPage
from EnumsPackage.Homeware import Homeware
from EnumsPackage.Stationery import Stationery
from EnumsPackage.TshirtsAndSweatShirtsSorting import TshirtsAndSweatShirtsSorting
from EnumsPackage.Emolyne import Emolyne

from EnumsPackage.TshirtsAndSweatShirts import TshirtsAndSweatShirts

class HomePage(BasePage):
 
    def __init__(self, driver):
        super().__init__(driver)

    '''Title'''
    def get_home_page_title(self, title):
        return self.get_title(title)

    '''To check Cart icon'''
    def is_cart_icon_exist(self):
        self.if_alert()
        return self.is_visible(Locators.CART_ICON)

    '''To check if clothing tab and sub tabs are clickable or not'''
    def clickClothingTab(self):
        self.if_alert()
        for sorting in Clothing:
            element = self.driver.find_element_by_link_text("Clothing")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()

    '''To check if HomeWare tab and sub tabs are clickable or not'''
    def clickHomeWareTab(self):
        self.if_alert()
        for sorting in Homeware:
            element = self.driver.find_element_by_link_text("Homeware")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()

    '''To check if Stationery tab and sub tabs are clickable or not'''
    def clickStationeryTab(self):
        self.if_alert()
        for sorting in Stationery:
            element = self.driver.find_element_by_link_text("Stationery")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()

    '''To check if Beauty tab and sub tabs are clickable or not'''
    def clickBeautyTab(self):
        self.if_alert()
        for sorting in Beauty:
            element = self.driver.find_element_by_link_text("Beauty")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()
    
    '''To check Shop Home tab is clickable or not'''
    def clickShopHomeTab(self):
        self.if_alert()
        self.driver.find_element_by_link_text("Shop Home")

    '''clicking New In tab and asserting 24 products filter per page'''
    def clickNewInTab(self):
        self.if_alert()
        self.driver.find_element_by_xpath("(//*[text()='New In '])[2]").click()
        self.driver.find_element_by_xpath("//button[@class='value-picker-button']//span[contains(text(),'Display')]").click()
        page = self.driver.find_element_by_xpath(
            "//button[contains(text(),'%s')]" % str(DisplayPerPage.Display_per_page_24.value))
        page.click()
        time.sleep(3)
        element_found = self.driver.find_elements_by_xpath("//div[@class='product-item product-item--vertical  1/3--tablet-and-up 1/3--desk']")
        time.sleep(3)
        print(len(element_found))
        assert len(element_found) == 24

    '''To check virtua; gifts tab is clickable or not'''
    def clickVirtualGiftsTab(self):
        self.if_alert()
        self.driver.find_element_by_link_text("Virtual Gifts").click()

    '''To check Sale tab is clickable or not'''
    def clickSaleTab(self):
        self.if_alert()
        self.driver.find_element_by_link_text("Sale")

    '''To check cart is clickable or not'''
    def clickOnCartButton(self):
        self.if_alert()
        self.driver.find_element_by_xpath("//*[text()='Cart']").click()

    '''Logout functionality'''
    def do_logout(self):
        self.if_alert()
        self.do_click(Locators.LOGOUT_BUTTON)


    


