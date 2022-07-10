from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class SearchFlights(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FILTER_BY_ONE = '//*[contains(text(),"1 stop")]'

    def filtering_flights(self):
        return self.driver.find_elements(By.XPATH, self.FILTER_BY_ONE)