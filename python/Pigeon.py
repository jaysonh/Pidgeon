from Configuration import Configuration
from DeviceHandler import DeviceHandler
from Scheduler import Scheduler
from MQTTHandler import MQTTHandler
from DeviceInHandler import DeviceInHandler
import os
import time
from AsciiPigeon import DrawAsciiPigeon
from tkinter import *
from tkinter import ttk
import tkinter as tk
from GUIMainWindow import *
from LogicHandler import *
from Logging import *
import sys

version = "0.0.1"
    
def mainLoop():
    while True:
        time.sleep(0.01) # wait

if __name__ == "__main__":

    headless = 0
    # can give an option to run in headless mode
    if len(sys.argv) == 2:
        headless = int(sys.argv[1])
    
    SetupLogging()
    DrawAsciiPigeon()
    logger.info(f"Pigeon version {version}")

    configPath = os.getcwd() + "/../data/config"

    # These files contain the scheduled iteams and the edeviceson which the yacttt
    configFiles = []
    configFiles.append(configPath + "/devices.json")
    configFiles.append(configPath + "/sensors.json")
    configFiles.append(configPath + "/schedule.json")
    configFiles.append(configPath + "/logic.json")
    configFiles.append(configPath + "/ui.json")

    
    configuration  = Configuration( configFiles )
    
    device_handler = DeviceHandler( configuration.get("devices") )
    sensor_handler = DeviceInHandler( configuration.get("sensors") )
    
    # initalise scheduler last to ensure other components have been set up
    scheduler = Scheduler( configuration.get("schedule"), device_handler, sensor_handler )
     
    logic = LogicHandler( configuration.get("logic") ) 

    if headless == 0:
        # main loop
        gui = GuiMainWindow( configuration.get("userinterface"), 
                            configuration.get("devices"), 
                            configuration.get("sensors"), 
                            configuration.get("schedule"), 
                            configuration.get("logic"),
                            scheduler.updateScheduleEvent,
                            scheduler.removeScheduleEvent,
                            scheduler.getNextRunTimesEvent )
    else:
        mainLoop()

    scheduler.stop()
    MQTTHandler.getInstance().stopAll()
    device_handler.stopThreads()
    
    for thread in threading.enumerate():
        print(thread.name)
  
   