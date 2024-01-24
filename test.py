import logging
import logging.config
from my_logger.custom_logger import setup_logging, available_config
import pytest

CONFIG_FOLDER = "log_config/"


def test_setup_logging_existing_config():
    """Check if logger is created succesfully."""
    logger = setup_logging("base.json")
    assert isinstance(logger, logging.Logger)


def test_setup_logging_nonexistent_config(caplog, tmp_path):
    """Check if error is raised correctly."""
    with pytest.raises(
        FileNotFoundError,
        match="The specified config file 'nonexistent_config.json' does not exist.",
    ):
        setup_logging("nonexistent_config.json")


def test_available_config(capfd):
    """See if all available config files are shown."""
    expected_output = (
        "base.json\n"
    )  # Add other expected config file names if applicable
    available_config()
    captured = capfd.readouterr()
    assert captured.out == expected_output
