import logging

from modules.examples.dataclass import User
from modules.examples.logger import Example as LoggingExample
from modules.logger import setup_logger

setup_logger()
logger = logging.getLogger("my_app")  # __name__ is a common choice


def main():
    LoggingExample()

    # Dataclasses
    u1 = User(name="Michael", id=1, email="foo@example.com")
    u2 = User(name="Hans", id=2)
    print(u2.email)
    print(u1 == u2)


if __name__ == "__main__":
    main()
