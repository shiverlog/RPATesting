import time
import pytest
from conftest import setup
from selenium.webdriver.common.by import By
import logging
import utilities.custom_logger as cl


# mark.usefixtures decorator 사용
@pytest.mark.usefixtures("setup")
class TestNavigationAndScroll:

    log = cl.custom_logger(logging.DEBUG)

    def test_navigation_and_scroll(self):
        # div.gnb 안 clearfix ul .li .a 요소 찾기
        li_elements = self.driver.find_elements(By.CSS_SELECTOR, "div.gnb ul.clearfix > li a")

        # a tag 이름 List 화 후 log 로 찍어보기
        a_tag_names = [element.text for element in li_elements]
        self.log.info("Navigation: " + ", ".join(a_tag_names))
        self.log.info(f"Number of <a> tags: {len(a_tag_names)}")

        for i in range(len(li_elements)):
            try:
                # 각 요소 가져오기
                li_elements = self.driver.find_elements(By.CSS_SELECTOR, "div.gnb ul.clearfix > li a")
                element = li_elements[i]

                # 각 요소 링크 클릭
                self.log.info(f"Clicking on: {element.text}")
                element.click()

                # 스크롤 다운
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.log.info("Scrolled to the bottom of the page.")

                # 뒤로 가기
                self.driver.back()
                time.sleep(2)

            except Exception as e:
                self.log.info(f"Error: {e}")
                time.sleep(2)