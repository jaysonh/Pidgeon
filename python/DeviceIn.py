import json
from typing import List
from MQTTHandler import *
from DeviceInMQTT import *
from DeviceInGetHttp import *

class DeviceIn:

    def __init__(self, json_data : json):
        self.type = json_data["type"]
        # MQTT Type takes a request on an MQTT address and sends the result back on another address
        if( self.type == "mqtt"):
            self.device = DeviceInMQTT(json_data  )
        if( self.type == "httpGet"):
            self.device = DeviceInGetHttp(json_data  )
        else:
            print("Error invalid sensor type")
        pass
                                                                                                                     