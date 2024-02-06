import logging
import logging.config
import yaml
import pathlib
import os

CURRENT_LOCATION = os.path.abspath(__file__)
CONFIG_FOLDER = os.path.dirname(CURRENT_LOCATION) + "\\log_config\\"


class MyLogger(logging.Logger):
    @classmethod
    def setup_logging(cls, config_name: str = "base.yaml") -> logging.Logger:
        """
        Create custom logger child based on provided config.

        Args:
            config_name (str): Name of the json config file.

        """

        config_path = pathlib.Path(CONFIG_FOLDER + config_name)
        if not config_path.exists():
            raise FileNotFoundError(
                f"The specified config file '{config_name}' does not exist. "
                f"Run custom_logger.available_config to find the available config files."
            )

        with open(config_path) as cf:
            config = yaml.load(cf, Loader=yaml.FullLoader)

        logging.setLoggerClass(cls)
        # Set config for logging
        logging.config.dictConfig(config)

        # Create logger that is not root logger.
        logger = logging.getLogger(__name__)
        return logger


def Available_config():
    """Print out the available config files in project."""
    for file in os.listdir(CONFIG_FOLDER):
        print(file)


def main():
    Available_config()

    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")


# Create logger that can be imported
logging.setLoggerClass(MyLogger)
logger = logging.getLogger(__name__)
logger = logger.setup_logging()

if __name__ == "__main__":
    main()
