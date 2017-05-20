from LogModule import Log

if __name__ == "__main__":
    logger = Log.getLogger()
    logger.debug("this is a debug message")
    logger.warning("this is a warning message")
    logger.info("this is a info")

