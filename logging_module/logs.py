import logging

#create basic config to handle logs
log = logging.basicConfig(filename = 'mylogs',filemode = 'w',level=logging.DEBUG,
                          format = "%(asctime)s-%(name)s-%(levelname)s-%(message)s")

# create instance for logging
logger = logging.getLogger("__name__")

logger.info("information messsage")
logger.debug("debug message")
logger.critical("critical message")
logger.warning("warning message")
logger.exception("exception message")
logger.error("error message")




