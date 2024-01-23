import logging


class Foo:

    @staticmethod
    def calculate():
        logger = logging.getLogger(__name__)  # __name__ is a common choice
        logger.info("Hui")
