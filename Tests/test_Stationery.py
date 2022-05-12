import pytest
import allure 
from allure_commons.types import AttachmentType
from Pages.LoginPage import LoginPage
from Pages.Stationery import StationeryTab
from Tests.test_Base import BaseTest


class Test_StationeryTab(BaseTest):
    @pytest.mark.enamelPins
    # @allure.description('''Adding Enamel pins in cart''')
    def test_addingEnamelPinsInCart(self):
        self.loginPage = LoginPage(self.driver)
        enamel = StationeryTab(self.driver)
        enamel.if_alert()
        enamel.addProductsOfEnamelPinBadgesinCart()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)