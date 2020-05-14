# -*- coding:utf-8 -*-
import time
from retrying import retry
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GooglePage(object):

    start_url = "https://www.google.com/imghp?hl=en&tab=wi&ogbl"
    img_locator = "//img[@alt!='' and not(contains(@alt, 'Google Doodles'))]"
    search_box_locator = "q"

    def __init__(self, dr):
        self.driver = dr
        self.wait = WebDriverWait(self.driver, 30)

    def wait_page_loaded(self):
        self.wait.until(PageLoaded())

    def go_to_img_search_page(self):
        self.driver.get(self.start_url)
        self.wait.until(EC.presence_of_element_located((By.NAME, self.search_box_locator)))

    @retry(
        stop_max_attempt_number=5,
        wait_random_min=500,
        wait_random_max=999)
    def search_img_by_keyword(self, keyword):
        search_box = self.driver.find_element_by_name(self.search_box_locator)
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        #self.wait.until(EC.title_contains(keyword))
        self.wait_page_loaded()
        time.sleep(2)

    def get_images(self, keyword, number=10):
        img_data_list, count = [], 0
        print(self.img_locator.format(keyword))
        #img_elements = self.driver.find_elements_by_xpath(self.img_locator.format(keyword))
        img_elements = self.driver.find_elements_by_xpath(self.img_locator)
        print(len(img_elements))
        print("Get {} pictures".format(len(img_elements)))
        for element in img_elements:
            print(element.get_attribute("alt"))
            img_data_list.append(element.get_attribute("src"))
            count = count + 1
            if count == number:
                break

        return img_data_list


class PageLoaded:
    def __call__(self, dr):
        ready = dr.execute_script(
                "return document.readyState=='complete';"
            )
        if ready:
            return True
        else:
            return False
