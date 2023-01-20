import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":

        service_obj = Service("C:/Selenium/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
         # open URL
        driver.maximize_window()
    elif browser_name == "firefox":
        #firefox invocation
        service_obj1=Service("C:/Selenium/geckodriver.exe")
        driver=webdriver.Firefox(service=service_obj1)
    driver.get("https://www.myfancycrafts.com/")

    request.cls.driver= driver
    yield
    driver.close()



