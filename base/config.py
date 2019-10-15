import traceback
from selenium import webdriver
import os

class Config():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "http://localhost:3100"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            # Set chrome driver
            chromedriver = "C:/Users/fonit/workspace/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(1920, 1080)
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver