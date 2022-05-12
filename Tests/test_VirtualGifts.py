import pytest
import allure 
from allure_commons.types import AttachmentType
from Pages.LoginPage import LoginPage
from Pages.VirtualGifts import VirtualGiftsTab
from Tests.test_Base import BaseTest


class Test_VirtualGifts(BaseTest):
    @pytest.mark.virtualgifts
    # @allure.description('''Adding virtual gifts in cart''')
    def test_addingVirtualGiftsInCart(self):
        self.loginPage = LoginPage(self.driver)
        virtualGift = VirtualGiftsTab(self.driver)
        virtualGift.addVirtualGiftsInCart()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)