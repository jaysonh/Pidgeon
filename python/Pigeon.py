from Configuration import Configuration
from DeviceHandler import DeviceHandler
from Scheduler import Scheduler
from MQTTHandler import MQTTHandler

import schedule
import time


version = "0.0.1"
    
if __name__ == "__main__":
    print(f"Pigeon version {version}")

    # These files contain the scheduled iteams and the edeviceson which the yacttt
    configFiles = []
    configFiles.append("../data/config/devicesOut.json")
    configFiles.append("../data/config/devicesIn.json")
    configFiles.append("../data/config/schedule.json")
    configFiles.append("../data/config/mqtt_broker.json")

    configuration  = Configuration( configFiles )
    
    device_handler = DeviceHandler( configuration.get("devicesOut"), 
                                    configuration.get("devicesIn") )
    
    # initalise scheduler last to ensure other components have been set up
    scheduler = Scheduler( configuration.get("schedule"), device_handler)
     
    # main loop
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    print("Finished ")
   