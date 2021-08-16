from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)