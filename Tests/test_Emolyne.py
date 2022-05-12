import pytest
import allure 
from allure_commons.types import AttachmentType
from Pages.Emolyne import BeautyTab
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class Test_EmolyneTab(BaseTest):
    @pytest.mark.emolyne
    # @allure.description('''Verifying Emolyne items are getting added in the Cart or not''')
    def test_addingEmolyneItemsInCart(self):
        self.loginPage = LoginPage(self.driver)
        emolyne = BeautyTab(self.driver)
        emolyne.addEmolyneItemsInCart()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)