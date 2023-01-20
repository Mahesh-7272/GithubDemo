from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self,driver):
        self.driver=driver


    shop=(By.XPATH,"//a[text()='18K Gold Plated Name Necklace With Heart']")
    value=(By.ID,"text-1659023123063")
    cart=(By.NAME,"add-to-cart")
    checkout=(By.CSS_SELECTOR,"a[href*='checkout']")


    # self.driver.find_element(By.XPATH,"//a[text()='18K Gold Plated Name Necklace With Heart']").click()
    def searchProduct(self):
        return self.driver.find_element(*ShopPage.shop)

    # self.driver.find_element(By.ID,"text-1659023123063").send_keys("mahesh")
    def insertValue(self):
        return self.driver.find_element(*ShopPage.value)

    #        self.driver.find_element(By.NAME,"add-to-cart").click()
    def addToCart(self):
        return self.driver.find_element(*ShopPage.cart)
    #         self.driver.find_element(By.CSS_SELECTOR,"a[href*='checkout']").click()
    def checkButton(self):
        return self.driver.find_element(*ShopPage.checkout)
