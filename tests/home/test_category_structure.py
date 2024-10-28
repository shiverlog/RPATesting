import logging
import time
import pytest
from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from conftest import setup


@pytest.mark.usefixtures("setup")
class TestCategoryStructure:
    log = cl.custom_logger(logging.DEBUG)

    def test_category_structure(self):
        # div.category 요소 찾기
        try:
            # SeleniumDriver 인스턴스 생성
            driver = SeleniumDriver(self.driver)

            # wait_for_element() 메서드(단일요소)를 사용해 버튼 대기
            category_button = driver.wait_for_element(
                locator="div.category a.btn_category",
                locatorType="css",
                timeout=10
            )
            self.log.info("Category button found and clickable.")

            # 마우스 오버 수행
            driver.mouse_hover(category_button)
            self.log.info("Hovered over the category button.")

            # get_element() 메서드를 사용해 버튼 대기
            large_categories = driver.get_elements(
                locator="li.category_lg > ul > li > a",
                locatorType="css"
            )
            if large_categories:
                self.log.info(f"Found {len(large_categories)} large categories.")
                for category in large_categories:
                    driver.mouse_hover(category)
                    driver.log.info(f"2-depth: {category.text}")

                    middle_categories = driver.get_elements(
                        locator="ul.category_mid > li > a",
                        locatorType="css"
                    )

                    for middle_category in middle_categories:
                        driver.mouse_hover(middle_category)  # 마우스 오버 수행

                        # 3depth 카테고리 가져오기
                        # small_categories = self.driver.find_elements(By.CSS_SELECTOR, "ul.category_sm > li > a")
                        # sm_category_names = [element.text for element in small_categories]
                        # self.log.info("Category sm: " + ", ".join(sm_category_names))
                        # self.log.info(f"3-depth <a> tags: {len(sm_category_names)}")

                    time.sleep(0.5)

            # 마우스 오버 수행
            driver.mouse_hover(large_categories)
            self.log.info("Hovered over the category button.")

        except Exception as e:
            self.log.error(f"Error during hover or click: {e}")
            self.log.info(f"Error: {e}")
