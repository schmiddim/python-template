import logging



logger = logging.getLogger(__name__)  # __name__ is a common choice


class Example:
    def __init__(self):
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")

        try:
            1 / 0
        except ZeroDivisionError:
            logger.exception("exception message")