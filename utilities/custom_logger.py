import inspect
import logging
import sys
import os


def custom_logger(logLevel=logging.DEBUG, log_to_console=True):

    # Retrieve the name of the currently called class or function
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # logger handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # set logger
    logger.setLevel(logging.DEBUG)

    # automation file handlers
    log_file = os.path.join(os.getcwd(), 'automation.log')
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(logLevel)

    # console handlers
    if log_to_console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logLevel)

        # console formatter
        console_formatter = logging.Formatter('%(name)s - %(levelname)s: %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    # file formatter
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_formatter)

    # add logger
    logger.addHandler(file_handler)
    return logger
