import pytest, inspect, logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text_verify):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text_verify)))

    def getLogger(self):
        logger_name = inspect.stack()[1][3]  # what the hell is this.
        # 매개변수를 넘기면 logger에 테스트케이스가 출력되도록 할 수 있음.
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # log를 넘겨준 파일 핸들러에 출력

        logger.setLevel(logging.INFO)
        return logger