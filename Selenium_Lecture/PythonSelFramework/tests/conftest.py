import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
    elif browser_name == 'firefox':
        driver = webdriver.Firefox('/Users/jonathan/study/TDD/Selenium_Lecture/geckodriver')
    else:
        raise Exception("Not Valid browser name option")
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    request.cls.driver = driver
    yield 
    driver.close()

