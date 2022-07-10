#request is a special fixture in pytest.
#the connection between test class and conftest is request fixture.
#we have to pass the request parameter to the fixture and make driver instance and wait as a class variable
# because we can use in every test file.


import pytest
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(autouse=True)
def setup(request, browser, url='https://www.makemytrip.com/'):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'ff':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    logging.info('closing the browser')
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope='session', autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session', autouse=True)
def url(request):
    return request.config.getoption("--url")
