import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        logger = self.getLogger()
        logger.critical("test started")
        self.driver.find_element_by_css_selector('input[name="name"]').send_keys(getData['first_name'])
        self.driver.find_element_by_name('email').send_keys(getData['last_name'])
        self.driver.find_element_by_id('exampleCheck1').click()

        # select class provide the methods to handle the options in dropdown
        dropdown = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        dropdown.select_by_visible_text(getData['gender'])

        # xpath
        self.driver.find_element_by_xpath("//input[@type='submit']").click()

        message = self.driver.find_element_by_class_name("alert-success").text

        assert "success" in message.lower()

        self.driver.refresh()
    
    @pytest.fixture(params=HomePageData.home_page_data)
    def getData(self, request):
        return request.param