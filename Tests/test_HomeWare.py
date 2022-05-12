import allure 
from allure_commons.types import AttachmentType
import pytest
from Pages.HomeWare import HomewareTab
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class Test_HomeWare(BaseTest):
    @pytest.mark.foodDrinks
    # @allure.description('''Verifying food and drinks products are getting added in the cart or not''')
    def test_TshirtsAndSweatshirtstabs(self):
        self.loginPage = LoginPage(self.driver)
        homeWare = HomewareTab(self.driver)
        homeWare.addFoodAndDrinksInCart()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)