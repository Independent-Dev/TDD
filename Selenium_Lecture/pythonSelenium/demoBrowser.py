from selenium import webdriver

# browser exposes an executable file
# Through Selenium test we need to invoke the executable file which will then invoke actual browser 
# driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
driver = webdriver.Firefox(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/geckodriver')

driver.get("https://www.youtube.com/")
print(driver.title, driver.current_url)
driver.maximize_window()

driver.get("https://www.youtube.com/watch?v=clMEk_5NXVI&ab_channel=%ED%9D%B0%ED%86%A0%EC%BB%A4")

driver.back()

driver.refresh()
driver.minimize_window()
driver.close()