from selenium import webdriver
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver

import logging
import utilities.custom_logger as cl


class TestMainLayout:

    # Logger
    log = cl.custom_logger(logging.DEBUG)

    def test_menu_booting(self):
        base_url = "https://m.kshop.co.kr/display/ec/display/main"
        self.driver = webdriver.Chrome()
        self.driver.get(base_url)
        self.log.info(f"Opened {base_url}")

        try:
            category_element = self.driver.find_element(By.CLASS_NAME, 'category')
            self.log.info(f"Category: {category_element.text}")
        except Exception as e:
            self.log.error(f"Not Find Category Element: {e}")

        self.driver.quit()