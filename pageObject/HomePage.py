from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver=driver

    shop=(By.XPATH,"//a[text()='Birthday Gifts']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)# we add star to deserialized it as touple
        #driver.find_element(By.XPATH,"//a[text()='Birthday Gifts']")




    print("hii how are you")
