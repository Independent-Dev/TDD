import logging

def test_logging():
    # __name__을 넘기면 logger에 테스트케이스가 출력되도록 할 수 있음.
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)  # log를 넘겨준 파일 핸들러에 출력

    logger.setLevel(logging.INFO)

    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
