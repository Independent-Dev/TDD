from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys('ind')
sleep(2)
driver.find_element_by_link_text("India").click()
assert driver.find_element_by_id('autosuggest').get_attribute('value') == "India"