import json
from DeviceDMX import DeviceDMX
from DeviceRebble import DeviceRebble
from DeviceMQTT import DeviceMQTT

class Device:
    
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
        else:
            raise  Exception(f"Invalid device type: {self.type}")