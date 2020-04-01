###############################################################################
# logger.py
#
# Contacts: Manuel Weber
# DATE: 02.03.2020
###############################################################################

import logging

class Logger:

    def __init__(self, name):
        # Create a custom logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('logfile.log')
        c_handler.setLevel(logging.DEBUG)
        f_handler.setLevel(logging.DEBUG)

        # Create formatters and add it to handlers
        my_format = logging.Formatter('%(asctime)s %(name)-20s %(levelname)-10s %(message)s')
        c_handler.setFormatter(my_format)
        f_handler.setFormatter(my_format)

        # Add handlers to the logger
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

        # log
        self.logger.info('Logger initialized for module: %s',name)

    def log_critical(self, message):
        self.logger.critical(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_debug(self, message):
        self.logger.debug(message)
