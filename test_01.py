from Tools.get_logs import logger
logger=logger()
try:
    int(a)
except Exception as e:
    logger.exception(e)
