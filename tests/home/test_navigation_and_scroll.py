import pytest
from selenium.webdriver.common.by import By


# Use mark.usefixtures decorator
@pytest.mark.usefixtures("setup")
class TestNavigationAndScroll:

    def __init__(self):
        self.driver = None

    def test_navigation_and_scroll(self):
        # Get all <li> elements inside the gnb section
        li_elements = self.driver.find_elements(By.CSS_SELECTOR, "div.gnb ul.clearfix > li a")

        # Iterate through each link and perform actions
        for element in li_elements:
            try:
                print(f"Clicking on: {element.text}")
                element.click()  # Click the link
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print("Scrolled to the bottom of the page.")
                self.driver.back()  # Go back to the previous page
            except Exception as e:
                print(f"Error: {e}")