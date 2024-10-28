import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *

import utilities.custom_logger as cl
import logging


# Function to set Chrome options
def get_options():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('start-maximized')
    return options


# Function to set ChromeDriver service
def get_service():
    chromedriver_path = os.getenv('CHROME_DRIVER_PATH', 'E:\\KTAlphaTestAutomation\\chromedriver.exe')
    return Service(executable_path=chromedriver_path)


# Initializes SeleniumDriver with driver, logger, options, and service
class SeleniumDriver():

    # SeleniumDriver
    def __init__(self, driver):
        # Driver
        self.driver = driver
        # Logger
        self.log = cl.custom_logger(logging.DEBUG)
        # Option
        self.options = get_options()
        # Service
        self.services = get_service()
        self.log.info("SeleniumDriver initialized with Chrome options and service.")

    # LocatorType
    def get_by_type(self, locatorType):
        locator_type = locatorType.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "tag":
            return By.TAG_NAME
        elif locator_type == "partial_link":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    # Searches and returns a web element
    def get_element(self, locator, locatorType="id"):
        element = None
        try:
            locator_type = locatorType.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator " + locator + "and locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator " + locator + "and locatorType: " + locatorType)
            return None
        return element

    # Searches and returns a web elements
    def get_elements(self, locator, locatorType="id"):
        try:
            locator_type = locatorType.lower()
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            self.log.info(f"Found {len(elements)} elements with locator {locator} and locatorType {locatorType}")
            return elements
        except Exception as e:
            self.log.error(f"Elements not found with locator {locator}. Error: {e}")
            return []

    # Clicks on a web element
    def element_click(self, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def mouse_hover(self, element):
        try:
            # WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info(f"Hovered over element: {element.text}")
        except Exception as e:
            self.log.warning(f"Warning: Could not hover over element. Proceeding anyway. Error: {e}")

    # Sends input to a web element
    def send_keys(self, data, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)  # 입력 실패 메시지 출력
            print_stack()

    # Checks if an element is present
    def is_element_present(self, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            if element is not None:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    # Waits for an element to become clickable
    def wait_for_element(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element