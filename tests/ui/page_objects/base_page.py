from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:
    def init(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def close(self):
        self.driver.close()
        