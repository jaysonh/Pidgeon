import json
from DeviceHandler import DeviceHandler
from DeviceInHandler import DeviceInHandler
from DeviceOutControl import DeviceOutControl
from DeviceInControl import DeviceInControl
from ActionSet import ActionSet
from ActionRamp import ActionRamp
from ActionRampTarget import *
from datetime import datetime
from Logging import *

class ScheduleAction:
    deviceID = ""
    
    def __init__(self, deviceID : str,  d :DeviceOutControl, a : ActionSet ):
        logger.debug(f"Initialising ScheduleAction for {deviceID}")
        self.deviceID = deviceID
        self.action = a
        self.device = d

    def run(self):
        logger.debug(f"Start running action for device: {self.deviceID}")
        
        self.time = str(datetime.datetime.now())
        self.action.run( self.device )    
       