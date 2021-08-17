import logging
import inspect


class BaseClass:
    # 이렇게 로그를 이용해 출력하게 되면 html report에 해당 내용이 출력됨. 
    def getLogger(self):
        logger_name = inspect.stack()[1][3]  # what the hell is this.
        print(inspect.stack())
        # 매개변수를 넘기면 logger에 테스트케이스가 출력되도록 할 수 있음.
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # log를 넘겨준 파일 핸들러에 출력

        logger.setLevel(logging.INFO)
        return logger