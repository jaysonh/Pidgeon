from Configuration import Configuration
from DeviceHandler import DeviceHandler
from Scheduler import Scheduler
from MQTTHandler import MQTTHandler
from SensorHandler import SensorHandler

import schedule
import time
from AsciiPigeon import drawPigeon

version = "0.0.1"
    
if __name__ == "__main__":
    drawPigeon()
    print(f"Pigeon version {version}")

    # These files contain the scheduled iteams and the edeviceson which the yacttt
    configFiles = []
    configFiles.append("../data/config/devices.json")
    configFiles.append("../data/config/sensors.json")
    configFiles.append("../data/config/schedule.json")

    configuration  = Configuration( configFiles )
    
    device_handler = DeviceHandler( configuration.get("devices") )
    sensor_handler = SensorHandler( configuration.get("sensors") )
    
    # initalise scheduler last to ensure other components have been set up
    scheduler = Scheduler( configuration.get("schedule"), device_handler, sensor_handler )
     
    # main loop
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    print("Finished ")
   