import logging
import calendar
import time
import datetime

def SetupLogging():
    

    
    current_datetime = datetime.datetime.now()
    timestamp_format = "%Y-%m-%d_%H-%M-%S"
    custom_timestamp = current_datetime.strftime(timestamp_format)

    logFileName = "log" + custom_timestamp + ".log"
    logPath = "../logs/" + logFileName
    print(f"timestamp: {custom_timestamp}")
    logging.basicConfig(filename=logPath, encoding='utf-8', level=logging.DEBUG)

if __name__ == "__main__":
  SetupLogging()