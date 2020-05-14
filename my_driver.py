# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MyDriver(object):

    def __init__(self):
        self.driver = None

    def get_driver(self, browser="chrome"):
        if browser.lower() == "chrome":
            self.driver = self.chrome_driver()
            return self.driver
        else:
            raise AssertionError("We only implemented codes for Chrome!")

    @staticmethod
    def chrome_driver(headless=False):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(
            executable_path='chromedriver',
            options=chrome_options)
        return driver
