import json
from DeviceHandler import DeviceHandler
from DeviceInHandler import DeviceInHandler
from DeviceOutControl import DeviceOutControl
from DeviceInControl import DeviceInControl
from ActionSet import ActionSet
from ActionRamp import ActionRamp
from ActionRampTarget import *
from datetime import datetime

class ScheduleAction:
    deviceID = ""
    
    def __init__(self, deviceID : str,  d :DeviceOutControl, a : ActionSet ):
        self.deviceID = deviceID
        self.action = a
        self.device = d

    def run(self):
        self.time = str(datetime.now())
        self.action.run( self.device )
        #print(f"{self.time}setting {self.action.get()} from: {self.deviceID} ")  
        #self.device.sendData( self.action.get() )      
       