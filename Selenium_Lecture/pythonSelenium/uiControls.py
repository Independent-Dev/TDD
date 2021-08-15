from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radio_button = driver.find_elements_by_name("radioButton")
radio_button[2].click()

validate_text = "Option3"
driver.find_element_by_css_selector("#name").send_keys(validate_text)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
assert validate_text in alert.text
alert.accept()

driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert

sleep(3)
alert.dismiss()

sleep(5)
driver.close()
