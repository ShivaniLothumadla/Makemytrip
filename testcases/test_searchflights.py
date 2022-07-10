import pytest
import logging
from ddt import ddt, data, unpack, file_data
from pages.homepage import HomePage
from utilities.utils import Utils
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s', datefmt='%y: %m: %d')


@ddt
@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = HomePage(self.driver)
        self.ut = Utils()

    # hardcoded data
    @data(('Hyderabad', 'New Delhi', 'Fri Jul 01 2022', 'Sat Jul 02 2022', '1 stop'))
    @unpack
    # @file_data('../Testdata/test.yaml')
    def test_search_flights(self, fromplace, toplace, fromdate, todate, stop):
        # search_flights_result = self.lp.searchflights('Hyderabad', 'New Delhi', 'Fri Jul 01 2022', 'Sat Jul 02 2022')
        search_flights_result = self.lp.searchflights()
        self.lp.closelanguagesuggetion()
        self.lp.depart_from(fromplace)
        self.lp.going_to(toplace)
        self.lp.depart_date(fromdate)
        self.lp.return_date(todate)
        # self.lp.scrollTo()
        self.lp.search()
        flight_filters = search_flights_result.filtering_flights()
        self.ut.assertListItems(flight_filters, stop)
        log = self.ut.logger()
        log.debug(flight_filters)
