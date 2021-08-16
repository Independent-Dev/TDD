# section16
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop'").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    # print(product.find_element_by_xpath("div/h4/a").text)
    if "Blackberry" == product.find_element_by_xpath("div/h4/a").text:
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
driver.find_element_by_id('country').send_keys('ind')
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'India')))
driver.find_element_by_link_text('India').click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
assert 'Success' in driver.find_element_by_class_name("alert-success").text
driver.get_screenshot_as_file("screen.png")
driver.close()