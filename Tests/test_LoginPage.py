import sys, os
import time
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import allure
import pytest
from Locators.Locators import Locators
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Pages.LoginPage import LoginPage 
from Locators.Locators import Locators
from allure import severity, severity_level

class Test_Login(BaseTest):


    # @allure.description('''Login with correct credentials''')
    @pytest.mark.order()
    @severity(severity_level.CRITICAL)
    def test_verify_login_into_app(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)
    
    
    # @pytest.mark.order(3)
    # def test_verify_logout_outoff_app(self):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.do_login()
    #     time.sleep(3)
    #     self.loginPage.do_logout()
    #     allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)
        

    # @pytest.mark.order(4)
    # def test_verify_login_user(self):
    #     self.loginPage = LoginPage(self.driver)
        
    #     self.loginPage.do_login()
    #     self.loginPage.if_alert()
    #     Logged_IN = self.loginPage.logged_in_user()
    #     assert Logged_IN == TestData.LOGGED_IN_USER
    #     allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    # '''login with incorrect credentials'''
    # @pytest.mark.order(5)
    # def test_verify_login_into_app_with_incorrect_credentials(self):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.do_login_with_incorrect_credentials()
    #     error_msg = self.loginPage.get_element_text(Locators.ERROR_MESSAGE)
    #     assert error_msg == TestData.LOGIN_WITH_INCORRECT_CREDENTIALS_MESSAGE
    #     allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    # def test_everythingOfLoginPage(self):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.do_login()
    #     title = self.loginPage.get_title()
    #     assert title == TestData.LOGIN_PAGE_TITLE
    #     print(title)
    #     Logged_IN = self.loginPage.logged_in_user()
    #     assert Logged_IN == TestData.LOGGED_IN_USER
    #     print(Logged_IN)
    #     time.sleep(3)
    #     self.loginPage.do_logout()
    #     self.loginPage.do_login_with_incorrect_credentials()
    #     error_msg = self.loginPage.get_element_text(Locators.ERROR_MESSAGE)
    #     assert error_msg == TestData.LOGIN_WITH_INCORRECT_CREDENTIALS_MESSAGE


