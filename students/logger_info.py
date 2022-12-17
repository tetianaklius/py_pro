import logging

logger = logging.getLogger("main_students")
logger.setLevel(logging.INFO)

filehandler = logging.FileHandler("logger.log")
filehandler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)