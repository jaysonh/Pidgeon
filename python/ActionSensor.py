from Action import Action
from DeviceOutControl import DeviceOutControl
from DeviceInControl import *
import json
from Logging import *

class ActionSensor(Action):

    v = 0
    
    def __init__(self, json_data : json ) -> None:
        logger.info("Creating ActionSensor")
               
    def run(self, device : DeviceInControl):
        logger.debug(f"run ActionSensor")
        
        device.update()
        