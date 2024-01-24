import json
import logging.config
import logging.handlers
import pathlib


def setup_logger( config_file="./stdout-logging-config.json"):
    config_file = pathlib.Path(config_file)
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)

