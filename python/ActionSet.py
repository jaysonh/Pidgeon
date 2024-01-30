from Action import Action
from DeviceOutControl import DeviceOutControl
import json
from Logging import *

class ActionSet(Action):

    v = 0
    
    def __init__(self, json_data : json ) -> None:
        logger.info("Creating ActionSet {self.data  }")
        self.data = json_data["value"]        

    def run(self, device : DeviceOutControl):
        logger.debug(f"run ActionSet: {self.data}")
        
        if type(self.data) is list:
            device.sendData(self.data )
        else:
            device.sendData([ self.data] )
        