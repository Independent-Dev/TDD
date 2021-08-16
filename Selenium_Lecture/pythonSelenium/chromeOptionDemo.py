# section15
from selenium import webdriver

# 여기에 나오는 것들은 전부 chrome options python을 검색해보면 알 수 있음.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")

driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver', options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
