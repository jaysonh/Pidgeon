from Configuration import Configuration
from DeviceHandler import DeviceHandler
from Scheduler import Scheduler
from MQTTHandler import MQTTHandler
from SensorHandler import SensorHandler
import os
import time
from AsciiPigeon import drawPigeon

version = "0.0.1"
    
if __name__ == "__main__":
    drawPigeon()
    print(f"Pigeon version {version}")

    configPath = os.getcwd() + "/../data/config"

    # These files contain the scheduled iteams and the edeviceson which the yacttt
    configFiles = []
    configFiles.append(configPath + "/devices.json")
    configFiles.append(configPath + "/sensors.json")
    configFiles.append(configPath + "/schedule.json")

    configuration  = Configuration( configFiles )
    
    device_handler = DeviceHandler( configuration.get("devices") )
    sensor_handler = SensorHandler( configuration.get("sensors") )
    
    # initalise scheduler last to ensure other components have been set up
    scheduler = Scheduler( configuration.get("schedule"), device_handler, sensor_handler )
     
    # main loop
    while True:
        time.sleep(1)
    
    print("Exiting application") 
   