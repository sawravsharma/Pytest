import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import xlrd
from Locators.Locators import Locators
from Config.config import TestData
from Pages.BasePage import BasePage

class LoginPage(BasePage):

    '''constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    '''Page Actions for login page'''

    '''this is use to login to application'''

    def acceptCookies(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()

    def do_login(self):
        self.if_alert()
        self.do_click(Locators.CLICK_ON_MY_ACCOUNT)
        self.do_send_keys(Locators.EMAIL, TestData.USERNAME)
        self.do_send_keys(Locators.PASSWORD, TestData.PASSWORD)
        self.do_click(Locators.LOGIN_BUTTON)
    
    # def do_logout(self):
    #     self.if_alert()
    #     self.do_click(Locators.CLICK_ON_MY_ACCOUNT)
    #     self.do_click(Locators.LOGOUT_BUTTON)