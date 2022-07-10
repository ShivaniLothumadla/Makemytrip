from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def scrollTo(self):
        pageLength = self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return document.body.scrollHeight')
        match = False
        while match == False:
            lastcount = pageLength
            sleep(3)
            pageLength = self.driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return document.body.scrollHeight')
            if lastcount == pageLength:
                match = True
        sleep(4)

    def wait_for_element_to_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(ec.presence_of_all_elements_located((locator_type, locator)))
        return elements

