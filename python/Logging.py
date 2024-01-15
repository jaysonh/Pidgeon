import logging
import calendar
import time
import datetime

logger = logging.getLogger(__name__)

def SetupLogging():
    

    
    current_datetime = datetime.datetime.now()
    timestamp_format = "%Y-%m-%d_%H-%M-%S"
    custom_timestamp = current_datetime.strftime(timestamp_format)

    logFileName = "log" + custom_timestamp + ".log"
    logPath = "../logs/" + logFileName
    print(f"timestamp: {custom_timestamp}")

    logger.setLevel(logging.DEBUG)
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(logPath)
    c_handler.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.DEBUG)
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    logger.debug(f"Started logging at time {custom_timestamp }")

if __name__ == "__main__":
  SetupLogging()