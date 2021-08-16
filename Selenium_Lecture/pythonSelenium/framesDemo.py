from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
# iframe, frameset, frame
driver.find_element_by_css_selector('#tinymce').clear()
driver.find_element_by_css_selector('#tinymce').send_keys("I am able to automate")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name('h3').text)
# driver.close()
