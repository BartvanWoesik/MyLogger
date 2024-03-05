import logging
import logging.config
from my_logger.custom_logger import available_config, logger
import pytest


def test_setup_logging_existing_config():
    """Check if logger is created succesfully."""
    assert isinstance(logger, logging.Logger)


def test_setup_logging_nonexistent_config(caplog, tmp_path):
    """Check if error is raised correctly."""

    config_name = "nonexistent_config.json"
    with pytest.raises(FileNotFoundError):
        logger.setup_logging(config_name)


def test_available_config(capfd):
    """See if all available config files are shown."""
    expected_output = "base\n"
    available_config()
    captured = capfd.readouterr()
    assert captured.out == expected_output
