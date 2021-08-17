import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
@pytest.mark.e2e
class TestOne(BaseClass):
    def test_e2e(self):
        print(self.driver)
        homepage = HomePage(self.driver)
        homepage.shopItems().click()

        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            # print(product.find_element_by_xpath("div/h4/a").text)
            if "Blackberry" == product.find_element_by_xpath("div/h4/a").text:
                product.find_element_by_xpath("div/button").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
        self.driver.find_element_by_id('country').send_keys('ind')

        self.verifyLinkPresence('India')

        self.driver.find_element_by_link_text('India').click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        assert 'Success' in self.driver.find_element_by_class_name("alert-success").text
        self.driver.get_screenshot_as_file("screen.png")