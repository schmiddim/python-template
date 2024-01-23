import logging
from modules.logger import setup_logger
from modules.logic import Foo
setup_logger()
logger = logging.getLogger("my_app")  # __name__ is a common choice


def main():
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    Foo.calculate()
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")


if __name__ == "__main__":
    main()
