# app/common/Logger.py
import logging
from injector import inject, singleton

@singleton
class AppLogger:
    def __init__(self, name='app', file='app.log', level=logging.DEBUG):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler = logging.FileHandler(file)
        handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        #self.logger.addHandler(handler)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message, exc_info=True)