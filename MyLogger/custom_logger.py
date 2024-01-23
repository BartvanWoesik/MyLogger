import logging
import logging.config
import json
import pathlib
import os

CONFIG_FOLDER = "MyLogger/log_config/"

def setup_logging(config_name : str = 'base.json') ->logging.Logger:
    """ 
    Create custom logger child based on provided config.

    Args:
        config_name (str): Name of the json config file.
    
    """

    config_path = pathlib.Path(CONFIG_FOLDER + config_name)


    if not config_path.exists():
        raise FileNotFoundError(f"The specified config file '{config_name}' does not exist. "
                                f"Run custom_logger.available_config to find the available config files.")

    with open(config_path) as cf:
        config = json.load(cf)

    # Set config for logging
    logging.config.dictConfig(config)

    # Create logger that is not root logger. 
    logger = logging.getLogger(__name__)
    return logger

def available_config():
    """Print out the available config files in project."""
    for file in os.listdir(CONFIG_FOLDER):
        print(file)


def main():
    available_config()
    logger = setup_logging()
    logging.basicConfig(level="INFO")
    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")


if __name__ == "__main__":
    main()