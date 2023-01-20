import logging

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass

    def Actions(self,text):
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.CSS_SELECTOR,text)).perform()