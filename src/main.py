import logging
import os

from dotenv import load_dotenv

from modules.examples.dataclass import User
from modules.examples.logger import Example as LoggingExample
from modules.logger import setup_logger

setup_logger()
logger = logging.getLogger("my_app")  # __name__ is a common choice

load_dotenv()  # Load variables from .env file into the environment


def main():
    LoggingExample()

    # Dataclasses
    u1 = User(name="Michael", id=1, email="foo@example.com")
    u2 = User(name="Hans", id=2)
    print(u2.email)
    print(u1 == u2)

    # Load env variables
    print(os.getenv("DATABASE_HOST"), os.getenv("DATABASE_USER"), os.getenv("MAIL"))

    # @todo arg parser

if __name__ == "__main__":
    main()
