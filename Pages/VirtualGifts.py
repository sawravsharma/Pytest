import random
import string
import sys
import time
from Pages.BasePage import BasePage
from EnumsPackage.VirtualGifts import VirtualGifts


class VirtualGiftsTab(BasePage):
     
    def __init__(self, driver):
        super().__init__(driver)

    '''Function for adding virtual gifts in the cart'''
    def addVirtualGiftsInCart(self):
        self.if_alert()
        self.driver.find_element_by_link_text("Virtual Gifts").click()
        time.sleep(5)
        for gift in VirtualGifts:
            giftEle = self.driver.find_element_by_xpath(
                "//span[contains(text(),'%s')]/following-sibling::a[contains(text(),'Send now')]" % str(gift.value))
            if(giftEle.is_displayed()):
                giftEle.click()
            else:
                pass
                print(gift.value," : ","no product available")
            '''For sending message with the gift'''
            try:
                self.driver.find_element_by_xpath("//*[@id='star-message']").send_keys(
                ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10)))
            except:
                print(gift.value," : ","Message box not available for this gift")
            '''For clicking on Add to cart'''
            try:
                giftAddInCart = self.driver.find_element_by_xpath(  
                    "//div[@class='product-form__payment-container']//button[text()='Add to cart']")
                giftAddInCart.click()
            except:
                pass
                print(gift.value," : ", "Gift currently not available")
            '''This will again take us to virtual gifts page'''
            self.driver.find_element_by_link_text("Virtual Gifts").click()