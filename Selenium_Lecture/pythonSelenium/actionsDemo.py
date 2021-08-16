from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
menu = driver.find_element_by_id('mousehover')
action.move_to_element(menu).perform()

action.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
action = ActionChains(driver)
driver.implicitly_wait(5)
action.double_click(driver.find_element_by_tag_name('button')).perform()

alert = driver.switch_to.alert()
alert.accept()