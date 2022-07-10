from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By

from pages.search_results_page import SearchFlights


class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LANGUAGESUGGETION = '*[class="langCardClose"]'
    DEPART_FROM_FEILD = '*[id="fromCity"]'
    GOING_TO_FEILD = '*[id="toCity"]'
    GET_ALL_RESULTS = '[class="react-autosuggest__suggestions-list"]>li'
    DEPART_DATE = "//span[contains(text(),'DEPARTURE')]"
    GET_ALL_DATES = '//*[@class="DayPicker-Body"]//div[@aria-disabled="false"]'
    RETURN_DATE = "//span[contains(text(),'RETURN')]"
    SEARCH_BUTTON = "//a[contains(text(),'Search')]"

    def closelanguagesuggetion(self):
        self.driver.find_element(By.CSS_SELECTOR, self.LANGUAGESUGGETION).click()

    def getDepartFromField(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.DEPART_FROM_FEILD)

    def going_to_feild(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.GOING_TO_FEILD)

    def get_all_results(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.GET_ALL_RESULTS)

    def get_all_dates(self):
        return self.driver.find_elements(By.XPATH, self.GET_ALL_DATES)

    def depart_from(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)
        search_results = self.get_all_results()
        for result in search_results:
            if departlocation in result.text:
                result.click()
                break

     # provide going to location
    def going_to(self, gnglocation):
        # self.going_to_feild().click()
        self.going_to_feild().send_keys(gnglocation)
        self.getDepartFromField().send_keys(Keys.ENTER)
        search_results = self.get_all_results()
        for result in search_results:
            if gnglocation in result.text:
                result.click()
                break

    def departdate(self):
        return self.driver.find_element(By.XPATH, self.DEPART_DATE)

    def depart_date(self, departdate):
        self.departdate().click()

        all_dates = self.get_all_dates()
        for date in all_dates:
            if date.get_attribute('aria-label') == departdate:
                date.click()
                break

    def returndate(self):
        return self.driver.find_element(By.XPATH, self.RETURN_DATE)

    def return_date(self, returndate):
        self.returndate().click()
        all_dates = self.get_all_dates()
        for date in all_dates:
            if date.get_attribute('aria-label') == returndate:
                date.click()
                break

    def search(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON).click()

    def searchflights(self):
        search_flights = SearchFlights(self.driver)
        return search_flights
