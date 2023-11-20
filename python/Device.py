import json
from DeviceDMX import DeviceDMX
from DeviceRebble import DeviceRebble
from DeviceMQTT import *
from DeviceOSC import *
from DeviceKKC import *

class Device:
    
    value = 0

    def __init__(self, json_data : json ):
        
        self.id = json_data["id"]
        self.name = json_data["name"]
        self.numChannels = json_data["numChannels"]
        self.type = json_data["type"]

        if( self.type == "dmx"):
            self.outputDevice = DeviceDMX(json_data  )
        elif( self.type == "rebble"):
            self.outputDevice = DeviceRebble( json_data  )
        elif( self.type == "mqtt"):
            self.outputDevice = DeviceMQTT( json_data  )   
        elif( self.type == "osc"):
            self.outputDevice = DeviceOSC( json_data  )  
        elif( self.type == "kkc"):
            self.outputDevice = DeviceKKC( json_data  )      
        else:
            raise  Exception(f"Invalid device type: {self.type}")
    
    def sendData(self, data = [] ):
        #self.outputDevice.sendData( data )
        pass
    def sendData(self, v : float):
        self.outputDevice.sendData( v )
        pass

    def getValue(self) -> int:
        return self.outputDevice.getValue()
    
    def getValues(self) -> []:
        return self.outputDevice.getValues()
