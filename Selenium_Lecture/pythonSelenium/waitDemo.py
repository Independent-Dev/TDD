from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)  # wait until element show up implicitly

driver.find_element_by_css_selector("input.search-keyword").send_keys('ber')
sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

list_added = []
for button in buttons:
    list_added.append(button.find_element_by_xpath('parent::div/parent::div/h4').text)
    button.click()

print(list_added)


driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# explicit wait
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'promoCode')))

list_added_2 = []
veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    list_added_2.append(veg.text)
print(list_added_2)

assert list_added == list_added_2

originalAmount = driver.find_element_by_css_selector('.discountAmt').text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.promoInfo')))
discountAount = driver.find_element_by_css_selector('.discountAmt').text

assert  float(originalAmount) > float(discountAount)
print(driver.find_element_by_css_selector("span.promoInfo").text)
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")

# 여기서 부동소수점 덧셈은 정확성을 보장할 수 있을 것인가..??
sum_all = sum(float(amount.text) for amount in amounts)
assert sum_all == float(driver.find_element_by_class_name("totAmt").text)
print(sum_all)
    
driver.close()