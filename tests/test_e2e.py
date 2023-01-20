import time

import pytest
from TestData.PageData import HomePageData
from pageObject.HomePage import HomePage
from pageObject.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self, getData):
        # click on shop button
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        # search for products
        searchProd = ShopPage(self.driver)
        searchProd.searchProduct().click()
        # insert value in text box
        insValue = ShopPage(self.driver)
        insValue.insertValue().send_keys(getData["name1"])
        # add to cart button
        addCart = ShopPage(self.driver)
        addCart.addToCart().click()

        # hover to checkout button
        self.Actions("a[title='Cart']")
        # action=ActionChains(self.driver)
        # action.move_to_element(self.driver.find_element(By.CSS_SELECTOR,"a[title='Cart']")).perform()
        # click on checkout button
        checkOut = ShopPage(self.driver)
        checkOut.checkButton().click()
        time.sleep(5)

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param


    print("this ios just for testing purpose")
