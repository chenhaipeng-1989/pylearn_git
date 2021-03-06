import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="test.log",
    datefmt="%Y-%m-%d %H:%M:%S",
    format="ã%(asctime)s %(levelname)sã %(lineno)d: %(message)s"
)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")