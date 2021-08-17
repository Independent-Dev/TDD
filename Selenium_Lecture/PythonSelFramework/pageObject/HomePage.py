from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver) -> None:
        self.driver = driver
    
    # 이런 것들을 하드코딩하는 것이 아니라 함수화하는 것이 기본 컨셉
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
       return self.driver.find_element(*HomePage.shop)