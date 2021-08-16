# section15
# selenium과 js의 관계 이건 따로 정리하는 게 필요하겠다...
# selenium webdriver가 정확히 어떤 일을 하는 것인지 이해하는 것인지 알 필요가 있겠다.
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name('name').send_keys('hello')
print("text: ", driver.find_element_by_name('name').text)
print("attribute: ", driver.find_element_by_name('name').get_attribute('value'))
print("script: ", driver.execute_script('return document.getElementsByName("name")[0].value'))
