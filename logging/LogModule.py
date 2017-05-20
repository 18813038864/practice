import logging

class Log:
    logger = None

    @staticmethod
    def getLogger():
        if Log.logger is not None:
            return Log.logger

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        Log.logger = logger
        return logger