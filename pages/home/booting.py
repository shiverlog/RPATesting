from selenium import webdriver
from base.selenium_driver import SeleniumDriver

import logging
import utilities.custom_logger as cl


def test_ui_booting():
    base_url = "https://m.kshop.co.kr/display/ec/display/main"
    driver = webdriver.Chrome()
    driver.get(base_url)


class UIBooting:

    # Logger
    log = cl.custom_logger(logging.DEBUG)

    # Init
    def __init__(self):
        self.selenium_driver = SeleniumDriver(self)
        self.driver = None

    def initialize_driver(self):
        if self.driver is None:
            self.driver = self.selenium_driver.driver()
