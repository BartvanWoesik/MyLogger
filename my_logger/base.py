yellow = "\x1b[33;20m"
reset = "\x1b[0m"

Loggers = {
    "base": {
        "version": 1,
        "formatters": {
            "simple": {
                "format": f" %(asctime)s - {yellow} %(levelname)s {reset} \t: %(name)s - %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "simple",
                "stream": "ext://sys.stdout",
            }
        },
        "loggers": {
            "root": {  # Add this section to override the root logger
                "level": "DEBUG",  # Set the desired log level for the root logger
                "handlers": [],
            },
            "my_logger": {"level": "INFO", "handlers": ["console"]},
        },
    }
}
