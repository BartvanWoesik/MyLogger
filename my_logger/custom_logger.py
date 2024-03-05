import logging
import logging.config

from my_logger.base import Loggers


class MyLogger(logging.Logger):
    @classmethod
    def setup_logging(cls, config_name: str = "base") -> logging.Logger:
        """
        Create custom logger child based on provided config.

        Args:
            config_name (str): Name of the json config file.

        """

        if config_name not in list(Loggers.keys()):
            raise FileNotFoundError(
                f"The specified config file '{config_name}' does not exist. Run custom_logger.available_config to find the available config files."
            )

        logging.setLoggerClass(cls)
        # Set config for logging
        logging.config.dictConfig(Loggers[config_name])

        # Create logger that is not root logger.
        logger = logging.getLogger(__name__)
        return logger


def available_config():
    """Print out the available config files in project."""
    for file in list(Loggers.keys()):
        print(file)


# Create logger that can be imported
logging.setLoggerClass(MyLogger)
logger = logging.getLogger(__name__)
logger = logger.setup_logging()
logger.info("Logger is set up.")
