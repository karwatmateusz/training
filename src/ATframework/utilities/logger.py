import logging
import inspect
from datetime import datetime


def Logger(logLevel):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # Log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(
        filename=f"logs__{datetime.today().strftime('%m-%d_%H-%M')}.log",
        mode="w",
    )

    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s: %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
