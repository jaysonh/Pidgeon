import json
from typing import List
from MQTTHandler import *
from DeviceInMQTT import *
from DeviceInGetHttp import *
from DeviceInRebble import *

from Logging import *

class DeviceIn:

    def __init__(self, json_data : json):
        self.type = json_data["type"]

        # select device in type
        if( self.type == "mqtt"):
            self.device = DeviceInMQTT(json_data  )
        if( self.type == "httpGet"):
            self.device = DeviceInGetHttp(json_data  )
        if( self.type == "rebbleIn"):
            self.device = DeviceInRebble(json_data)
        else:
            logger.error("Error invalid sensor type")
        
    def update(self):
        self.device.update()

    def stop(self):
        self.device.stop()
                                                                                                                     