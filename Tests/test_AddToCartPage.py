import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import pytest
import allure 
from allure_commons.types import AttachmentType
from Pages.AddToCartPage import AddToCartPage
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest

class Test_AddTOCartPage(BaseTest):

    # @allure.description('''Verifying items added in cart''')
    @pytest.mark.addToCart
    @pytest.mark.order()
    def test_verify_item_in_cart(self):
        self.loginPage = LoginPage(self.driver)
        addToCart = AddToCartPage(self.driver)
        addToCart.is_items_exist_in_cart()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)